
import page1_data_analysis
import page2_compare_cars
import page3_find_cars


import streamlit as st
from streamlit_option_menu import option_menu

PAGES = {
    
    "Data Visualization": page1_data_analysis,
    "Compare Cars":page2_compare_cars,
    "Find Car Details":page3_find_cars,
    
    
}
selection = option_menu(menu_title='',
                        options=list(PAGES.keys()), orientation="horizontal")
page = PAGES[selection]
page.app()

