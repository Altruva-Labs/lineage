"""Chapter 4.3.2: Logistic Regression as a Learning Setup.

This demonstrates logistic regression in a full supervised learning context:
- Binary classification task
- Training and evaluation
- Probability calibration

We use implementations from Chapter 4.2.3 (Linear Models).
"""

import sys
from pathlib import Path
import math

project_root = Path(__file__).parent.parent.parent.parent
sys.path.insert(0, str(project_root))

from core import dot, sigmoid, accuracy_score


class LogisticRegressionSetup:
    """Logistic regression for binary classification tasks."""

    def __init__(self, learning_rate=0.01, epochs=1000):
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.model = LogisticRegressionModel(learning_rate, epochs)
        self.feature_means = None
        self.feature_stds = None

    def fit(self, X_train, y_train):
        """Train logistic regression with feature normalization."""
        # Normalize features
        X_train = self._normalize(X_train, fit=True)
        self.model.fit(X_train, y_train)
        return self

    def predict(self, X_test):
        """Predict binary labels."""
        X_test = self._normalize(X_test, fit=False)
        return self.model.predict(X_test)

    def predict_proba(self, X_test):
        """Get probability of positive class."""
        X_test = self._normalize(X_test, fit=False)
        return self.model.predict_proba(X_test)

    def evaluate(self, X_test, y_test):
        """Evaluate classification performance."""
        predictions = self.predict(X_test)
        accuracy = accuracy_score(y_test, predictions)
        return {"accuracy": accuracy}

    def _normalize(self, X, fit=False):
        """Feature normalization."""
        if fit:
            n_features = len(X[0]) if X else 0
            self.feature_means = []
            self.feature_stds = []

            for j in range(n_features):
                col = [X[i][j] for i in range(len(X))]
                mean = sum(col) / len(col)
                variance = sum((x - mean) ** 2 for x in col) / len(col)
                std = math.sqrt(variance) if variance > 0 else 1.0
                self.feature_means.append(mean)
                self.feature_stds.append(std)

        X_norm = []
        for i in range(len(X)):
            row = [(X[i][j] - self.feature_means[j]) / self.feature_stds[j]
                   for j in range(len(X[i]))]
            X_norm.append(row)
        return X_norm


class LogisticRegressionModel:
    """Logistic regression binary classifier."""

    def __init__(self, learning_rate=0.01, epochs=1000):
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.weights = []
        self.bias = 0.0

    def fit(self, X, y):
        """Train using gradient descent on log loss."""
        n_samples = len(X)
        n_features = len(X[0]) if X else 0
        self.weights = [0.0] * n_features
        self.bias = 0.0

        for _ in range(self.epochs):
            grad_w = [0.0] * n_features
            grad_b = 0.0

            for features, target in zip(X, y):
                z = dot(self.weights, features) + self.bias
                prediction = sigmoid(z)
                error = prediction - target

                for j in range(n_features):
                    grad_w[j] += error * features[j]
                grad_b += error

            scale = 1.0 / n_samples
            for j in range(n_features):
                self.weights[j] -= self.learning_rate * scale * grad_w[j]
            self.bias -= self.learning_rate * scale * grad_b

        return self

    def predict(self, X):
        """Predict binary labels."""
        return [1 if self.predict_proba_one(x) >= 0.5 else 0 for x in X]

    def predict_proba(self, X):
        """Get probabilities."""
        return [self.predict_proba_one(x) for x in X]

    def predict_proba_one(self, x):
        """Get probability for single sample."""
        z = dot(self.weights, x) + self.bias
        return sigmoid(z)


if __name__ == "__main__":
    # Email spam classification example
    # Features: word frequency features
    # Target: 1=spam, 0=not spam

    X_train = [
        [5, 2],   # Email with 5 occurrences of "free" and 2 of "click"
        [1, 0],   # Normal email
        [4, 3],   # Likely spam
        [2, 1],   # Normal
        [6, 4],   # Likely spam
        [1, 1],   # Normal
    ]

    y_train = [1, 0, 1, 0, 1, 0]  # Labels: spam/not spam

    X_test = [
        [5, 3],   # Test
        [1, 0],   # Test
    ]
    y_test = [1, 0]

    # Train
    setup = LogisticRegressionSetup(learning_rate=0.01, epochs=1000)
    setup.fit(X_train, y_train)

    # Evaluate
    metrics = setup.evaluate(X_test, y_test)
    print(f"Test Accuracy: {metrics['accuracy']:.2%}")

    # Predict with probabilities
    proba = setup.predict_proba([[5, 3], [1, 0]])
    print(f"Spam probabilities: {[round(p, 2) for p in proba]}")

    print("\nLogistic Regression Learning Setup complete!")
