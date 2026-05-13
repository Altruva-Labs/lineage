"""Chapter 4.3.10: t-SNE as an Unsupervised Learning Setup.

t-Distributed Stochastic Neighbor Embedding for visualization.
"""

import math
import random


class TSNESetup:
    """t-SNE for nonlinear dimensionality reduction and visualization."""

    def __init__(self, n_components=2, perplexity=30, learning_rate=200, n_iters=1000):
        self.n_components = n_components
        self.perplexity = perplexity
        self.learning_rate = learning_rate
        self.n_iters = n_iters
        self.embedding = None

    def fit_transform(self, X):
        """Fit and transform data."""
        n_samples = len(X)
        
        # Compute pairwise distances
        distances = self._pairwise_distances(X)
        
        # Initialize embedding
        self.embedding = [[random.gauss(0, 1e-4) for _ in range(self.n_components)] 
                         for _ in range(n_samples)]
        
        # Gradient descent
        for iteration in range(self.n_iters):
            # Compute gradients
            gradients = self._compute_gradients(distances)
            
            # Update embedding
            lr = self.learning_rate if iteration < self.n_iters / 2 else self.learning_rate / 2
            for i in range(n_samples):
                for j in range(self.n_components):
                    self.embedding[i][j] -= lr * gradients[i][j]
        
        return self.embedding

    def _pairwise_distances(self, X):
        """Compute pairwise Euclidean distances."""
        n = len(X)
        dist = [[0.0] * n for _ in range(n)]
        
        for i in range(n):
            for j in range(i + 1, n):
                d = math.sqrt(sum((X[i][k] - X[j][k]) ** 2 for k in range(len(X[0]))))
                dist[i][j] = d
                dist[j][i] = d
        
        return dist

    def _compute_gradients(self, distances):
        """Simplified gradient computation."""
        n = len(distances)
        gradients = [[0.0] * self.n_components for _ in range(n)]
        
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                
                # Euclidean distance in embedding space
                d_ij = math.sqrt(sum((self.embedding[i][k] - self.embedding[j][k]) ** 2 
                                    for k in range(self.n_components)))
                
                if d_ij > 1e-8:
                    # Simplified t-SNE gradient
                    coeff = 1.0 / (1 + d_ij ** 2)
                    for k in range(self.n_components):
                        gradients[i][k] += coeff * (self.embedding[i][k] - self.embedding[j][k])
        
        return gradients


if __name__ == "__main__":
    random.seed(42)
    # 3D data
    X = [[random.gauss(0, 1), random.gauss(0, 1), random.gauss(0, 1)] for _ in range(30)]
    
    tsne = TSNESetup(n_components=2, n_iters=100)
    embedding = tsne.fit_transform(X)
    
    print(f"2D embedding shape: (30, 2)")
    print(f"First sample embedded: {[round(x, 2) for x in embedding[0]]}")
