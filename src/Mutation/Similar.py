import synonyms


def find_near(word):
    """
    this method supposed to change the word into similar meaning word,
    mostly change it to the most similar meaning one
    :param word: the word needed to be change to similar meaning word
    :return: similar meaning word and the similarity
    word_list[1]: the most similar word of param word
    nearby[1][1]: the similarity
    """
    nearby = synonyms.nearby(word)
    word_list = nearby[0]
    if len(word_list) == 0:
        return None, 0
    else:
        return word_list[1], nearby[1][1]


def compare_chs_sentence(sen1, sen2, threshold=0):
    """
    to check the two Chinese sentences input whether be similar, if not, may change the way of mutation
    :param sen1: the original sentence
    :param sen2: the mutated sentence
    :param threshold: how much the two sentence are likely is okay
    :return: True for the two sentence are similar, false for not
    """
    score = synonyms.compare(sen1, sen2)
    return False if score <= threshold else True

# @online{Synonyms:hain2017,
#   author = {Hai Liang Wang, Hu Ying Xi},
#   title = {中文近义词工具包Synonyms},
#   year = 2017,
#   url = {https://github.com/huyingxi/Synonyms},
#   urldate = {2017-09-27}
# }


if __name__ == "__main__":
    print(synonyms.display("今天"))
    print(synonyms.display("天气"))
    print(synonyms.display("真好"))
    print(synonyms.display("做"))
    print(synonyms.display("作业"))
    print(synonyms.display("喜欢"))
    print(synonyms.display("故事"))
    print(synonyms.display("猫"))
    print(synonyms.display("可爱"))
    print(synonyms.display("一种"))
    print(synonyms.display("动物"))
    print(synonyms.display("今天天气"))
