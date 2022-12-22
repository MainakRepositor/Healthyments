import streamlit as st
from Sentiment import *
from chart import *
from Scrape import *
import datetime

from PIL import Image
import corpora
#Page Config
st.set_page_config(page_title="ITSA")
st.markdown("# Interactive Text Sentiment Analysis System")
st.markdown("")
st.sidebar.markdown("# Navigation Pane")
show_page = st.sidebar.selectbox(label="Choose page", options=["Welcome", "Type In Prompt", "Scrape From Twitter"])



if show_page=="Welcome":
    '''
        ##### Welcome, this interactive web app is aimed to demonstrate the working of text sentiment analysis
    '''
    image = Image.open('Photos/photo-1523961131990-5ea7c61b2107.jpeg')
    st.image(image)
    
    '''
        ---
        ##### To begin:
        - ###### Open the navigation pane
        - ###### Chose the method to be used for sentiment analysis [Select the desired page from the drop down]
        - ###### Play around and view analysis
        ---
        ##### Few things to keep in mind

        - ###### Polarity refers to the strength of the emotion 
            - -1 being strongly negative and
            - +1 being strongly positive
        - ###### Subjectivity as the name suggests, refers to how subjective the text is
            - 0 being completely objective [for eg facts]
            - 1 being completely subjective 
        - ###### As with all machine learning systems, it will not be 100% accurate and might have biases
        ---
    '''

elif show_page=="Type In Prompt":

    image = Image.open("Photos/photo-1529236183275-4fdcf2bc987e.jpeg")
    st.image(image)

    st.markdown("### Evaluate Your Custom Text")

    txt = st.text_area(label="Enter text")
    corrspell = st.checkbox(label="Use spelling corrector")
    evaluate = st.button(label="Compute Sentiment")

    #main
    if evaluate and txt!="":
        
        with st.spinner("Computing Sentiment"):
            
            po,su = sentiment(txt, corrspell)
            col1, col2 = st.columns([1, 1])

            with col1:
                st.write("Polarity : ")
                st.write(po)
                
            with col2:
                st.write("Subjectivity")
                st.write(su)
            
            chart(po, su)

else:

    image = Image.open('Photos/sdfsf.png')
    st.image(image)

    st.markdown("### Evaluate Twitter Fetched Text")
    txt = st.text_area(label="Enter what you want to search")
    tweetCount = st.slider(label="Choose no of tweets to scrape", min_value=1, value=10, max_value=1150)
    
    
    #Date Picker
    col1, col2 = st.columns([1, 1])
    with col1:
        begin=st.date_input(label="Starting Date", value=datetime.date.today()-datetime.timedelta(days=1), min_value=datetime.date.today()-datetime.timedelta(days=1000), max_value=datetime.date.today()-datetime.timedelta(days=1))
    
    with col2:
        finish=st.date_input(label="Finishing Date", value=datetime.date.today(), min_value=datetime.date.today()-datetime.timedelta(days=999), max_value=datetime.date.today())
    
    #Ensure starting date before finishing date
    if finish<=begin:
        st.error("Error \nStarting date must be < Finishing Date") 
        st.stop()
    get_tweet = st.button(label="Scrape and Analyze tweets")
    
    if get_tweet:

        if txt=="":
            st.error("Error \nEmpty search string")
            st.stop()
    
        with st.spinner("Loading"):
            

            data, data_clean = scrape_tweets(txt, tweetCount, begin, finish)
            
            if len(data)==0:
                st.error("No data")
                st.stop()

            st.markdown("")
            st.markdown("")
            st.markdown("")

            st.markdown("## Result")
            st.markdown("---")
            
            tweetSentiment(data_clean)

            with st.expander("Show scraped Twitter tweets"):
                                
                st.markdown("#### Raw")
                st.write(data)
                
                st.markdown("#### Processed")
                st.write(data_clean)


