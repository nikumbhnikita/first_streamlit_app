import pandas
import streamlit
import requests
import snowflake.connector
from urllib.error import URLError
streamlit.title("My Mom's New Healthy Dinner ")
streamlit.header('Breakfast Menu')
streamlit.text(' 🥣  Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑 🍞 Avacado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)
def get_fruitvice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon",+this_fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    return fruityvice_normalized 
streamlit.header("Fruityvice Fruit Advice!")
try :
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("please select a fruit to get a choice:")
  else:
    #streamlit.write('The user entered ', fruit_choice)
    back_from_function=get_fruitvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)
except URLERROR as e:
  streamlit.error()
# write your own comment - what does this do?
#streamlit.dataframe(fruityvice_normalized)

#my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
#my_cur = my_cnx.cursor()
#my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
#my_data_rows = my_cur.fetchall()

streamlit.header("The fruit load list contains:")
def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
        my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
        return my_cur.fetchall()
    
 if streamlit.button('Get a fruit list'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_rows = my_cur.get_fruit_load_list()
    streamlit.dataframe(my_data_rows)
    
#add_my_fruit=streamlit.text_input('What fruit would you like to add ?')
#streamlit.write('The user entered ', add_my_fruit)
#my_cur.execute("insert into pc_rivery_db.public.fruit_load_list values ('from streamlit')")
