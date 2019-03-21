import pickle
import os
import numpy


data = []
if os.path.getsize('C3_train.pkl') > 0:
    with open('C3_train.pkl', 'rb') as f:
        file = open("output_pkl.txt",'w')
        data = pickle.load(f)
        print(len(data))
        print(data)
        file.write(str(data))
else:
    print('empty file')
