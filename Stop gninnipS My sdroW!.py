def spin_words(sentence):
    l =[]
    for i in sentence.split(" "):
        if len(i)>=5:
            l.append(i[::-1])
        else:
            l.append(i)
    return ' '.join(l)
