import pandas as pd
import streamlit as st
from datetime import datetime
from streamlit_folium import folium_static
import folium
import json

def mapa():
    # Leer datos de demoras
    data = pd.read_csv("datasets/delays.csv")

    data['delivery_time'] = pd.to_timedelta(data['delivery_time'])
    data['sellerToCarry_time'] = pd.to_timedelta(data['sellerToCarry_time'])
    data['carry_time'] = pd.to_timedelta(data['carry_time'])

    st.title("Delivery Time Analysis")
    # Show the average delivery time
    average_delivery_time = data['delivery_time'].mean()
    average_delivery_time = str(average_delivery_time).split(':')[0]+"hs"
    st.subheader("Average Brazil delivery time: "+":blue["+average_delivery_time+"]")

    # Show the average delivery time by seller state
    average_by_state = data.groupby('sellerState', as_index=False)[['delivery_time', 'sellerToCarry_time','carry_time']].mean()
    average_by_state = average_by_state.sort_values("delivery_time")

    top_5_states = average_by_state.head(5).reset_index(drop=True).astype(str)
    top_5_states['delivery_time'] = top_5_states['delivery_time'].astype(str).str.split(":").str[0] + "hs"
    top_5_states['sellerToCarry_time'] = top_5_states['sellerToCarry_time'].astype(str).str.split(":").str[0] + "hs"
    top_5_states['carry_time'] = top_5_states['carry_time'].astype(str).str.split(":").str[0] + "hs"

    bottom_5_states = average_by_state.tail(5).reset_index(drop=True).astype(str)
    bottom_5_states['delivery_time'] = bottom_5_states['delivery_time'].astype(str).str.split(":").str[0] + "hs"
    bottom_5_states['sellerToCarry_time'] = bottom_5_states['sellerToCarry_time'].astype(str).str.split(":").str[0] + "hs"
    bottom_5_states['carry_time'] = bottom_5_states['carry_time'].astype(str).str.split(":").str[0] + "hs"

    st.subheader("Top 5 States with the :green[Best Average] Delivery Time:")
    st.dataframe(top_5_states)
    st.subheader("Bottom 5 States with the :red[Worst Average] Delivery Time:")
    st.dataframe(bottom_5_states)

    # MAPA POR ESTADOS
    # coordinations of Federal District

    statesDelays = pd.read_csv("datasets/statesDelays.csv")
    with open('datasets/data.json', 'r') as fp:
        meshes_data = json.load(fp)

    federal_district = [-15.7757875,-48.0778477]

    # creating the map object
    basemap = folium.Map(
        location=federal_district,
        zoom_start=4,
        tiles='cartodbpositron'
    )

    # plotting the choropleth
    legends = 'Delays'
    folium.Choropleth(
        geo_data=meshes_data,
        data=statesDelays,
        name=legends,
        columns=['id','delivery_time'],
        key_on='feature.properties.codarea',
        fill_color='YlOrRd',
        fill_opacity=1.0,
        line_opacity=0.7,
        legend_name=legends
    ).add_to(basemap)

    # adding all controls to the map
    folium.LayerControl().add_to(basemap)

    # finally displaying the map
    folium_static(basemap)

    st.subheader("Customers Distribution")
    heatmapData = pd.read_csv("datasets/heatmap.csv")

    # create a map
    m = folium.Map(location=[heatmapData['customerLat'].mean(), heatmapData['customerLong'].mean()], zoom_start=4)

    # create a heatmap layer
    hm = folium.plugins.HeatMap(heatmapData[['customerLat', 'customerLong', 'intensity']].values.tolist(), 
                                name='HeatMap', overlay=True, control=False, radius = 11, min_opacity = 0.5)
    hm.add_to(m)

    # display the map
    folium_static(m)

    st.subheader("City Delay Calculator")
    # Crear un mapa base
    map_br = folium.Map(location=[-14.235004, -51.92528], zoom_start=4)

    data['delivery_time'] = data['delivery_time'].astype(str)
    data['sellerToCarry_time'] = data['sellerToCarry_time'].astype(str)
    data['carry_time'] = data['carry_time'].astype(str)

    # Crear un selectbox para la ciudad de origen
    origin_city = st.selectbox("Select the departure City:", data['sellerCity'].unique())

    # Crear un selectbox para la ciudad de destino
    destination_city = st.selectbox("Select the destination City:", data['customerCity'].unique())

    def color_producer(delay):
        delay = delay.split(".")[0]
        # Convert the string to a datetime object
        delay_obj = datetime.strptime(delay, "%d days %H:%M:%S")
        refer_obj = datetime.strptime("1900-01-14", "%Y-%m-%d")
        if delay_obj > refer_obj:
            return 'red'
        else:
            return 'green'

    # Crear una función para actualizar el mapa
    def update_map(origin_city, destination_city):
        # Filtrar datos para mostrar solo las rutas seleccionadas
        filtered_data = data[(data['sellerCity'] == origin_city) & (data['customerCity'] == destination_city)]

        # Recorrer todas las filas del archivo de datos filtrado
        for i in range(0, len(filtered_data)):
            # Crear una línea entre las coordenadas
            route = folium.PolyLine(
                locations=[[filtered_data.iloc[i]['sellerLat'], filtered_data.iloc[i]['sellerLong']],
                        [filtered_data.iloc[i]['customerLat'], filtered_data.iloc[i]['customerLong']]],
                color=[color_producer(filtered_data.iloc[i]['delivery_time'])],
                weight=5,
                opacity=.8
            )
            
            route.add_child(
                folium.Popup("<b>Total Delivery time: </b>" + filtered_data.iloc[i]['delivery_time'] + "<br>"+
                            "<b>Seller to Carry time: </b>" + filtered_data.iloc[i]['sellerToCarry_time'] + "<br>"+
                            "<b>Carry time: </b>" + filtered_data.iloc[i]['carry_time'] + "<br>", max_width=200)
            )
            # Añadir la ruta al mapa
            route.add_to(map_br)

    # Añadir un botón para actualizar el mapa
    if st.button("Update Map"):
        update_map(origin_city, destination_city)
        
    folium_static(map_br)
