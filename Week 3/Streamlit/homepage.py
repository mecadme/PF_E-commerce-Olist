import streamlit as st

def homepage():

    st.set_page_config(
        page_title="Olist Tools",
        page_icon=":earth_americas:",
        layout="wide"
    )

    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox("Go to page", ["Delivery Time", "Product Recommendation", "Sentiment Analysis"])

    if page == "Sentiment Analysis":
        import sentiment
        sentiment.sentiment()

    if page == "Product Recommendation":
        import productRS
        productRS.productRS()

    elif page == "Delivery Time":
        import mapa
        mapa.mapa()

if __name__ == "__main__":
    homepage()