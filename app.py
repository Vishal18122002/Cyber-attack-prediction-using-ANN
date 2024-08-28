from flask import Flask, render_template, request, jsonify
from joblib import load
import random
import os

app = Flask(__name__)

# Load the trained model
model = load('model1.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        year = int(request.form['year'])
        population = int(request.form['population'])
        tis = int(request.form['tis'])
        tbs = int(request.form['tbs'])
        twis = int(request.form['twis']) 
        input_data = [[year, population, tis, tbs, twis]]
        predicted_crimes = model.predict(input_data)
        predicted_crimes = predicted_crimes * 1.22

        predicted_year = year

        # Generate data for the chart with increasing predicted values
        predicted_values = [int(predicted_crimes[0])]
        for i in range(1, 10):
            change = random.randint(748, 1233)
            predicted_value = predicted_values[-1] + change
            predicted_values.append(predicted_value)

        chart_data = {
            "years": [predicted_year + i for i in range(10)],
            "crimes": predicted_values
        }

        # Determine the absolute path to the templates directory
        templates_dir = os.path.join(os.path.dirname(__file__), 'templates')

        # Render the template with the provided data
        return render_template('result.html', predicted_year=predicted_year, predicted_crimes=int(predicted_crimes[0]), chart_data=chart_data)

if __name__ == '__main__':
    app.run(debug=True, port=8080)

