import numpy as np
import pandas as pd
from sklearn.model_selection import cross_validate
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from joblib import load

# Load the dataset
df = pd.read_csv('/Users/vishal/venv/static/cyber_attack_dataset-5.csv')

# Define the state information
state_info = {
    "state": "Tamil Nadu",
    "year": 2023,
    "population": 83900000,
    "tis": 14800000,
    "tbs": 5860000,
    "twis": 74300000
}

state = state_info['state']

# Prepare features (X) and target variable (y)
X = df.drop(['Unique Code', 'State', 'Cases Reported'], axis=1)
y = df['Cases Reported']

# Number of models for ensemble
num_models = 10

# List to store metric values for each model
metric_values = []

# Metrics to calculate
scoring_metrics = ['neg_mean_absolute_error', 'neg_mean_squared_error', 'r2']

# Loop through the number of models
for i in range(num_models):
    # Load the RandomForestRegressor model from the .pkl file
    model_filename = f'model_random_forest_{i+1}.pkl'
    model = load(model_filename)

    # Use cross-validation to evaluate the model's performance
    scores = cross_validate(model, X, y, cv=5, scoring=scoring_metrics)

    # Print the metrics for each model
    print(f"\nMetrics for Model {i + 1}:")
    for metric, values in scores.items():
        print(f"{metric}: {np.mean(values)}")

    # Make predictions for the specific state
    input_data = [state_info['year'], state_info['population'], state_info['tis'], state_info['tbs'], state_info['twis']]
    predicted_crimes = model.predict([input_data])
    predicted_crimes = predicted_crimes * 1.22

    # Append the predicted value to the list
    metric_values.append({
        'MAE': mean_absolute_error(y, model.predict(X)),
        'MSE': mean_squared_error(y, model.predict(X)),
        'R2': r2_score(y, model.predict(X)),
    })

# Calculate the mean metrics across all models
mean_metrics_across_models = {
    'MAE': np.mean([m['MAE'] for m in metric_values]),
    'MSE': np.mean([m['MSE'] for m in metric_values]),
    'R2': np.mean([m['R2'] for m in metric_values]),
}

print("\nOverall Mean Metrics Across Models:")
for metric, value in mean_metrics_across_models.items():
    print(f"{metric}: {value}")
