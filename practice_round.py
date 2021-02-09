import random
import string
from collections import Counter

file_name = 'e_many_teams'
w1 = 0
w2 = 0.8
w3 = 0.2
max_size = 0
max_freq = 0


#hello
def parser():
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
    frequency = sum([(max_freq-population_list.get(i))/max_freq for i in item])/len(item)
    size = len(item)/max_size
    rand_num = random.random()
    return frequency*w1 + size*w2 + rand_num*w3

def potatoMain(length, info_array):
    population_list = Counter(row for item in info_array for row in item) 
    global max_freq
    max_freq = max(population_list.values())
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

def automatic():
    max_w1 = 0
    max_score = 0
    global w1
    global w2
    w1 = 0
    w2 = 1
    for i in range(0,10):
        [length, info] = parser()
        final_indexes = potatoMain(length, info)
        write(create_result(final_indexes, length))
        cur_score = score()
        if(cur_score>max_score):
            max_score = cur_score
            max_w1 = w1

        w1 += 0.1
        w2 -= 0.1
        return max_score, max_w1
        


if __name__ == '__main__':
    [length, info] = parser()
    final_indexes = potatoMain(length, info)
    write(create_result(final_indexes, length))
    score()
    #automatic()
