""" Sobel Operator """
import math;

#Sobel Convolutional Kernels
HORIZONTAL_SOBEL_KERNEL = [
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1],
];

VERTICAL_SOBEL_KERNEL = [
    [-1, -2, -1],
    [0, 0, 0],
    [1, 2, 1]
];

def read_image():
    image = []
    print("Enter the 5x5 grayscale image matrix row by row (5 values per row separated by commas):")
    for _ in range(5):
        row = input().split(",")
        image.append([int(value) for value in row])
    return image

def sobel_convolution(image, kernel):
    pass

def combine_sobel_convolutions(horizontal, vertical):
    pass

def print_matrix(matrix):
    pass

def main():
    # Read Image Matrix
    image = read_image();
    print("Original Image Matrix")
    print_matrix(image)

    # Apply horizontal Sobel operator
    horizontal_matrix = sobel_convolution(image, HORIZONTAL_SOBEL_KERNEL)
    print("After Applying Horizontal Sobel Operator:")
    print_matrix(horizontal_matrix)
    
    # Apply vertical Sobel operator
    vertical_matrix = sobel_convolution(image, VERTICAL_SOBEL_KERNEL)
    print("After Applying Vertical Sobel Operator:")
    print_matrix(vertical_matrix)
    
    # Combine results
    processed_image = combine_sobel_convolutions(horizontal_matrix, vertical_matrix)
    print("Final Processed Image (After Combining Results):")
    print_matrix(processed_image)


if __name__ == '__main__':
    main()