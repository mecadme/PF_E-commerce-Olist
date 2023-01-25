import streamlit as st
import translators as ts
import nltk   
import pickle

filename='model.sav'
loaded_model = pickle.load(open(filename, 'rb'))

with open('vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

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