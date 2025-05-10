import  streamlit as st

st.title("unit_converter")

st.write("write a conversion")
conversion = st.selectbox("type of conversion",["kilograms to grams" ,"grams to kilograms","kilometers to meters" ,"meters to kilometers"])


def kg_g(x):
    return x*1000

def g_kg(x):
    return x/1000

def km_m(x):
    return x*1000

def m_km(x):
    return x/1000

num =st.number_input("value:", min_value=0.0 )

if st.button("calculate"):
    if conversion == "kilograms to grams":
        result =kg_g(num)
        st.write(f"{num} kilograms is {result} grams")
    elif conversion =="grams to kilograms":
        result =g_kg(num)
        st.write(f"{num} grams is {result} kilogram")
    elif conversion =="kilometers to meters":
        result =km_m(num)
        st.write(f"{num} kilometers is {result} meters")
    elif conversion =="meters to kilometers":
        result =m_km(num)
        st.write(f"{num} meters is {result} kilometers")
