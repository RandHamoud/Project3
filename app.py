import streamlit as st
import pandas as pd 
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
import matplotlib as plt
import seaborn as sns
from streamlit_option_menu import option_menu

villas_df = pd.read_csv('Clean Data\clean_aqqar_villas2.csv')
land_df = pd.read_csv('Clean Data\clean_land.csv')
appartment_df = pd.read_csv('Clean Data\clean_real_estate.csv')



with st.sidebar:
    selected = option_menu(
        menu_title = "Menu",
        options = ["Home", "Appartments", "Villas", "Lands"],
        default_index = 0
    )


if selected == "Home":
        st.title(f"Welcome to the Home ")
        st.markdown('## Introduction :')
        st.write("Riyadh, the dynamic capital of Saudi Arabia, presents a wealth of opportunities in its real estate market. From sprawling lands awaiting development to luxurious villas and state-of-the-art apartments, the city caters to every preference and lifestyle. Let’s dive into what makes each of these real estate types a worthy consideration for investors and future residents alike.")
        
        st.markdown('## Data Overview :')
        st.write("to be filled")
        
        """st.markdown('## Discrption :')
        st.write("to be filled")"""

    
if selected == "Appartments":
    
    st.title(f"Welcome to the {selected} page")
    st.markdown('## Introduction :')
    st.write("to be filled")

    
    # comment....
    real_estate_location = appartment_df['location'].value_counts()
    fig = px.pie(real_estate_location, values=real_estate_location.values, names=real_estate_location.index, title='Percentage of appartment in Riyadh Proviance')
    st.plotly_chart(fig)
    st.write("to be filled")

    # comment....
    price_avg = appartment_df[['price', 'location']]
    price_avg =price_avg.groupby('location').mean('price')
    price_avg = price_avg.sort_values(by='price', ascending=False)
    fig = px.bar(price_avg, x=price_avg.index, y='price', title='Average Price per Location', color_discrete_sequence=['#0064ce'])
    st.plotly_chart(fig)
    st.write("to be filled")
    


if selected == "Villas":
    
    st.title(f"Welcome to the {selected} page")
    
    st.markdown('## Introduction :')
    st.write("to be filled")
    
    # comment....
    villas_location = villas_df['location'].value_counts()
    fig = px.pie(villas_location, values=villas_location.values, names=villas_location.index, title='Percentage of Villas in Riyadh Proviance')
    st.plotly_chart(fig)
    st.write("to be filled")
    
    
    # comment ...............
    price_avg = villas_df[['price', 'location']]
    price_avg = price_avg.groupby('location').mean('price')
    price_avg = price_avg.sort_values(by='price', ascending=False)
    fig = px.bar(price_avg, x=price_avg.index, y='price', title='Average Price per Location', color_discrete_sequence=['#0064ce'])
    st.plotly_chart(fig)
    st.write("to be filled")
    
    
    hood_avg = villas_df.groupby('neighbourhood')['square price'].mean().reset_index()
    hood_avg = hood_avg.sort_values(by='square price', ascending=False)
    fig = px.bar(hood_avg[:10], x='neighbourhood', y='square price', title='Sample Bar Chart', color_discrete_sequence=['#0064ce'])
    st.plotly_chart(fig)
    
    fig = px.bar(hood_avg[-10:], x='neighbourhood', y='square price', title='Sample Bar Chart', color_discrete_sequence=['#0064ce'])
    st.plotly_chart(fig)
    

    
    """plt.figure(figsize=(8, 6))
    sns.histplot(villas_df['square price'], kde=True, bins=50)
    plt.xlabel('Price per Square Foot (USD)')
    plt.ylabel('Count')
    plt.title('Distribution of Square Price')
    plt.axvline(villas_df['square price'].median(), color='red', linestyle='--', label='Median')
    plt.text(80, 5000, f"Median price per sq. ft.: {villas_df['square price'].median():.2f} USD")
    st.pyplot(plt)""" 
    

if selected == "Lands":
    
    st.title(f"Welcome to the {selected} page")
    st.markdown('## Introduction :')
    st.write("to be filled")
    
    # Average Square Price per Square Meter by City 
    avg_price_per_sq_meter = land_df.groupby('المدينة')['سعر المتر'].mean().reset_index()
    avg_price_per_sq_meter = avg_price_per_sq_meter.sort_values(by='سعر المتر', ascending=False)
    fig = px.bar(avg_price_per_sq_meter, x='المدينة', y='سعر المتر',
                    title='Average Square Price per Square Meter by City')
    st.plotly_chart(fig)
    st.write("to be filled")


    # The 10 most expensive neighborhoods in Riyadh 
    land_riyadh = land_df[land_df['المدينة'] == 'الرياض']
    avg_price_per_sq_meter = land_riyadh.groupby('الحي')['سعر المتر'].mean().reset_index()
    avg_price_per_sq_meter = avg_price_per_sq_meter.sort_values(by='سعر المتر', ascending=False)
    fig = px.bar(avg_price_per_sq_meter[:10], x='الحي', y='سعر المتر',
                    title='The 10 most expensive neighborhoods in Riyadh')    
    st.plotly_chart(fig)
    st.write("to be filled")
    
    
    # The 10 cheapest neighborhoods in Riyadh 
    fig = px.bar(avg_price_per_sq_meter[:10], x='الحي', y='سعر المتر',
                    title='The 10 cheapest neighborhoods in Riyadh')
    st.plotly_chart(fig)
    st.write("to be filled")
    
    
    # 
    avg_price_per_perpuse = land_df.groupby('الغرض')['سعر المتر'].mean().reset_index()
    avg_price_per_perpuse = avg_price_per_perpuse.sort_values(by='سعر المتر', ascending=False)
    fig = px.bar(avg_price_per_perpuse, x='الغرض', y='سعر المتر',
                    title='Average Square Meter Price by Purpose')
    st.plotly_chart(fig)
    st.write("to be filled")



