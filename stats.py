
chara_count = {}

def word_count(text):
    words = text.split()
    total_words = len(words)
    return total_words

def character_count(text):
    lowercase = text.lower()
    characters = list(lowercase)
    for chara in characters:
        if chara not in chara_count:
            chara_count[chara] = 1
        else:
            chara_count[chara] += 1
    return chara_count

def prepare_dic(dic):
    sorted_charas = []
    for chara, figure in dic.items():
        sorted_charas.append({"char": chara, "num": figure})
    return sorted_charas

        

def sort_characters(dic):
    return dic["num"]

