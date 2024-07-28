import streamlit as st
import pickle

pickle_in = open("Diabetes.pkl","rb")
classifier=pickle.load(pickle_in)

import streamlit as st
def welcome():
    return "Welcome All"

def predict_diabetes(Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age):
    prediction=classifier.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
    print(prediction)
    return prediction

def main():
    st.title("Diabetes Predictor")
    html_temp = """
    <div style ="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Diabetes Prediction ML App </h2>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    Pregnancies =  st.text_input("Pregnancies","Type here")
    Glucose =  st.text_input("Glucose","Type here")
    BloodPressure =  st.text_input("Blood Pressure","Type here")
    SkinThickness =  st.text_input("Skin Thickness","Type here")
    Insulin =  st.text_input("Insulin","Type here")
    BMI =  st.text_input("BMI","Type here")
    DiabetesPedigreeFunction =  st.text_input("Diabetes Pedigree Function","Type here")
    Age =  st.text_input("Age","Type here")
    result=""
    if st.button("Predict"):
        result=predict_diabetes(Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets Learn")
        st.text("Built with Streamlit")
        
        
if __name__=='__main__':
    main()