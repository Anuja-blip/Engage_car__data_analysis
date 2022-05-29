#importing libraries
import streamlit as st
import random
import numpy as np
import pandas as pd
import plotly
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
from st_aggrid import AgGrid

def app():
    #reading file
    df = pd.read_csv('new_engage_file.csv')
    
    st.text("Buying a car is an important decision and\na daunting task which might turn out to be intimidating for first-time buyers.\nBut a little research eases a person’s car buying decision . \nYou can run through a car comparison here.")
    
    #create a side bar where u can choose 2 or 3 cars to compare
    with st.sidebar:
        st.markdown("**CHOOSE **")
        choose = st.radio("", ['2cars', '3cars']) #radio buttons
    
    # user choose 2 cars
    if choose == '2cars':
                
        st.subheader('SELECT TWO CARS OF YOUR CHOICE')
        left_col, right_col = st.columns(2) #create two columns 
        count = 0# key for creating multiple similar selectbox

        with left_col:
            
            #selectbox to store the make of the cars
            brand = left_col.selectbox(
                "Select Make", options=df['Make'].unique(), index=0, key=count)
            new_df = df[df.Make == brand] #store the dataframe where make is selected brand name
            
            #selectbox to store the model names corresponding to the selected brand/make name
            model_name = left_col.selectbox(
                "Select a Model", options=new_df['Model'].unique(), index=0, key=count)
            new_df = df[df.Model == model_name] #store the dataframe  where model_name is selected model from the selectbox
            
            #selectbox to store the variant corresponding to the selected brand/make name and model 
            variant_name = left_col.selectbox(
                "select a Variant", options=new_df['Variant'].unique(), index=0, key=count)
        
        #in right column create  3 selectbox of make, model, variant similar to left column
        with right_col:

            count += 1
            brand2 = right_col.selectbox(
                "Select Make", options=df['Make'].unique(), index=0, key=count)
            new_df = df[df.Make == brand2]

            model_name2 = right_col.selectbox(
                "Select a Model", options=new_df['Model'].unique(), index=0, key=count)
            new_df = df[df.Model == model_name2]

            variant_name2 = right_col.selectbox(
                "select a Variant", options=new_df['Variant'].unique(), index=0, key=count)

        #container - show the selected car details
        car_details = st.container()
        with car_details:
            #function which return the selected features cell value for selected make, model and variant
            #for the first selected car
            def first_car(x):
                value1 = df.loc[(df['Make'] == brand) & (
                    df['Model'] == model_name) & (df['Variant'] == variant_name)][x].values[0]
                return value1
            
            #function which return the selected features cell value for selected make, model and variant
            #for the second selected car
            def second_car(x):
               value2 = df.loc[(df['Make'] == brand2) & (
                    df['Model'] == model_name2) & (df['Variant'] == variant_name2)][x].values[0]
               return value2
            
           
        #store the summary of two cars in an expander
        with st.expander("SUMMARY"):
             #dataframe to store the summary(like - price, fuel_type etc) of the two cars 
            summary = [
                ['', brand, brand2],
                ['Model', first_car('Model'), second_car('Model')],
                ['Ex_Showroom_Price(Rs.)', first_car('Price'),
                 second_car('Price')],
                ['Body Type', first_car('Body_Type'), second_car('Body_Type')],
                ['Power', first_car('Power'), second_car('Power')],
                ['Mileage(km/l)', first_car('Mileage'),
                 second_car('Mileage')],
                ['Fuel Type', first_car('Fuel_Type'), second_car('Fuel_Type')]
            ]
            
            #create table to store the summary of two cars 
            fig = ff.create_table(summary, height_constant=20)
            for i in range(len(fig.layout.annotations)):
                fig.layout.annotations[i].font.size = 20
            st.plotly_chart(fig)
        
        #store the ENGINE DETAILS of two cars in an expander
        with st.expander("Engine Details"):
            #dataframe to store the engine details(like - displacement, engine_type etc) of the two cars 
            engine_details = [
                ['', brand, brand2],
                ['Engine_Type', first_car('Engine_Type'),
                 second_car('Engine_Type')],
                ['Displacement(cc)', first_car('Displacement'),
                 second_car('Displacement')],
                ['Torque', first_car('Torque'), second_car('Torque')],
                ['Cylinders no', first_car('Cylinders'), second_car('Cylinders')],
                ['Drivetrain', first_car('Drivetrain'), second_car('Drivetrain')],
                ['Emission_Norm', first_car('Emission_Norm'),
                 second_car('Emission_Norm')],
            ]
            #create table to store the summary of two cars 
            fig = ff.create_table(engine_details, height_constant=20)
            for i in range(len(fig.layout.annotations)):
                fig.layout.annotations[i].font.size = 20
            st.plotly_chart(fig)
            
        #store the DIMENSIONS of two cars in an expander
        with st.expander("Dimensions"):
             #dataframe to store the Dimensions(like - weight, length etc) of the two cars    
            dimensions=[
                 ['',brand,brand2],
                 ['Length (mm)',first_car('Length'),second_car('Length')],
                 ['Width (mm)',first_car('Width'),second_car('Width')],
                 ['Height (mm)',first_car('Height'),second_car('Height')],
                 ['Gross weight',first_car('Gross_Vehicle_Weight'),second_car('Gross_Vehicle_Weight')],
                 ['Kerb Weight( kg)',first_car('Kerb_Weight'),second_car('Kerb_Weight')],
                 ['Wheelbase',first_car('Wheelbase'),second_car('Wheelbase')],
                 ['Turning Radius',first_car('Minimum_Turning_Radius'),second_car('Minimum_Turning_Radius')]      
                           
             ] 
            #create table to store the dimensions of two cars 
            fig = ff.create_table(dimensions, height_constant=20)
            for i in range(len(fig.layout.annotations)):
                fig.layout.annotations[i].font.size = 20
            st.plotly_chart(fig)  
        
        #store the Luxary_Entertainment of two cars in an expander
        with st.expander("Luxary_Entertainment"):
             #dataframe to store the Luxary_Entertainment(like - weight, length etc) of the two cars    
            Luxary_Entertainment=[
                 ['',brand,brand2],
                 ['Seating_Capacity',first_car('Seating_Capacity'),second_car('Seating_Capacity')],
                 ['Seats_Material',first_car('Seats_Material'),second_car('Seats_Material')],
                 ['Doors',first_car('Doors'),second_car('Doors')],
                 ['CD_Player',first_car('CD_/_MP3_/_DVD_Player'),second_car('CD_/_MP3_/_DVD_Player')],
                 ['USB_Ports',first_car('USB_Ports'),second_car('USB_Ports')],
                 ['Bluetooth',first_car('Bluetooth'),second_car('Bluetooth')],
                 ['Infotainment_Screen',first_car('Infotainment_Screen'),second_car('Infotainment_Screen')],
            ] 
            #create table to store the Luxary_Entertainment of two cars 
            fig = ff.create_table(Luxary_Entertainment, height_constant=20)
            for i in range(len(fig.layout.annotations)):
                fig.layout.annotations[i].font.size = 20
            st.plotly_chart(fig)      

    # user choose 3 cars
    if choose == '3cars':
        st.subheader('SELECT THREE CARS OF YOUR CHOICE')
        
        left_col, mid_col, right_col = st.columns(3) #create  3 columns       
        count = 0 #key for creating multiple similar selectbox
        
        
        with left_col:
            #selectbox to store the make of the cars
            brand = left_col.selectbox(
                "Select Make", options=df['Make'].unique(), index=0, key=count)
            new_df = df[df.Make == brand]#store the dataframe where make is selected brand name
            
            #selectbox to store the model names corresponding to the selected brand/make name
            model_name = left_col.selectbox(
                "Select a Model", options=new_df['Model'].unique(), index=0, key=count)
            new_df = df[df.Model == model_name]#store the dataframe  where model_name is selected model from the selectbox
            
            #selectbox to store the variant corresponding to the selected brand/make name and model 
            variant_name = left_col.selectbox(
                "select a Variant", options=new_df['Variant'].unique(), index=0, key=count)
        
        #in mid column create  3 selectbox of make, model, variant similar to left column
        with mid_col:

            count += 1
            brand2 = mid_col.selectbox(
                "Select Make", options=df['Make'].unique(), index=0, key=count)
            new_df = df[df.Make == brand2]

            model_name2 = mid_col.selectbox(
                "Select a Model", options=new_df['Model'].unique(), index=0, key=count)
            new_df = df[df.Model == model_name2]

            variant_name2 = mid_col.selectbox(
                "select a Variant", options=new_df['Variant'].unique(), index=0, key=count)
        
        #in right column create  3 selectbox of make, model, variant similar to left column
        with right_col:

            count += 1
            brand3 = right_col.selectbox(
                "Select Make", options=df['Make'].unique(), index=0, key=count)
            new_df = df[df.Make == brand3]

            model_name3 = right_col.selectbox(
                "Select a Model", options=new_df['Model'].unique(), index=0, key=count)
            new_df = df[df.Model == model_name3]

            variant_name3 = right_col.selectbox(
                "select a Variant", options=new_df['Variant'].unique(), index=0, key=count)
        
        #container - show the selected car details
        car_details = st.container()

        with car_details:
            #function which return the selected features cell value for selected make, model and variant
            #for the first selected car
            def first_car(x):
                df1 = df.loc[(df['Make'] == brand) & (
                    df['Model'] == model_name) & (df['Variant'] == variant_name)][x].values[0]
                return df1
            
            #function which return the selected features cell value for selected make, model and variant
            #for the second selected car
            def second_car(x):
                df2 = df.loc[(df['Make'] == brand2) & (
                    df['Model'] == model_name2) & (df['Variant'] == variant_name2)][x].values[0]
                return df2
            
            #function which return the selected features cell value for selected make, model and variant
            #for the third selected car
            def third_car(x):
                df3 = df.loc[(df['Make'] == brand3) & (
                    df['Model'] == model_name3) & (df['Variant'] == variant_name3)][x].values[0]
                return df3
            
            
                    
         #store the summary of three cars in an expander     
        with st.expander("SUMMARY"):
        #dataframe to store the summary(like - price, fuel_type etc) of the two cars 
            summary = [
                ['', brand, brand2, brand3],
                ['Model', first_car('Model'), second_car('Model'), third_car('Model')],
                ['Price(Rs.)', first_car('Price'),
                 second_car('Price'), third_car('Price')],
                ['Body Type', first_car('Body_Type'), second_car(
                    'Body_Type'), third_car('Body_Type')],
                ['Power', first_car('Power'), second_car('Power'), third_car('Power')],
                ['Fuel Type', first_car('Fuel_Type'), second_car(
                    'Fuel_Type'), third_car('Fuel_Type')]
            ]
        
            #create table to store the summary of three cars 
            fig = ff.create_table(summary, height_constant=20)
            for i in range(len(fig.layout.annotations)):
                fig.layout.annotations[i].font.size = 20
            st.plotly_chart(fig)
        
        #store the ENGINE DETAILS of three cars in an expander
        with st.expander("Engine Details"):
             #dataframe to store the engine details(like - displacement, engine_type etc) of the three cars 
            engine_details = [
                ['', brand, brand2, brand3],
                ['Displacement(cc)', first_car('Displacement'),
                 second_car('Displacement'), third_car('Displacement')],
                ['Torque', first_car('Torque'), second_car('Torque'), third_car('Torque')],
                ['Cylinders no', first_car('Cylinders'), second_car(
                    'Cylinders'), third_car('Cylinders')],
                ['Drivetrain', first_car('Drivetrain'), second_car(
                    'Drivetrain'), third_car('Drivetrain')],
                ['Emission_Norm', first_car('Emission_Norm'),
                 second_car('Emission_Norm'), third_car('Emission_Norm')],
            ]
            #create table to store the engine details of three cars 
            fig = ff.create_table(engine_details, height_constant=20)
            for i in range(len(fig.layout.annotations)):
                fig.layout.annotations[i].font.size = 20
            st.plotly_chart(fig)
        
        #store the DIMENSIONS of three cars in an expander
        with st.expander("Dimensions"):
             #dataframe to store the Dimensions(like - weight, length etc) of the three cars    
            dimensions=[
                 ['',brand,brand2,brand3],
                 ['Length (mm)',first_car('Length'),second_car('Length'),third_car('Length')],
                 ['Width (mm)',first_car('Width'),second_car('Width'),third_car('Width')],
                 ['Height (mm)',first_car('Height'),second_car('Height'),third_car('Height')],
                 ['Gross weight',first_car('Gross_Vehicle_Weight'),second_car('Gross_Vehicle_Weight'),third_car('Gross_Vehicle_Weight')],
                 ['Kerb Weight (kg)',first_car('Kerb_Weight'),second_car('Kerb_Weight'),third_car('Kerb_Weight')],
                 ['Wheelbase',first_car('Wheelbase'),second_car('Wheelbase'),third_car('Wheelbase')],
                 ['Turning Radius',first_car('Minimum_Turning_Radius'),second_car('Minimum_Turning_Radius'),third_car('Minimum_Turning_Radius')]                
             ] 
            #create table to store the dimensions of three cars 
            fig = ff.create_table(dimensions, height_constant=20)
            for i in range(len(fig.layout.annotations)):
                fig.layout.annotations[i].font.size = 20
            st.plotly_chart(fig)
        
        
        #store the Luxary_Entertainment of three cars in an expander
        with st.expander("Luxary_Entertainment"):
             #dataframe to store the Luxary_Entertainment(like - weight, length etc) of the three cars    
            Luxary_Entertainment=[
                 ['',brand,brand2,brand3],
                 ['Seating_Capacity',first_car('Seating_Capacity'),second_car('Seating_Capacity'),third_car('Seating_Capacity')],
                 ['Seats_Material',first_car('Seats_Material'),second_car('Seats_Material'),third_car('Seats_Material')],
                 ['Doors',first_car('Doors'),second_car('Doors'),third_car('Doors')],
                 ['CD_Player',first_car('CD_/_MP3_/_DVD_Player'),second_car('CD_/_MP3_/_DVD_Player'),third_car('CD_/_MP3_/_DVD_Player')],
                 ['USB_Ports',first_car('USB_Ports'),second_car('USB_Ports'),third_car('USB_Ports')],
                 ['Bluetooth',first_car('Bluetooth'),second_car('Bluetooth'),third_car('Bluetooth')],
                 ['Infotainment_Screen',first_car('Infotainment_Screen'),second_car('Infotainment_Screen'),third_car('Infotainment_Screen')],
            ] 
            #create table to store the Luxary_Entertainment of three cars 
            fig = ff.create_table(Luxary_Entertainment, height_constant=20)
            for i in range(len(fig.layout.annotations)):
                fig.layout.annotations[i].font.size = 20
            st.plotly_chart(fig)
                
            
