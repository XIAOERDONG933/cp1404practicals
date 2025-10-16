"""
Word Occurrences
Estimate: 15 minutes
Actual:   32 minutes
"""
import string

def main():
    """Receive user input text, count the number of times, and format the output."""
    text = input("Text: ")
    word_counts = count_word_occurrences(text)

    sorted_words = sorted(word_counts.keys())
    max_length = max(len(word) for word in sorted_words)

    for word in sorted_words:
        print(f"{word:{max_length}} : {word_counts[word]}")

def count_word_occurrences(text):
    """Count the occurrences of words in a string."""
    text = text.lower().translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    word_counts = {}

    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    return word_counts

main()