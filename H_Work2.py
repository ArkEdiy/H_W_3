import random

def get_numbers_ticket(min, max, quantity):
    if not (1 <= min <= max <= 1000) or not(1 <= quantity <= max - min + 1):        
        return[]
    
    return sorted(random.sample(range(min, max + 1), quantity))

min = 1
max = 49
quantity = 6

lottery_numbers = get_numbers_ticket(min, max, quantity)
print("Ваші лотерейні числа:", lottery_numbers)
