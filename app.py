
import pandas as pd
 
import numpy as np

import streamlit as st






crops = pd.read_csv('df_crops.csv').set_index('Produce_Variety')
print(crops)

st.title('CROPS')
st.subheader('Avarage price of various crops')

st.markdown('The avarage price of various crops')

st.line_chart(crops['Values_in_Ksh'])



st.subheader('Volume in kilograms')

st.markdown('The avarage kilograms of various crops')

st.bar_chart(crops.Volume_in_Kgs)

