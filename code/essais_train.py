import csv
import cv2

def csv_write():
    with open('test.csv', 'w') as file:
        writer = csv.writer(file)
        file.write("label;")
        for i in range(0, 10000):
            file.write("pixel"+str(i)+";")

        file.write("\n")


def reshape_thresh(thresh):
    thresh = cv2.resize(thresh, (100, 100))
    return thresh


def to_list(thresh):

    data = []
    for i in range(thresh.shape[0]):
        for j in range(thresh.shape[1]):
            if thresh[i, j] > 120:
                nb = 1
            else:
                nb = 0
        
            data.append(nb)

    return data



def write_data_into_csv(data, label):

    with open('test.csv', 'a') as file:
        writer = csv.writer(file)
        file.write(label+";")
        for i in data:
            file.write(str(i)+";")

        file.write("\n")
















