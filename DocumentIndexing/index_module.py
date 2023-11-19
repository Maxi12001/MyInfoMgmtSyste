#TODO: download spacy
#TODO: define an entrypoint for the service
#TODO: I need to design how this system will work 
import spacy
from collections import defaultdict
from pathlib import Path

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

def read_file(file_path):
    """
    Read a text file from the given path.

    Args:
        file_path (str): The path to the text file.

    Returns:
        str: The content of the file as a string.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
    return content

def extract_topics(text):
    """
    Extract topics from a text using spaCy.

    Args:
        text (str): The text to extract topics from.

    Returns:
        list: A list of topics extracted from the text.
    """
    # Process the text with spaCy
    doc = nlp(text)
    
    # Extract noun phrases as topics
    topics = [chunk.text for chunk in doc.noun_chunks]

    return topics

def create_index(file_path):
    """
    Create an index for a document.

    Args:
        file_path (str): The path to the text file.

    Returns:
        dict: A dictionary where topics are keys and their frequency in the document is the value.
    """
    content = read_file(file_path)
    topics = extract_topics(content)
    
    # Create a defaultdict to store the index
    index = defaultdict(int)
    
    # Count the frequency of each topic in the document
    for topic in topics:
        index[topic] += 1

    return dict(index)

if __name__ == "__main__":
    file_path = "path/to/your/document.txt"
    index = create_index(file_path)
    
    # Print the index
    for topic, frequency in index.items():
        print(f"Topic: {topic}, Frequency: {frequency}")