"""Supervised learning demos built from classical ML models."""

from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path


def load_module(module_path):
    spec = spec_from_file_location(module_path.stem, module_path)
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


BASE_DIR = Path(__file__).resolve().parents[2] / "2_Classical_ML_Models"
linear_module = load_module(BASE_DIR / "1_Linear_Models" / "code.py")
tree_module = load_module(BASE_DIR / "2_Decision_Trees" / "code.py")
knn_module = load_module(BASE_DIR / "3_Nearest_Neighbor_Methods" / "code.py")


def run_supervised_demo():
    print("Supervised learning with classical models\n")

    X_reg = [[1], [2], [3], [4], [5], [6]]
    y_reg = [3, 5, 7, 9, 11, 13]
    linear = linear_module.LinearRegressionGD(learning_rate=0.01, epochs=3000).fit(X_reg, y_reg)
    reg_predictions = linear.predict(X_reg)
    print("Linear regression")
    print("mse:", round(linear_module.mean_squared_error(y_reg, reg_predictions), 6))

    X_clf = [[0.1], [0.3], [0.7], [0.9], [1.2], [1.5]]
    y_clf = [0, 0, 0, 1, 1, 1]
    logistic = linear_module.LogisticRegressionGD(learning_rate=0.5, epochs=4000).fit(X_clf, y_clf)
    log_predictions = logistic.predict(X_clf)
    print("\nLogistic regression")
    print("accuracy:", round(linear_module.accuracy_score(y_clf, log_predictions), 4))

    X_tree = [
        [2, 35],
        [3, 40],
        [6, 78],
        [5, 74],
        [1, 20],
        [7, 82],
    ]
    y_tree = [0, 0, 1, 1, 0, 1]
    tree = tree_module.DecisionTreeClassifier(max_depth=3).fit(X_tree, y_tree)
    tree_predictions = tree.predict(X_tree)
    print("\nDecision tree")
    print("accuracy:", round(tree_module.accuracy_score(y_tree, tree_predictions), 4))

    X_knn = [[1, 1], [1.2, 0.8], [4, 4], [4.2, 3.8], [0.8, 1.1], [3.9, 4.1]]
    y_knn = [0, 0, 1, 1, 0, 1]
    knn = knn_module.KNNClassifier(k=3).fit(X_knn, y_knn)
    knn_predictions = knn.predict(X_knn)
    print("\nk-nearest neighbors")
    print("accuracy:", round(knn_module.accuracy_score(y_knn, knn_predictions), 4))


if __name__ == "__main__":
    run_supervised_demo()
