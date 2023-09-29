import streamlit as st
import pickle

model = pickle.load(open('svr.pkl', 'rb'))


def predict(input_data):
    try:
        prediction = model.predict(input_data)
        return prediction
    except Exception as e:
        return str(e)


def main():
    st.title("Placement Package Predictor")
    
    st.write("Enter your CGPA below and click 'Predict' to estimate your placement package.")
    
    cgpa = st.number_input('Enter your CGPA', min_value=0.0, max_value=10.0, step=0.01)
    
    result = None
    
    if st.button('Predict'):
        if cgpa is not None:
            result = predict([[cgpa]])
    
    if result is not None:
        st.success(f"Predicted Package: {result[0]:.2f} lakhs")
    else:
        st.warning("Please enter a valid CGPA and click 'Predict'.")

if __name__ == '__main__':
    main()
        
         
        
    
    
    