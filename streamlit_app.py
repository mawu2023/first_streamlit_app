import streamlit
import pandas

streamlit.title('My Parents New Healthy Dinner')
streamlit.header('Breakfast Favorites')
streamlit.text(' 🥣 Omega3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# load file into df
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index("Fruit")

# add object picker
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
# display the list
streamlit.dataframe(my_fruit_list)   
