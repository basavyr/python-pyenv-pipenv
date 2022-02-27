from tabnanny import check
from timeit import default_timer
import time
import random


_MIN_NUMBER = 5
_MAX_NUMBER = 35
_SUMM = 100


def get_random_number():
    """ Generates a random number between [5 and 35]"""
    rd_n = random.randrange(_MIN_NUMBER, _MAX_NUMBER)
    return rd_n


def generate_array_fixed_sum(array_sum):
    """
    - generate a random array with numbers that add up to a fixed limit: array_sum
    """
    random_array = []

    total_sum = 0
    checker = True

    # ****************************
    start = default_timer()
    # ****************************
    while(checker):
        rng = get_random_number()
        if(total_sum + _MIN_NUMBER > array_sum):
            """stop the loop if the summation reaches a point where the smallest possible rng will overflow it"""
            remainder = array_sum - total_sum
            random_array.append(remainder)
            print(f'❌ will stop the rng with remainder {remainder}')
            checker = False
        elif(total_sum + rng < array_sum):
            """add rng to the array if the summation is smaller than the cap value of 100"""
            print(f'✅ found good number {rng} with current sum to {total_sum}')
            total_sum = total_sum + rng
            random_array.append(rng)
        elif(total_sum + rng == array_sum):
            print(f'🔥 will stop the rng with sum {total_sum}')
            total_sum = total_sum + rng
            random_array.append(rng)
            checker = False
    # ****************************
    end = default_timer()
    # ****************************

    proc_time = float(end - start)
    return random_array, sum(random_array), total_sum


def generate_array_fixed_number(arr_size, arr_sum):
    """
    - generate a random array with a fixed number of elements
    - the random array needs to sum up to a fixed sum
    """
    total_sum = 0
    checker = True
    id_counter = 0
    rng_array = []

    while checker:
        rng = get_random_number()
        id_counter = id_counter + 1
        if(total_sum + rng <= arr_sum):
            if(len(rng_array) + 1 <= arr_size):
                print(f'will add {rng} to the array {rng_array}')
                rng_array.append(rng)
                total_sum = total_sum + rng
            else:
                checker = False
        else:
            checker = False

    return rng_array, total_sum


def main():
    w = generate_array_fixed_number(4, 100)
    print(w)


if __name__ == '__main__':
    main()
