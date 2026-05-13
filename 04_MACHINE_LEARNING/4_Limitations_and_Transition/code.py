"""Chapter 4.4: Classical ML Limitations and the Transition to Deep Learning

This module demonstrates the scaling challenge that forced the AI community
to transition from classical machine learning to neural networks.

Key insights:
1. Classical ML requires explicit feature engineering
2. Feature engineering doesn't scale to complex domains (images, text, audio)
3. Deep learning learns features automatically via neural networks
4. This enables scaling to larger datasets and more complex problems

Instructions:
- This code shows simple examples of:
  * Why high-dimensional data is hard with classical ML
  * Curse of dimensionality
  * Why neural networks became necessary for automatic feature learning
"""

from typing import List, Tuple
import math
import random


def euclidean_distance(x1: List[float], x2: List[float]) -> float:
    """Compute Euclidean distance between two points."""
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(x1, x2)))


def curse_of_dimensionality_demo():
    """
    Demonstrate the curse of dimensionality.
    
    As dimensions increase, points become increasingly sparse.
    - In 2D: neighbors are reasonably close
    - In 100D: all points are far apart!
    
    This breaks distance-based methods (k-NN, KNN clustering, etc.)
    """
    print("Curse of Dimensionality Demo")
    print("=" * 60)
    print()
    
    n_points = 1000
    
    for n_dims in [2, 10, 50, 100, 500]:
        # Generate random points in n_dims dimensions
        points = [
            [random.uniform(-1, 1) for _ in range(n_dims)]
            for _ in range(n_points)
        ]
        
        # Pick a reference point
        ref_point = points[0]
        
        # Find closest and farthest neighbors
        distances = [
            euclidean_distance(ref_point, p)
            for p in points[1:]
        ]
        
        min_dist = min(distances)
        max_dist = max(distances)
        avg_dist = sum(distances) / len(distances)
        
        print(f"Dimensions: {n_dims:3d}")
        print(f"  Closest neighbor distance:  {min_dist:.4f}")
        print(f"  Farthest neighbor distance: {max_dist:.4f}")
        print(f"  Average distance:           {avg_dist:.4f}")
        print(f"  Ratio (farthest/closest):   {max_dist/min_dist:.2f}×")
        print()
    
    print("Observation: As dimensions increase, all points become equally far apart.")
    print("This breaks k-NN and other distance-based methods!")
    print()


def feature_engineering_challenge():
    """
    Demonstrate why feature engineering is hard and doesn't scale.
    
    For simple problems, hand-crafted features work.
    For complex problems, humans can't design good features.
    """
    print("Feature Engineering Challenge")
    print("=" * 60)
    print()
    
    print("Problem 1: Handwritten Digit Recognition (MNIST)")
    print("-" * 60)
    print()
    print("Raw input: 28×28 pixel values = 784 dimensions")
    print()
    print("Possible hand-crafted features:")
    print("  1. Pixel intensity histogram (10 bins)")
    print("  2. Gradient magnitude (8 orientations)")
    print("  3. Stroke thickness / width")
    print("  4. Center of mass location")
    print("  5. Symmetry measures")
    print("  6. Contour shape features")
    print("  Total: ~50-100 features")
    print()
    print("Problem: Missing the right features.")
    print("  - 'Is there a loop?' (good for 6, 8, 9)")
    print("  - 'Slant angle' (good for 1, 7)")
    print("  - 'Curvature' (good for 2, 3, 5)")
    print()
    print("These require domain expertise to hand-engineer!")
    print()
    print()
    
    print("Problem 2: Object Recognition (ImageNet)")
    print("-" * 60)
    print()
    print("Raw input: 1000×1000 color images = 3,000,000 dimensions")
    print()
    print("Hand-crafted features:")
    print("  - SIFT features (only handles specific patterns)")
    print("  - HOG (Histogram of Oriented Gradients)")
    print("  - Color, texture, shape descriptors")
    print()
    print("Problem: Humans can't manually design features for")
    print("'cats', 'cars', 'trees' across infinite visual variations.")
    print()
    print()
    
    print("Problem 3: Natural Language Processing (Text)")
    print("-" * 60)
    print()
    print("Raw input: Sequences of ~50,000 unique words")
    print()
    print("Hand-crafted features:")
    print("  - Bag-of-words (lose all order) → doesn't work for negation")
    print("  - n-grams (lose long-range context)")
    print("  - Syntactic features (expensive to compute)")
    print()
    print("Problem: 'not bad' vs 'bad' mean opposite things.")
    print("Hard-coded rules fail on variations.")
    print()
    print()


