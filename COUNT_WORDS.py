
import string

def Words_from_file():
    with open('text_file.txt', 'r', encoding='utf-8') as file:
        text = file.read()
    raw_words = text.split()
    words = []
    for word in raw_words:
        words.append(word.strip(string.punctuation).lower())

    return words


def count_words(words):
    word_freq = {}
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    return word_freq


def sort_by_frequency(word_freq):
    return sorted(word_freq.items(), key=lambda item: item[1], reverse=True)

def main():
    words = Words_from_file()
    word_freq = count_words(words)
    sorted_word_freq = sort_by_frequency(word_freq)
    print(sorted_word_freq)

if __name__ == "__main__":
    main()