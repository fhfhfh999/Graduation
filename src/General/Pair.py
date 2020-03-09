class Pair:
    """Storage of a pair of sentence

    this class can store at most two sentence, they can be "" or a real string
    but "" is not really meaningful, it is just default

    Attributes:
        __original_sentence: the first sentence stored
        __mutated_sentence: the second sentence stored
    """

    def __init__(self, original_sentence, mutated_sentence=""):
        self.__original_sentence = original_sentence
        self.__mutated_sentence = mutated_sentence

    def add_all(self, original_sentence, mutated_sentence):
        """in case the init part didn't set successfully

        if the init part did not set sentences successfully, it will use default value
        if the error need to be correct, use this method
        also can be used in test

        :param original_sentence: the first sentence stored
        :param mutated_sentence: the second sentence stored
        """
        self.__original_sentence = original_sentence
        self.__mutated_sentence = mutated_sentence

    def set_mutation(self, mutated_sentence):
        """
        set the mutation sentence
        :param mutated_sentence: the sentence mutated from original sentence
        """
        self.__mutated_sentence = mutated_sentence

    def get_original_sentence(self):
        """get sentence1

        :return: the first of two sentence stored in the pair
        """
        return self.__original_sentence

    def get_mutated_sentence(self):
        """get sentence2

        :return: the second of two sentence stored in the pair
        """
        return self.__mutated_sentence

    def __len__(self):
        """

        :return: the number of meaningful sentences in the pair, not default
        """
        length = 0
        if self.__original_sentence != "":
            length += 1
        if self.__mutated_sentence != "":
            length += 1
        return length

    def __bool__(self):
        """ check whether the pair is meaningful

        if the two sentence stored inside is not default and two sentences are not same, it is meaningful

        :return:
        true for two sentence both be meaningful,
        false for at least one sentence is default
        """
        if self.__original_sentence != "" & self.__mutated_sentence != "" & self.__original_sentence != self.__mutated_sentence:
            return True
        else:
            return False



