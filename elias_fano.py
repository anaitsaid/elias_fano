import math
import hashlib
import sys

with open(sys.argv[1], 'r') as example:  # reading the file name from the first argument
    lst = []  # the list of integers we want to encode
    lst2 = []  # the list of upper bits converted into integers minus the previous element
    low = []  # the list of lower bits in binary but written as string
    up = []  # the list of upper bits in binary but written as string
    L = []  # the list of lower bits in their integer form
    U = []  # the list of upper bits in their integer form
    output = ""  # string containing all the lower bits in one sequence
    output2 = ""  # string containing all the upper bits in one sequence

    for line in example:  # inserting our file in a list for usage
        lst.append(int(line))

    l = int(math.log(lst[len(lst) - 1] / len(lst), 2))  # calculating l=log2(m/n)

    for x in lst:  # separating the lower bits
        x = x & 2 ** l - 1  # integer AND (2^l)-1 converts all the upper bits to 0 and leaves the lower bits
        temp = format(x, "b")  # converting resulting integer into binary as string
        temp = temp.zfill(l)  # filling all our binary resulting values to l characters to fit the format
        output += temp  # and then concatenating each value in one string

    prev = 0
    for x in lst:  # separating the upper bits and subtracting the previous element
        x = x >> l  # right bit shift to remove the l bits
        lst2.append(x - prev)  # subtracting the previous element and adding it to a list
        prev = x  # saving the current element for the next loop sequence

    for x in lst2:  # converting our upper bits to unary
        for i in range(x):
            output2 += "0"  # adding zeros equal to the number needed
        output2 += "1"  # then ending our number with a 1, all of this will be concatenated in one string

    if len(output) % 8 != 0:  # making sure our lower bits are in packs of 8 bits
        for x in range(8 - len(output) % 8):
            output += "0"

    if len(output2) % 8 != 0:  # making sure our upper bits are in packs of 8 bits
        for x in range(8 - len(output2) % 8):
            output2 += "0"

    print("l ", l)

    print("L")

    for x in range(len(output) // 8):  # a loop that stores our resulting lower bits in a list of 8 bits each
        temp = output[x * 8:(x * 8) + 8]  # slicing the singular string by 8
        low.append(temp)  # adding it to a list
        print(temp)  # printing the resulting list

    print("U")

    for x in range(len(output2) // 8):  # a loop that stores our resulting upper bits in a list of 8 bits each
        temp = output2[x * 8:(x * 8) + 8]  # slicing the singular string by 8
        up.append(temp)  # adding it to a list
        print(temp)  # printing the resulting list

    for x in low:  # converting our binary list of lower bits to integer
        L.append(int(x, 2))

    for x in up:  # converting our binary list of upper bits to integer
        U.append(int(x, 2))

    m = hashlib.sha256()
    m.update(bytearray(L))  # updating m with the bytearray of L since it doesn't accept integer
    m.update(bytearray(U))  # updating m with the bytearray of U since it doesn't accept integer
    digest = m.hexdigest()
    print(digest)
