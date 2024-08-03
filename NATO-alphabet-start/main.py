import pandas
data=pandas.read_csv("nato_phonetic_alphabet.csv")
nato_data={row.letter:row.code for(index,row) in data.iterrows()}

def generate():
    word=input("Enter a key:").upper()
    try:
        output=[nato_data[letter] for letter in word]
    except KeyError:
        print("Sorry use only letters as input")
        generate()
    else:
        print(output)

generate()