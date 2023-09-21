from flask import Flask, render_template, request
import pickle

model = pickle.load(open("customer.pkl", "rb"))

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def predict():
    
    if request.method == "GET":
        return render_template("index.html")
    else:
        # Retrieve data from the form
        CustomerId = request.form['CustomerId']
        credit_score = float(request.form['CreditScore'])
        geography = request.form['Geography']
        gender = request.form['Gender']
        age = float(request.form['Age'])
        tenure = float(request.form['Tenure'])
        balance = float(request.form['Balance'])
        num_of_products = float(request.form['NumOfProducts'])
        has_cr_card = 'HasCrCard' in request.form  # Updated to check if it's present
        is_active_member = 'IsActiveMember' in request.form  # Updated to check if it's present
        estimated_salary = float(request.form['EstimatedSalary'])
        
        # Input data for scaling
        input_data = [[geography, gender, CustomerId,credit_score, age, tenure, balance, num_of_products, has_cr_card, is_active_member, estimated_salary]]
        
        # input_data_scaled = scaler.transform(input_data)
        
        # # Combine all input data into a single list
        # final_input = [geography, gender, CustomerId] + input_data_scaled.tolist()[0]
        
        prediction = model.predict(input_data)
        
        result = ""
        
        if prediction[0] == 1:
            result = "Person will leave the Bank"
        else:
            result = "Person will not leave the Bank"
        
        return render_template("result.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
