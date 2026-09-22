def is_isogram(phrase):
    clean_phrase = phrase.replace("-", "").replace(" ", "").lower()
    phrase_list = list(clean_phrase)
    return len(set(phrase_list)) == len(phrase_list)
