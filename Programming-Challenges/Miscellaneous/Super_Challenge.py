'''
Created on Feb 2, 2015

@author: mayberryr
'''
fname = "dream.txt"

num_lines = 0
num_words = 0
num_chars = 0

with open(fname, 'r') as f:
    for line in f:
            words = line.split()
            num_lines += 1
            num_words += len(words)
            num_chars += len(line)

print("There are", num_lines, "lines.")
print("The total word count is:", num_words)
print("The total character amt (with spaces):", num_chars)
