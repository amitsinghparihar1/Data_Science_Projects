import streamlit as st
import pickle

model=pickle.load(open('svr.pkl','rb'))


def predict(input_data):

    prediction=model.predict(input_data)
    return prediction
    

def main():
    
    st.title("Placement Package Predictor")
    cgpa = st.text_input('Enter the cgpa')
    
    result=[]
    
    if st.button('Predict Prediction'):
         result= predict([[cgpa]])
         
    st.success(result)
    
if __name__=='__main__':
    main()
        
         
        
    
    
    