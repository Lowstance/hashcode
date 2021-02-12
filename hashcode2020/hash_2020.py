file_name = 'hashcode2020/f_libraries_of_the_world'

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

def sortBooks(lib_book, book_scores): 
    for k in range(len(lib_book)):
        n = len(lib_book[k]) 
        y = [book_scores[int(l)] for l in lib_book[k]]
        lib_book[k] = [x for _,x in sorted(zip(y, lib_book[k]), reverse=True)]
    return lib_book

def sortLibraries(lib_array, lib_book): 
    n = len(lib_array)
    y = [k[2] for k in lib_array]
    Z = [x for _,x in sorted(zip(y,zip(lib_array, lib_book)))]
    return Z


def write(final_indexes):
    file2 = open(file_name+'_results.txt', 'w')
    file2.write(''.join(i for i in final_indexes))
    file2.close()

if __name__ == '__main__':
    first_line, book_scores, lib_array, lib_book = parser()
    sortLibraries(lib_array, sortBooks(lib_book, book_scores))

