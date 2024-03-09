import random

def get_numbers_ticket(min, max, quantity):
    if min >= 1 and max <= 1000:
        if quantity >= min and quantity <= max:
            random_numbers_list = []
            while quantity >= min:
                random_number = random.randint(min, max)
                if random_number not in random_numbers_list:
                    random_numbers_list.append(random_number)
                    quantity -= 1

            random_numbers_list_sorted = sorted(random_numbers_list)                  
            return random_numbers_list_sorted         
        else:
            print('Oops! Value of quantity is not in range from min to max. Try again...')
    else:
        print('Oops! Value of min or max are not in range from 1 to 1000. Try again...')


