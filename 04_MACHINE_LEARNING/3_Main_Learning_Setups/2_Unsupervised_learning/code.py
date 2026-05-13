"""Unsupervised learning demos built from classical ML models."""

from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path


def load_module(module_path):
    spec = spec_from_file_location(module_path.stem, module_path)
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


BASE_DIR = Path(__file__).resolve().parents[2] / "2_Classical_ML_Models"
cluster_module = load_module(BASE_DIR / "4_Clustering_and_Dimensionality_Reduction" / "code.py")


def run_unsupervised_demo():
    print("Unsupervised learning with classical models\n")

    X = [
        [1.0, 1.2],
        [1.1, 0.9],
        [4.0, 4.2],
        [3.9, 3.8],
        [0.9, 1.1],
        [4.2, 4.1],
    ]

    kmeans = cluster_module.KMeans(k=2, random_state=1).fit(X)
    print("k-means clustering")
    print("labels:", kmeans.labels_)
    print("centroids:", [[round(value, 3) for value in center] for center in kmeans.centroids])

    pca = cluster_module.PCA(n_components=1)
    reduced = pca.fit_transform(X)
    print("\nPCA")
    print("1D projection:", [round(row[0], 4) for row in reduced])


if __name__ == "__main__":
    run_unsupervised_demo()
