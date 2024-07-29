import streamlit as st
import pickle

pickle_in = open("Diabetes.pkl","rb")
classifier=pickle.load(pickle_in)

import streamlit as st
def welcome():
    return "Welcome All"

def predict_diabetes(Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age):
    prediction=classifier.predict([[
        int(Pregnancies), int(Glucose), int(BloodPressure),int(SkinThickness),
        int(Insulin), float(BMI), float(DiabetesPedigreeFunction), int(Age)]])
    print(prediction)
    return prediction

def main():
    st.title("Diabetes Predictor")
    html_temp = """
    <div style="
        background: linear-gradient(135deg, #03c9c6, #0a9f9d);
        padding: 20px;
        border-radius: 10px;
        box-shadow: 2px 2px 12px rgba(0, 0, 0, 0.2);
        text-align: center;">
        <h2 style="
            color: white;
            font-family: Arial, sans-serif;
            font-weight: bold;
            margin: 0;
            ">
            Diabetes Prediction ML App
        </h2>
    </div>
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
    display=""
    if st.button("Predict"):
        try:
            result=predict_diabetes(Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age)
    
            if result==1:
                display="You are Diabetic"
            else:
                display="You are not Diabetic"

            st.success('The Output is: {}'.format(display))
        
        except Exception as e:
            print(e)
            st.error("Please Enter Valid Data")

    if st.button("About"):
        st.text("This App uses Predictive Modelling to predict diabetes")
        st.text("Built with Streamlit")
        
        
if __name__=='__main__':
    main()