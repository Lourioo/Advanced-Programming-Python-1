# task 12
s = input('Enter a string: ')
for word in s.split():
    if word.endswith("l"):
        print(word)
