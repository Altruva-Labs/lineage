"""
Linear Regression Implementation from Scratch

This module implements linear regression using two approaches:
1. Normal Equation (closed-form solution)
2. Gradient Descent (iterative solution)

"""

import numpy as np
from typing import Tuple, List
import matplotlib.pyplot as plt


class LinearRegressionNormalEquation:
    """
    Linear Regression using the Normal Equation (closed-form solution).
    
    The normal equation finds the optimal weights directly:
    w = (X^T * X)^(-1) * X^T * y
    
    Advantages:
    - Finds exact solution in one step
    - No hyperparameters to tune
    
    Disadvantages:
    - Slow for very large datasets
    - Requires matrix inversion (can be unstable)
    """
    
    def __init__(self):
        self.weights = None
        self.bias = None
        self.mean_x = None
        self.std_x = None
    
    def fit(self, X: np.ndarray, y: np.ndarray) -> 'LinearRegressionNormalEquation':
        """
        Learn the model from training data using the normal equation.
        
        Args:
            X: Training features of shape (n_samples, n_features)
            y: Training targets of shape (n_samples,)
        
        Returns:
            self: Returns the fitted model
        """
        
        # Store statistics for later prediction normalization
        self.mean_x = np.mean(X, axis=0)
        self.std_x = np.std(X, axis=0) + 1e-8  # Avoid division by zero
        
        # Normalize features for stability
        X_normalized = (X - self.mean_x) / self.std_x
        
        # Add bias term (column of ones)
        X_with_bias = np.column_stack([np.ones(X_normalized.shape[0]), X_normalized])
        
        # Normal equation: w = (X^T * X)^(-1) * X^T * y
        # This minimizes the sum of squared errors
        XtX = X_with_bias.T @ X_with_bias
        Xty = X_with_bias.T @ y
        
        # Solve the system
        coefficients = np.linalg.lstsq(XtX, Xty, rcond=None)[0]
        
        # Store bias and weights separately
        self.bias = coefficients[0]
        self.weights = coefficients[1:]
        
        return self
    
    def predict(self, X: np.ndarray) -> np.ndarray:
        """
        Make predictions on new data.
        
        Args:
            X: Features of shape (n_samples, n_features)
        
        Returns:
            Predictions of shape (n_samples,)
        """
        if self.weights is None:
            raise ValueError("Model must be fitted before prediction")
        
        # Normalize using training statistics
        X_normalized = (X - self.mean_x) / self.std_x
        
        # y_hat = X * w + b
        predictions = X_normalized @ self.weights + self.bias
        return predictions
    
    def score(self, X: np.ndarray, y: np.ndarray) -> float:
        """
        Calculate R-squared (coefficient of determination).
        
        R^2 = 1 - (SS_res / SS_tot)
        
        Where:
        - SS_res = sum of squared residuals
        - SS_tot = total sum of squares
        
        Args:
            X: Features
            y: True targets
        
        Returns:
            R-squared score (1.0 is perfect, 0 is baseline)
        """
        y_pred = self.predict(X)
        ss_res = np.sum((y - y_pred) ** 2)
        ss_tot = np.sum((y - np.mean(y)) ** 2)
        return 1 - (ss_res / ss_tot)


