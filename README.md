# Diamond Price Prediction Web App

This repository contains a Flask web application for predicting diamond prices. The prediction model is built using a dataset from Kaggle and the app allows users to enter diamond characteristics to receive a price estimate.

## Environment Setup

To set up the project environment, follow these steps:

1. Create a new conda environment:
```bash
conda create -p venv python==3.9 -y
```

3. Activate the conda evnvironment
```bash
conda activate venv/
```


## Dataset 
The dataset used for training the model can be downloaded from Kaggle:
https://www.kaggle.com/datasets/colearninglounge/gemstone-price-prediction

## Running the Application
```bash
python app.py
```

This will start a local web server. Open a web browser and navigate to http://localhost:5000 to view the application.


## Project Structure
 The project has the following directory structure:

- artifacts: Contains serialized models and other artifacts used by the web app.
- logs: Contains log files for the application.
- notebooks: Jupyter notebooks used for exploration and model development.
- src: The source code for the model and Flask application.
- DimondPricePrediction: The main package for the prediction model.
- components: Modules for different components of the model.
- pipelines: Modules for data processing and prediction pipelines.
- utils: Utility modules for common functions.
- templates: HTML templates for the Flask application.
- venv: The conda environment for the project.
app.py: The entry point for the Flask web application.
