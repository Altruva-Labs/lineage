"""Logistic Regression — from-scratch implementation

Logistic Regression is a classification model that predicts probabilities using
the sigmoid function applied to a linear combination of features.

Unlike linear regression, it estimates the probability that a sample
belongs to a positive class (1) or negative class (0).

Instructions:
- Read the `LogisticRegression` class.
- Run this file to see demo on a simple classification task.
"""

from typing import List
import math


def sigmoid(z: float) -> float:
    """Sigmoid activation function: maps any real number to (0, 1)."""
    # Clip z to avoid overflow in exp
    z = max(-500, min(500, z))
    return 1.0 / (1.0 + math.exp(-z))


def accuracy_score(y_true: List[int], y_pred: List[int]) -> float:
    """Compute classification accuracy."""
    if not y_true:
        return 0.0
    correct = sum(1 for t, p in zip(y_true, y_pred) if t == p)
    return correct / len(y_true)


def log_loss(y_true: List[int], y_pred_proba: List[float]) -> float:
    """
    Compute binary cross-entropy (log loss).
    
    Formula: -1/n * sum(y*log(p) + (1-y)*log(1-p))
    
    Where y is true label (0 or 1) and p is predicted probability.
    """
    n = len(y_true)
    if n == 0:
        return 0.0
    
    total_loss = 0.0
    for y, p in zip(y_true, y_pred_proba):
        # Avoid log(0) by clipping probabilities
        p = max(1e-15, min(1 - 1e-15, p))
        if y == 1:
            total_loss += -math.log(p)
        else:
            total_loss += -math.log(1 - p)
    
    return total_loss / n


class LogisticRegression:
    """
    Logistic Regression for binary classification.
    
    Learns a linear combination of features, applies sigmoid to get
    probabilities, then compares with true labels using cross-entropy loss.
    
    Training via gradient descent.
    """
    
    def __init__(self, learning_rate: float = 0.01, n_iterations: int = 1000):
        """
        Initialize Logistic Regression.
        
        Args:
            learning_rate: Step size for gradient descent.
            n_iterations: Number of training iterations.
        """
        self.learning_rate = learning_rate
        self.n_iterations = n_iterations
        self.weights: List[float] = []
        self.bias: float = 0.0
        self.loss_history: List[float] = []
    
    def fit(self, X: List[List[float]], y: List[int]) -> 'LogisticRegression':
        """
        Train the logistic regression model using gradient descent.
        
        Args:
            X: Training features (list of feature vectors).
            y: Training labels (0 or 1).
        
        Returns:
            self: Returns the fitted model.
        """
        n_samples = len(X)
        n_features = len(X[0]) if X else 0
        
        # Initialize weights and bias
        self.weights = [0.0] * n_features
        self.bias = 0.0
        self.loss_history = []
        
        # Gradient descent loop
        for iteration in range(self.n_iterations):
            # Forward pass: compute predictions
            predictions_proba = []
            for i in range(n_samples):
                z = self.bias + sum(
                    w * X[i][j] for j, w in enumerate(self.weights)
                )
                prob = sigmoid(z)
                predictions_proba.append(prob)
            
            # Backward pass: compute gradients
            dw = [0.0] * n_features
            db = 0.0
            
            for i in range(n_samples):
                error = predictions_proba[i] - y[i]
                db += error
                for j in range(n_features):
                    dw[j] += error * X[i][j]
            
            # Normalize gradients
            dw = [g / n_samples for g in dw]
            db = db / n_samples
            
            # Update weights and bias
            self.weights = [w - self.learning_rate * g for w, g in zip(self.weights, dw)]
            self.bias -= self.learning_rate * db
            
            # Track loss
            loss = log_loss(y, predictions_proba)
            self.loss_history.append(loss)
        
        return self
    
    def predict_proba(self, X: List[List[float]]) -> List[float]:
        """
        Predict probabilities of positive class (1) for each sample.
        
        Args:
            X: Feature vectors.
        
        Returns:
            Probabilities (values in [0, 1]).
        """
        probabilities = []
        for x in X:
            z = self.bias + sum(w * val for w, val in zip(self.weights, x))
            prob = sigmoid(z)
            probabilities.append(prob)
        return probabilities
    
    def predict(self, X: List[List[float]], threshold: float = 0.5) -> List[int]:
        """
        Predict class labels (0 or 1) for each sample.
        
        Args:
            X: Feature vectors.
            threshold: Decision threshold (default 0.5).
                      Predict 1 if probability >= threshold, else 0.
        
        Returns:
            Predicted labels.
        """
        probabilities = self.predict_proba(X)
        return [1 if p >= threshold else 0 for p in probabilities]


if __name__ == "__main__":
    # Simple 2-class classification example
    # Features: [feature1, feature2]
    # Class: 0 or 1
    
    X_train = [
        [1.0, 2.0],
        [2.0, 2.5],
        [1.5, 1.8],
        [5.0, 8.0],
        [8.0, 8.0],
        [9.0, 9.5],
    ]
    y_train = [0, 0, 0, 1, 1, 1]
    
    # Train
    model = LogisticRegression(learning_rate=0.01, n_iterations=100)
    model.fit(X_train, y_train)
    
    # Predict
    y_pred = model.predict(X_train)
    
    print("Logistic Regression Demo")
    print("=" * 40)
    print(f"Training accuracy: {accuracy_score(y_train, y_pred):.2%}")
    print(f"Final training loss: {model.loss_history[-1]:.4f}")
    
    print("\nSample predictions:")
    for i, (x, true_y, pred_y) in enumerate(zip(X_train, y_train, y_pred)):
        prob = model.predict_proba([x])[0]
        print(f"Sample {i}: features={x}, true={true_y}, pred={pred_y}, prob={prob:.3f}")
    
    # New predictions
    print("\nPredicting on new data:")
    X_new = [[3.0, 3.0], [7.0, 7.0]]
    proba = model.predict_proba(X_new)
    predictions = model.predict(X_new)
    for x, prob, pred in zip(X_new, proba, predictions):
        print(f"Features {x}: probability={prob:.3f}, predicted_class={pred}")
