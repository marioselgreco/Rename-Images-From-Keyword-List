import os
import random
import openai

# OpenAI API key setup
openai.api_key = 'yourkey'

def get_keyword_suggestions(prompt):
    """
    Get keyword suggestions from OpenAI based on the prompt.
    """
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Provide a list of keywords related to: {prompt}",
            max_tokens=60,
            n=1,
            stop=None,
            temperature=0.5
        )
        keywords = response.choices[0].text.strip().split(',')
        return [keyword.strip() for keyword in keywords]
    except Exception as e:
        print(f"Error getting keyword suggestions: {e}")
        return []

def rename_images(folder_path, keywords_file):
    if not os.path.exists(folder_path) or not os.path.exists(keywords_file):
        print("Folder or keywords file not found.")
        return

    with open(keywords_file, 'r', encoding='utf-8') as file:
        keywords = [keyword.strip() for keyword in file.readlines()]

    image_files = [file for file in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, file))]

    for file in image_files:
        keyword = random.choice(keywords)
        # Here you could replace or augment the chosen keyword with suggestions from the OpenAI API
        # For example, if you have a way to describe the image, you could use:
        # description = "A brief description of the image"
        # suggested_keywords = get_keyword_suggestions(description)
        # keyword = random.choice(suggested_keywords + [keyword])

        shuffled_filename = ' '.join(random.sample(keyword.split(), len(keyword.split())))
        file_name, extension = os.path.splitext(file)
        new_filename = os.path.join(folder_path, f"{shuffled_filename}{extension}")
        counter = 1
        while os.path.exists(new_filename):
            new_filename = os.path.join(folder_path, f"{shuffled_filename}_{counter}{extension}")
            counter += 1

        try:
            os.rename(os.path.join(folder_path, file), new_filename)
            print(f"Renaming {file} to {new_filename}")
        except OSError as e:
            print(f"Error renaming {file}: {e}")

if __name__ == "__main__":
    folder_path = "C:\\Users\\SEO\\Desktop\\rozfouska.wordpress.com\\img"
    keywords_file = "C:\\Users\\SEO\\Desktop\\rozfouska.wordpress.com\\keys.txt"
    rename_images(folder_path, keywords_file)
