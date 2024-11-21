# Match statement ->  # Switch in Java
# match the op and execute
# Python > 3.10

# match variable:
#       case pattern1:
#           # code block
#       case pattern2:
#           # code block

# Write a program to ask the user which browser he wants to run automation.

browser_name = input("Enter the browser name \n")
match browser_name:
    case "Firefox":
        print("Starting Firefox!!!!")
    case "Chrome":
        print("Execute the Chrome code!!!!")
    case "Edge":
        print("Execute the Edge code!!!!")
    case "Safari":
        print("Execute the Safari code!!!!")
    case _:   # default
        print("Browser not found!!!!")

