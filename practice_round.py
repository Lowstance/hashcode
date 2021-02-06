import random
import string
from collections import Counter

file_name = 'e_many_teams'
w1 = 300
w2 = 1
max_size = 1

#hello
#parser IT WORKS

def parser(file_name):
    global max_size
    file1 = open(file_name+'.in', 'r')
    first_line = file1.readline()
    first_line = first_line[:-1].split(" ")
    info_array = []
    for i in range(0 , int (first_line[0])):
        token_line = file1.readline()
        if int(token_line[0]) > max_size:
            max_size = int(token_line[0])
        info_array.append(token_line[2:-1].split(" "))
    file1.close()
    return [int(i) for i in first_line] , info_array


def write(final_indexes):
    file2 = open(file_name+'_results.in', 'w')
    file2.write(''.join(i for i in final_indexes))
    file2.close()

def evaluate(item, population_list):
    frequency = 1 / sum([population_list.get(i) for i in item])
    #print("freq" + str(frequency*w1))
    size = len(item)/max_size
    #print("size" + str(size*w2))
    return frequency*w1 + size*w2

def potatoMain(length, info_array):
    population_list = Counter(row for item in info_array for row in item) 

    score_list = []
    for i in range(0, length[0]):
        score_list.append([evaluate(info_array[i], population_list), i])

    score_list.sort(key=lambda pair: pair[0], reverse = True)

    result = [0]*length[0]
    for i in range(0, length[0]):
        result[i] = score_list[i][1]

    return result

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

if __name__ == '__main__':
    [length, info] = parser(file_name)
    final_indexes = potatoMain(length, info)
    write(create_result(final_indexes, length))