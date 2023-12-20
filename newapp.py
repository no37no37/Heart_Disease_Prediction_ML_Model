import pandas as pd
import numpy as np
import streamlit as st 
import pickle as pk

model = pk.load(open(r'C:\Users\acer\Downloads\Heart_disease_model.pk1','rb'))

data = pd.read_csv(r'C:\Users\acer\Downloads\Heart_Disease_Prediction.ipynb')

st.header('Heart Disease Predictor')

st.selectbox('Choose Gender', data['Gender'].unique())
if gender == 'Male':
    gen = 1
else:
    gen = 0
    
age = st.number_input('Enter Age')
currentSmoker = st.number_input('Is Patient currentSmoker')
cigsPerDay = st.number_input('Enter cigsPerDay')
BPMeds = st.number_input('Is Patient on BPMeds')
prevalentStroke = st.number_input('Is Patient Had Stroke')
prevalentHyp = st.number_input('Enter prevalentHyp status')
diabetes = st.number_input('Enter Diabetes status')
totChol = st.number_input('Enter totChol')
sysBP = st.number_input('Enter sysBP')
diaBP = st.number_input('Enter diaBP')
BMI = st.number_input('Enter BMI')
heartRate = st.number_input('Enter heartRate')
glucose = st.number_input('Enter glucose')

if st.button('Predict'):

    input = np.array([[gen,age,currentSmoker,cigsPerDay,BPMeds,prevalentStroke,prevalentHyp,diabetes,totChol,sysBP,diaBP,BMI.heartRate,glucose]])

    output = model.predict(input)
    if output[0] == 0:
        stn = 'Patient is healthy, No Heart Disease'
    else:
        stn = 'Patient May have Heart Disease'
    st.markdown(stn)