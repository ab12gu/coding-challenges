'''
  filename:         train_phone_finder.py
  by:               abhay gupta
  date created:     22-04-05

  desc: 
  The customer held out 8 images with similar statistics to the training set and is going to
    test your phone detector on them. The customer has an automated script for testing your phone
    detector. Please submit 2 executable python3 scripts:

  1) train_phone_finder.py takes a single command line argument which is a path to a
        folder with labeled images and labels.txt that has been attached to this
        description. This script may generate any artifacts you want in the current folder.
        Here is what a terminal command will look like:
    > python train_phone_finder.py ~/find_phone

  2) find_phone.py takes a single command line argument which is a path to the jpeg
        image to be tested. This script may use data in the local folder previously
        generated by train_phone_finder.py . This script has to print the normalized
        coordinates of the phone detected on this test image in the format shown below.
        Here is what a terminal command will look like. Please, notice space separated
        float numbers on a single line without parentheses (!):
    > python find_phone.py ~/find_phone_test_images/51.jpg
    0.2551 0.3129
'''

import sys
import os

def labelled_data(labels_folder):
    ''' 
        read label data and sort        
        parameters:     labels_folder   
    '''

    print(labels_folder)

    # read data
    with open(labels_folder) as file_open:
        lines = file_open.readlines()

    data = {}
    data_value = []

    # sort data into dictionary 
    for line in lines:
        number = int(line.split(".")[0])
        data_value.append(float(line.split(" ")[1]))
        data_value.append(float(line.split(" ")[2]))
        data[number] = data_value
        data_value = []

    # sort dictionary
    data = {k: v for k, v in sorted(list(data.items()))}

    # check data values
    print(data)

    return data


def extract_images(data_folder):

    for filename in os.listdir(data_folder):
        if filename.split('.')[1] == "jpg": 
            print(filename)


if __name__ == "__main__":
    ''' 
    main script to find phone in image 
    '''

    # get input argument (directory name)
    data_folder = sys.argv[1]

    # parse labels.txt into organized data
    labels_folder = os.path.join(data_folder, "labels.txt")
    data = labelled_data(labels_folder)

    # extract images into dataset
    extract_images(data_folder)

    #print(f"Arguments count: {len(sys.argv)}")
    #for i, arg in enumerate(sys.argv):
        #print(f"Argument {i:>6}: {arg}")

    print("hello")