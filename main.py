import pandas

df=pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_words={row.letter:row.code for index,row in df.iterrows()}


word=input("Enter the word: ").upper()
phonetic_word=[phonetic_words[i] for i in word]
print(phonetic_word)
