import streamlit as st
import pandas as pd
import numpy as np

def productRS():
    #Cargar los datos de la matriz de co-ocurrencia en un DataFrame
    matrix_data = pd.read_csv("datasets/co-occurrence_matrix.csv")
    product_names  = pd.read_csv("datasets/product_category_df.csv")

    matrix_data = matrix_data.merge(product_names , on="product_id")
    # crear un diccionario con las relaciones id-nombre de producto
    product_names_dict = product_names.set_index('product_id').to_dict()['product_name']

    # reemplazar los ids de las columnas en matrix_data por los nombres correspondientes
    matrix_data.rename(columns=product_names_dict, inplace=True)

    #Crear una lista de productos para el selectbox
    product_list = matrix_data["product_name"].unique()

    st.title("Product Recommendation System")
    selected_product = st.selectbox("Select a product", product_list)

    st.write("Selected product: " + selected_product)

    #Filtrar los datos de la matriz para mostrar solo los productos relacionados
    filtered_matrix = matrix_data[matrix_data["product_name"] == selected_product]

    limit = st.slider("Limit:",0.0,1.0,0.2)
    #Filtro solo las columnas numericas y las que superen el slider
    filtered_matrix = filtered_matrix[filtered_matrix.select_dtypes(include=[np.number]).columns]
    filtered_matrix = filtered_matrix.loc[:, filtered_matrix.apply(lambda x: x.max() > limit)]
    #Filtro el producto seleccionado
    filtered_matrix = filtered_matrix.drop(selected_product, axis=1)

    #Mostrar la matriz de co-ocurrencia en una tabla
    st.dataframe(filtered_matrix)
    st.markdown("---")