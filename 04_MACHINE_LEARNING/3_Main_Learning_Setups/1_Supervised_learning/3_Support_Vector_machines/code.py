"""Chapter 4.3.3: Support Vector Machines as a Learning Setup.

This demonstrates SVM in a practical supervised learning context:
- Data preparation and normalization
- Model training
- Making predictions with confidence scores

We use kernel SVM from Chapter 4.2.26.
"""

import sys
from pathlib import Path
import math

project_root = Path(__file__).parent.parent.parent.parent
sys.path.insert(0, str(project_root))


def linear_kernel(x1, x2):
    """Linear kernel: K(x, y) = x · y."""
    return sum(a * b for a, b in zip(x1, x2))


def rbf_kernel(gamma=0.1):
    """RBF kernel factory."""
    def kernel(x1, x2):
        sq_dist = sum((a - b) ** 2 for a, b in zip(x1, x2))
        return math.exp(-gamma * sq_dist)
    return kernel


class SVMSetup:
    """Support Vector Machine learning setup for classification.

    Shows how to:
    - Prepare data (normalization is important for SVM)
    - Train SVM with appropriate kernel
    - Evaluate performance
    - Make predictions
    """

    def __init__(self, kernel=None, C=1.0):
        """
        Args:
            kernel: Kernel function (default: linear)
            C: Regularization parameter
        """
        self.kernel = kernel or linear_kernel
        self.C = C
        self.model = SimpleSVM(kernel=self.kernel, C=C)
        self.feature_means = None
        self.feature_stds = None

    def fit(self, X_train, y_train):
        """Train SVM with feature normalization."""
        # Normalize
        X_train = self._normalize(X_train, fit=True)

        # Convert to -1, 1 labels if needed
        unique_labels = list(set(y_train))
        if 0 in unique_labels:
            y_train = [1 if y == 1 else -1 for y in y_train]

        self.model.fit(X_train, y_train)
        return self

    def predict(self, X_test):
        """Predict class labels."""
        X_test = self._normalize(X_test, fit=False)
        return self.model.predict(X_test)

    def decision_function(self, X_test):
        """Get raw decision scores."""
        X_test = self._normalize(X_test, fit=False)
        return self.model.decision_function(X_test)

    def evaluate(self, X_test, y_test):
        """Evaluate accuracy."""
        predictions = self.predict(X_test)
        # Convert to 0,1 if needed
        predictions = [1 if p == 1 else 0 for p in predictions]
        accuracy = sum(1 for t, p in zip(y_test, predictions) if t == p) / len(y_test)
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


class SimpleSVM:
    """Simplified SVM implementation for learning setup."""

    def __init__(self, kernel=None, C=1.0, learning_rate=0.01, epochs=100):
        self.kernel = kernel or linear_kernel
        self.C = C
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.alphas = []
        self.bias = 0.0
        self.X_train = []
        self.y_train = []

    def fit(self, X, y):
        """Fit SVM using simple SGD."""
        self.X_train = [list(x) for x in X]
        self.y_train = list(y)
        n = len(X)

        self.alphas = [0.0] * n
        self.bias = 0.0

        for epoch in range(self.epochs):
            for i in range(n):
                decision = self._compute_decision(i)
                margin = self.y_train[i] * decision

                if margin < 1:
                    self.alphas[i] += self.learning_rate
                    self.bias += self.learning_rate * self.y_train[i]

        return self

    def predict(self, X):
        """Predict class labels (-1 or 1)."""
        return [1 if self._compute_decision_full(x) >= 0 else -1 for x in X]

    def decision_function(self, X):
        """Get raw decision values."""
        return [self._compute_decision_full(x) for x in X]

    def _compute_decision(self, i):
        """Compute decision for training sample."""
        decision = 0.0
        for j in range(len(self.X_train)):
            if self.alphas[j] > 0:
                k = self.kernel(self.X_train[j], self.X_train[i])
                decision += self.alphas[j] * self.y_train[j] * k
        return decision + self.bias

    def _compute_decision_full(self, x):
        """Compute decision for new sample."""
        decision = 0.0
        for j in range(len(self.X_train)):
            if self.alphas[j] > 0:
                k = self.kernel(self.X_train[j], x)
                decision += self.alphas[j] * self.y_train[j] * k
        return decision + self.bias


if __name__ == "__main__":
    # Classification example
    X_train = [
        [1.0, 1.0],
        [2.0, 2.0],
        [5.0, 5.0],
        [6.0, 6.0],
    ]
    y_train = [0, 0, 1, 1]

    X_test = [
        [1.5, 1.5],
        [5.5, 5.5],
    ]
    y_test = [0, 1]

    # Linear SVM
    setup = SVMSetup(kernel=linear_kernel, C=1.0)
    setup.fit(X_train, y_train)

    metrics = setup.evaluate(X_test, y_test)
    print(f"SVM Accuracy: {metrics['accuracy']:.2%}")

    decisions = setup.decision_function(X_test)
    print(f"Decision scores: {[round(d, 2) for d in decisions]}")

    print("\nSVM Learning Setup complete!")

    # RBF kernel example
    setup_rbf = SVMSetup(kernel=rbf_kernel(gamma=0.5), C=1.0)
    setup_rbf.fit(X_train, y_train)
    print(f"RBF SVM Accuracy: {setup_rbf.evaluate(X_test, y_test)['accuracy']:.2%}")
