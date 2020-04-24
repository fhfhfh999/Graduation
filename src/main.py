from General.Pair import Pair
from General.Pairs import Pairs
from Mutation.mutate import Mutation
from Translation import *
from dataInsert.Data import Data
from Compare.Semantic_similarity_WordNet import similarity


if __name__ == '__main__':
    threshold = 0.8
    translator = Translator.getTranslator()
    data = Data()
    mutation = Mutation()
    all_pair = data.get_sentence()
    output_pairs = []
    number = 0
    count = 0
    for pair in all_pair:
        if len(pair) == 1:
            sentence = pair.get_original_sentence()
            mutated_sentence = mutation.mutate(sentence)
            pair.set_mutation(mutated_sentence)
        if bool(pair):
            number += 1
            original_translation = translator.translate(pair.get_original_sentence())
            mutated_translation = translator.translate(pair.get_mutated_sentence())
            if similarity(original_translation, mutated_translation) > threshold:
                count += 1
            else:
                translated_pair = Pair(original_translation, mutated_translation)
                pairs = Pairs(pair, translated_pair)
                output_pairs.append(pairs)

    print(count/number)
    if len(output_pairs) != 0:
        print("not accurate translation:")
        for pairs in output_pairs:
            cn_pair = pairs.get_original_sentences()
            en_pair = pairs.get_translated_sentences()
            original_sentence = cn_pair.get_original_sentence()
            mutated_sentence = cn_pair.get_mutated_sentence()
            original_translation = en_pair.get_original_sentence()
            mutated_translation = en_pair.get_mutated_sentence()
            print("original sentence:" + original_sentence)
            print("mutated_sentence:" + mutated_sentence)
            print("original_translation:" + original_translation)
            print("mutated_translation:" + mutated_translation)

    # end of code
    data.close()

# def compare(sentence1, sentence2):
#     """
#
#     :param sentence1: the first sentence need to be compared
#     :param sentence2: the second sentence need to be compared
#     :return: whether the sentence are similar
#     """
#     return False
#
#
# def exchange(sentence):
#     """
#     this method get a sentence have similar meaning with ordinary sentence(Chinese)
#     :param sentence: ordinary sentence
#     :return: similar sentence of ordinary sentence
#     """
#     return sentence
