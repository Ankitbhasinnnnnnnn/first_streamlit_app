import streamlit 
import pandas

streamlit.title('My Parents New Healthy Diner') 

streamlit.header('Breakfast menu')
streamlit.text('Omega 3 & Blueberry oatmeal')
streamlit.text('kale , Spinach  Rocket Smoothie')
streamlit.text('Hard-boiled Free-Range Egg')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.multiselect("Pick Some fruits:" , list(my_fruit_list.index)),['Avocado', 'Strawberries'])



streamlit.dataframe(my_fruit_list)
