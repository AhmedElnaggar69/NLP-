docs =[
    "i like eggs",
    "i hate cats",
    "i like eggs and i like cats"
]
unique = set()
for doc in docs:
    for word in doc.split():
        unique.add(word)

headers = ["Document"] + sorted(unique)

mat = [headers]
for doc in docs:
    mat.append([doc] + [0] * len(unique))


sums = []
for docIndex,doc in enumerate(docs, start=1):
    sumInDoc = 0
    for word in doc.split():
        col = headers.index(word)
        if word in unique:
            mat[docIndex][col] +=1
            sumInDoc+=1
    sums.append(sumInDoc)


for docIndex,doc in enumerate(docs, start=1):
    for word in set(doc.split()):
        col = headers.index(word)
        mat[docIndex][col] /= sums[docIndex-1]


for row in mat:
    temp = []
    for col in row:
        temp.append(col)
    print(temp)

