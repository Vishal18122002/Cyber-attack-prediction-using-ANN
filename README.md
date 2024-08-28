# Cyber Attack Prediction Model

This project involves the prediction of cyber attack cases based on various factors such as year, population, and the number of internet subscribers. The prediction is carried out using a RandomForestRegressor model from scikit-learn.

## Overview

The project uses a dataset to train multiple RandomForest models. It predicts the number of cyber attacks for a given state and year based on the provided input features. The results include the predicted range of cyber attacks, calculated using the mean and standard deviation of predictions from multiple models.

## Dataset

The dataset used in this project is stored in a CSV file named `cyber_attack_dataset-5.csv`. It contains the following columns:

- **Unique Code**: A unique identifier for each row.
- **State**: The name of the state.
- **Year**: The year of the recorded data.
- **Population**: The population of the state for that year.
- **TIS**: Total Internet Subscribers in the state.
- **TBS**: Total Broadband Subscribers in the state.
- **TWIS**: Total Wireless Subscribers in the state.
- **Cases Reported**: The number of cyber attack cases reported.

## Installation

To run the model, follow the steps below:

1. **Clone the repository**:

    ```bash
    git clone https://github.com/your-username/cyber-attack-prediction.git
    cd cyber-attack-prediction
    ```

2. **Install the required dependencies**:

    Make sure you have Python and pip installed. Then, run:

    ```bash
    pip install -r requirements.txt
    ```

3. **Run the model script**:

    ```bash
    python model.py
    ```

## Usage

### Input Data

The script uses a dictionary named `state_info` to store the input data for the prediction. The fields are:

- **state**: The state for which the prediction is made.
- **year**: The year for which the prediction is made.
- **population**: The population of the state.
- **tis**: Total Internet Subscribers.
- **tbs**: Total Broadband Subscribers.
- **twis**: Total Wireless Subscribers.


### Key Points:
- **Model Training and Prediction**: The README provides details on how the model is trained and how predictions are made.
- **Installation and Usage**: Steps for running the model script are included.
- **Demo Link**: The demo link is included for users to view the project in action.

Replace `"Vishal G"` and `"sivavishal1812@gmail.com"` with your actual GitHub username and email address. You can also customize any other details as necessary.

### Preview Video link : https://drive.google.com/file/d/1tQar9y2n7PTQduKXsNaj2zXdX2SHbKQG/view?usp=drive_link



