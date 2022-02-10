import numpy as np
from keras.preprocessing import image
import keras
import os
import pickle
import pyreadstat
import pathlib



def convertChar(response):
    if response[0][0] == 1:
        return('ა')
    elif response[0][1] == 1:
        return ('ბ')
    elif response[0][2] == 1:
        return ('გ')
    elif response[0][3] == 1:
        return ('დ')
    elif response[0][4] == 1:
        return ('ე')
    elif response[0][5] == 1:
        return ('ვ')
    elif response[0][6] == 1:
        return ('ზ')
    elif response[0][7] == 1:
        return ('თ')
    elif response[0][8] == 1:
        return ('ი')
    elif response[0][9] == 1:
        return ('კ')
    elif response[0][10] == 1:
        return ('ლ')
    elif response[0][11] == 1:
        return ('მ')
    elif response[0][12] == 1:
        return ('ნ')
    elif response[0][13] == 1:
        return ('ო')
    elif response[0][14] == 1:
        return ('პ')
    elif response[0][15] == 1:
        return ('ჟ')
    elif response[0][16] == 1:
        return ('რ')
    elif response[0][17] == 1:
        return ('ს')
    elif response[0][18] == 1:
        return ('ტ')
    elif response[0][19] == 1:
        return ('უ')
    elif response[0][20] == 1:
        return ('ფ')
    elif response[0][21] == 1:
        return ('ქ')
    elif response[0][22] == 1:
        return ('ღ')
    elif response[0][23] == 1:
        return ('ყ')
    elif response[0][24] == 1:
        return ('შ')
    elif response[0][25] == 1:
        return ('ჩ')
    elif response[0][26] == 1:
        return ('ც')
    elif response[0][27] == 1:
        return ('ძ')
    elif response[0][28] == 1:
        return ('წ')
    elif response[0][29] == 1:
        return ('ჭ')
    elif response[0][30] == 1:
        return ('ხ')
    elif response[0][31] == 1:
        return ('ჯ')
    elif response[0][32] == 1:
        return ('ჰ')


os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
model = keras.models.load_model("4poch10model.h5")

file_name = "test.txt"
stPath = "DATA/"
completeName = file_name
directory = os.fsencode(stPath)
file1 = open(completeName, "w")

directory = os.fsencode(stPath)
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    path = stPath + filename
    try:
        img = image.load_img(path, target_size = (40,100))
        img = image.img_to_array(img)
        img = np.expand_dims(img, axis = 0)
        result = model.predict(img)
        result = convertChar(result)
        filename23 = pathlib.Path(path).stem
        file1.write(filename23 +"-"+result +"\n")
    except:
        print("wrong ffile: " + path)

file1.close()
            
