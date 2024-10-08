import numpy as np
from sklearn.datasets import load_diabetes
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score




def main() : 

	# Load the Diabetes dataset
	diabetes = load_diabetes()
	X = diabetes.data  # Features
	y = diabetes.target  # Target variable 


	# Split dataset into training set and test set
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


	# Create Decision Tree regressor object
	tree_regressor = DecisionTreeRegressor(random_state=42)

	# Train Decision Tree Regressor
	tree_regressor.fit(X_train, y_train)

	# Predict the response for test dataset
	y_pred = tree_regressor.predict(X_test)

	# Model Evaluation
	mse = mean_squared_error(y_test, y_pred)
	r2 = r2_score(y_test, y_pred)
	print("Mean Squared Error:", mse)
	print("R^2 Score:", r2)



if __name__ == "__main__" : 
	main()




