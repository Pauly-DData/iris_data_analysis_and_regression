# Importing necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error

# Load the Iris dataset
df = pd.read_csv(r"/kaggle/input/iris/Iris.csv")

# Data Analysis
print('Maximum number of the value for sepal_length:', df['SepalLengthCm'].max())
print('Distinct values for species:', df['Species'].unique())
print('Number of flowers per species:')
print(df['Species'].value_counts())

# Preparing data for Linear Regression Model
X = df[['SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']]
y = df['SepalLengthCm']

# Splitting the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.65, random_state=101)

# Training the Linear Regression Model
model = LinearRegression()
model.fit(X_train, y_train)

# Making Predictions
predictions = model.predict(X_test)

# Model Evaluation
print('Mean Squared Error:', mean_squared_error(y_test, predictions))
print('Mean Absolute Error:', mean_absolute_error(y_test, predictions))
print('Coefficient of Determination (R^2):', model.score(X_train,y_train))
print('Intercept:', model.intercept_)
print('Slope:', model.coef_)

# Predictions for given values
print('Prediction for petal length 5.1, sepal width 2.5, and petal width 1.1:', model.predict([[5.1, 2.5, 1.1]])[0])
print('Prediction for petal length 7.5, sepal width 3.0, and petal width 1.8:', model.predict([[7.5, 3.0, 1.8]])[0])
print('Prediction for petal length 4.6, sepal width 3.5, and petal width 0.2:', model.predict([[4.6, 3.5, 0.2]])[0])
