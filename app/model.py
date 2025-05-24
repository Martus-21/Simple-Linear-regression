import numpy as np
from sklearn.linear_model import LinearRegression

class SimpleLinearRegression:
    def __init__(self):
        X = np.array([[1], [2], [3], [4], [5]]) 
        y = np.array([3, 5, 7, 9, 11])
        self.model = LinearRegression()
        self.model.fit(X, y)
    
    def predict(self, value):
        try:
            
            value = np.array(value).reshape(-1, 1)  
            return float(self.model.predict(value)[0])
        except ValueError:
            raise ValueError("Input must be a numeric value!")