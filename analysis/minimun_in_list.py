import time
import random


# O(n^2)
def find_min1(number_list):
    min_num = number_list[0]
    cur_num = 0
    for i in number_list:
        for j in number_list:
            if i < j:
                cur_num = i
            else:
                cur_num = j
            if cur_num < min_num:
                min_num = cur_num
    return min_num


# O(n)
def find_min2(number_list):
    min_num = number_list[0]
    for i in number_list:
        if i < min_num:
            min_num = i
    return min_num


def cal_time(func, num_lists):
    for num_list in num_lists:
        start = time.time()
        min_num = func(num_list)
        end = time.time()
        print min_num, " function time: ", end - start


def main():
    random_number_list = [random.sample(range(1000000), n) for n in [10, 100, 1000]]
    print "O(n^2) function"
    cal_time(find_min1, random_number_list)
    print "O(n) function"
    cal_time(find_min2, random_number_list)


main()

