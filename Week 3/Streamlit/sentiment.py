import streamlit as st
import translators as ts
import nltk   
import pickle
import pandas as pd
import matplotlib.pyplot as plt                                
import seaborn as sns


def sentiment():

    nltk.download('stopwords')
    nltk.download('rslp')
    nltk.download('punkt')
    nltk.download('wordnet')

    #filename='datasets/model.sav'
    #loaded_model = pickle.load(open(filename, 'rb'))

    with open('datasets/model.sav', 'rb') as f:
        loaded_model = pickle.load(f)

    with open('datasets/vectorizer.pkl', 'rb') as f:
        vectorizer = pickle.load(f)

    comments=pd.read_csv('datasets/comments.csv')

    def year_percentage(dataFrame=comments, year=2016):
        data_year=dataFrame[dataFrame['review_creation_year']==year]
        total_comments_year=data_year['review_type'].value_counts()
        percentage_positives_year=round(((total_comments_year[0]+total_comments_year[2])/total_comments_year.sum())*100,2)
        return(percentage_positives_year, 100-percentage_positives_year) 

    def CSAT_graph(dataFrame=comments, year=2016):
        data_year=dataFrame[dataFrame['review_creation_year']==year]
        # Create a figure with 2 subplots (1 row, 2 columns)
        #fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6,3))

        fig1, ax1 = plt.subplots(figsize=(12,6))
        fig2, ax2 = plt.subplots(figsize=(6,3.63))

        # Create the semi-donut chart
        val = [year_percentage(dataFrame, year)[1], year_percentage(dataFrame, year)[0]]
        label = [val[1], ""]

        # append data and assign color
        label.append("")
        val.append(sum(val))  # 50% blank
        colors = ['gray', 'lightblue', 'white']

        # plot
        ax1.pie(val, labels=label, colors=colors, textprops={'fontsize': 8})
        ax1.add_artist(plt.Circle((0, 0), 0.61, color='white'))
        ax1.set_title("", fontsize=8)
        ax1.set_position([0, 0, 0.5, 0.5])

        # Create the histogram
        ax2=sns.histplot(data_year['review_score'], bins=5,fill=sns.color_palette('Blues'))
        ax2.set_title('Total Score Count')
        ax2.set_xlabel("Review Score")
        ax2.set_ylabel("")
        ax2.set_position([0, 0, 0.7, 0.1])

        plt.tight_layout()

        col1, col2 = st.columns(2)
        
        with col1:
            st.pyplot(fig1)
        with col2:
            st.pyplot(fig2)
        #st.pyplot(fig)


    def Preprocessing(text):
        stemmer = nltk.stem.RSLPStemmer()
        text = text.lower().replace('.','').replace(';','').replace('-','').replace(':','').replace(')','')
        stopwords = set(nltk.corpus.stopwords.words('portuguese'))
        stopwords.remove('não')
        stopwords.remove('nem')
        words = [stemmer.stem(i) for i in text.split() if not i in stopwords]
        return (" ".join(words))

    def translation(text):
        translated=ts.translate_text(text,'google', to_language= 'pt')
        return translated

    def new_prediction(text):
        vectorized_text = vectorizer.transform([text])
        pred = loaded_model.predict(vectorized_text)
        return pred

    st.title("Sentiment Analysis!")

    # Create a text box and store the entered text in a variable
    text = st.text_input("Enter the comment that you want to analyze 👇")
    # Display the entered text
    if text:
        # Display the analysis
        if(new_prediction(Preprocessing(translation(text)))[0] == "positive"):
            st.subheader("Your comment is: :green[Positive]")
        elif(new_prediction(Preprocessing(translation(text)))[0] == "negative"):
            st.subheader("Your comment is: :red[Negative]")
        else:
            st.subheader("Your comment is: Neutral")

    # Create a list of years
    years = [2016, 2017, 2018]

    # Use st.selectbox() to create a dropdown menu for the year filter
    st.title("Costumer Satisfaction Score")
    selected_year = st.selectbox("Select a year to filter by:", years)

    st.write(CSAT_graph(comments,selected_year))