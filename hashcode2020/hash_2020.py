file_name = 'hash_Code_2020/f_libraries_of_the_world'



def parser():
    file1 = open(file_name+'.txt', 'r')
    data = file1.readlines()
    first_line = data[0][:-1].split(" ")
    book_scores = data[1][:-1].split(" ")
    lib_array = [i[:-1].split(" ") for i in data[2::2]]
    lib_book = [i[:-1].split(" ") for i in data[3::2]]
    file1.close()
    return first_line, book_scores, lib_array, lib_book


def fill_array(lib_book):
    indexes = []
    for i in range(len(lib_book)):
        indexes.append([i, len(lib_book[i])])
        indexes.append(lib_book[i])

    return indexes

def deleteduplicate(books, truth_table):
    book = []
    for i in books:
        if truth_table[int(i)] == True:
            continue
        truth_table[int(i)] = True
        book.append(i)
    return book

def middleStep(lib_book , first_line):
    truth_table = [False for i in range(int(first_line[0]))]
    for i in range(len(lib_book)):
        lib_book[i] = deleteduplicate(lib_book[i] , truth_table)

def sortBooks(lib_book, book_scores): 
    for k in range(len(lib_book)):
        n = len(lib_book[k]) 
        y = [book_scores[int(l)] for l in lib_book[k]]
        lib_book[k] = [x for _,x in sorted(zip(y, lib_book[k]), reverse=True)]
    return lib_book

def sortLibraries(lib_array, books): 
    n = len(lib_array)
    id = [i for i in range(len(lib_array))]
    #y = [k[2] for k in lib_array]
    y = [len(i) for i in books]
    #print(y)
    Z = [x for _,x in sorted(zip(y,zip(books, id)) , reverse = True)]
    return Z

def optimizeBook(lib_book):
    return [list(set(i)) for i in lib_book]

def buildArray(info, first_line):
    final_indexes = []
    final_indexes.append(len(info))
    for i in range(len(info)):
        temp = []
        if not info[i][0]:
            continue
        temp.append([info[i][1], len(info[i][0])])
        temp.append(info[i][0])
        final_indexes.append(temp)
    return final_indexes
    

def write(final_indexes):
    file2 = open(file_name+'_results.txt', 'w')
    file2.write(''.join(i for i in final_indexes))
    file2.close()





if __name__ == '__main__':
    first_line, book_scores, lib_array, lib_book = parser()
    middleStep(lib_book , first_line)
    sortBooks(lib_book , book_scores)
    final_array = sortLibraries(lib_array , lib_book)
    #lib_book = optimizeBook(lib_book)
    buildArray(final_array , first_line)
