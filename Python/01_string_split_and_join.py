# HackerRank-Challenges-Solutions 🚀

This code defines a function split_and_join that takes a string, splits it into a list of words using spaces as separators, and then joins the words using hyphens. 
The modified string is then returned.

     

def split_and_join(line):
  
    a = line.split(" ")    # Split the line into a list of words using spaces as separators

    b = "-".join(a)        # Join the words using hyphens

    return(b)


if __name__ == '__main__':

    line = input()           # Input a line of text

    result = split_and_join(line)    # Call the function 

    print(result)                    # print the result
