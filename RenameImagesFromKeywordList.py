import os
import random

# Path to the folder containing the images
folder_path = "C:\\Users\\SEO\\Desktop\\tumblr.psareftikoskosmos\\img"

# Path to the text file containing the list of keywords
keywords_file = "C:\\Users\\SEO\Desktop\\tumblr.psareftikoskosmos\\keys_eng.txt"

# Check if the folder and keywords file exist
if not os.path.exists(folder_path) or not os.path.exists(keywords_file):
    print("Folder or keywords file not found.")
    exit()

# Read the keywords from the text file
with open(keywords_file, 'r', encoding='utf-8') as file:
    keywords = file.readlines()
keywords = [keyword.strip() for keyword in keywords]

# Get the list of image files in the folder
image_files = [file for file in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, file))]

# Assign each image a keyword
for file in image_files:
    # Get a random keyword
    keyword = random.choice(keywords)

    # Generate a new filename by rearranging the words from the keyword
    shuffled_filename = ' '.join(random.sample(keyword.split(), len(keyword.split())))

    # Extract the file extension from the original filename
    file_name, extension = os.path.splitext(file)

    # Create the new filename with the original extension
    new_filename = os.path.join(folder_path, f"{shuffled_filename}{extension}")

    # If the new filename already exists, append a number to make it unique
    counter = 1
    while os.path.exists(new_filename):
        new_filename = os.path.join(folder_path, f"{shuffled_filename}_{counter}{extension}")
        counter += 1

    # Rename the file
    try:
        os.rename(os.path.join(folder_path, file), new_filename)
        print(f"Renaming {file} to {new_filename}")
    except OSError as e:
        print(f"Error renaming {file}: {e}")

print("Images have been renamed.")
