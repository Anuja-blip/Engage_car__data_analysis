#importing libraries
import streamlit as st
import numpy as np
import pandas as pd
import plotly
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go
from st_aggrid import AgGrid


def app():
    #reading file
    df = pd.read_csv('new_engage_file.csv')
    manufacturer="" 
    price="" #declare  var
    
    #create a side bar where u can choose on which parameter(make, price, body type)u want tosort cars
    with st.sidebar:
        st.markdown("### SORT BY ")
        x = st.radio(" ", ("by price",
                                 "by make", "by body_type")) #radio buttons
        
        
    if x == "by price":

        price = st.radio("What's your budget", ("below 10 lakhs",
                                                "between 10 - 50 lakhs", "between 50 lakhs - 1 cr", "above 1cr"))
        st.subheader(
            "List of BRANDS of cars  "+price)

    if price == "below 10 lakhs":
        def func1(x):
            df1 = df.loc[df['carsrange'] == 'Budget'][x].unique()
            df1 = pd.DataFrame(df1, columns=[x])
            return df1

    if price == "between 10 - 50 lakhs":
        def func2(x):
            df2 = df.loc[df['carsrange'] == 'Medium'][x].unique()
            df2 = pd.DataFrame(df2, columns=[x])
            return df2
    if price == "between 50 lakhs - 1 cr":
        def func3(x):
            df3 = df.loc[df['carsrange'] == 'Medium_High'][x].unique()
            df3 = pd.DataFrame(df3, columns=[x])
            return df3

    if price == "above 1cr":
        def func4(x):
            df4 = df.loc[df['carsrange'] == 'Highend'][x].unique()
            df4 = pd.DataFrame(df4, columns=[x])
            return df4

    details = st.container()
    with details:

        left_col, right_col = st.columns(2)
        if x == "by price":
            right_col.text(
                "Select make ,model and variant \nto view the details of that car of \nprice "+price)
        count = 0

        def func(df, starting_price, ending_price):
            global brand, model_name, variant_name
            df= df[(df['Ex_Showroom_Price'] >=starting_price) & (df['Ex_Showroom_Price'] <=ending_price)]
            print(df[['Price', 'carsrange']])
            brand = right_col.selectbox(
                "Select Make", options=df['Make'].unique(), index=0, key=count)
            # dataframe of the selected make /brand name
            new_df = df[df.Make == brand]

            model_name = right_col.selectbox(
                "Select a Model", options=new_df['Model'].unique(), index=0, key=count)
            new_df = df[df.Model == model_name]  # contains selected model name

            variant_name = right_col.selectbox(
                "select a Variant", options=new_df['Variant'].unique(), index=0, key=count)
            return variant_name

        if price == "below 10 lakhs":
            left_col.table(func1('Make'))
            df_new = df.query(' carsrange=="Budget" ')
            func(df_new, 0, 1000000)

        if price == "between 10 - 50 lakhs":
            left_col.write(func2('Make'))
            df_new = df.query(' carsrange=="Medium" ')
            func(df_new, 1000000, 5000000)

        if price == "between 50 lakhs - 1 cr":
            left_col.write(func3('Make'))
            df_new = df.query(' carsrange=="Medium_High" ')
            func(df_new, 5000000, 100000000)

        if price == "above 1cr":
            left_col.write(func4('Make'))
            df_new = df.query(' carsrange=="Highend" ')
            func(df_new, 10000000, 250000000)
        if x == "by price":

            def selected_car(x):
                df1 = df.loc[(df['Make'] == brand) & (
                    df['Model'] == model_name) & (df['Variant'] == variant_name)][x].values[0]
                return df1

            data_matrix = [['Features', brand],
                           ['Model', selected_car('Model')],
                           ['Ex_Showroom_Price(Rs.)', selected_car(
                               'Price')],
                           ['Body Type', selected_car('Body_Type')],
                           ['Power', selected_car('Power')],
                           ['Mileage(km/l)', selected_car('fueleconomy')],
                           ['Fuel Type', selected_car('Fuel_Type'), ]
                           ]
            with st.expander("OVERVIEW"):

                fig = ff.create_table(data_matrix, height_constant=20)
                for i in range(len(fig.layout.annotations)):
                    fig.layout.annotations[i].font.size = 20
                st.plotly_chart(fig)

            engine_details = [
                ['Engine_Details', brand],
                ['Engine_Type', selected_car('Engine_Type')],
                ['Displacement(cc)', selected_car('Displacement')],
                ['Torque', selected_car('Torque')],
                ['Cylinders no', selected_car('Cylinders')],
                ['Drivetrain', selected_car('Drivetrain')],
                ['Emission_Norm', selected_car('Emission_Norm')],
            ]
            with st.expander("ENGINE DETAILS"):
                fig = ff.create_table(engine_details, height_constant=20)
                for i in range(len(fig.layout.annotations)):
                    fig.layout.annotations[i].font.size = 20
                st.plotly_chart(fig)
            
            #store the DIMENSIONS of two cars in an expander
        with st.expander("Dimensions"):
             #dataframe to store the Dimensions(like - weight, length etc) of the two cars    
            dimensions=[
                 ['',brand],
                 ['Length (mm)',selected_car('Length')],
                 ['Width (mm)',selected_car('Width')],
                 ['Height (mm)',selected_car('Height')],
                 ['Gross weight',selected_car('Gross_Vehicle_Weight')],
                 ['Kerb Weight( kg)',selected_car('Kerb_Weight')],
                 ['Wheelbase',selected_car('Wheelbase')],
                 ['Turning Radius',selected_car('Minimum_Turning_Radius')]      
                           
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
                 ['',brand],
                 ['Seating_Capacity',selected_car('Seating_Capacity')],
                 ['Seats_Material',selected_car('Seats_Material')],
                 ['Doors',selected_car('Doors')],
                 ['CD_Player',selected_car('CD_/_MP3_/_DVD_Player')],
                 ['USB_Ports',selected_car('USB_Ports')],
                 ['Bluetooth',selected_car('Bluetooth')],
                 ['Infotainment_Screen',selected_car('Infotainment_Screen')],
            ] 
            #create table to store the Luxary_Entertainment of two cars 
            fig = ff.create_table(Luxary_Entertainment, height_constant=20)
            for i in range(len(fig.layout.annotations)):
                fig.layout.annotations[i].font.size = 20
            st.plotly_chart(fig)      

    if x == "by make":
        st.subheader("Select a Make")
        manufacturer = st.selectbox(
            " ", options=df['Make'].unique(), index=0)
        new_df = df[df.Make == manufacturer]
        st.subheader("The details of cars of brand " + manufacturer)

        features = st.container()

        with features:

            df1 = df.loc[(df['Make'] == manufacturer)]

            new_df1 = (df1[['Model', 'Variant', 'Body_Type',
                            'Ex_Showroom_Price', 'Fuel_Type','Engine_Type','Power','fueleconomy']])
            AgGrid(new_df1)

    global body 
    if x == "by body_type":
        st.subheader("Select a Body_Type")
        body = st.selectbox(
            " ", options=df['Body_Type'].unique(), index=0)
        new_df = df[df.Make == manufacturer]
        st.subheader("The details of cars of body type " + body)

        brand_details = st.container()

        with brand_details:

            df1 = df.loc[(df['Body_Type'] == body)]

            new_df1 = (df1[['Make', 'Model', 'Variant', 'Body_Type',
                            'Ex_Showroom_Price', 'Fuel_Type','Engine_Type','Power','fueleconomy']])

            AgGrid(new_df1)