class LinearRegressionGradientDescent:
    """
    Linear Regression using Gradient Descent (iterative learning).
    
    This approach:
    1. Starts with random weights
    2. Iteratively updates weights to reduce error
    3. Uses the gradient of the loss function to guide updates
    
    Advantages:
    - Scales well to huge datasets
    - Flexible (can use different learning algorithms)
    - Can be stopped early
    
    Disadvantages:
    - Requires hyperparameter tuning (learning rate, iterations)
    - Convergence is not guaranteed for non-convex problems
    """
    
    def __init__(self, learning_rate: float = 0.01, n_iterations: int = 1000, 
                 regularization: str = 'none', lambda_reg: float = 0.01):
        """
        Initialize the gradient descent linear regression.
        
        Args:
            learning_rate: Step size for updates (eta in the formula)
            n_iterations: Number of training iterations
            regularization: 'none', 'l1' (Lasso), 'l2' (Ridge)
            lambda_reg: Regularization strength
        """
        self.learning_rate = learning_rate
        self.n_iterations = n_iterations
        self.regularization = regularization
        self.lambda_reg = lambda_reg
        
        self.weights = None
        self.bias = None
        self.mean_x = None
        self.std_x = None
        self.loss_history = []
    
    def fit(self, X: np.ndarray, y: np.ndarray) -> 'LinearRegressionGradientDescent':
        """
        Learn the model from training data using gradient descent.
        
        Args:
            X: Training features of shape (n_samples, n_features)
            y: Training targets of shape (n_samples,)
        
        Returns:
            self: Returns the fitted model
        """
        n_samples, n_features = X.shape
        
        # Store statistics for normalization
        self.mean_x = np.mean(X, axis=0)
        self.std_x = np.std(X, axis=0) + 1e-8
        
        # Normalize features
        X_normalized = (X - self.mean_x) / self.std_x
        
        # Initialize weights and bias
        self.weights = np.zeros(n_features)
        self.bias = 0
        
        # Training loop
        for iteration in range(self.n_iterations):
            # Forward pass: make predictions
            y_pred = X_normalized @ self.weights + self.bias
            
            # Calculate error
            error = y_pred - y
            
            # Calculate gradients
            # dJ/dw = (2/n) * X^T * (y_pred - y)
            dw = (2 / n_samples) * (X_normalized.T @ error)
            db = (2 / n_samples) * np.sum(error)
            
            # Add regularization to weights (not bias)
            if self.regularization == 'l2':
                dw += (2 * self.lambda_reg / n_samples) * self.weights
            elif self.regularization == 'l1':
                dw += (self.lambda_reg / n_samples) * np.sign(self.weights)
            
            # Update parameters
            # w_new = w_old - learning_rate * gradient
            self.weights -= self.learning_rate * dw
            self.bias -= self.learning_rate * db
            
            # Record loss for visualization
            mse = np.mean(error ** 2)
            self.loss_history.append(mse)
            
            # Print progress every 100 iterations
            if (iteration + 1) % 100 == 0:
                print(f"Iteration {iteration + 1}/{self.n_iterations}, Loss: {mse:.6f}")
        
        return self
    
    def predict(self, X: np.ndarray) -> np.ndarray:
        """
        Make predictions on new data.
        
        Args:
            X: Features of shape (n_samples, n_features)
        
        Returns:
            Predictions of shape (n_samples,)
        """
        if self.weights is None:
            raise ValueError("Model must be fitted before prediction")
        
        X_normalized = (X - self.mean_x) / self.std_x
        predictions = X_normalized @ self.weights + self.bias
        return predictions
    
    def score(self, X: np.ndarray, y: np.ndarray) -> float:
        """
        Calculate R-squared score.
        
        Args:
            X: Features
            y: True targets
        
        Returns:
            R-squared score
        """
        y_pred = self.predict(X)
        ss_res = np.sum((y - y_pred) ** 2)
        ss_tot = np.sum((y - np.mean(y)) ** 2)
        return 1 - (ss_res / ss_tot)


# ============================================================================
# Example Usage
# ============================================================================

