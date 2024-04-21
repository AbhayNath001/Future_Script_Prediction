import cv2
import numpy as np

def separate_pixels(image_paths):
    result_matrices = []
    
    for image_path in image_paths:
        img = cv2.imread(image_path)
        img = cv2.resize(img, (20, 19))
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _, binary_img = cv2.threshold(gray, 128, 1, cv2.THRESH_BINARY)
        binary_img = cv2.resize(binary_img, (20, 19))
        result_matrices.append(binary_img)
    return result_matrices

def save_binary_images_as_csv(result_matrices, output_csv_path):
    flattened_arrays = [matrix.ravel() for matrix in result_matrices]
    column_names = [f'col{i + 1}' for i in range(flattened_arrays[0].shape[0])]
    np.savetxt(output_csv_path, flattened_arrays, delimiter=',', header=','.join(column_names), comments='', fmt='%d')

image_paths = ['k.jpg', 'kh.jpg', 'g.jpg']
result_matrices = separate_pixels(image_paths)
print(result_matrices)