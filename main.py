# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def read_file():
    # opening the file in read mode
    my_file = open("wordle.txt", "r")

    # reading the file
    data = my_file.read()
    my_file.close()

    return data.split("\n")



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    words = read_file()

first_try = input("What is the first attempt green letters, enter emptys with asterisks?")


#eliminates words that don't match the green letter pattern
for i in range(len(words)):
    word = words[i]
    for j in range(0, len(word)):
            if first_try[j] == '*':
                continue
            if word[j] != first_try[j]:
                words[i] = '0'
                break

#eliminates words that have elminated letters


eliminated_letters = input("input a comma seperated list of letters that are eliminated: ").split(',')
for i in range(len(words)):
    word = words[i]
    for j in range(0, len(eliminated_letters)):
        if eliminated_letters[j] in word:
            words[i] = '0'


for word in words:
    if word != '0':
        print(word)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
