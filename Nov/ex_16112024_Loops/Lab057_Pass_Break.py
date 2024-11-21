for i in range(0,10,1):
    if i == 6 or i ==5:
        print(i)
    else:
        pass  # pass is a placeholder statement that does nothing
    # It's used when a statement is syntactically required no action is needed.

    # |i| Condition | O/P
    # |0| 0 == 6 -> False or 0 == 5 -> False| O/P = Nothing will be printed
    # |1| 1 == 6 -> False or 1 == 5 -> False| O/P = Nothing will be printed
    # |2| 2 == 6 -> False or 2 == 5 -> False| O/P = Nothing will be printed
    # |3| 3 == 6 -> False or 3 == 5 -> False| O/P = Nothing will be printed
    # |4| 4 == 6 -> False or 4 == 5 -> False| O/P = Nothing will be printed
    # |5| 5 == 6 -> False or 5 == 5 -> True| O/P = 5
    # |6| 6 == 6 -> True or 6 == 5 -> False| O/P = 6
    # |7| 7 == 6 -> False or 7 == 5 -> False| O/P = Nothing will be printed
    # |8| 8 == 6 -> False or 8 == 5 -> False| O/P = Nothing will be printed
    # |9| 9 == 6 -> False or 9 == 5 -> False| O/P = Nothing will be printed
    # |10| 10 == 6 -> False or 10 == 5 -> False| For loop finished