def example_house_price_prediction():
    """
    Example: Predicting house prices from size and number of bedrooms.
    """
    print("=" * 70)
    print("LINEAR REGRESSION EXAMPLE: House Price Prediction")
    print("=" * 70)
    
    # Create synthetic training data
    np.random.seed(42)
    n_samples = 100
    
    # Features: size (sqft) and bedrooms
    size = np.random.uniform(1000, 4000, n_samples)
    bedrooms = np.random.randint(1, 6, n_samples).astype(float)
    X_train = np.column_stack([size, bedrooms])
    
    # Target: price (synthetic relationship)
    # Price ≈ 150 * size + 50000 * bedrooms + 100000 + random noise
    y_train = 150 * size + 50000 * bedrooms + 100000 + np.random.normal(0, 20000, n_samples)
    
    # Create test data
    X_test = np.array([[2500, 4], [1800, 3], [3200, 5]])
    y_test = 150 * X_test[:, 0] + 50000 * X_test[:, 1] + 100000
    
    print("\n1. NORMAL EQUATION METHOD")
    print("-" * 70)
    
    # Train using normal equation
    model_ne = LinearRegressionNormalEquation()
    model_ne.fit(X_train, y_train)
    
    print(f"\nLearned weights: {model_ne.weights}")
    print(f"Learned bias: {model_ne.bias:.2f}")
    
    # Make predictions
    y_pred_ne = model_ne.predict(X_test)
    print(f"\nTest predictions (Normal Equation):")
    for i, (features, pred) in enumerate(zip(X_test, y_pred_ne)):
        print(f"  House {i+1} ({features[0]:.0f} sqft, {features[1]:.0f} bed): ${pred:,.0f}")
    
    # Score
    score_ne = model_ne.score(X_train, y_train)
    print(f"\nR-squared score on training data: {score_ne:.4f}")
    
    print("\n2. GRADIENT DESCENT METHOD")
    print("-" * 70)
    
    # Train using gradient descent
    model_gd = LinearRegressionGradientDescent(
        learning_rate=0.0001,
        n_iterations=500,
        regularization='none'
    )
    model_gd.fit(X_train, y_train)
    
    print(f"\nLearned weights: {model_gd.weights}")
    print(f"Learned bias: {model_gd.bias:.2f}")
    
    # Make predictions
    y_pred_gd = model_gd.predict(X_test)
    print(f"\nTest predictions (Gradient Descent):")
    for i, (features, pred) in enumerate(zip(X_test, y_pred_gd)):
        print(f"  House {i+1} ({features[0]:.0f} sqft, {features[1]:.0f} bed): ${pred:,.0f}")
    
    # Score
    score_gd = model_gd.score(X_train, y_train)
    print(f"\nR-squared score on training data: {score_gd:.4f}")
    
    print("\n3. COMPARISON")
    print("-" * 70)
    print(f"Normal Equation R²: {score_ne:.4f}")
    print(f"Gradient Descent R²: {score_gd:.4f}")
    print(f"Difference: {abs(score_ne - score_gd):.6f}")
    
    # Visualize loss history
    print("\n4. VISUALIZATION")
    print("-" * 70)
    
    plt.figure(figsize=(10, 5))
    
    # Loss history
    plt.subplot(1, 2, 1)
    plt.plot(model_gd.loss_history)
    plt.xlabel('Iteration')
    plt.ylabel('Mean Squared Error')
    plt.title('Training Loss Over Time')
    plt.grid(True, alpha=0.3)
    
    # Predictions vs actual (for test data visualization)
    plt.subplot(1, 2, 2)
    all_pred = model_ne.predict(X_train)
    plt.scatter(y_train, all_pred, alpha=0.6, label='Predictions')
    plt.plot([y_train.min(), y_train.max()], 
             [y_train.min(), y_train.max()], 
             'r--', lw=2, label='Perfect prediction')
    plt.xlabel('Actual Price ($)')
    plt.ylabel('Predicted Price ($)')
    plt.title('Predictions vs Actual Values')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('/tmp/linear_regression_example.png', dpi=100)
    print("Plot saved to /tmp/linear_regression_example.png")
    
    print("\n" + "=" * 70)
    print("Key Insights:")
    print("- Both methods learn similar patterns from the same data")
    print("- Normal equation finds the exact solution directly")
    print("- Gradient descent iteratively improves the solution")
    print("- For this simple problem, both achieve excellent R² scores")
    print("=" * 70)


if __name__ == "__main__":
    example_house_price_prediction()
