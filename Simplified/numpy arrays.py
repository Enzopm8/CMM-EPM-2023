import numpy as np

# Create arrays
array_zeros = np.zeros((2, 3))  # 2x3 array of zeros
array_ones = np.ones((2, 3))    # 2x3 array of ones
array_range = np.arange(0, 6, 1)  # Array with values from 0 to 6 (exclusive) with step 1

# Create random arrays
array_random_uniform = np.random.rand(2, 3)  # 2x3 array of random values from a uniform distribution [0, 1)
array_random_normal = np.random.randn(3, 3)   # 3x3 array of random values from a normal distribution

# Reshape and transpose arrays
reshaped_array = array_range.reshape(2, 3)  # Reshape to 2x3
transposed_array = array_ones.T  # Transpose (turns columns into rows and vice versa)

# Concatenate arrays (join arrays)
array_concatenated = np.concatenate((array_zeros, array_ones), axis=1)  # Concatenate horizontally

# Indexing and slicing
element = array_range[2]  # Get the element at index 2
subarray = array_concatenated[:, 2:4]  # Get columns 1 to 2

# Display arrays
print("Array of Zeros:")
print(array_zeros)

print("\nArray of Ones:")
print(array_ones)

print("\nArray from Range:")
print(array_range)

print("\nRandom Uniform Array:")
print(array_random_uniform)

print("\nRandom Normal Array:")
print(array_random_normal)

print("\nReshaped Array:")
print(reshaped_array)

print("\nTransposed Array:")
print(transposed_array)

print("\nConcatenated Array:")
print(array_concatenated)

print("\nIndexed Element:")
print(element)

print("\nSliced Subarray:")
print(subarray)
