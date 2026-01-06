
import streamlit as st
import joblib

import numpy as np

st.title('check the environtment')
#input data
carbon_emission=st.number_input("carborn emission Amount:",min_value=0.0, format="%f")
energy_output=st.number_input("energy_output:",min_value=0.0,format="%f")
renewability_index=st.number_input("renewability_index:",min_value=0.0,format="%f")
cost_efficiency=st.number_input("cost_efficiency:",min_value=0.0,format="%f")

#model importing
with open('sustainability_model.pkl','rb') as f:
    mod=joblib.load(f)
#predict
if st.button("Predicat"):
    input_data=np.array([[carbon_emission,energy_output,renewability_index,cost_efficiency]])

    prediction=mod.predict(input_data)
    #display the result
    if prediction[0]==1:
        st.success("congrats,This environment is sustainable")
    else:
        st.info("It is not sustainable")