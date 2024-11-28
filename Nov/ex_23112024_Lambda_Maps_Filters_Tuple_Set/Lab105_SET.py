# Find the first non-repeating character in a string sets
# swiss -> s-x, w- Answer

def first_non_repeating(string):
    for char in string:
        if string.count(char) == 1:
            return char
    return None

print(first_non_repeating("swiss"))
print(first_non_repeating("pepper"))
print(first_non_repeating("dada"))
print(first_non_repeating("annusinha"))
print(first_non_repeating("tammanaa"))