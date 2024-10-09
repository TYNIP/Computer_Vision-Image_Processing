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
    height = len(image)
    width = len(image[0])

    output = [[0 for _ in range(height)] for _ in range(width)]

    for i in range(1, height-1):
        for j in range(1, width-1):
            sum_conv = 0

            for k in range(-1, 2):
                for l in range(-1, 2):
                    sum_conv += kernel[k+1][l+1]*image[i+k][j+l]
            output[i][j] = sum_conv
    return output

def combine_sobel_convolutions(horizontal, vertical):
    height = len(horizontal)
    width = len(horizontal[0])

    combined = [[0 for _ in range(height)] for _ in range(width)]

    for i in range(1, height-1):
        for j in range(1, width-1):
            combined[i][j] = int(math.sqrt(horizontal[i][j]**2 + vertical[i][j]**2)) 
    return combined
            
def print_matrix(matrix):
    for row in matrix:
        print(" ".join([str(value) for value in row]))
    print()

def main():
    # Read Image Matrix
    image = read_image();
    print()
    print("Original Image Matrix")
    print_matrix(image)

    # Apply horizontal Sobel operator
    horizontal_matrix = sobel_convolution(image, HORIZONTAL_SOBEL_KERNEL)
    print("After Applying Horizontal Sobel Operator:")
    print()
    print_matrix(horizontal_matrix)
    
    # Apply vertical Sobel operator
    vertical_matrix = sobel_convolution(image, VERTICAL_SOBEL_KERNEL)
    print("After Applying Vertical Sobel Operator:")
    print()
    print_matrix(vertical_matrix)
    
    # Combine results
    processed_image = combine_sobel_convolutions(horizontal_matrix, vertical_matrix)
    print("Final Processed Image (After Combining Results):")
    print()
    print_matrix(processed_image)


if __name__ == '__main__':
    main()

""" 
EDGE CASES

200,200,200,200,200
200,50,50,50,200
200,50,100,50,200
200,50,50,50,200
200,200,200,200,200

"""