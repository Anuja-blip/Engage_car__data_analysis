# Engage_data_analysis
Language: Python
Framework: Streamlit

Libraries :
1. pandas
2. numpy
3. plotly
4. matplotlib
5. seaborn
6. AgGrid

Installation of libraries 
1. AgGrid
pip install streamlit-aggrid

2.Pandas
pip install pandas

3.Numpy
pip install numpy

4.Plotly
pip install plotly

5. Matplotlib
pip install matplotlib

6. Seaborn
pip install seaborn


How to run the project?
1.Clone or download this repository to your local machine
2.Install all the libraries mentioned above 
3.Open your terminal/command prompt from your project directory and run the file main.py by executing the command streamlit run main.py
and you will be redirected to a webpage in your browser
4. Go to your browser  and open the page


I have divided my work into two parts :
1. Exploratory Data Analysis
2. Website making

 Exploratory data analysis
1. I have done the eda on ‘cars_engage_2022.csv’ file data

2. UNDERSTANDING AND CLEANING DATA
            This step includes handling missing values , changing data types, Removing special    characters

3. DATA VISUALIZATION
            In this step I have plotted several charts and graphs to visualize the data and extract information from the data and ans several queries like
i) What are top 10 cars manufactured?
ii) Which body type or fuel type is prefered most?
Iii) How mileage, height, weight etc affects the car’s price for different make or body type?
iv) what are the most prefered  fuel type, body type , seating material for different ranged cars(like most expensive, medium , low  budgey)

etc.

Website making
           I made a 3  page Website using streamlit
1st  page :
           you can visualize the data and make different graphs and charts here.

    • Show dataframe.
    • Most prefered feature .
    • Compare car price based on 1 feature
    • Car feature vs Average Price for every cars price range Bar Chart
    • compare car price based on two features

2nd Page: 
         Compare two or  three cars .
    • Enter make, model, variant and get overview , engine details, dimensions, luxary details of the cars.

3rd Page : 
          Sort the cars based on price or make or body type

    • if you sort by price  then you get a list car brands under your budget and to get the details of the any  car under your budget enter the make , model , variant of the that car 
    • if you sort by make you get a list of cars under that brand
    •  same for car body type
 
       
