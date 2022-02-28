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


def generate_array_fixed_number(debug_mode, total_size, total_sum):
    """
    - generate a random array with a fixed number of elements
    - the random array needs to sum up to a fixed sum
    """
    checker = True

    """ array to store all the generated random numbers """
    array = []

    """ sum of the elements within the array """
    array_sum = 0

    """ size of the array """
    array_size = 0

    """ keep count of all the iterations within the while loop """
    counter = 0

    while checker:
        rng = get_random_number()
        """ 
        - first condition for adding numbers in the array
        - the sum of all elements within the array should not exceed total sum
        """
        if(array_sum + rng <= total_sum):
            if(debug_mode):
                print(f'Will add {rng} to the array -> {array}')
            array.append(rng)
            arr_size = len(array)
            array_sum = array_sum + rng
            """ the second condition for adding numbers in the array"""
            if(arr_size == total_size):
                """ stop the loop since the array reached maximum capacity """
                if(debug_mode):
                    print(f'Array is full -> {arr_size}')
                    print(f'Array {array} has the sum-> {array_sum}')
                if(array_sum <= total_sum):
                    if(debug_mode):
                        print(
                            f'removing the last element from the array -> {rng}')
                    array.pop()
                    final_term = total_sum - sum(array)
                    if(debug_mode):
                        print(
                            f'creating a final term to fill the array -> {final_term}')
                    array.append(final_term)
                    array_sum = sum(array)
                checker = False
        else:
            safety_rng = total_sum - array_sum
            print(
                f'cannot add {rng} to the array since it exceeds the limit...')
            print(f'will add {safety_rng} instread')
            array.append(safety_rng)
            array_sum = array_sum + safety_rng
            checker = False
    return array, array_sum


def main():
    w = generate_array_fixed_number(debug_mode=1, total_size=4, total_sum=100)
    print(w)


if __name__ == '__main__':
    main()
