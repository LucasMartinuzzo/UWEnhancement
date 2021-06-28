import os


def getfiles(path):
    filenames=os.listdir(path)
    print(filenames)
    return filenames



if __name__ == '__main__':

    if not os.path.exists('train.txt'):
        os.mknod('train.txt')
    training_path = './DATA/Train/train'
    a = getfiles(training_path)
    # a.spilt('')
    l = len(a)
    with open("train.txt", "w") as f:
        for i in range(l):
            print(a[i])
            x = a[i]
            f.write(x)
            f.write('\n')
        f.close()
    
    
    if not os.path.exists('test.txt'):
        os.mknod('test.txt')
    test_path = './DATA/Test/test'
    a = getfiles(test_path)
    # a.spilt('')
    l = len(a)
    with open("test.txt", "w") as f:
        for i in range(l):
            print(a[i])
            x = a[i]
            f.write(x)
            f.write('\n')
        f.close()

    print()