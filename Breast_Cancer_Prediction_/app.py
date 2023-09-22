from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

model = pickle.load(open("breast.pkl","rb"))

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template ("index.html")
        # Retrieve the form data 'area_mean',
    else:    
        radius_mean =float(request.form['radius_mean'])
        texture_mean = float(request.form['texture_mean'])
        smoothness_mean = float(request.form['smoothness_mean'])
        compactness_mean = float(request.form['compactness_mean'])
        concavity_mean = float(request.form['concavity_mean'])
        symmetry_mean = float(request.form['symmetry_mean'])
        fractal_dimension_mean = float(request.form['fractal_dimension_mean'])
        radius_se = float(request.form['radius_se'])
        texture_se = float(request.form['texture_se'])
        compactness_se = float(request.form['compactness_se'])
        concavity_se = float(request.form['concavity_se'])
        concave_points_se = float(request.form['concave_points_se'])
        symmetry_se = float(request.form['symmetry_se'])
        fractal_dimension_se = float(request.form['fractal_dimension_se'])
        smoothness_worst = float(request.form['smoothness_worst'])
        compactness_worst = float(request.form['compactness_worst'])
        concavity_worst = float(request.form['concavity_worst'])
        symmetry_worst = float(request.form['symmetry_worst'])
        fractal_dimension_worst = float(request.form['fractal_dimension_worst'])
        smoothness_se =float(request.form['smoothness_se'])

        input_data=[[radius_mean, radius_se,compactness_mean, compactness_se, compactness_worst, concavity_mean, smoothness_mean, 
                     smoothness_se, smoothness_worst, symmetry_se, symmetry_mean, symmetry_worst, concave_points_se,
                     concavity_se, concavity_worst,texture_mean, texture_se, fractal_dimension_mean, fractal_dimension_se,
                     fractal_dimension_worst]]
         
        prediction= model.predict(input_data)
        res=""
        if prediction[0]==0:
            res="Patient is non- cancerous"
        else:
            res="patient is cancerous"
    return render_template("result.html", res=res)

if __name__ == '__main__':
    app.run(debug=True)
