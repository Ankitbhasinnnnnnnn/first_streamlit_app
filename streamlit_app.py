import streamlit ;
import pandas ;
import snowflake.connector;
import requests;
from urllib.error import URLError
 
 
streamlit.title('My Parents New Healthier Diner')
 
streamlit.header('Breakfast')
streamlit.text(' 🥣 Omega 3 & blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avacado Toast')
 
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
 
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
 
fruit_selected =streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruit_to_show=my_fruit_list.loc[fruit_selected]
 
 
streamlit.dataframe(fruit_to_show)
 
streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information")
  else:
    streamlit.write('The user entered ', fruit_choice)
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    # write your own comment - what does this do?
    streamlit.dataframe(fruityvice_normalized)
except URLError as e:
  streamlit.error()
 
 
streamlit.header("View Our Fruit List -Add your Favourites")
def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("SELECT * from fruit_load_list")
    return my_cur.fetchall()
if streamlit.button('Get Fruit List'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows=get_fruit_load_list()
  my_cnx.close()
  streamlit.dataframe(my_data_rows)
# streamlit.dataframe(my_data_row)
def insert_row_snowflake(new_fruit):
  with my_cnx.cursor() as my_cur:
    my_cur.execute("insert into fruit_load_list values('"+new_fruit+"')")
    return "Thanks for adding" + new_fruit;
add_my_fruit= streamlit.text_input('What fruit would you like to add?','jackfruit')
if streamlit.button('Add a Fruit to the list '):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows=insert_row_snowflake(add_my_fruit)
  streamlit.text(my_data_rows)
 
# streamlit.write('thanks for adding ',add_my_fruit)
 
# my_cur.execute()
