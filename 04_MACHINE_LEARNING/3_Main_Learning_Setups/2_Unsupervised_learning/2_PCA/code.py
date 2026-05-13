"""Chapter 4.3.6: Principal Component Analysis as an Unsupervised Learning Setup.

This demonstrates PCA:
- Dimensionality reduction
- Feature extraction
- Variance explained
- Visualization preparation

Uses linear algebra for dimensionality reduction.
"""

import math


class PCASetup:
    """PCA for unsupervised dimensionality reduction."""

    def __init__(self, n_components=2):
        """
        Args:
            n_components: Number of principal components to keep
        """
        self.n_components = n_components
        self.mean = None
        self.components = None
        self.explained_variance = None

    def fit(self, X):
        """Fit PCA to data."""
        n_samples = len(X)
        n_features = len(X[0]) if X else 0

        # Center data
        self.mean = [sum(X[i][j] for i in range(n_samples)) / n_samples for j in range(n_features)]
        X_centered = [[X[i][j] - self.mean[j] for j in range(n_features)] for i in range(n_samples)]

        # Covariance matrix
        cov = self._covariance_matrix(X_centered)

        # Eigendecomposition (simplified: power iteration)
        eigenvectors, eigenvalues = self._eigen_decomposition(cov, min(self.n_components, n_features))

        # Sort by variance
        pairs = sorted(zip(eigenvalues, eigenvectors), reverse=True, key=lambda p: p[0])
        self.explained_variance = [p[0] / sum(eigenvalues) * 100 for p in pairs[:self.n_components]]
        self.components = [p[1] for p in pairs[:self.n_components]]

        return self

    def transform(self, X):
        """Project data onto principal components."""
        X_centered = [[X[i][j] - self.mean[j] for j in range(len(X[0]))] for i in range(len(X))]
        
        # Project
        X_transformed = []
        for x in X_centered:
            pc_coords = [self._dot(self.components[i], x) for i in range(min(self.n_components, len(self.components)))]
            X_transformed.append(pc_coords)

        return X_transformed

    def fit_transform(self, X):
        """Fit and transform in one step."""
        self.fit(X)
        return self.transform(X)

    def get_explained_variance_ratio(self):
        """Get percentage of variance explained."""
        return self.explained_variance

    def _covariance_matrix(self, X):
        """Compute covariance matrix."""
        n_samples = len(X)
        n_features = len(X[0]) if X else 0

        cov = [[0.0 for _ in range(n_features)] for _ in range(n_features)]

        for i in range(n_features):
            for j in range(n_features):
                cov[i][j] = sum(X[k][i] * X[k][j] for k in range(n_samples)) / n_samples

        return cov

    def _eigen_decomposition(self, matrix, n_components):
        """Simple eigendecomposition using power iteration."""
        n = len(matrix)
        eigenvalues = []
        eigenvectors = []

        A = [row[:] for row in matrix]  # Copy

        for _ in range(n_components):
            # Power iteration
            v = [1.0] * n  # Initial guess
            for __ in range(100):  # Power iterations
                Av = [self._dot(A[i], v) for i in range(n)]
                norm = math.sqrt(sum(x ** 2 for x in Av))
                if norm > 1e-10:
                    v = [x / norm for x in Av]

            # Eigenvalue
            Av = [self._dot(A[i], v) for i in range(n)]
            eigenvalue = self._dot(v, Av)
            eigenvalues.append(eigenvalue)
            eigenvectors.append(v)

            # Deflate matrix
            for i in range(n):
                for j in range(n):
                    A[i][j] -= eigenvalue * v[i] * v[j]

        return eigenvectors, eigenvalues

    @staticmethod
    def _dot(a, b):
        """Dot product."""
        return sum(x * y for x, y in zip(a, b))


if __name__ == "__main__":
    # 3D data to reduce to 2D
    import random
    random.seed(42)

    X = []
    for _ in range(30):
        # X and Y correlated, Z noise
        x = random.gauss(0, 1)
        X.append([x, x + random.gauss(0, 0.1), random.gauss(0, 0.5)])

    # PCA
    pca = PCASetup(n_components=2)
    X_reduced = pca.fit_transform(X)

    print(f"Original shape: (30, 3)")
    print(f"Reduced shape: (30, 2)")
    print(f"Variance explained: {[round(v, 1) for v in pca.get_explained_variance_ratio()]}%")
    print(f"Total variance: {sum(pca.get_explained_variance_ratio()):.1f}%")

    print(f"\nFirst sample reduced: {[round(x, 2) for x in X_reduced[0]]}")

    print("\nPCA Learning Setup complete!")
