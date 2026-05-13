# Chapter 4.2.4.2.4: Autoencoders

## The New Approach: Learn What Matters

So far, we have seen two strategies for dimensionality reduction:

1. **PCA**: Find mathematical directions of maximum variance (linear, interpretable, fast)
2. **t-SNE / UMAP**: Find directions that preserve local or global neighborhoods (nonlinear, visual, slow)

Both assume something: that the underlying structure is geometric. You can discover it by analyzing distances or variances.

But what if the important structure is **task-specific**?

For example, in facial recognition:
- PCA might find "brightness" and "contrast" as top components
- But what the model really cares about is "how much the face looks like the target person"

Autoencoders solve this by learning: 

> What representation is most useful for my specific problem?

---

## The Core Idea: Compression and Reconstruction

An autoencoder is a neural network that learns to compress data and then decompress it.

Think of it like:
- A photocopier that creates a tiny thumbnail
- Then uses the thumbnail to rebuild the original photo

The process forces the system to learn **what information matters** for reconstruction success.

---

## Architecture: Encoder + Decoder

```
Input (784 pixels for MNIST digit)
    ↓
Encoder: 784 → 256 → 128 → 64 → 32  (compress)
    ↓
Bottleneck: 32-dimensional "code" (learned representation)
    ↓
Decoder: 32 → 64 → 128 → 256 → 784  (decompress)
    ↓
Reconstructed Output (should match input)
```

**Encoder**: Does the compression. Takes a 784-pixel image and squashes it into 32 numbers.

**Bottleneck**: The compressed representation. These 32 numbers capture the "essence" of the digit.

**Decoder**: Does the decompression. Takes the 32 numbers and expands back to 784 pixels.

**Loss function**: Mean squared error (MSE) between input and output.

The goal: minimize this MSE by learning good "summarization" and "reconstruction" rules.

---

## How It Learns: Layer by Layer

When you train an autoencoder:

1. Feed an image through the encoder → get a 32-number code
2. Feed the code through the decoder → get reconstructed image
3. Measure error: how different is reconstruction from original?
4. Backpropagate this error to adjust weights in both encoder and decoder
5. Repeat with next batch

After many batches, the bottleneck learns to capture:
- Distinctive features of each digit
- Important patterns (curves, strokes)
- Ignores noise (random pixels)

---

## Real-World Example: Image Denoising

Imagine you have blurry photos of license plates.

**Approach 1**: Use a hand-designed filter (noise reduction filter from image processing).
- Works okay on average
- Bad on unusual photos

**Approach 2**: Train an autoencoder.
1. Feed it sharp license plate images → they should reconstruct perfectly
2. Feed it deliberately blurry plates → it learns to denoise
3. The bottleneck learns to extract the "core information" of a license plate
4. The decoder learns to fill in plausible details

After training, it denoise real blurry license plates far better than hand-designed filters.

The learned representation captures "what makes a license plate recognizable."

---

## Key Components

### Bottleneck Size
- Too small: Cannot reconstruct, loses important information
- Too large: Trivial compression, learns identity mapping
- Just right: Captures essential structure, discards noise
- Typical: Reduce by 10-50× from input

For MNIST (784 input):
- Try 32, 64, or 128

### Loss Function
Standard approach: **Mean Squared Error (MSE)**

$$J = \frac{1}{n} \sum_{i=1}^{n} ||x_i - \hat{x}_i||^2$$

Where:
- $x_i$ is the original input
- $\hat{x}_i$ is the reconstruction
- We average over all samples

Other options:
- **Binary crossentropy** (if inputs are 0/1, like binary image)
- **Structural similarity (SSIM)** (perceptually-motivated)

### Optimization
- Optimizer: Adam or SGD (from chapter 4.5.2)
- Learning rate: typically 0.001
- Batch size: 32-128
- Epochs: Until validation loss plateaus (20-100)

---

## Variants

### 1. Simple Autoencoder
What we described above. Works well for basic compression.

### 2. Deep Autoencoder
More layers. Can capture more complex nonlinear structure.

### 3. Convolutional Autoencoder (CAE)
Uses convolutional layers (good for images). Encodes spatial structure (neighborhood relationships).

### 4. Variational Autoencoder (VAE)
Adds a probabilistic constraint. Forces the bottleneck to follow a Gaussian distribution.
Enables: sampling new data, interpolation between data points.

### 5. Sparse Autoencoder
Penalizes the bottleneck for having large values. Forces sparse (few non-zero) representations.

---

## Strengths and Weaknesses

### Strengths
- **Learns task-specific compression**: Discovers what matters for your problem
- **Nonlinear**: Can capture curved, complex structures
- **End-to-end**: Neural networks are flexible, can adapt to any data type
- **Scalable**: Works with massive datasets
- **Interpretable bottleneck**: Use the code as features for downstream tasks

### Weaknesses
- **Data hungry**: Needs enough training examples to learn
- **Requires tuning**: Architecture, hyperparameters affect performance
- **Slower training**: More complex than linear methods
- **Black box**: Hard to understand what encoder learned
- **May overfit**: Can memorize training data if not careful

---

## When to Use Autoencoders

- **Feature learning**: You want learned features for downstream tasks (classification, clustering)
- **Denoising**: Input data is noisy
- **Anomaly detection**: Find unusual samples (high reconstruction error = unusual)
- **Data generation**: VAEs can generate new samples
- **Custom compression**: Need compression optimized for your data

---

## Autoencoder vs. Other Methods

| Method | Type | Speed | Interpretability | Best For |
|--------|------|-------|-----------------|----------|
| PCA | Linear | Fast | High | Quick baseline, visualization |
| t-SNE | Graph | Slow | Low | Visualization only |
| UMAP | Graph | Medium | Low | Visualization + features |
| Autoencoder | Neural | Medium | Low | Feature learning, task-specific |

---

## What Comes Next

Autoencoders are **unsupervised**: they learn without labels.

But what if you have labels and want to learn features that separate classes?

That is where **supervised** approaches come in: **neural networks trained for classification** (Chapter 5).

The encoder concept shows up again in more advanced neural architectures like:
- Residual networks (ResNets)
- Attention mechanisms
- Transformer models

All follow the same principle: learn efficient intermediate representations.
- The learned representation may not always be interpretable.

## 5. What Comes Next

Autoencoders bridge classical dimensionality reduction and deep learning.
They illustrate how learned representations can make downstream tasks (like clustering) easier.
