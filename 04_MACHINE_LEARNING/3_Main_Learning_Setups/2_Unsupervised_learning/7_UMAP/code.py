"""Chapter 4.3.11: UMAP as an Unsupervised Learning Setup.

Uniform Manifold Approximation and Projection.
"""

import math
import random


class UMAPSetup:
    """UMAP for nonlinear dimensionality reduction."""

    def __init__(self, n_components=2, n_neighbors=15, learning_rate=1.0, epochs=200):
        self.n_components = n_components
        self.n_neighbors = n_neighbors
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.embedding = None

    def fit_transform(self, X):
        """Fit and transform data."""
        n_samples = len(X)
        
        # Build graph (k-NN)
        graph = self._build_knn_graph(X)
        
        # Initialize embedding
        self.embedding = [[random.gauss(0, 0.01) for _ in range(self.n_components)] 
                         for _ in range(n_samples)]
        
        # Optimize
        for epoch in range(self.epochs):
            for i in range(n_samples):
                for j in graph[i]:
                    # Attractive force
                    d = math.sqrt(sum((self.embedding[i][k] - self.embedding[j][k]) ** 2 
                                     for k in range(self.n_components)))
                    if d > 0:
                        for k in range(self.n_components):
                            self.embedding[i][k] -= 0.8 * self.learning_rate * \
                                (self.embedding[i][k] - self.embedding[j][k]) / d
        
        return self.embedding

    def _build_knn_graph(self, X):
        """Build k-nearest neighbor graph."""
        n = len(X)
        graph = [[] for _ in range(n)]
        
        # Compute distances
        for i in range(n):
            neighbors = []
            for j in range(n):
                if i == j:
                    continue
                d = math.sqrt(sum((X[i][k] - X[j][k]) ** 2 for k in range(len(X[0]))))
                neighbors.append((d, j))
            
            neighbors.sort()
            graph[i] = [j for _, j in neighbors[:self.n_neighbors]]
        
        return graph


if __name__ == "__main__":
    random.seed(42)
    X = [[random.gauss(0, 1), random.gauss(0, 1), random.gauss(0, 1)] for _ in range(30)]
    
    umap = UMAPSetup(n_components=2, epochs=100)
    embedding = umap.fit_transform(X)
    
    print(f"UMAP 2D embedding shape: (30, 2)")
    print(f"First sample: {[round(x, 2) for x in embedding[0]]}")
