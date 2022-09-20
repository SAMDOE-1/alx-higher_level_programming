#!/usr/bin/python3
for i in 'abcdefghijklmnopqrstuvwxyz':
    if (i != "q" and i != "e"):
        continue

    print("{:c}".format(i), end="")
