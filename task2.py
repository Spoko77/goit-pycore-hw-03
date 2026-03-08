import random

def get_numbers_ticket(min, max, quantity):
    if (not isinstance(min, int) 
        or not isinstance(max, int) 
        or not isinstance(quantity, int)):
        return []

    if min < 1 or max > 1000 or quantity < 1:
        return []

    if min > max or quantity > (max - min + 1):
        return []

    return sorted(random.sample(range(min, max + 1), quantity))



lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)

lottery_numbers = get_numbers_ticket(1, 36, 5)
print("Ваші лотерейні числа:", lottery_numbers)


print(get_numbers_ticket(1, 49, 50))  # [] — quantity > діапазон
print(get_numbers_ticket(0, 49, 6))   # [] — min < 1
print(get_numbers_ticket(1, 1001, 6)) # [] — max > 1000
