# HackerRank-Challenges-Solutions 🚀
https://www.hackerrank.com/challenges/python-string-split-and-join/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign

This code defines a function split_and_join that takes a string, splits it into a list of words using spaces as separators, and then joins the words using hyphens. The modified string is then returned.
"""

def split_and_join(line):

    # write your code here

    a = line.split(" ")

    b = "-".join(a)

    return(b)


if __name__ == '__main__':

    line = input()

    result = split_and_join(line)

    print(result)
