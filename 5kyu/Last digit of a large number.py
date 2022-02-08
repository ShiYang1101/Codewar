
#Define a function that takes in two non-negative integers aaa and bbb and returns the last decimal digit of aba^ba 
#b
# . Note that aaa and bbb may be very large!

#For example, the last decimal digit of 979^79 
#7
#  is 999, since 97=47829699^7 = 47829699 
#7
# =4782969. The last decimal digit of (2200)2300({2^{200}})^{2^{300}}(2 
#200
# ) 
#2 
#300
 
# , which has over 109210^{92}10 
#92
#  decimal digits, is 666. Also, please take 000^00 
#0
#  to be 111.

#You may assume that the input will always be valid.

def last_digit(n1, n2):
    if n2 == 0:
        return 1
    dict = {0:1, 1:1, 2:4, 3:4, 4:2, 5:1, 6:1, 7:4, 8:4, 9:2}
    dict1 = {0:[0], 1:[1], 2:[6,2,4,8], 3:[1,3,9,7], 4:[6,4], 5:[5], 6:[6], 7:[1,7, 9, 3], \
            8:[6,8,4,2], 9:[1,9]}
    ind = n1 % 10
    num = n2 % dict[ind]
    
    return dict1[ind][num]
