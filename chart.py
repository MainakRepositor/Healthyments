import pandas as pd
import plotly.express as px
import streamlit as st

def chart(po, su):
        
        #Define Colors
        if po>=0:
            c1="#42f598"
        else:
            c1="#fa7066"
        
        #Convert lists to Pandas Datafram
        data = pd.DataFrame(
            [[po,0],[0,su]],
            index = ["Polarity", "Subjectivity"],
            columns = ["Polarity", "Subjectivity"]
        )
        
        #Make Figure
        fig = px.bar(
            data,
            labels  = {
                "index" : "",
                "value" : "value"
            },
            color_discrete_sequence=[c1,"#16d3f5"]
        )
        fig.update_layout(legend=dict(
            orientation="v",
            yanchor="bottom",
            y=-0.7,
            xanchor="left",
            x=0.01
            ))
          
        #Plot Fig
        st.plotly_chart(fig, use_container_width=True)

def tweetChart(positive, negative, neutral):
    data = pd.DataFrame(
            [
                [positive,0, 0],
                [0,negative, 0], 
                [0, 0, neutral]
            ],
            index = ["Positive", "Negative", "Neutral"],
            columns = ["No Of Positive Tweets", "No Of Negative Tweets", "No Of Neutral Tweets"]
        )
    
    #Make Figure
    fig = px.bar(
        data,
        labels  = {
            "index" : "Sentiment",
            "value" : "Number Of Tweets"
        },
        color_discrete_sequence=["#42f598", "#fa7066", "#16d3f5"]
    )
    fig.update_layout(legend=dict(
            orientation="v",
            yanchor="bottom",
            y=-0.7,
            xanchor="left",
            x=0.01
            ))
    #Plot Fig
    st.plotly_chart(fig, use_container_width=True)

def tweet_pie(positive, negative, neutral):
    data = {
        "polarity": pd.Series([positive, negative, neutral], index=["positive", "negative", "neutral"]),
    }
    data = pd.DataFrame(data)

    fig = px.pie(data, values='polarity', names=data.index, color=data.index,
                color_discrete_map={'positive':'#42f598',
                                    'negative':'#fa7066',
                                    'neutral':'#16d3f5'})
    fig.update_layout(legend=dict(
            orientation="v",
            yanchor="bottom",
            y=-0.7,
            xanchor="left",
            x=0.01
            ))
    st.plotly_chart(fig, use_container_width=True)