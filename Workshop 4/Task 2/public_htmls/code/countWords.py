def n0_punch(f):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    no_punct = ""
    for char in f:
        if char not in punctuations:
            no_punct = no_punct + char
    return no_punct

f = (input("Enter a String: ")).upper()
w = n0_punch(f)

x = list(w.split())

wordcount={}
for word in x:
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1
for k,v in wordcount.items():
    print(k , v)

print("DONE")