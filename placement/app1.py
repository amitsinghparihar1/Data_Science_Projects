from flask import Flask, render_template, request 
import pickle
model=pickle.load(open("svr.pkl","rb"))

app=Flask(__name__)
   
@app.route("/",methods=["GET","POST"])

def predict():
    if request.method=="GET":
        return render_template("index.html")
    else:
        cgpa=float(request.form["cgpa"])
       
        
    prediction=model.predict([[cgpa]])
    result=prediction[0]
    return render_template("result.html", result=result)


if __name__=="__main__":
    app.run(debug=True)
        
        
        
         

