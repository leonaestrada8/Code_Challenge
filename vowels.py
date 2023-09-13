def count_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = {v:0 for v in vowels}
    count_total = 0
    for char in string:
        if char.lower() in vowels:
            count[char.lower()] += 1 #contagem separada por vogal
            count_total += 1 #contagem total
    return count_total

sentence = input("Enter a sentence to check number of VOWELS: \n")
sentence = str(sentence)
print(count_vowels(sentence)) 
