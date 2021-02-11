
file_name = 'hashcode2020/a_example'

def parser():
    file1 = open(file_name+'.txt', 'r')
    data = file1.readlines()
    first_line = data[0].split(" ")
    book_scores = data[1].split(" ")
    lib_array = [i[:-1].split(" ") for i in data[2::2]]
    lib_book = [i[:-1].split(" ") for i in data[3::2]]
    file1.close()
    print(lib_array)
    print(lib_book)
    return lib_book


def fill_array(lib_book):
    indexes = []
    for i in range(len(lib_book)):
        indexes.append([i, len(lib_book[i])])
        indexes.append(lib_book[i])

    print(indexes)
    return indexes

def make_array(indexes):
    final_array = []
    final_array.append(f"{int(len(indexes)/2)}\n")
    for i in range(0, len(indexes), 2):
        line1 = f"{str(indexes[i][0])}  {str(indexes[i][1])}\n"
        final_array.append(line1)
        line2 = ''
        for j in range(len(indexes[i+1])):
            line2 += indexes[i+1][j] + ' '

        final_array.append(line2[:-1]+'\n')

    return final_array

def score():
    file1 = open(file_name+'_results.txt', 'r')
    file2 = open(file_name+'.txt', 'r')
    first_line = file1.readline()
    result = []
    for i 0->day:
        

def write(final_indexes):
    file2 = open(file_name+'_results.txt', 'w')
    file2.write(''.join(i for i in final_indexes))
    file2.close()

if __name__ == '__main__':
    write(make_array(fill_array(parser())))


