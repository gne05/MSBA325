#Import Libraries
import streamlit as st
import pandas as pd
import hydralit_components as hc
import os
from io import StringIO
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns

#Import the Dataset
data = pd.read_csv("dataset.csv")

# Set Page Icon,Title, and Layout
st.set_page_config(layout="wide",  page_title = "Sleep Health and Lifestyle")

#Set up the navigation bar
menu_data = [
{'label':"Introduction", 'icon': "bi bi-house"},
{'label':"Lifestyle", 'icon': "fas fa-suitcase"},
{'label':"Medical Conditions", 'icon': "fas fa-hospital"}]

over_theme = {'txc_inactive': 'white','menu_background':'#0178e4', 'option_active':'white'}

menu_id = hc.nav_bar(
    menu_definition=menu_data,
    override_theme=over_theme,
    hide_streamlit_markers=True,
    sticky_nav=True,
    sticky_mode='sticky',
)

# Introduction Page
if menu_id == "Introduction":
    st.markdown("<hr style='border-top: 3px solid black;'>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: black;'>Sleep Health and Lifestyle <i class='bi bi-heart-fill' style='color: red;'></i> </h2>", unsafe_allow_html=True)
    st.markdown("<hr style='border-top: 3px solid black;'>", unsafe_allow_html=True)
    st.subheader("Sleep is a fundamental and essential aspect of human life, playing a crucial role in maintaining overall health and well-being")
    sleep1 = st.image('sleep1.jpg', width=1000)

    st.markdown("<hr style='border-top: 3px solid black;'>", unsafe_allow_html=True)
    st.subheader("Lack of sleep can lead to: chronic health conditions, weakened immuned system, mental health issues as well as reduced quality of life")
    st.markdown(" ")
    st.markdown(" ")
    st.subheader("The aim of this study is to visualize using interactive figures the relationship between a person's lifestyle and his quality of sleep. In addition, we will check for the relationship between bad sleep habits and any medical condition")

# Lifestyle Page
if menu_id == "Lifestyle":
    st.markdown("<hr style='border-top: 3px solid black;'>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: black;'>Lifestyle and Occupation <i class='bi bi-heart-fill' style='color: red;'></i> </h2>", unsafe_allow_html=True)
    st.markdown("<hr style='border-top: 3px solid black;'>", unsafe_allow_html=True)

    st.subheader("This page is to analyze the quality of sleep of a person in relation to his lifestyle, occupation and gender")
    st.markdown("<hr style='border-top: 3px solid black;'>", unsafe_allow_html=True)

    with open('dataset.csv', 'rb') as file:
        content = file.read().decode('utf-8', errors='replace')

    df = pd.read_csv(StringIO(content))

    occupation = st.sidebar.selectbox("Select Occupation:", df['Occupation'].unique())
  
# Calculate the average sleep duration and quality for each Occupation
    filtered_df = df[df['Occupation'] == occupation]
    avg_sleep_duration = filtered_df['Sleep Duration'].mean()
    avg_sleep_quality = filtered_df['Quality of Sleep'].mean()

    
# Display the selected occupation and average sleep data
    st.markdown(" ")
    st.markdown(" ")
    st.markdown(" ")

    st.write(f"Average Sleep Duration for {occupation}: {avg_sleep_duration:.2f} hours")
    st.write(f"Average Sleep Quality for {occupation}: {avg_sleep_quality:.2f}")

    # Create a bar chart
    bar_colors = ['red', 'blue']
    fig = go.Figure()

    # Add bars for Sleep Duration and Sleep Quality
    fig.add_trace(go.Bar(x=['Sleep Duration', 'Sleep Quality'], y=[avg_sleep_duration, avg_sleep_quality],marker_color= bar_colors))

    # Set the chart title and labels
    fig.update_layout(
        title=f'Sleep Statistics for {occupation}',
        xaxis_title='Metric',
        yaxis_title='Average Value',
    )

    # Show the bar chart
    st.plotly_chart(fig)

    st.markdown("<hr style='border-top: 3px solid black;'>", unsafe_allow_html=True)

# Calculate the average sleep duration and quality for each gender
    gender = st.sidebar.selectbox("Select Gender:", df['Gender'].unique())
    # Calculate the average sleep duration and quality for each gender
    filtered_df = df[df['Gender'] == gender]
    avg_sleep_duration = filtered_df['Sleep Duration'].mean()
    avg_sleep_quality = filtered_df['Quality of Sleep'].mean()

    
