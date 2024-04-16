import sys
from collections import Counter

def count_word_occurrences(input:str, output:str):
    with open(input, 'r') as file:
        words = file.read().split()
    word_count = Counter(words)
    sorted_words = sorted(word_count.items(), key = lambda x: x[1], reverse = True)
    with open(output, 'w') as file:
        for word, count in word_count.most_common():
            file.write(f"{word}: {count}\n")

def question_8():
    # Your code here
    input = sys.argv[1]  # grab the input file
    output = sys.argv[2]  # grab the output file
    count_word_occurrences(input, output)

if __name__ == "__main__":
    question_8()
