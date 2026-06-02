import pandas
df=pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_words={row.letter:row.code for index,row in df.iterrows()}


def generate_phonetic():
    word=input("Enter the word: ").upper()
    try:
        phonetic_word=[phonetic_words[i] for i in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(phonetic_word)
generate_phonetic()
