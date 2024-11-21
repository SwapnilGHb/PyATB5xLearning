for number in range(10): # number - 0 to 9, times 10
    if number % 2 == 0:
        continue
    else:
        print(number)


# |i| Condition | O/P
# |0| 0 % 2 == 0 -> True| O/P = Skip No o/P
# |1| 1 % 2 == 0 -> False| O/P = 1
# |2| 2 % 2 == 0 -> True| O/P = Skip No O/P
# |3| 3 % 2 == 0 -> False| O/P = 3
# |4| 4 % 2 == 0 -> True| O/P = Skip No O/P
# |5| 5 % 2 == 0 -> False| O/P = 5
# |6| 6 % 2 == 0 -> True| O/P = Skip No O/P
# |7| 7 % 2 == 0 -> False| O/P = 7
# |8| 8 % 2 == 0 -> True| O/P = Skip No O/P
# |9| 9 % 2 == 0 -> False| O/P = 9