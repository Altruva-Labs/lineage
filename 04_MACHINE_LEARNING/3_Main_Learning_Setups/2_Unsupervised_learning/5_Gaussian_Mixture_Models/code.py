"""Chapter 4.3.9: Gaussian Mixture Models as an Unsupervised Learning Setup."""

import math
import random


class GMMSetup:
    """Gaussian Mixture Model for soft clustering."""

    def __init__(self, n_clusters=3, max_iters=100):
        self.n_clusters = n_clusters
        self.max_iters = max_iters
        self.means = []
        self.responsibilities = None

    def fit(self, X):
        """Fit GMM using EM algorithm."""
        n_samples = len(X)
        n_features = len(X[0]) if X else 0
        
        # Initialize random means
        indices = random.sample(range(n_samples), min(self.n_clusters, n_samples))
        self.means = [list(X[i]) for i in indices]
        
        for iteration in range(self.max_iters):
            # E-step: compute responsibilities
            responsibilities = self._e_step(X)
            
            # M-step: update means
            new_means = self._m_step(X, responsibilities)
            
            if self._converged(self.means, new_means):
                break
            self.means = new_means
        
        self.responsibilities = self._e_step(X)
        return self

    def predict(self, X):
        """Assign to most likely cluster."""
        responsibilities = []
        for x in X:
            resp = [self._gaussian_pdf(x, self.means[k]) for k in range(self.n_clusters)]
            total = sum(resp)
            if total > 0:
                resp = [r / total for r in resp]
            responsibilities.append(resp)
        return [max(range(self.n_clusters), key=lambda k: r[k]) for r in responsibilities]

    def _e_step(self, X):
        """E-step: compute responsibilities."""
        responsibilities = []
        for x in X:
            resp = [self._gaussian_pdf(x, self.means[k]) for k in range(self.n_clusters)]
            total = sum(resp)
            if total > 0:
                resp = [r / total for r in resp]
            else:
                resp = [1.0 / self.n_clusters] * self.n_clusters
            responsibilities.append(resp)
        return responsibilities

    def _m_step(self, X, responsibilities):
        """M-step: update means."""
        n_samples = len(X)
        new_means = []
        
        for k in range(self.n_clusters):
            N_k = sum(responsibilities[i][k] for i in range(n_samples))
            if N_k > 0:
                mean = [sum(responsibilities[i][k] * X[i][j] for i in range(n_samples)) / N_k
                       for j in range(len(X[0]))]
            else:
                mean = list(self.means[k])
            new_means.append(mean)
        
        return new_means

    @staticmethod
    def _gaussian_pdf(x, mean):
        """Gaussian probability."""
        dist = sum((a - b) ** 2 for a, b in zip(x, mean))
        return math.exp(-dist / 2)

    @staticmethod
    def _converged(old_means, new_means, tol=1e-4):
        """Check convergence."""
        for o, n in zip(old_means, new_means):
            if math.sqrt(sum((a - b) ** 2 for a, b in zip(o, n))) > tol:
                return False
        return True


if __name__ == "__main__":
    random.seed(42)
    X = [[random.gauss(0, 1), random.gauss(0, 1)] for _ in range(20)]
    
    gmm = GMMSetup(n_clusters=2)
    gmm.fit(X)
    labels = gmm.predict(X)
    print(f"GMM clusters: {labels}")
