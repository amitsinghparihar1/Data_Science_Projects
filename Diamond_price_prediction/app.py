from flask import Flask, render_template, request
import pickle

model= pickle.load(open("diamond.pkl", "rb"))

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def predict():
    if request.method=="GET":
        return render_template("index.html")
    else:
        try:
            carat = float(request.form['carat'])
            cut = int(request.form['cut'])
            color = int(request.form['color'])
            depth = float(request.form['depth'])
            table = float(request.form['table'])
            clarity_I1 = int(request.form.get('clarity_I1', 0))
            clarity_IF = int(request.form.get('clarity_IF', 0))
            clarity_SI1 = int(request.form.get('clarity_SI1', 0))
            clarity_SI2 = int(request.form.get('clarity_SI2', 0))
            clarity_VS1 = int(request.form.get('clarity_VS1', 0))
            clarity_VS2 = int(request.form.get('clarity_VS2', 0))
            clarity_VVS1 = int(request.form.get('clarity_VVS1', 0))
            clarity_VVS2 = int(request.form.get('clarity_VVS2', 0))
            
            input_data=[carat,cut, color, depth,table, clarity_I1,clarity_IF, clarity_SI1, clarity_SI2, clarity_VS1, clarity_VS2, clarity_VVS1, clarity_VVS2]
            prediction=model.predict([input_data])[0]
            res=prediction
            return render_template("result.html", res=res)
        
        except Exception as e:
            return render_template("index.html", res="Error: invalid input")

if __name__=="__main__":
    app.run(debug=True)