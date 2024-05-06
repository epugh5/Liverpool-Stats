import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import altair as alt
import seaborn as sns
import numpy as np
import warnings
warnings.filterwarnings('ignore')





#create columns for liverpool logo
col1, col2, col3 = st.columns(3)
with col1:
    st.write(' ')

with col2:

    st.image('Liverpool_Badge-1_480x480.webp.png',use_column_width='auto')

with col3:
    st.write(' ')

st.title("Liverpool's 2019 Statistics")

st.markdown('''
    :red[Browse Liverpool statistics on opponent teams and their game results for 2019!]''')

#create two tabs for dataset
tabs = ['Opponent Stats', 'Game Result Stats']
selected_tab = st.radio("Select Tabs", tabs)

#import csv data
@st.cache_data
def load_data(csv):
             df = pd.read_csv(csv)
             return df
liverpool = load_data("scores_and_fixtures.csv")

#if elif statement for content in different tabs
if selected_tab == "Opponent Stats":
        st.markdown("### <u>Opponent Stats</u>", unsafe_allow_html=True)

        st.write()
     
        #selectbox for different opponent statistics
        opponent = liverpool['Opponent'].unique() 
        opponent_choice = st.selectbox('Select an Opponent Team:', opponent) 
        filtered_df = liverpool.loc[liverpool['Opponent'] == opponent_choice]
        st.dataframe(filtered_df)
        st.set_option('deprecation.showPyplotGlobalUse', False)


        #description
        st.write("-")
        st.write(''':red[The graph below showcases Liverpools different opponents and the possesions made against these teams compared to the average possesions typically made.]''')
        st.write("-")
        

        #Bar graph showing possesions per team
        plt.figure(figsize=(8,3))

        plot=sns.barplot(x='Opponent',y='Poss', data=liverpool)
        plt.axhline(y=liverpool.Poss.mean(),color='k', xmin=0,xmax=1, alpha=0.8, linestyle='--')
        plt.axhline(y=50,xmin=0, xmax=1, color='red', alpha=0.8, linestyle='--')
        plt.xticks(rotation=90)
        plt.ylim(30,80)
        plot.text(0,liverpool.Poss.mean()+1,"Average Posssession")
        plot.text(0,51,"50% Posssession")

        st.pyplot()
        st.set_option('deprecation.showPyplotGlobalUse', False)


        st.write("")
        st.write("")
        st.write("")

        #description
        st.write(''':red[Below you can select goals for their team, goals agaisnt their team, ending results, possesions, and attendance to games in correlation to the opponent teams. This will give you a great visual for analyzing different outcomes for the 2019 season.]''')
        st.write("")

        #scatter plot map
        x_variable_options = ["GF", "GA", "Result", "Poss", "Attendance"]
        x_variable = st.selectbox("Select a Variable:", x_variable_options)
        y_variable = "Opponent"

        plt.figure(figsize=(7, 5))
        plt.scatter(liverpool[x_variable], liverpool[y_variable])
        plt.xlabel(x_variable)
        plt.ylabel(y_variable)
        plt.title("Scatter Plot")
        plt.grid(True)

        st.pyplot()




elif selected_tab == "Game Result Stats":

        st.markdown("### <u>Game Result Stats</u>", unsafe_allow_html=True)

        #description
        st.write("")
        st.write(''':red[Liverpool won the Champianship game in 2019, they had an outstanding season with a long winning streak consisting of 27 matches with one draw. The pie chart below is a great representation of this accomplishment.]''')
        st.write("")

        #pie chart to show wins, losses, draws
        x=[liverpool['Result'].value_counts().get('W', 0),liverpool['Result'].value_counts().get('D', 0),liverpool['Result'].value_counts().get('L', 0)]
        labels=['Win', 'Draw', 'Loss']
        explode=[0.01,0.01,0.01]

        fig, ax = plt.subplots(figsize=(8, 3))
        ax.pie(x=x, labels=labels, autopct='%1.2f%%', explode=explode)
        ax.axis('equal') 
        st.set_option('deprecation.showPyplotGlobalUse', False)

        st.pyplot()
        st.write("")

        #description
        st.write("")
        st.write(''':red[Browse the graph below for different insights on Liverpool's 
                 impressive possesions in all their game results.]''')
        
        
        #Bar chart showing possesions per game result
        result_labels = {'W': 'Win', 'L': 'Loss', 'D': 'Draw'}
        selected_result = st.selectbox("Choose a Game Result:", [result_labels[result] for result in liverpool['Result'].unique()])
        selected_result_value = [key for key, value in result_labels.items() if value == selected_result][0]
        filtered_df = liverpool[liverpool['Result'] == selected_result_value]
        plt.figure(figsize=(8, 3))
        sns.barplot(x='Result', y='Poss', hue='Venue', data=filtered_df)
        plt.axhline(y=filtered_df['Poss'].mean(), color='k', xmin=0, xmax=1)
        plt.ylim(50, 75)
    
        st.pyplot()

        #description
        st.write("")
        st.write(''':red[Use the heatmap below for a better understanding of the amount of goals scored on liverpools behalf compared to end game results. You can see the patterns for winning games vs losses and draws.]''')
        st.write("")

        #heatmap
        categorical_vars = ["Result", "GA"]
        encoded_df = pd.get_dummies(liverpool[categorical_vars])
        corr_matrix = encoded_df.corr()

        plt.figure(figsize=(8, 3))
        sns.heatmap(corr_matrix, annot=True, cmap='Reds', fmt=".2f")
        plt.title("End game results VS Goals for Liverpool")
        plt.xlabel("Result")
        plt.ylabel("Goals for Liverpool")
        st.pyplot()











        

        
              






