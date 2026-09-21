def translate(text):
    if " " in text:
        return " ".join(translate(word) for word in text.split())
        
    if text[0] in {'a', 'e', 'i', 'o', 'u'} or text[0:2] in {'xr', 'yt'}:
        return f"{text}ay"

    consonants = 0
    for index in range(len(text)):
        if text[index] not in {'a', 'e', 'i', 'o', 'u', 'y'}:
            consonants += 1
        elif text[index] == 'y' and index == 0:
            consonants += 1
        elif text[index] == 'y' and index != 0:
            return f"{text[index] + text[index + 1:] + text[0:index]}ay"
        else:
            break

    if text[consonants - 1:consonants + 1] == 'qu':
        return f"{text[consonants + 1:] + text[0:consonants + 1]}ay"
    if consonants >= 1:
        return f"{text[consonants:] + text[0:consonants]}ay"
