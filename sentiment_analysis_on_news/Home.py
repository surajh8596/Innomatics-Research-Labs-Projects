import streamlit as st
import os
import pickle
import pandas as pd
from matplotlib import image

#Add heading
st.header("Sentiment Analaysis on Times of India News Headlines")

#Resouece path
file_dir=os.path.dirname(os.path.abspath(__file__))
resource_file=os.path.join(file_dir, "resources")

#CountVectorizer path
vector_path=os.path.join(resource_file, "vectorizer")
vector=os.path.join(vector_path, "vectorizer.pkl")
count_vectorizer=pickle.load(open(vector, 'rb'))

#Best Model path
model_path=os.path.join(resource_file, "model")
best_model=os.path.join(model_path, "decision_tree.pkl")
decision_tree_clssifier=pickle.load(open(best_model, 'rb'))

#Function to clean text
import nltk
nltk.download('stopwords')
nltk.download('wordnet')
from nltk.corpus import stopwords
import re
from nltk.stem import  PorterStemmer, WordNetLemmatizer
stem=PorterStemmer()
lemma=WordNetLemmatizer()
stopword=stopwords.words('english')

def clean_text(text):
    text=str(text).lower()
    text=re.sub(pattern="[^a-zA-z]", repl=" ", string=text)
    text = [word for word in text.split(' ') if word not in stopword]
    text=" ".join(text)
    text = [lemma.lemmatize(word) for word in text.split(' ')]
    text=" ".join(text)
    return text

#Input from user
headlines=st.text_input(label="Enter News Headline to check Sentiment", placeholder="Enter News Headline")
news=pd.DataFrame({"headline":[headlines]})

#apply clean_text function
news['headline']=news['headline'].apply(clean_text)

#apply vectorization
headline_tf=count_vectorizer.transform(news['headline'])

#Predict the sentiment
sentiment=decision_tree_clssifier.predict(headline_tf)[0]

#Image path
image_file=os.path.join(resource_file, "image")
positive_face=os.path.join(image_file, "happy.jpg")
negative_face=os.path.join(image_file, "sad.jpg")
neutral_face=os.path.join(image_file, "neutral.jpg")

button=st.button("See Sentiment")

if button==True:
    if sentiment==0:
        st.subheader("Sentiment of News Headline is Neutral")
        img = image.imread(neutral_face)
        st.image(img)
    elif sentiment==1:
        st.subheader("Sentiment of News Headline is Positive")
        img = image.imread(positive_face)
        st.image(img)
    elif sentiment==2:
        st.subheader("Sentiment of News Headline is Negative")
        img = image.imread(negative_face)
        st.image(img)

#Background Image
page_bg_img = '''
<style>
.stApp {
background-image: url("https://thumbs.dreamstime.com/b/television-breaking-news-studio-interior-realistic-vector-tv-show-broadcasting-room-pedestal-podium-desk-big-displays-220724190.jpg");
background-size: cover;
background-position: top center;
background-repeat: no-repeat;
background-attachment: local;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)
