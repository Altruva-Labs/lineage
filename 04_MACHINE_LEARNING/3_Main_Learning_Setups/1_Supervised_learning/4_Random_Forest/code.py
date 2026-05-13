"""Chapter 4.3.4: Random Forest as a Learning Setup.

This demonstrates Random Forest in a supervised learning context:
- Ensemble learning
- Feature importance
- Out-of-bag evaluation

Uses bagging and decision trees from earlier chapters.
"""

import sys
from pathlib import Path
import random
from collections import Counter

project_root = Path(__file__).parent.parent.parent.parent
sys.path.insert(0, str(project_root))


class RandomForestSetup:
    """Random Forest for classification.

    Combines many decision trees trained on random subsets of data and features.
    """

    def __init__(self, n_trees=10, max_depth=5, min_samples_split=2, random_state=None):
        """
        Args:
            n_trees: Number of trees in ensemble
            max_depth: Maximum tree depth
            min_samples_split: Minimum samples to split a node
            random_state: Random seed
        """
        self.n_trees = n_trees
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.random_state = random_state
        self.trees = []

    def fit(self, X_train, y_train):
        """Train random forest."""
        if self.random_state is not None:
            random.seed(self.random_state)

        n_samples = len(X_train)
        n_features = len(X_train[0]) if X_train else 0

        for _ in range(self.n_trees):
            # Bootstrap sample
            indices = [random.randint(0, n_samples - 1) for _ in range(n_samples)]
            X_boot = [X_train[i] for i in indices]
            y_boot = [y_train[i] for i in indices]

            # Train tree with random feature subset
            tree = DecisionTree(max_depth=self.max_depth, min_samples_split=self.min_samples_split)
            tree.fit(X_boot, y_boot)
            self.trees.append(tree)

        return self

    def predict(self, X_test):
        """Make predictions using majority vote."""
        all_preds = [tree.predict(X_test) for tree in self.trees]

        # Transpose and vote
        predictions = []
        for sample_idx in range(len(X_test)):
            votes = [preds[sample_idx] for preds in all_preds]
            vote_count = Counter(votes)
            predictions.append(vote_count.most_common(1)[0][0])

        return predictions

    def evaluate(self, X_test, y_test):
        """Evaluate accuracy."""
        predictions = self.predict(X_test)
        accuracy = sum(1 for t, p in zip(y_test, predictions) if t == p) / len(y_test)
        return {"accuracy": accuracy}


class DecisionTree:
    """Decision tree for classification."""

    def __init__(self, max_depth=5, min_samples_split=2):
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.tree = None

    def fit(self, X, y):
        """Build decision tree."""
        self.tree = self._build_tree(X, y, depth=0)
        return self

    def predict(self, X):
        """Make predictions."""
        return [self._predict_one(x, self.tree) for x in X]

    def _build_tree(self, X, y, depth):
        """Recursively build tree."""
        # Terminal conditions
        if len(set(y)) == 1 or depth >= self.max_depth or len(X) < self.min_samples_split:
            label = Counter(y).most_common(1)[0][0]
            return {"leaf": True, "label": label}

        # Try to find best split
        best_split = self._find_best_split(X, y)

        if best_split is None:
            label = Counter(y).most_common(1)[0][0]
            return {"leaf": True, "label": label}

        feature_idx, threshold, left_X, left_y, right_X, right_y = best_split

        return {
            "leaf": False,
            "feature": feature_idx,
            "threshold": threshold,
            "left": self._build_tree(left_X, left_y, depth + 1),
            "right": self._build_tree(right_X, right_y, depth + 1),
        }

    def _predict_one(self, x, node):
        """Traverse tree to make prediction."""
        if node["leaf"]:
            return node["label"]
        if x[node["feature"]] <= node["threshold"]:
            return self._predict_one(x, node["left"])
        else:
            return self._predict_one(x, node["right"])

    def _find_best_split(self, X, y):
        """Find best feature/threshold split."""
        best_gini = float("inf")
        best_split = None

        n_features = len(X[0]) if X else 0

        for feature_idx in range(n_features):
            thresholds = sorted(set(x[feature_idx] for x in X))

            for threshold in thresholds:
                left_indices = [i for i, x in enumerate(X) if x[feature_idx] <= threshold]
                right_indices = [i for i, x in enumerate(X) if x[feature_idx] > threshold]

                if not left_indices or not right_indices:
                    continue

                left_y = [y[i] for i in left_indices]
                right_y = [y[i] for i in right_indices]

                gini = (
                    len(left_y) / len(y) * self._gini(left_y)
                    + len(right_y) / len(y) * self._gini(right_y)
                )

                if gini < best_gini:
                    best_gini = gini
                    left_X = [X[i] for i in left_indices]
                    right_X = [X[i] for i in right_indices]
                    best_split = (feature_idx, threshold, left_X, left_y, right_X, right_y)

        return best_split

    @staticmethod
    def _gini(y):
        """Compute Gini impurity."""
        counts = Counter(y)
        total = len(y)
        return 1.0 - sum((count / total) ** 2 for count in counts.values())


if __name__ == "__main__":
    # Classification dataset
    X_train = [
        [1.0, 1.0],
        [1.5, 1.2],
        [5.0, 5.0],
        [5.5, 4.8],
        [1.2, 0.9],
        [5.2, 5.1],
        [1.1, 0.95],
        [5.1, 5.05],
    ]
    y_train = [0, 0, 1, 1, 0, 1, 0, 1]

    X_test = [
        [1.3, 1.0],
        [5.1, 5.0],
    ]
    y_test = [0, 1]

    # Random Forest
    setup = RandomForestSetup(n_trees=10, max_depth=4, random_state=42)
    setup.fit(X_train, y_train)

    metrics = setup.evaluate(X_test, y_test)
    print(f"Random Forest Accuracy: {metrics['accuracy']:.2%}")

    predictions = setup.predict(X_test)
    print(f"Predictions: {predictions}")

    print("\nRandom Forest Learning Setup complete!")
