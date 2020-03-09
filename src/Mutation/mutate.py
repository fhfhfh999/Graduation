import pkuseg

from src.Mutation import Similar


class Mutation:
    def __init__(self):
        self.__seg = pkuseg.pkuseg()

    def cut(self, sentence):
        """
        separate the sentence into words, like "今天天气真好" --- ["今天""天气""真""好"]
        :param sentence:
        :return: a list store the words
        """
        separate_list = self.__seg.cut(sentence)
        return separate_list

    def mutate(self, sentence):
        words = self.cut(sentence)
        most_fixable_pair = [0, None, 0]  # 3 param means: place, word with close meaning, how similar they are
        for i in range(len(words)):
            word = words[i]
            similar_word, similarity = Similar.find_near(word)
            if similarity > most_fixable_pair[2]:
                most_fixable_pair[0] = i
                most_fixable_pair[1] = similar_word
                most_fixable_pair[2] = similarity
        if most_fixable_pair[1] is not None:
            words[most_fixable_pair[0]] = most_fixable_pair[1]
        mutated_sentence = ""
        for word in words:
            mutated_sentence += word
        return mutated_sentence


if __name__ == '__main__':
    mutation = Mutation()
    print(mutation.mutate("你好吗"))


