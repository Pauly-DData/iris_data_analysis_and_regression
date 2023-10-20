# Iris Data Analysis and Regression
This repository showcases an analysis performed on the classic Iris dataset and building a linear regression model to predict the sepal length of an iris plant.

# Goals
This data analysis task consists of two parts. In the first part, the Iris dataset is loaded, and Python methods are used to answer four questions related to the data attributes, their maximum and distinct values, and the number of flowers per species in the dataset. In the second part, a linear regression model is created using 65% of the Iris dataset for testing and the remaining for training, with the goal of predicting the sepal length of an iris plant using the sepal width, petal length, and petal width attributes. Several questions are asked about the independent variable, the mean of predicted values, and predictions for given attribute values. Finally, there are four statements about the relationship between the y_test and y_pred datasets, and the task asks to identify the correct statements. The assessment aims to assess the understanding of loading and analyzing a dataset, building a linear regression model, and evaluating its accuracy.

## Overview:
- **Data Loading**: The Iris dataset is loaded into the environment.
- **Data Analysis**: Python methods are utilized to answer specific questions about the dataset, such as attributes' maximum and distinct values and the number of flowers per species.
- **Linear Regression Model**: A linear regression model is developed using 65% of the Iris dataset for testing and the remaining for training. The model aims to predict the sepal length of an iris plant based on attributes like sepal width, petal length, and petal width.

## Data Analysis Highlights:
- Determined the maximum value for the attribute `sepal_length`.
- Identified the unique species in the dataset.
- Counted the number of flowers per species.

## Linear Regression Model:
- The model uses three independent variables: `sepal_width`, `petal_length`, and `petal_width` to predict the dependent variable `sepal_length`.
- The dataset is split into 65% for testing and 35% for training with a `random_state` of 101.
- Model performance metrics like mean squared error, mean absolute error, and coefficient of determination (R^2) are calculated.
- Predictions are also made for given attribute values to demonstrate the model's capability.

## Libraries Used:
- `pandas`: For data manipulation and analysis.
- `sklearn`: For machine learning model creation and evaluation.

## Getting Started:
1. Clone this repository.
2. Ensure you have the required libraries installed.
3. Run `iris_data_analysis_and_regression.ipynb` to view the analysis and model creation process.
