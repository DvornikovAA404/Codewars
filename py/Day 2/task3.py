# You are going to be given a word.
# Your job is to return the middle character of the word.
# If the word's length is odd, return the middle character.
# If the word's length is even, return the middle 2 characters.

def get_middle(s):
    a = len(s)//2
    return s[a] if len(s)%2 else s[a-1:a+1]

print(get_middle("abcd"))
print(get_middle("123456789"))