# Display the selected gender and average sleep data
    st.write(f"Average Sleep Duration for {gender}: {avg_sleep_duration:.2f} hours")
    st.write(f"Average Sleep Quality for {gender}: {avg_sleep_quality:.2f}")

    # Create a bar chart
    bar_colors = ['pink', 'green']
    fig = go.Figure()

    # Add bars for Sleep Duration and Sleep Quality
    fig.add_trace(go.Bar(x=['Sleep Duration', 'Sleep Quality'], y=[avg_sleep_duration, avg_sleep_quality],marker_color= bar_colors))

    # Set the chart title and labels
    fig.update_layout(
        title=f'Sleep Statistics for {gender}',
        xaxis_title='Metric',
        yaxis_title='Average Value',
    )

    # Show the bar chart
    st.plotly_chart(fig)

    st.markdown("<hr style='border-top: 3px solid black;'>", unsafe_allow_html=True)

#Display the count of sleep disorders by occupation
    sleep_disorder = st.sidebar.selectbox("Select Sleep Disorder:", df['Sleep Disorder'].unique())
    filtered_df = df[df['Sleep Disorder'] == sleep_disorder]

    fig = px.histogram(
    filtered_df,
    x='Occupation',
    title=f'Sleep Disorder Count per Occupation for {sleep_disorder}',
    )

    fig.update_layout(xaxis_title='Occupation', yaxis_title='Count')

    st.plotly_chart(fig)

    st.markdown("<hr style='border-top: 3px solid black;'>", unsafe_allow_html=True)

# Calculate the average physical activity level for each sleep duration
    average_activity = df.groupby('Sleep Duration')['Physical Activity Level'].mean().reset_index()

    # Create a scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(average_activity['Physical Activity Level'], average_activity['Sleep Duration'], marker='o')

    # Annotate each point with sleep duration value
    for index, row in average_activity.iterrows():
        plt.annotate(f"Sleep: {row['Sleep Duration']} hrs", (row['Physical Activity Level'], row['Sleep Duration']), textcoords='offset points', xytext=(0,10), ha='center')

    # Customize the plot
    plt.title('Average Physical Activity Level vs. Sleep Duration')
    plt.xlabel('Average Physical Activity Level')
    plt.ylabel('Sleep Duration (hours)')

    # Show the plot
    st.pyplot(plt)

if menu_id == "Medical Conditions":
    st.markdown("<hr style='border-top: 3px solid black;'>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: black;'>Medical Conditions<i class='bi bi-heart-fill' style='color: red;'></i> </h2>", unsafe_allow_html=True)
    st.markdown("<hr style='border-top: 3px solid black;'>", unsafe_allow_html=True)

    st.subheader("This page is to analyze if a bad quality of sleep can lead to health and medical conditions")
    st.markdown("<hr style='border-top: 3px solid black;'>", unsafe_allow_html=True)    

    st.sidebar.header('Sleep Duration Filter')
    sleep_duration_filter = st.sidebar.slider('Select Sleep Duration Range', min(data['Sleep Duration']), max(data['Sleep Duration']), (6.5, 8.0))

    filtered_data = data[(data['Sleep Duration'] >= sleep_duration_filter[0]) & (data['Sleep Duration'] <= sleep_duration_filter[1])]

    # Calculate the average heart rate for the filtered data
    average_heart_rate = filtered_data['Heart Rate'].mean()

    # Create a DataFrame with counts of BMI categories for each sleep duration filter
    count_data = filtered_data.groupby('BMI Category').size().reset_index(name='Count')

    # Display the average heart rate as text
    st.write(f'Average Heart Rate: {average_heart_rate:.2f} bpm')

    # Plotly bar chart
    fig = px.bar(count_data, x='BMI Category', y='Count', title=f'Count of BMI Categories for Sleep Duration between {sleep_duration_filter[0]} and {sleep_duration_filter[1]} hours')

    # Streamlit app
    st.title('Sleep Duration and BMI Category Visualization')

    # Display the filtered data
    st.write(f'Showing data for Sleep Duration between {sleep_duration_filter[0]} and {sleep_duration_filter[1]} hours:')
    # st.write(filtered_data)
    st.write(filtered_data[['BMI Category', 'Blood Pressure', 'Heart Rate']])

    # Display the Plotly chart
    st.plotly_chart(fig)




   






