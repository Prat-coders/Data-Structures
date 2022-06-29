from collections import Counter


def most_frequent(ask):
    num_words = {}
    for char in ask:
        if char not in num_words:
            num_words[char] = 1
        else:
            num_words[char] += 1
    final_output = Counter(num_words).most_common()
    return final_output


print(most_frequent('Mississippi'))
