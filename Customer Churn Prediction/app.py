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
        geography = 'Geography' in request.form # Updated to check if it's present
        gender = request.form['Gender']
        age = float(request.form['Age'])
        tenure = float(request.form['Tenure'])
        balance = float(request.form['Balance'])
        num_of_products = float(request.form['NumOfProducts'])
        has_cr_card = 'HasCrCard' in request.form  # Updated to check if it's present
        is_active_member = 'IsActiveMember' in request.form  # Updated to check if it's present
        estimated_salary = float(request.form['EstimatedSalary'])
        
        input_data = [[geography, gender, CustomerId,credit_score, age, tenure, balance, num_of_products, has_cr_card, is_active_member, estimated_salary]]
        
        prediction = model.predict(input_data)
        
        result = ""
        
        if prediction[0] == 1:
            result = "Person will leave the Bank"
        else:
            result = "Person will not leave the Bank"
        
        return render_template("result.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
