word = input("Enter some words ")
word_str = word.split()
for el in range(int(len(word_str))):
    if len(word_str[el]) >= 10:
        print(f"{el + 1}" + " " + f"{word_str[el][0:10]}")
    else:
        print(f"{el + 1}" + " " + f"{word_str[el]}")

