"""Chapter 4.3.5: K-Means as an Unsupervised Learning Setup.

This demonstrates K-Means clustering in practice:
- Data preparation
- Finding optimal K
- Interpreting clusters
- Using clusters for downstream tasks

Uses K-Means from Chapter 4.2.21.
"""

import math
import random
from collections import defaultdict


class KMeansSetup:
    """K-Means clustering as an unsupervised learning setup.

    Shows practical workflow for clustering tasks.
    """

    def __init__(self, n_clusters=3, max_iters=100, random_state=None):
        """
        Args:
            n_clusters: Number of clusters
            max_iters: Maximum iterations
            random_state: Random seed
        """
        self.n_clusters = n_clusters
        self.max_iters = max_iters
        self.random_state = random_state
        self.centroids = []
        self.labels = []

    def fit(self, X):
        """Fit K-Means clustering."""
        if self.random_state is not None:
            random.seed(self.random_state)

        n_samples = len(X)

        # Initialize: random centroids
        indices = random.sample(range(n_samples), self.n_clusters)
        self.centroids = [list(X[i]) for i in indices]

        for iteration in range(self.max_iters):
            # Assign clusters
            self.labels = self._assign_clusters(X)

            # Compute new centroids
            new_centroids = self._compute_centroids(X)

            # Check convergence
            if self._centroids_converged(new_centroids):
                break

            self.centroids = new_centroids

        return self

    def predict(self, X):
        """Assign new points to nearest centroid."""
        return [self._nearest_centroid(x) for x in X]

    def get_centroids(self):
        """Get cluster centers."""
        return self.centroids

    def inertia(self, X):
        """Compute inertia (within-cluster sum of squares)."""
        total = 0.0
        for i, x in enumerate(X):
            label = self.labels[i]
            dist = self._euclidean(x, self.centroids[label])
            total += dist ** 2
        return total

    def silhouette_score(self, X):
        """Compute silhouette score (measure of cluster quality)."""
        if len(set(self.labels)) == 1:
            return 0.0

        scores = []
        for i, x in enumerate(X):
            # Intra-cluster distance
            a = self._avg_intra_distance(X, i)

            # Nearest cluster distance
            b = self._nearest_cluster_distance(X, i)

            if max(a, b) > 0:
                silhouette = (b - a) / max(a, b)
            else:
                silhouette = 0.0

            scores.append(silhouette)

        return sum(scores) / len(scores) if scores else 0.0

    def _assign_clusters(self, X):
        """Assign each point to nearest centroid."""
        labels = []
        for x in X:
            nearest = self._nearest_centroid(x)
            labels.append(nearest)
        return labels

    def _nearest_centroid(self, x):
        """Find nearest centroid."""
        distances = [self._euclidean(x, c) for c in self.centroids]
        return distances.index(min(distances))

    def _compute_centroids(self, X):
        """Compute new centroids from assignment."""
        n_features = len(X[0]) if X else 0
        new_centroids = []

        for k in range(self.n_clusters):
            cluster_points = [X[i] for i in range(len(X)) if self.labels[i] == k]

            if not cluster_points:
                # Keep old centroid if empty
                new_centroids.append(list(self.centroids[k]))
            else:
                # Compute mean
                centroid = [
                    sum(p[j] for p in cluster_points) / len(cluster_points)
                    for j in range(n_features)
                ]
                new_centroids.append(centroid)

        return new_centroids

    def _centroids_converged(self, new_centroids):
        """Check if centroids have converged."""
        threshold = 1e-4
        for old, new in zip(self.centroids, new_centroids):
            if self._euclidean(old, new) > threshold:
                return False
        return True

    @staticmethod
    def _euclidean(a, b):
        """Euclidean distance."""
        return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))

    def _avg_intra_distance(self, X, i):
        """Average distance to others in same cluster."""
        cluster_points = [X[j] for j in range(len(X)) if self.labels[j] == self.labels[i]]
        if len(cluster_points) <= 1:
            return 0.0
        distances = [self._euclidean(X[i], p) for p in cluster_points if p != X[i]]
        return sum(distances) / len(distances) if distances else 0.0

    def _nearest_cluster_distance(self, X, i):
        """Distance to nearest cluster (not current)."""
        min_dist = float("inf")
        for k in range(self.n_clusters):
            if k == self.labels[i]:
                continue
            cluster_points = [X[j] for j in range(len(X)) if self.labels[j] == k]
            if cluster_points:
                avg_dist = sum(self._euclidean(X[i], p) for p in cluster_points) / len(cluster_points)
                min_dist = min(min_dist, avg_dist)
        return min_dist if min_dist != float("inf") else 0.0


def find_optimal_k(X, k_range=(2, 10)):
    """Find optimal number of clusters using elbow method."""
    inertias = []

    for k in range(k_range[0], k_range[1] + 1):
        setup = KMeansSetup(n_clusters=k, random_state=42)
        setup.fit(X)
        inertias.append(setup.inertia(X))

    return inertias


if __name__ == "__main__":
    # Synthetic dataset: 2D points
    random.seed(42)
    X = []

    # Cluster 1
    for _ in range(20):
        X.append([1 + random.gauss(0, 0.5), 1 + random.gauss(0, 0.5)])

    # Cluster 2
    for _ in range(20):
        X.append([5 + random.gauss(0, 0.5), 5 + random.gauss(0, 0.5)])

    # Cluster 3
    for _ in range(20):
        X.append([2 + random.gauss(0, 0.5), 5 + random.gauss(0, 0.5)])

    # Find optimal K
    inertias = find_optimal_k(X, k_range=(2, 6))
    print("Inertias for K=2 to 6:", [round(i, 1) for i in inertias])

    # Train with K=3
    setup = KMeansSetup(n_clusters=3, random_state=42)
    setup.fit(X)

    print(f"Cluster assignments (first 5): {setup.labels[:5]}")
    print(f"Cluster centers: {[[round(x, 2) for x in c] for c in setup.centroids]}")
    print(f"Inertia: {setup.inertia(X):.2f}")
    print(f"Silhouette Score: {setup.silhouette_score(X):.3f}")

    print("\nK-Means Learning Setup complete!")
