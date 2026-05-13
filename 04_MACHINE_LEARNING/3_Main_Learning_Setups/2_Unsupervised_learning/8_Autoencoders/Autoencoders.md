# Chapter 4.3.2.8: Autoencoders

Autoencoders are neural network models that learn compact representations by reconstructing their inputs.
They are a powerful tool for nonlinear dimensionality reduction and representation learning.

## 1. Core Idea

An autoencoder has an encoder that maps inputs into a lower-dimensional latent space, and a decoder that reconstructs the input from the latent code.
Training minimizes reconstruction error.

## 2. How It Works

- Choose an architecture for encoder and decoder.
- Train end-to-end with a reconstruction loss (e.g., mean squared error).
- The bottleneck latent code is used as the reduced representation.

## 3. Strengths

- Captures nonlinear structure not possible with PCA.
- The learned representation can be used for clustering, classification, or anomaly detection.

## 4. Limits

- Requires careful tuning (architecture, regularization).
- Training can be more resource-intensive than classical methods.

## 5. Learn More

See the classical models chapter:
`LINEAGE/04_MACHINE_LEARNING/2_Classical_ML_Models/4_Clustering_and_Dimensionality_Reduction/2_Dimensionality_Reduction/4_Autoencoders.md`
