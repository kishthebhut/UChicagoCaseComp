import pickle
import os

if os.path.getsize('C3_train.pkl') > 0:
    with open('C3_train.pkl', 'rb') as f:
        data = pickle.load(f)
        file = open("testfile.txt",'w')
        file.write(str(data))
        print(data)
else:
    print('empty file')
