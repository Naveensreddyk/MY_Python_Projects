import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

new_dictionary = {row.letter: row.code for (index, row) in data.iterrows()} #used dictionary comprehension.

word = input("Enter a word:").upper()

output_list =[new_dictionary[letter] for letter in word] #used list comprehension

print(output_list)

