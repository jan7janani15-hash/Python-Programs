def length_of_last_word(s):
    words=s.split()
    return len(words[-1])
s="   Embedded Python   "
print("Length of last word:",length_of_last_word(s))