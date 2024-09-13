# **House Price Predictor**

## Overview

This repository contains a project aimed at predicting house prices using machine learning techniques. The project involves preparing data, training a model, evaluating its performance, building a Flask application, and deploying it on AWS.

## Table of Contents

- [**House Price Predictor Model - Demo**](http://housepriceprediction-env.eba-2nsnmvcn.eu-north-1.elasticbeanstalk.com/)
  - [Introduction](#introduction)
  - [Features](#features)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Data](#data)
  - [Model](#model)
  - [Results](#results)
  - [Contributing](#contributing)
  - [License](#license)

## Introduction

The House Price Predictor project utilizes machine learning to forecast house prices based on various input features. The project demonstrates data preprocessing, model training, and evaluation using Python. Additionally, it includes building a Flask application for serving the model and deploying the application on AWS.

## Features

- Predict house prices from the Number of Private Rooms feature.
- Utilizes Python libraries like pandas, scikit-learn, matplotlib, and seaborn.
- Includes data preprocessing, model training, evaluation, building a Flask application, and deployment on AWS.

## Installation

To set up this project, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/AnoopGeorge418/House-Price-Predictor.git
   cd House-Price-Predictor

2. **Install the required dependencies:**
   Create a virtual environment and install the necessary packages:
    ```bash
    conda create -p House-env python==3.11 -y
    conda activate House-env/
    pip install -r requirements.txt

## Usage
To train, test, and deploy the model, follow these instructions:

1. Prepare your data:
    - Ensure your dataset matches the expected format. Place your data file in the data directory.

2. Run the training script:
   ```bash
   python train_model.py
   - This script will preprocess the data, train the model, and save it.

3. Build and run the Flask application:
    - Start the Flask server:
    ```bash
    python app.py
    - The application will be available at http://127.0.0.1:5000/.

4. Deploy the Flask application to AWS:
    - Follow the instructions in the aws-deployment.md file for deploying the Flask application to AWS Elastic Beanstalk and codepipeline.

## Data
   - The dataset should include features relevant to house pricing. Example columns: `Number_of_Private_Rooms`
   - Ensure the data is preprocessed to handle missing values, encode categorical variables, and scale numerical features.

## Model
The model used is a Linear Regression model implemented with scikit-learn.

### Training
The model is trained using train_model.py:
- Loads and preprocesses data
- Splits data into training and test sets
- Trains the Linear Regression model
- Evaluates performance
- Saves the trained model

### Evaluation
Performance metrics such as Mean Squared Error (MSE) and R-squared are used to evaluate the model.

## Results
After running train_model.py, the model's performance metrics are displayed, and the trained model is saved in the models directory with a .pkl extension.

## Contributing
Contributions are encouraged. To contribute:
- Fork the repository.
- Create a new branch for your changes.
- Commit your changes.
- Push to your fork.
- Create a pull request to the original repository.

## License
This project is licensed under the MIT License. See the [LICENSE](https://github.com/AnoopGeorge418/House-Price-Predictor?tab=MIT-1-ov-file) file for more details.