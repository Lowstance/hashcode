import random
import string
from collections import Counter
from random import choice

file_name = 'c_many_ingredients'
standard = 1200
n = 50

def parser():
    file1 = open(file_name+'.in', 'r')
    first_line = file1.readline()
    first_line = first_line[:-1].split(" ")
    info_array = []
    for i in range(0 , int (first_line[0])):
        token_line = file1.readline()
        info_array.append(token_line[2:-1].split(" "))

    file1.close()
    return [int(i) for i in first_line] , info_array


def write(final_indexes):
    file2 = open(file_name+'_results.in', 'w')
    file2.write(''.join(i for i in final_indexes))
    file2.close()

def select(length , num_ps , pinakas):
    teams = []
    for i in range(num_ps):
        num = random.randrange(0,length[0])
        while (pinakas[num] == False) or (num in teams):
            num = random.randrange(0,length[0])
        teams.append(num)
    #print(pinakas)
    return teams

def evaluate(teams , info_array , l_standard):
    #score = sum([len(info_array[i]) for i in teams])
    score = len(list(filter(None, set([item for j in teams for item in info_array[int(j)]]))))
    #print(teams)
    #print(score)
    #print(l_standard)
    return True if score > l_standard else False

def findTeams(length , num_ps , pinakas , info_array): 
    l_standard = standard
    counter = 0
    teams = select(length , num_ps , pinakas)  
    while not evaluate(teams , info_array , l_standard):
        if (counter > n) :
            counter = 0
            l_standard  = 0.9*l_standard
        teams = select(length , num_ps , pinakas)
        counter += 1
    for i in teams: pinakas[i] = False
    #if l_standard == standard :
    #    print(l_standard)
    #print(teams)
    #print(pinakas)
    return teams

def createTeams(length , info_array):
    rand_ps = []
    pinakas = [True for i in info_array]
    counter = 0

    for j in range(length[3]):
        if(counter + 3 >= length[0]):
            break
        rand_ps += findTeams(length , 4 , pinakas , info_array)
        counter += 4

    for j in range(length[2]):
        if(counter + 2 >= length[0]):
            break  
        rand_ps += findTeams(length , 3 , pinakas , info_array)
        counter += 3

    for j in range(length[1]):
        if(counter + 1 >= length[0]):
            break    
        rand_ps += findTeams(length , 2 , pinakas , info_array)
        counter += 2
    #print(pinakas)
    return rand_ps

def create_result(final_indexes, length):
    counter = 0
    result_array = []
    for i in range (0, length[3]):
        if(counter + 3 >= length[0]):
            break
        line = "4 " + str(final_indexes[counter]) + " " + str(final_indexes[counter+1]) + " " + str(final_indexes[counter+2]) + " " + str(final_indexes[counter+3]) + "\n"
        result_array.append(line)
        counter = counter + 4

    for i in range (0, length[2]):
        if(counter + 2 >= length[0]):
            break
        line = "3 " + str(final_indexes[counter]) + " " + str(final_indexes[counter+1]) + " " + str(final_indexes[counter+2])+ "\n"
        result_array.append(line)
        counter = counter + 3

    for i in range (0, length[1]):
        if(counter + 1 >= length[0]):
            break
        line = "2 " + str(final_indexes[counter]) + " " + str(final_indexes[counter + 1]) + "\n"
        result_array.append(line)
        counter = counter + 2

    result_array.insert(0, str(len(result_array)) + "\n")
    return result_array

def score():
    file1 = open(file_name+'_results.in', 'r')
    file2 = open(file_name+'.in', 'r')
    first_line = file1.readline()
    result = []
    for i in range(0 , int (first_line[:-1])):
        token_line = file1.readline()
        result.append(token_line[2:-1].split(" "))
    #print(result)
    first_line1 = file2.readline()
    info_array = []
    first_line1 = first_line1[:-1].split(" ")
    for i in range(0 , int (first_line1[0])):
        token_line = file2.readline()
        info_array.append(token_line[2:-1].split(" "))


    score = [0] * int(first_line[:-1])
    for i in range(0, int(first_line[:-1])):
        score[i] = len(list(filter(None, set([item for j in result[i] for item in info_array[int(j)]]))))
        score[i] = score[i]**2

    file1.close()
    file2.close()
    print(sum(score))
    return sum(score)

if __name__ == '__main__':
    [length, info] = parser()
    result = createTeams(length , info)
    #print(result)
    write(create_result(result, length))
    score()