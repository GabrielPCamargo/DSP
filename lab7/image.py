import numpy as np
import matplotlib.pyplot as plt
from skimage import data
from skimage.color import rgb2gray
import os

def uniform_quantization(X, n_bits):
    """
    Perform uniform quantization on input array X to 2^n_bits discrete levels.
    
    Parameters:
    X (numpy.ndarray): Input array (vector or matrix) to quantize.
    n_bits (int): Number of bits for quantization (2^n_bits levels).
    
    Returns:
    numpy.ndarray: Quantized array with the same shape as X.
    """
    levels = 2 ** n_bits - 1
    X_min = np.min(X)
    X_max = np.max(X)
    delta = (X_max - X_min) / levels
    normalized = (X - X_min) / delta
    quantized = np.round(normalized)
    X_quantized = quantized * delta + X_min
    return X_quantized

# Create output directory if it doesn't exist
output_dir = "quantized_images"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Load image
imagem = plt.imread('./im.jpg', 'jpg')
grayscale = rgb2gray(imagem)
Im_gray = np.round(grayscale * 255)

# Bits to quantize
bits_list = [7, 6, 5, 4, 3, 2, 1]

# Set up plot
plt.figure(figsize=(15, 10))

# Save and display original image
plt.subplot(4, 2, 1)
plt.imshow(Im_gray, cmap='gray', vmin=0, vmax=255)
plt.title('Original (8 bits)')
plt.axis('off')
plt.imsave(os.path.join(output_dir, 'original_8bits1.png'), Im_gray, cmap='gray', vmin=0, vmax=255)

# Quantize, save, and display for each bit level
for i, n_bits in enumerate(bits_list, 1):
    Im_quantized = uniform_quantization(Im_gray, n_bits)
    unique_levels = len(np.unique(Im_quantized))
    
    plt.subplot(4, 2, i + 1)
    plt.imshow(Im_quantized, cmap='gray', vmin=0, vmax=255)
    if n_bits == 1:
        plt.title(f'{n_bits} bit')
    else:  
        plt.title(f'{n_bits} bits')
    plt.axis('off')
    # Save quantized image
    plt.imsave(os.path.join(output_dir, f'quantized_{n_bits}bits1.png'), Im_quantized, cmap='gray', vmin=0, vmax=255)
    print(f'Saved: quantized_{n_bits}bits.png with {unique_levels} unique levels')

plt.tight_layout()
plt.show()