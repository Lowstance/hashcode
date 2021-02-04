import random
import string
from math import sqrt


def program():
    file1 = open('e_many_teams.in', 'r')
    file2 = open('result4.in', 'w')
    line = file1.readline()
    line = line[:-1].split(" ")
    
    lines = []
    for i in range (0, 500):
        token_line = file1.readline()
        lines.append(token_line[0:-1].split(" "))
    
    first = 0
    counter1 = 0
    for i in range (0, int(line[1])):
        if(counter1 + 1 >= int(line[0])):
            break
        counter1 = counter1 + 2
        first = first + 1

    for i in range (0, int(line[2])):
        if(counter1 + 2 >= int(line[0])):
            break
        counter1 = counter1 + 3
        first = first + 1

    for i in range (0, int(line[3])):
        if(counter1 + 3 >= int(line[0])):
            break
        counter1 = counter1 + 4
        first = first + 1

    file2.write(str(first) + "\n")

    counter = 0
    for i in range (0, int(line[1])):
        if(counter + 1 >= int(line[0])):
            break
        str1 = "2" + " " + str(counter) + " " + str(counter + 1) + "\n"
        file2.write(str1)
        counter = counter + 2

    for i in range (0, int(line[2])):
        if(counter + 2 >= int(line[0])):
            break
        str1 = "3" + " " + str(counter) + " " + str(counter+1) + " " + str(counter+2)+ "\n"
        file2.write(str1)
        counter = counter + 3

    for i in range (0, int(line[3])):
        if(counter + 3 >= int(line[0])):
            break
        str1 = "4" + " " + str(counter) + " " + str(counter+1) + " " + str(counter+2) + " " + str(counter+3) + "\n"
        file2.write(str1)
        counter = counter + 4

    

    file1.close()
    file2.close()


if __name__ == '__main__':
    k = program()