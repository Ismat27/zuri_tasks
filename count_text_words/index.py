def count_words(text):
    """
        The function counts number of words in a given text
    """

    new_text = text.strip().split(' ')
    return len(new_text)

print('Number of words: ', count_words('all is well in the well')) # expected output: 6
