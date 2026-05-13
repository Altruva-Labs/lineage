"""Chapter 4.3.12: Autoencoders as an Unsupervised Learning Setup.

Neural network-based dimensionality reduction and feature learning.
"""

import random
import math


class SimpleAutoencoder:
    """Simplified autoencoder for dimensionality reduction."""

    def __init__(self, input_dim, encoding_dim, learning_rate=0.01, epochs=100):
        self.input_dim = input_dim
        self.encoding_dim = encoding_dim
        self.learning_rate = learning_rate
        self.epochs = epochs
        
        # Encoder weights
        self.W_encoder = [[random.gauss(0, 0.01) for _ in range(input_dim)]
                         for _ in range(encoding_dim)]
        self.b_encoder = [0.0] * encoding_dim
        
        # Decoder weights
        self.W_decoder = [[random.gauss(0, 0.01) for _ in range(encoding_dim)]
                         for _ in range(input_dim)]
        self.b_decoder = [0.0] * input_dim

    def fit(self, X):
        """Train autoencoder."""
        for epoch in range(self.epochs):
            total_loss = 0.0
            
            for x in X:
                # Forward pass
                encoded = self._encode(x)
                decoded = self._decode(encoded)
                
                # Compute loss
                loss = sum((x[i] - decoded[i]) ** 2 for i in range(len(x)))
                total_loss += loss
                
                # Backward pass (simplified)
                self._update_weights(x, encoded, decoded)
            
            if epoch % 20 == 0:
                avg_loss = total_loss / len(X)
        
        return self

    def encode(self, X):
        """Encode data to latent space."""
        return [self._encode(x) for x in X]

    def decode(self, Z):
        """Decode from latent space."""
        return [self._decode(z) for z in Z]

    def reconstruct(self, X):
        """Encode and decode (reconstruct)."""
        encoded = self.encode(X)
        return self.decode(encoded)

    def _encode(self, x):
        """Forward pass through encoder."""
        z = []
        for i in range(self.encoding_dim):
            val = self.b_encoder[i] + sum(self.W_encoder[i][j] * x[j] for j in range(len(x)))
            z.append(self._relu(val))
        return z

    def _decode(self, z):
        """Forward pass through decoder."""
        x_reconstructed = []
        for i in range(self.input_dim):
            val = self.b_decoder[i] + sum(self.W_decoder[i][j] * z[j] for j in range(len(z)))
            x_reconstructed.append(self._sigmoid(val))
        return x_reconstructed

    def _update_weights(self, x, encoded, decoded):
        """Simplified weight update."""
        # Backward pass (simplified - single step)
        for i in range(len(decoded)):
            error = x[i] - decoded[i]
            self.b_decoder[i] += self.learning_rate * error
            for j in range(self.encoding_dim):
                self.W_decoder[i][j] += self.learning_rate * error * encoded[j]

    @staticmethod
    def _relu(x):
        return max(0, x)

    @staticmethod
    def _sigmoid(x):
        return 1 / (1 + math.exp(-x))


if __name__ == "__main__":
    random.seed(42)
    
    # 10D data
    X = [[random.gauss(0, 1) for _ in range(10)] for _ in range(20)]
    
    # Train autoencoder: 10 -> 3 -> 10
    ae = SimpleAutoencoder(input_dim=10, encoding_dim=3, epochs=50)
    ae.fit(X)
    
    # Encode
    encoded = ae.encode(X)
    print(f"Encoded shape: (20, 3)")
    print(f"First sample encoded: {[round(z, 2) for z in encoded[0]]}")
    
    # Reconstruct
    reconstructed = ae.reconstruct(X)
    print(f"Reconstructed shape: (20, 10)")
