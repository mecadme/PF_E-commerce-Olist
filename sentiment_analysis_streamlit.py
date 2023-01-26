#libries
import streamlit as st
import translators as ts
import nltk   
import pickle
import pandas as pd
import matplotlib.pyplot as plt                                
import seaborn as sns
# import the models and the data

#dataset
comments=pd.read_csv('Datasets\comments.csv')

# ML sentiment analysis model    
filename='model.sav'
loaded_model = pickle.load(open(filename, 'rb'))

#vectorizer
with open('vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)


#functions

def year_percentage(dataFrame=comments, year=2016):
    data_year=dataFrame[dataFrame['review_creation_year']==year]
    total_comments_year=data_year['review_type'].value_counts()
    percentage_positives_year=round(((total_comments_year[0]+total_comments_year[2])/total_comments_year.sum())*100,2)
    return(percentage_positives_year, 100-percentage_positives_year) 

def CSAT_graph(dataFrame=comments, year=2016):
    data_year=dataFrame[dataFrame['review_creation_year']==year]
    # Create a figure with 2 subplots (1 row, 2 columns)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(5,2))

    # Create the semi-donut chart
    label = ["Unsatisfied", "Satisfied"]
    val = [year_percentage(dataFrame, year)[1], year_percentage(dataFrame, year)[0]]

    # append data and assign color
    label.append("")
    val.append(sum(val))  # 50% blank
    colors = ['gray', 'lightblue', 'white']

    # plot
    ax1.pie(val, labels=label, colors=colors)
    ax1.add_artist(plt.Circle((0, 0), 0.61, color='white'))
    ax1.set_title("Semi-Donut Chart")
    ax1.set_position([0, 0, 0.7, 0.1])

    # Create the histogram
    ax2=sns.histplot(data_year['review_score'], bins=5,fill=sns.color_palette('Blues'))
    ax2.set_title('Histogram')

    plt.tight_layout()
    st.pyplot(fig)

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

st.write("Sentiment Analysis!")
st.write('version 0.1')

# Create a text box and store the entered text in a variable
text = st.text_input("Enter the comment that you want to analyze:")
# Display the entered text
st.write("Your comment:", text)

# Display the analysis
st.write("Your comment is: ", new_prediction(Preprocessing(translation(text))))

# Create a list of years
years = [2016, 2017, 2018]

# Use st.selectbox() to create a dropdown menu for the year filter
selected_year = st.selectbox("Select a year to filter by:", years)

st.write(CSAT_graph(comments,selected_year))