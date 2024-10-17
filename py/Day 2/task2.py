# An isogram is a word that has no repeating letters, consecutive or non-consecutive.
# Implement a function that determines whether a string that contains only letters is an isogram.
# Assume the empty string is an isogram. Ignore letter case.

def is_isogram(string):
    return ''.join([s for s in string if s.isalpha() and string.lower().count(s.lower())==1]) == string

print(is_isogram("Dermatoglyphics"))

