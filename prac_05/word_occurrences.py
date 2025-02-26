"""
Word Occurrences
Estimate: 20 minutes
Actual:   27 minutes
"""

input_text = input("Text: ")
words = input_text.split()
word_to_count = {}
for word in words:
    if word not in word_to_count:
        word_to_count[word] = 1
    else:
        word_to_count[word] += 1

sorted_word_to_count = sorted(word_to_count.items(), key=lambda x: x[0])
max_word_length = max([len(word) for word in word_to_count.keys()])
for word, count in sorted_word_to_count:
    print(f"{word:{max_word_length}} : {count}")