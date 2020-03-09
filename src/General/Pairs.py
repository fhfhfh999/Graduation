class Pairs:
    """Storage of two pairs, translated or not translated

        this class will store two pair of sentence, one is the sentence pair originally input
        another is the pair translated. This class is mainly used while the translation is not clear
        return this class as the progress

        Attributes:
            __pair1: the sentence pair input
            __pair2: the sentence pair translated
        """

    __pair2 = None

    def __init__(self, pair1):
        self.__pair1 = pair1
        self.__IS_TRANSLATED = 0

    def input_translate(self, pair2):
        """
        input the translated sentences
        while init the Pairs, the ordinary sentences are the Chinese sentence needed to be translated in pair1
        this method fill the translated sentences of ordinary sentences pair2
        :param pair2: translated sentences, expected to be English
        """
        self.__pair2 = pair2
        if pair2 is not None:
            self.__IS_TRANSLATED = 1

    def get_original_sentence(self):
        return self.__pair1

    def get_translated_sentence(self):
        return self.__pair2

    def __bool__(self):
        """
        to check the sentence pair are not none
        :return: if the pair1 and pair2 in pairs are both not None
        """
        if self.__IS_TRANSLATED == 1:
            return True
        else:
            return False

    def __str__(self):
        """
        return all sentences in Pairs
        :return: all sentences in Pairs, separated with "/n"
        """
        ans = self.__pair1.get_original_sentence + "/n" + self.__pair1.get_mutated_sentence + "/n" + self.pair2.get_original_sentence + "/n" + self.pair2.get_mutated_sentence
        return ans

    def __repr__(self):
        """
        print out the sentences
        """
        state = "translated" if self.__IS_TRANSLATED == 1 else "not translated"
        print("the sentence pair is " + state)
        print("target sentence 1 is :" + self.__pair1.get_original_sentence)
        print("target sentence 2 is :" + self.__pair1.get_mutated_sentence)
        print("translated sentence 1 is :" + self.pair2.get_original_sentence)
        print("translated sentence 2 is :" + self.pair2.get_mutated_sentence)

