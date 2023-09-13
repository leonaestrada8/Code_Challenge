


def count_bits(n):
    return bin(n).count("1")

number = int(input("Enter a number for bits counting: \n"))
count_bits = count_bits(number)


bits = bin(number)[2:]
print(f"{number} in bits :{bits}")
print(f"Bit count :{count_bits}")

