import os
import re
from collections import Counter

def clean_text(text):
    # Convert text to lowercase
    text = text.lower()

    # Remove special characters, symbols, and punctuation
    cleaned_text = re.sub(r'[^\w\s]', '', text)
    return cleaned_text

def tokenize_text(text):
    # Tokenize the text and remove stop words and words of length less than 4
    stop_words = set(['this', 'that', 'take', 'want', 'which', 'then', 'than', 'will', 'with',
                      'have', 'after', 'such', 'when', 'some', 'them', 'could', 'make', 'though',
                      'from', 'were', 'also', 'into', 'they', 'their', 'there', 'because'])
    tokens = [word for word in text.split() if len(word) >= 4 and word not in stop_words]
    return tokens

def classify_review(filename):
    # Extract the number of stars from the filename
    stars = int(filename.split('_')[1].split('.')[0])

    # Classify the review as positive or negative based on the number of stars
    if stars >= 6 and stars <= 10:
        return "Positive"
    elif stars >= 1 and stars <= 5:
        return "Negative"
    else:
        return "Unknown"

def main():
    # Specify the directory containing the review files
    folder_path = "reviews"

    # List all files in the directory
    files = os.listdir(folder_path)

    # Initialize a Counter to count word frequencies
    word_counter = Counter()

    # Process each review file
    for file in files:
        classification = classify_review(file)
        if classification == "Positive":
            with open(os.path.join(folder_path, file), 'r') as f:
                content = f.read()

                # Clean the text
                cleaned_content = clean_text(content)

                # Tokenize the cleaned text
                tokens = tokenize_text(cleaned_content)

                # Update word counter with token frequencies
                word_counter.update(tokens)

    # Get the top 100 words used in positive reviews
    top_words = word_counter.most_common(100)

    # Print the top 100 words, ten words per line
    print("Top 100 Words Used in Positive Reviews")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    for i in range(0, 100, 10):
        words_line = [word for word, _ in top_words[i:i+10]]
        print(" ".join(words_line))

if __name__ == "__main__":
    main()

