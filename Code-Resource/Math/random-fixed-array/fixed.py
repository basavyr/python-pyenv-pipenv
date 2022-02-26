from tabnanny import check
from timeit import default_timer
import time
import random


_MIN_NUMBER = 5
_MAX_NUMBER = 35
SUMM = 555


def get_random_number():
    """ Generates a random number between [5 and 35]"""
    rd_n = random.randrange(_MIN_NUMBER, _MAX_NUMBER)
    return rd_n


def generate_fixed_array(arr_size):
    random_array = []

    total_sum = 0
    checker = True

    # ****************************
    start = default_timer()
    # ****************************
    while(checker):
        rng = get_random_number()
        if(total_sum + _MIN_NUMBER > SUMM):
            """stop the loop if the summation reaches a point where the smallest possible rng will overflow it"""
            remainder = SUMM - total_sum
            random_array.append(remainder)
            print(f'❌ will stop the rng with remainder {remainder}')
            checker = False
        elif(total_sum + rng < SUMM):
            """add rng to the array if the summation is smaller than the cap value of 100"""
            print(f'✅ found good number {rng} with current sum to {total_sum}')
            total_sum = total_sum + rng
            random_array.append(rng)
        elif(total_sum + rng == SUMM):
            print(f'🔥 will stop the rng with sum {total_sum}')
            total_sum = total_sum + rng
            random_array.append(rng)
            checker = False
    # ****************************
    end = default_timer()
    # ****************************

    proc_time = float(end - start)
    return random_array, sum(random_array), total_sum


def main():
    w = generate_fixed_array(5)
    print(w)


if __name__ == '__main__':
    main()
