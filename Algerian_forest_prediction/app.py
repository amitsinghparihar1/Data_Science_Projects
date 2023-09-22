from flask import Flask, render_template, request
import pickle

model=pickle.load(open("algerian.pkl","rb"))

app=Flask(__name__)

@app.route("/", methods=["GET","POST"])

def predict():
    if request.method=="GET":
        return render_template("index.html")
    else:
       Temperature = float(request.form["Temperature"])
       RH = float(request.form["RH"])
       Ws = float(request.form["Ws"])
       Rain = float(request.form["Rain"])
       FFMC = float(request.form["FFMC"])
       DMC = float(request.form["DMC"])
       ISI = float(request.form["ISI"])
       Classes = float(request.form["Classes"])
       Region = float(request.form["Region"])
       
       input_data = [[Temperature, RH, Ws, Rain, FFMC, DMC, ISI, Classes,
       Region]]
       prediction = model.predict(input_data)
       result = prediction
       
       return render_template("result.html",result=result)
        
if __name__=="__main__":
    app.run(debug=True)