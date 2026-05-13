"""Chapter 4.3.7: DBSCAN as an Unsupervised Learning Setup.

DBSCAN: Density-Based Spatial Clustering of Applications with Noise.

Key advantages:
- Finds clusters of arbitrary shape
- Automatically detects number of clusters
- Identifies outliers/noise points
"""

import math


class DBSCANSetup:
    """DBSCAN clustering setup."""

    def __init__(self, epsilon=0.5, min_samples=5):
        """
        Args:
            epsilon: Maximum distance between neighbors
            min_samples: Minimum samples in neighborhood for core point
        """
        self.epsilon = epsilon
        self.min_samples = min_samples
        self.labels = None
        self.n_clusters = 0

    def fit(self, X):
        """Fit DBSCAN."""
        n_samples = len(X)
        self.labels = [-1] * n_samples  # -1 for noise
        cluster_id = 0

        for i in range(n_samples):
            if self.labels[i] != -1:
                continue

            neighbors = self._get_neighbors(X, i)
            if len(neighbors) < self.min_samples:
                # Mark as noise
                self.labels[i] = -1
            else:
                # Start new cluster
                self._expand_cluster(X, i, neighbors, cluster_id)
                cluster_id += 1

        self.n_clusters = len(set(l for l in self.labels if l >= 0))
        return self

    def predict(self, X_new):
        """Predict labels for new points (assign to nearest cluster)."""
        if self.labels is None:
            raise ValueError("Model not fitted yet")

        labels = []
        for x in X_new:
            # Find nearest labeled point
            min_dist = float("inf")
            nearest_label = -1
            for i, label in enumerate(self.labels):
                dist = self._euclidean(x, X_new[i] if i < len(X_new) else x)
                if dist < min_dist:
                    min_dist = dist
                    nearest_label = label
            labels.append(nearest_label)
        return labels

    def _expand_cluster(self, X, point_idx, neighbors, cluster_id):
        """Recursively expand cluster."""
        self.labels[point_idx] = cluster_id
        
        i = 0
        while i < len(neighbors):
            neighbor_idx = neighbors[i]
            
            if self.labels[neighbor_idx] == -1:
                self.labels[neighbor_idx] = cluster_id
            elif self.labels[neighbor_idx] != -1:
                i += 1
                continue
            
            # Check if neighbor is core point
            new_neighbors = self._get_neighbors(X, neighbor_idx)
            if len(new_neighbors) >= self.min_samples:
                neighbors.extend(new_neighbors)
            
            i += 1

    def _get_neighbors(self, X, point_idx):
        """Get neighbors within epsilon distance."""
        neighbors = []
        for i in range(len(X)):
            if self._euclidean(X[point_idx], X[i]) <= self.epsilon:
                neighbors.append(i)
        return neighbors

    @staticmethod
    def _euclidean(a, b):
        return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))


if __name__ == "__main__":
    import random
    random.seed(42)

    # Clustered data with outliers
    X = []
    for _ in range(20):
        X.append([1 + random.gauss(0, 0.3), 1 + random.gauss(0, 0.3)])
    for _ in range(20):
        X.append([5 + random.gauss(0, 0.3), 5 + random.gauss(0, 0.3)])
    # Add outliers
    X.append([0, 5])
    X.append([5, 0])

    dbscan = DBSCANSetup(epsilon=0.8, min_samples=5)
    dbscan.fit(X)

    print(f"Number of clusters: {dbscan.n_clusters}")
    print(f"Noise points: {sum(1 for l in dbscan.labels if l == -1)}")
    print(f"First 5 labels: {dbscan.labels[:5]}")

    print("\nDBSCAN Learning Setup complete!")
