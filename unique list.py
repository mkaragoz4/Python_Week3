numbers = [1, 5, 5, 30, 30, 45]
def get_unique_numbers(numbers):
    tekrarsız_sayılar = []
    unique_numbers = set(numbers)
    for number in unique_numbers:
        tekrarsız_sayılar.append(number)
    return tekrarsız_sayılar
print("Tekrarsız sayılar:", get_unique_numbers(numbers))