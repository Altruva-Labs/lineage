"""Chapter 4.3.8: Hierarchical Clustering as an Unsupervised Learning Setup."""

import math


class HierarchicalClusteringSetup:
    """Agglomerative hierarchical clustering."""

    def __init__(self, n_clusters=3, linkage="ward"):
        self.n_clusters = n_clusters
        self.linkage = linkage
        self.labels = None

    def fit(self, X):
        """Build dendrogram and cut at appropriate level."""
        n_samples = len(X)
        
        # Initialize: each point is a cluster
        clusters = [[i] for i in range(n_samples)]
        distances = [[0] * len(clusters) for _ in range(len(clusters))]

        while len(clusters) > self.n_clusters:
            # Find closest clusters
            min_dist = float("inf")
            merge_i, merge_j = 0, 1
            
            for i in range(len(clusters)):
                for j in range(i + 1, len(clusters)):
                    dist = self._cluster_distance(X, clusters[i], clusters[j])
                    if dist < min_dist:
                        min_dist = dist
                        merge_i, merge_j = i, j

            # Merge clusters
            clusters[merge_i].extend(clusters[merge_j])
            clusters.pop(merge_j)

        # Assign labels
        self.labels = [-1] * n_samples
        for cluster_id, cluster in enumerate(clusters):
            for point_idx in cluster:
                self.labels[point_idx] = cluster_id

        return self

    def _cluster_distance(self, X, cluster1, cluster2):
        """Compute distance between clusters."""
        if self.linkage == "ward":
            return self._ward_distance(X, cluster1, cluster2)
        elif self.linkage == "complete":
            return max(self._euclidean(X[i], X[j]) for i in cluster1 for j in cluster2)
        else:  # single
            return min(self._euclidean(X[i], X[j]) for i in cluster1 for j in cluster2)

    @staticmethod
    def _ward_distance(X, cluster1, cluster2):
        """Ward linkage distance."""
        c1_mean = [sum(X[i][j] for i in cluster1) / len(cluster1) for j in range(len(X[0]))]
        c2_mean = [sum(X[i][j] for i in cluster2) / len(cluster2) for j in range(len(X[0]))]
        return sum((a - b) ** 2 for a, b in zip(c1_mean, c2_mean))

    @staticmethod
    def _euclidean(a, b):
        return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))


if __name__ == "__main__":
    import random
    random.seed(42)
    X = [[random.gauss(0, 1), random.gauss(0, 1)] for _ in range(20)]

    hc = HierarchicalClusteringSetup(n_clusters=3)
    hc.fit(X)
    print(f"Hierarchical clustering labels: {hc.labels}")
