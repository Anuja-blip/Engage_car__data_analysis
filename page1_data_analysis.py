# importing libraries

import streamlit as st
import numpy as np
import pandas as pd
import plotly
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")


def app():
    # reading the file
    df = pd.read_csv('new_engage_file.csv')

    with st.sidebar:
        st.markdown("#### List of Different Types of Visualization ")
        st.text("1.Frequency of Different \nCar Features ")
        st.text("2.Compare the feature \nwith the car price ")
        st.text("3.Car feature vs Average Price \nper cars price range Bar Chart")
        st.text("4.Compare the car Price \nbased on Two features")
    header = st.container()
    with header:
        st.title("WELCOME TO CAR DATA ANALYSIS")
        # enter the no of rows , create a widget

        number_input = st.number_input(
            "how many rows would you like to see ", min_value=1, max_value=1276, value=10, step=1)
        # checkbox for show dataframe
        show_data = st.checkbox("Show Data")
        if show_data:
            st.dataframe(data=df.head(number_input), width=2000, height=1000)

   # frequency of each car feature
    feature1 = st.container()
    with feature1:
        # creating two columns in this container
        st.subheader("Frequency of Different Car Features")
        input_col, chart_col = st.columns(2)

        # creating a selectbox in the left column to
        features = input_col.selectbox("Which feature's frequency chart would you like to see", options=[
            'Make', 'Body_Type', 'Fuel_Type', 'Drivetrain', 'Cylinders', 'Seating_Capacity'], index=0)

        # max value for the slider
        maxValue = len(pd.unique(df[features]))

        # storing the value selected in the slider
        top_n = input_col.slider("How many  top "+features + " would you like to see", min_value=1,
                                 max_value=maxValue, value=5, step=1)

        # dataframe to store the frequecy of the feature selected
        new_df = pd.DataFrame(df[features].value_counts()).head(top_n)
        new_df = new_df.reset_index()
        new_df.columns = [features, 'count']

        # create the pie chart
        fig = px.pie(new_df, values='count', names=features)
        fig.update_layout(showlegend=False, width=300, height=300,
                          margin=dict(l=1, r=1, b=1, t=1))
        chart_col.write(fig)
        chart_col.text(
            "To see the name of the selected feature\n hover over the pie chart")

        # create a table to store the feature and their frequency
        input_col.table(df[features].value_counts().head(top_n))

    # container for comparing a car feature with Price
    feature2 = st.container()
    with feature2:
        st.subheader("Compare the feature with the car price")
        # create two columns
        input_col, table_col = st.columns(2)

        # selectbox to select a feature for the x axis
        x_axis = input_col.selectbox("which feature would you like to compare", options=[
            'Make', 'Variant', 'Body_Type', 'Engine_Type', 'Fuel_Type', 'Drivetrain', 'Cylinders', 'Seating_Capacity'], index=0)

        # max value for the slider
        # total unique types for each feature
        maxValue = len(pd.unique(df[x_axis]))
        top_n = input_col.slider("How many cars price would you like to see", min_value=1,
                                 max_value=maxValue, value=5, step=1)
        
        # selectbox for graph type
        chart_type = st.radio("Select the Chart Type",
                              ("BAR GRAPH", "LINE CHART", "SCATTER PLOT"))

        # group the selected feature according to the Maximum price
        PriceByType = df.groupby(x_axis).max().sort_values(
            'Ex_Showroom_Price', ascending=False).head(top_n)
        PriceByType = PriceByType.reset_index()

        if chart_type == "BAR GRAPH":
            fig = px.bar(x=x_axis, y="Ex_Showroom_Price", text_auto='.2s', hover_data=[
                         'Make', 'Model', 'Variant'], color=x_axis, data_frame=PriceByType)

        if chart_type == "LINE CHART":
            fig = px.line(x=x_axis, y="Ex_Showroom_Price",  hover_data=[
                'Make', 'Model', 'Variant'], data_frame=PriceByType)

        if chart_type == "SCATTER PLOT":
            fig = px.scatter(x=x_axis, y="Ex_Showroom_Price",  hover_data=[
                'Make', 'Model', 'Variant'], data_frame=PriceByType)
        
        st.markdown("###### Most Expensive "+x_axis+"s in decending order")
        # create the chart
        st.plotly_chart(fig, container_width=True)
        st.text("The table of "+x_axis+",  Model, Price and their count")

        # create a table to store the feature model, variant  and their count
        st.table(df[[x_axis, 'Model', 'Ex_Showroom_Price']
                    ].value_counts().head(top_n))
     
    # container for Car feature vs Average Price per cars price range Bar Chart
    feature3 = st.container()
    with feature3:
        st.subheader(
            "Car feature vs Average Price for every cars price range Bar Chart")
    left_col, right_col = st.columns(2)  # create two columns for input
    # selectbox to select a feature for the x axis
    features = left_col.selectbox("Which feature would you like to compare ", options=[
        'Body_Type', 'Fuel_Type', 'Drivetrain', 'Engine_Type', 'Cylinders', 'Seating_Capacity','Seats_Material'], index=2)
    
    right_col.markdown("###### Description of price range")
    right_col.text(
        "Budget= under 10 lakhs \nMedium=between 10 -50 lakhs \nMedium_High= between 50 lakhs - 1 cr \nHiighend=Above 1 Cr")

    new_df = pd.DataFrame(df.groupby([features, 'carsrange'])[
        'Ex_Showroom_Price'].mean().unstack(fill_value=0))

    fig = px.histogram(df, x=features, y="Ex_Showroom_Price",
                       color='carsrange', barmode='group',
                       histfunc='avg',
                       height=400)
    st.plotly_chart(fig)


# container for comparing car's price based on two features
    feature4 = st.container()
    with feature4:
        st.subheader("Compare the car Price based on Two features")
        input_col, table_col = st.columns(2)

     # create a selectbox for selecting a feature for x_axis
        x_axis = input_col.selectbox(" Select the First feature ", options=[
            'Mileage', 'Kerb_Weight', 'Displacement'], index=0)

    # selectbox for another feature
        colour = input_col.selectbox("Select another feature ", options=[
            'Make','Body_Type', 'Fuel_Type', 'Drivetrain'], index=0)
     # radio buttom for chart type
        chart_type = table_col.radio("Select the Chart Type",
                                     ("2D Scatter Plot", "3D Scatter Plot"))
        st.markdown("###### PRICE vs "+x_axis+" for differnt "+colour)

        if chart_type == "2D Scatter Plot":
            fig = px.scatter(df, x=x_axis, y="Ex_Showroom_Price", color=colour)

        if chart_type == "3D Scatter Plot":
            fig = px.scatter_3d(df, x=x_axis, z='Ex_Showroom_Price',
                                y=colour, color='Make', width=800, height=750)
        fig.update_layout(showlegend=True)

      #   show the chart
        st.plotly_chart(fig, container_width=True)
