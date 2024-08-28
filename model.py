import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib

df = pd.read_csv('/Users/vishal/cyberattack prediction 2/cyber_attack_dataset-5.csv')

state_info = {
    "state": "Tamil Nadu",
    "year": 2023,
    "population": 83900000,
    "tis": 14800000,
    "tbs": 5860000,
    "twis": 74300000
}

state = state_info['state']

x = df.drop(['Unique Code', 'State', 'Cases Reported'], axis=1)
y = df['Cases Reported']

num_models = 10  

all_predictions = []
trained_models = []

for i in range(num_models):
    model = RandomForestRegressor(n_estimators=100, random_state=i)  
    model.fit(x, y)
    trained_models.append(model)  # Store the trained model
    
    input_data = [state_info['year'], state_info['population'], state_info['tis'], state_info['tbs'], state_info['twis']]
    predicted_crimes = model.predict([input_data])
    predicted_crimes = predicted_crimes * 1.22

    all_predictions.append(predicted_crimes[0])
    
    # Save the trained model to a file
joblib.dump(model,'model1.pkl')

mean_prediction = np.mean(all_predictions) * 3.4
std_deviation = np.std(all_predictions) * 3.4

print("State:", state)
print(f"Predicted crime in {state_info['year']} is between {int(mean_prediction - std_deviation)} and {int(mean_prediction + std_deviation)}")
