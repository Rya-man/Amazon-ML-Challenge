import easyocr
import os

# Initialize the EasyOCR reader
reader = easyocr.Reader(['en'])  # This will load the model into memory

# Specify the output file path
outputfile = 'output/output.txt'

# Specify the directory containing images
image_folder = 'images'

# Open the output file in write mode
with open(outputfile, 'w') as file:
    # Get the total number of images (assuming the highest file number is 131287)
    num_images = 131288 # Set this to the actual total number of images you have
    
    # Iterate over all the images in numerical order
    for i in range(10047,num_images):
        img_file = f"{i}.jpg"  # Generate the image filename
        img_path = os.path.join(image_folder, img_file)
        
        # Check if the file exists (in case some files are missing)
        if os.path.exists(img_path):
            # Run OCR on the image
            result = reader.readtext(img_path)
            
            # Collect all detected text into a single line
            concatenated_text = ''.join([text for bbox, text, confidence in result])
            
            # Write the concatenated text to the output file
            file.write(f"{concatenated_text}\n")

