#Program to count number of words in a file and which word is repeated many times
fname = input("Enter file name: ")
num_words = 0
with open(fname, 'r') as f:
    for line in f:
        words = line.split()
        num_words += len(words)
print("Number of words:")
print(num_words)


handle = open(fname)

count = dict()
for line in handle:
    words = line.split()
    for word in words:
        count[word] = count.get(word,0)+1

bc = None
bw = None
for w,c in count.items():
    if bc is None or (c > bc):
        bc = c
        bw = w

print("Repeated word and count: ")
print(bw,"\n",bc)