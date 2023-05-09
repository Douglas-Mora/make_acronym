def to_acronym(sentence):
    return "".join(word[0] for word in sentence.split()).upper()


print(to_acronym("Sentence to test"))