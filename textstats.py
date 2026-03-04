john1 = """In the beginning was the Word, and the Word was with God, and the Word was God. 
He was in the beginning with God. All things were made through him, and without him was not any thing made that was made. 
In him was life, and the life was the light of men. 
The light shines in the darkness, and the darkness has not overcome it.

There was a man sent from God, whose name was John. 
He came as a witness, to bear witness about the light, that all might believe through him. 
He was not the light, but came to bear witness about the light.

The true light, which gives light to everyone, was coming into the world. 
He was in the world, and the world was made through him, yet the world did not know him. 
He came to his own, and his own people did not receive him. 
But to all who did receive him, who believed in his name, he gave the right to become children of God, who were born, not of blood nor of the will of the flesh nor of the will of man, but of God.

And the Word became flesh and dwelt among us, and we have seen his glory, glory as of the only Son from the Father, full of grace and truth."""


def count_chars(text):
    """
    Returns the total number of characters in a string.

    >>> count_chars("Hello world")
    11
    >>> count_chars("")
    0
    >>> count_chars(john1)
    1103
    """
    pass


def count_words(text):
    """
    Returns the total number of words in a string.
    Words are separated by spaces or newlines.

    >>> count_words("Hello world")
    2
    >>> count_words("   extra   spaces   ")
    2
    >>> count_words("")
    0
    >>> count_words(john1)
    224
    """
    pass


def count_sentences(text):
    """
    Returns the number of sentences in a string.
    Sentences end with '.', '!', or '?'.

    >>> count_sentences("Hello world. How are you? I am fine!")
    3
    >>> count_sentences("")
    0
    >>> count_sentences("No punctuation")
    0
    >>> count_sentences(john1)
    13
    """
    pass


def count_paras(text):
    """
    Returns the number of paragraphs in a string.
    Paragraphs are separated by exactly two newlines.

    >>> count_paras("Para 1\\n\\nPara 2")
    2
    >>> count_paras("One single paragraph")
    1
    >>> count_paras("")
    0
    >>> count_paras(john1)
    4
    """
    pass


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    print("All tests passed.")

    print(count_chars(john1), "chars")
    print(count_words(john1), "words")
    print(count_sentences(john1), "sentences")
    print(count_paras(john1), "paragraphs")
