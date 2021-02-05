import random
import string

file_name = 'e_many_teams'
margin = 2

#hello
#parser IT WORKS
def parser(file_name):
    file1 = open(file_name+'.in', 'r')
    first_line = file1.readline()
    first_line = first_line[:-1].split(" ")
    info_array = []
    for i in range(0 , int (first_line[0])):
        token_line = file1.readline()
        info_array.append(token_line[0:-1].split(" "))
    file1.close()
    return first_line, info_array


def write(final_indexes, length):
    first = 0
    counter1 = 0

    for i in range (0, int(length[3])):
        if(counter1 + 3 >= int(length[0])):
            break
        counter1 = counter1 + 4
        first = first + 1
        
    for i in range (0, int(length[2])):
        if(counter1 + 2 >= int(length[0])):
            break
        counter1 = counter1 + 3
        first = first + 1

    for i in range (0, int(length[1])):
        if(counter1 + 1 >= int(length[0])):
            break
        counter1 = counter1 + 2
        first = first + 1
        
    file2 = open(file_name+'_results.in', 'w')
    file2.write(str(first) + "\n")

    counter = 0

    for i in range (0, int(length[3])):
        if(counter + 3 >= int(length[0])):
            break
        line = "4 " + str(final_indexes[counter]) + " " + str(final_indexes[counter+1]) + " " + str(final_indexes[counter+2]) + " " + str(final_indexes[counter+3]) + "\n"
        file2.write(line)
        counter = counter + 4

    for i in range (0, int(length[2])):
        if(counter + 2 >= int(length[0])):
            break
        line = "3 " + str(final_indexes[counter]) + " " + str(final_indexes[counter+1]) + " " + str(final_indexes[counter+2])+ "\n"
        file2.write(line)
        counter = counter + 3

    for i in range (0, int(length[1])):
        if(counter + 1 >= int(length[0])):
            break
        line = "2 " + str(final_indexes[counter]) + " " + str(final_indexes[counter + 1]) + "\n"
        file2.write(line)
        counter = counter + 2

    file2.close()

def compare(array_1, array_2):
    return True if sum([1 if array_1[1:].count(element) else 0 for element in array_2[1:]]) < margin else False


def potatoMain(length, info_array):
    population_list = []
    population_count_list= []
    for i in range (0, int(length[0])):
        for item in info_array[i][1:]:
            if population_list.count(item) == 0:
                population_list.append(item)
                population_count_list.append(1)
            else:
                population_count_list[population_list.index(item)] += 1

    score_list = []
    for i in range(0, int(length[0])):
        score_list.append([sum([population_count_list[population_list.index(item)] for item in info_array[i][1:]]), i])

    score_list.sort(key=lambda pair: pair[0], reverse = True)

    result = [0]*int(length[0])
    counter = 0
    for i in range(0, int(length[0]), 2):
        result[i] = score_list[int(i/2)][1]
        if(i+1 >= int(length[0])):
            break
        result[i+1] = score_list[int(length[0])-1-int(i/2)][1]
    return result


if __name__ == '__main__':
    [length, info] = parser(file_name)
    final_indexes = potatoMain(length, info)
    write(final_indexes, length)

