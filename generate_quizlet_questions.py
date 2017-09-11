import random

data = open("The Key/phrases.txt", "r")
output = open("The Key/questions.txt", "w")

# data = open("Academic_Writing/phrases_audience.txt", "r")
# output = open("Academic_Writing/questions_audience.txt", "w")

sentences = []
for line in data:
    sentences.append(line[:-1])

quizlet = []
for i in range(len(sentences)):
    sentence = sentences[i].split(' ')
    print (sentence)
    if len(sentence) < 3:
        continue
    index = []
    print (len(sentence))
    d3 = (int)((len(sentence)) / 3)

    for j in range(len(sentence)):
        index.append(j)
    random.shuffle(index)

    id1 = index[:d3]
    id2 = index[d3:(2*d3)]
    id3 = index[(2*d3):(3*d3)]

    s = []
    for j in range(len(sentence)):
        if j in id1:
            s.append("________")
        else:
            s.append(sentence[j])
    s = sentence + ["|"] + s
    quizlet.append(' '.join(s))

    s = []
    for j in range(len(sentence)):
        if j in id2:
            s.append("________")
        else:
            s.append(sentence[j])
    s = sentence + ["|"] + s
    quizlet.append(' '.join(s))

    s = []
    for j in range(len(sentence)):
        if j in id3:
            s.append("________")
        else:
            s.append(sentence[j])
    s = sentence + ["|"] + s
    quizlet.append(' '.join(s))

for s in quizlet:
    print (s)


for i in range(len(quizlet)):
    output.write(quizlet[i] + "\n")
    if(i % 30 == 29):
        output.write("\n\n\n\n\n")
output.close()