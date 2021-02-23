import sys

freq = {}

for word in input("Enter string").split(" "):
    freq[word] = 1 + freq.get(word, 0)

for w in sorted(freq.keys()):
    print(w, freq[w])
print(freq)

def myFun(x, y):
    """my function

    :x: TODO
    :y: TODO
    :returns: TODO

    """
    return x * y

print(myFun(3, 4))

ages = {"Sam" : 4, "Mary" : 3, "Bill" : 2} 
for name in ages.keys():
    print(name, ages[name])

