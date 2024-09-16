import easyocr
import concurrent.futures
import os
import cv2  # OpenCV for resizing images
import torch

# Initialize the EasyOCR reader, ensure GPU is used if available
reader = easyocr.Reader(['en'], gpu=torch.cuda.is_available())

def preprocess_image(image_path, target_size=(1024, 1024)):
    """Resize image to target size (smaller size for faster processing)."""
    img = cv2.imread(image_path)
    img = cv2.resize(img, target_size, interpolation=cv2.INTER_AREA)
    return img

def process_image(image_path):
    """Function to perform OCR on a single image with resizing."""
    # Preprocess image (resize for faster processing)
    preprocessed_image = preprocess_image(image_path)
    result = reader.readtext(preprocessed_image)
    return result

# List of image paths (assume these are in a directory)
image_dir = '/path/to/your/image_directory'
image_paths = [os.path.join(image_dir, img) for img in os.listdir(image_dir) if img.endswith('.jpg')]

# Use concurrent futures for parallel processing
with concurrent.futures.ThreadPoolExecutor() as executor:
    results = list(executor.map(process_image, image_paths))

# Results contain OCR outputs for each image
for image_path, result in zip(image_paths, results):
    print(f"Text from {image_path}: {result}")
