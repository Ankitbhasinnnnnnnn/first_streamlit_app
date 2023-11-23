import streamlit 
import pandas

streamlit.title('My Parents New Healthy Diner') 


my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.multiselect("Pick Some fruits:" , list(my_fruit_list.index),['Avocado', 'Strawberries'])



streamlit.dataframe(my_fruit_list)