def scaling_problem_demo():
    """
    Show why classical ML doesn't scale to modern dataset sizes.
    """
    print("Scaling Problem: Classical ML vs. Big Data")
    print("=" * 60)
    print()
    
    # Memory and computation requirements
    scenarios = [
        ("Iris Dataset", 150, 4),
        ("MNIST", 70000, 784),
        ("ImageNet", 1000000, 3*227*227),  # 3 channels, 227×227 images
        ("ImageNet (full)", 14000000, 3*1024*1024),  # 1024×1024
    ]
    
    print("Dataset | Samples | Dimensions | Classical ML Problem")
    print("-" * 60)
    
    for name, n_samples, n_features in scenarios:
        # k-NN memory: store all training data + compute pairwise distances
        # Complexity: O(n * d) space, O(n_test * n_train * d) time
        
        memory_gb = (n_samples * n_features * 8) / (1024**3)  # 8 bytes per float64
        distance_time_seconds = (n_samples * n_features) / 1e9  # rough estimate
        
        if memory_gb > 10:
            problem = f"MEMORY: {memory_gb:.1f} GB needed!"
        elif distance_time_seconds > 1:
            problem = f"TIME: {distance_time_seconds:.1f} sec per prediction"
        else:
            problem = "OK"
        
        print(f"{name:20} | {n_samples:7d} | {n_features:10d} | {problem}")
    
    print()
    print("Feature engineering scaling:")
    print("  - MNIST: feasible to hand-engineer features")
    print("  - ImageNet: extremely difficult and time-consuming")
    print("  - Video: nearly impossible to hand-code all patterns")
    print()
    print()


def why_neural_networks_are_necessary():
    """
    Explain why neural networks solved these problems.
    """
    print("Why Neural Networks Solved These Problems")
    print("=" * 60)
    print()
    
    print("1. AUTOMATIC FEATURE LEARNING")
    print("-" * 60)
    print()
    print("Classical ML: Features are hand-designed before training.")
    print("  Input → [hand-crafted features] → Model → Output")
    print()
    print("Neural Networks: Features are learned automatically.")
    print("  Input → [Layer 1: learns edges] → [Layer 2: learns shapes]")
    print("      → [Layer 3: learns objects] → Output")
    print()
    print("Result: No manual feature engineering needed!")
    print()
    print()
    
    print("2. HIERARCHICAL LEARNING")
    print("-" * 60)
    print()
    print("Early layers learn simple patterns (edges, texture).")
    print("Middle layers combine these into complex patterns (shapes, parts).")
    print("Late layers recognize high-level concepts (objects, classes).")
    print()
    print("Classical ML can't naturally do this hierarchy.")
    print()
    print()
    
    print("3. SCALING TO DATA")
    print("-" * 60)
    print()
    print("Neural networks benefit from large datasets.")
    print("Classical ML requires feature engineering regardless of data size.")
    print()
    print("More data → Better neural network")
    print("More data → More feature engineering needed for classical ML!")
    print()
    print()
    
    print("4. TRANSFER LEARNING")
    print("-" * 60)
    print()
    print("Train a neural network on ImageNet (1M images).")
    print("Transfer learned features to your task (e.g., medical images).")
    print()
    print("Classical ML: Hard to transfer hand-crafted features.")
    print("Neural networks: Features are portable and reusable.")
    print()
    print()


def feature_learning_illustration():
    """
    Simple illustration of how neural networks learn features.
    """
    print("How Neural Networks Learn Features (Simplified)")
    print("=" * 60)
    print()
    
    print("Example: MNIST Digit Recognition")
    print()
    print("Layer 1 (learns edges):")
    print("  - Detects horizontal lines")
    print("  - Detects vertical lines  ")
    print("  - Detects diagonal edges")
    print("  ~32 feature maps")
    print()
    
    print("Layer 2 (learns shapes):")
    print("  - Detects corners (edges combining)")
    print("  - Detects curves")
    print("  - Detects intersections")
    print("  ~64 feature maps")
    print()
    
    print("Layer 3 (learns objects):")
    print("  - Detects digit parts (loops, stems, curves)")
    print("  - '6' features: has a loop, stem at top")
    print("  - '8' features: has two loops")
    print("  - '1' features: straight line, curves at top/bottom")
    print("  ~128 feature maps")
    print()
    
    print("Output layer (recognizes digits):")
    print("  - Combines part detectors into digit classes")
    print("  - 10 neurons (one per digit 0-9)")
    print()
    
    print("Result: Automatically learned features across 3 levels!")
    print("No feature engineering needed.")
    print()


def _demo():
    """Run all demonstration sections."""
    curse_of_dimensionality_demo()
    print()
    feature_engineering_challenge()
    print()
    scaling_problem_demo()
    print()
    why_neural_networks_are_necessary()
    print()
    feature_learning_illustration()
    print()
    print("=" * 60)
    print("SUMMARY: Classical ML hit a wall on:")
    print("  1. High-dimensional data (images, audio)")
    print("  2. Complex, non-linear patterns")
    print("  3. Large-scale datasets")
    print()
    print("Neural networks solved these by learning features automatically.")
    print("This is why we transition from Classical ML to Deep Learning.")
    print("=" * 60)


if __name__ == "__main__":
    _demo()
