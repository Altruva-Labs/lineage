"""Chapter 4.3.1: Linear Regression as a Learning Setup.

This file demonstrates linear regression in a practical learning setup:
- How to prepare data
- How to train and evaluate the model
- How to make predictions on new data

We use the implementations from Chapter 4.2.3 (Linear Models).
"""

import sys
from pathlib import Path

# Import from the model implementations
project_root = Path(__file__).parent.parent.parent.parent
sys.path.insert(0, str(project_root))

from core import dot, mean_squared_error


class LinearRegressionSetup:
    """Linear regression for supervised learning tasks.

    A learning setup shows how to:
    1. Prepare training data
    2. Train the model
    3. Evaluate performance
    4. Make predictions on new data
    """

    def __init__(self, learning_rate=0.01, epochs=1000):
        """
        Args:
            learning_rate: Step size for gradient descent
            epochs: Number of training iterations
        """
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.model = LinearRegressionModel(learning_rate, epochs)
        self.X_train = None
        self.y_train = None
        self.feature_means = None
        self.feature_stds = None

    def fit(self, X_train, y_train):
        """
        Train the linear regression model.

        Includes normalization of features for numerical stability.
        """
        self.X_train = X_train
        self.y_train = y_train

        # Normalize features
        self.X_train = self._normalize(self.X_train, fit=True)

        # Train model
        self.model.fit(self.X_train, self.y_train)
        return self

    def predict(self, X_test):
        """Make predictions on new data."""
        X_test = self._normalize(X_test, fit=False)
        return self.model.predict(X_test)

    def evaluate(self, X_test, y_test):
        """Evaluate model on test data."""
        predictions = self.predict(X_test)
        mse = mean_squared_error(y_test, predictions)
        rmse = mse ** 0.5
        return {"mse": mse, "rmse": rmse}

    def _normalize(self, X, fit=False):
        """Normalize features to mean=0, std=1."""
        if fit:
            n_features = len(X[0]) if X else 0
            self.feature_means = []
            self.feature_stds = []

            for j in range(n_features):
                col = [X[i][j] for i in range(len(X))]
                mean = sum(col) / len(col)
                variance = sum((x - mean) ** 2 for x in col) / len(col)
                std = variance ** 0.5 if variance > 0 else 1.0

                self.feature_means.append(mean)
                self.feature_stds.append(std)

        # Normalize
        X_normalized = []
        for i in range(len(X)):
            row = []
            for j in range(len(X[i])):
                normalized = (X[i][j] - self.feature_means[j]) / self.feature_stds[j]
                row.append(normalized)
            X_normalized.append(row)

        return X_normalized


class LinearRegressionModel:
    """Simple linear regression model."""

    def __init__(self, learning_rate=0.01, epochs=1000):
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.weights = []
        self.bias = 0.0

    def fit(self, X, y):
        n_samples = len(X)
        n_features = len(X[0]) if X else 0
        self.weights = [0.0] * n_features
        self.bias = 0.0

        for _ in range(self.epochs):
            grad_w = [0.0] * n_features
            grad_b = 0.0

            for features, target in zip(X, y):
                prediction = dot(self.weights, features) + self.bias
                error = prediction - target

                for j in range(n_features):
                    grad_w[j] += error * features[j]
                grad_b += error

            scale = 2.0 / n_samples
            for j in range(n_features):
                self.weights[j] -= self.learning_rate * scale * grad_w[j]
            self.bias -= self.learning_rate * scale * grad_b

        return self

    def predict(self, X):
        return [dot(self.weights, features) + self.bias for features in X]


if __name__ == "__main__":
    # Real estate price prediction example
    # Features: square footage, number of bedrooms
    # Target: price in thousands

    X_train = [
        [1.5, 3],  # 1500 sq ft, 3 bedrooms
        [2.0, 4],  # 2000 sq ft, 4 bedrooms
        [1.0, 2],  # 1000 sq ft, 2 bedrooms
        [3.0, 5],  # 3000 sq ft, 5 bedrooms
        [1.2, 2],  # 1200 sq ft, 2 bedrooms
        [2.5, 4],  # 2500 sq ft, 4 bedrooms
    ]

    y_train = [
        300,  # Prices in thousands
        400,
        200,
        500,
        250,
        450,
    ]

    X_test = [
        [1.8, 3],  # Test case
        [2.2, 4],
    ]

    y_test = [350, 420]

    # Setup and train
    setup = LinearRegressionSetup(learning_rate=0.01, epochs=1000)
    setup.fit(X_train, y_train)

    # Evaluate
    metrics = setup.evaluate(X_test, y_test)
    print(f"Test RMSE: {metrics['rmse']:.2f}k")

    # Predict on new data
    predictions = setup.predict([[1.8, 3], [2.2, 4]])
    print(f"Predictions: {[round(p, 0) for p in predictions]}k")

    print("\nLinear Regression Learning Setup complete!")
    print("This shows the full workflow: prepare -> train -> evaluate -> predict")
