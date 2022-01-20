Moving Zeros To The End

def move_zeros(array):
    if 0 not in array:
        return array
    boolean = True
    while boolean:
        for i in range(len(array)):
            if array[i] == 0:
                for j in range(i, len(array)):
                    if array[j] != 0:
                        array[i], array[j] = array[j], array[i]
                        break
        for k in range(2, len(array) + 2):
            if all([x == 0 for x in array[-1:-k:-1]]) and 0 not in array[:-k + 1]:
                print("!!!")
                boolean = False
                break
    return array
 
import codewars_test as test
from solution import move_zeros

# import codewars_test as test
# from solution import move_zeros

# @test.it("Basic tests")
# def youarecute():
#     test.assert_equals(move_zeros(
#         [1, 2, 0, 1, 0, 1, 0, 3, 0, 1]),
#         [1, 2, 1, 1, 3, 1, 0, 0, 0, 0])
#     test.assert_equals(move_zeros(
#         [9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]),
#         [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
#     test.assert_equals(move_zeros([0, 0]), [0, 0])
#     test.assert_equals(move_zeros([0]), [0])
#     test.assert_equals(move_zeros([]), [])
