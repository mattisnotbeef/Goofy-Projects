sentence = str(input("type your sentence/paragraph here"))

def multiocularOmaker(sentence):
    for i in sentence:
        if i.lower() == "o":
            sentence = sentence.replace(i, "ꙮ")
    return sentence

print(multiocularOmaker(sentence))