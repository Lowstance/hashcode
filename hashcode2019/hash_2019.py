file_name = 'hashcode2019/a_example'

def parser():
    file1 = open(file_name+'.txt', 'r')
    data = file1.readlines()
    lines = [i[:-1].split(" ") for i in data[1:]]
    photos = [[i[0] , int(i[1]) , i[2:-1]] for i in lines]
    #print(photos)
    file1.close()
    return photos

def putPhotos (photos):
    final_indexes = []
    n = -1
    for i in range(len(photos)):
        if photos[i][0] == 'H' :
            if n == -1 :
                n = i
            else:
                final_indexes.append([n,i])
                n = -1
            continue
        final_indexes.append(i)
    return final_indexes

if __name__ == '__main__':
    info = parser()
    print(putPhotos(info))