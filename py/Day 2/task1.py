# Your task is to make a function that can take any
# non-negative integer as an argument and return it with its digits
# in descending order. Essentially, rearrange the digits to create the highest possible number.


def descending_order(num):
    print(''.join(i for i in sorted([s for s in str(num)], reverse=True)))

descending_order(15)
descending_order(125)
descending_order(1545242311)
descending_order(113134345)
descending_order(1553532)

