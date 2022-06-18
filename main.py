def most_frequent(ask):
    num_words = {}
    for char in ask:
        if char not in num_words:
            num_words[char] = 1
        else:
            num_words[char] += 1
    return num_words


print(most_frequent('mississippi'))
