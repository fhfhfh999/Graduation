from nltk.corpus import wordnet as wn
from nltk import word_tokenize, pos_tag


def penn_to_wn(tag):
    """
    Convert between a Penn Treebank tag to a simplified Wordnet tag
    :param tag: the pos of the vocabulary
    :return: the acceptable pos of words, include noun, verb, adjective, adverb
    """
    if tag.startswith('N'):
        # noun
        return 'n'

    if tag.startswith('V'):
        # verb
        return 'v'

    if tag.startswith('J'):
        # adjective
        return 'a'

    if tag.startswith('R'):
        # adverb
        return 'r'

    return None


def tagged_to_synset(word, tag):
    wn_tag = penn_to_wn(tag)
    if wn_tag is None:
        return None
    try:
        return wn.synsets(word, wn_tag)[0]
    except:
        return None


def sentence_similarity(sentence1, sentence2):
    s1 = pos_tag(word_tokenize(sentence1))
    s2 = pos_tag(word_tokenize(sentence2))

    synsets1 = [tagged_to_synset(*tagged_word) for tagged_word in s1]
    synsets2 = [tagged_to_synset(*tagged_word) for tagged_word in s2]

    synsets1 = [synset for synset in synsets1 if synset is not None]
    synsets2 = [synset for synset in synsets2 if synset is not None]

    score = 0.0
    count = 0
    for synset1 in synsets1:
        scores = []
        best_score = 0
        for synset2 in synsets2:
            scores.append(synset1.path_similarity(synset2))
        for s in scores:
            if s is not None:
                best_score = max(s, best_score)
        score += best_score
        count += 1
    score /= count
    return score


def similarity(sentence1, sentence2):
    """ compute the symmetric sentence similarity using Wordnet """
    return (sentence_similarity(sentence1, sentence2) + sentence_similarity(sentence2, sentence1)) / 2


if __name__ == "__main__":
    sen1 = "The weather is so good today"
    sen2 = "Today's weather is great"
    print(similarity(sen1, sen2))

    # sentences = [
    #     "Dogs are awesome.",
    #     "Some gorgeous creatures are felines.",
    #     "Dolphins are swimming mammals.",
    #     "Cats are not beautiful animals.",
    # ]
    #
    # focus_sentence = "Cats are beautiful animals."
    #
    # for sentence in sentences:
    #     print("similarity of sentence1:\"", focus_sentence,
    #           "\" and sentence2:\"", sentence, "\" are :", similarity(focus_sentence, sentence))

