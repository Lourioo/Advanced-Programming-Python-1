# task 14
s = input('Enter a string: ')
for word in s.split():
    if word.startswith("a") or word.endswith("i"):
        print(word)
