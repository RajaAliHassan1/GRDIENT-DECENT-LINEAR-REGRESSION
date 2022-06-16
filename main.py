#IMPORTING LIBRARIES
import random
import pandas as pd
import numpy as np
import openpyxl


#READING EXCEL DATA FROM EXCEL FILE
path = 'model.xlsx'; # PATH TO THE FEATURE FILE
df = pd.read_excel(path); # READING THE EXCEL FILE
weights = df.to_numpy(); # CONVERTING DATA FRAME TO NUMPY ARRAY

#READING EXCEL DATA FROM EXCEL FILE
path = 'testing.xlsx'; # PATH TO THE FEATURE FILE
df = pd.read_excel(path); # READING THE EXCEL FILE
data = df.to_numpy(); # CONVERTING DATA FRAME TO NUMPY ARRAY
prediction = list();
#################################################
def normalize(prediction):

    i = 0;
    while i < 197:
        temp = (((prediction[i] - min(prediction)) / (max(prediction) - min(prediction)))* 200);
        prediction.append(temp);
        i = i + 1
    return prediction
#################################################
i = 0;
j = 0;
sum = 0;
while i < 31:
    while j < 9502:
        sum = sum + (data[i][j]*weights[j]);
        j = j + 1
    j = 0;
    prediction.append(sum);
    print(sum)
    sum = 0;
    i = i + 1
print("before normalization")
print(prediction)

predicts = list();
predicts = normalize(prediction);
#################################################
# 1 2 5 10 20 50 100 200
Classification = [1,2,5,10,20,50,100,200]
distance = list();
i = 0;
j = 0;
while i < 31:
    while j < 8:
        distance.append( Classification[j] - predicts[i]);
        j = j + 1;

    min_value = min(distance)
    min_value = min(distance)
    min_index = distance.index(min_value)
    predicts[i] = Classification[min_index];
    distance.clear()
    j = 0;
    i = i + 1;






print(predicts)


