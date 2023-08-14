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

import cv2
import numpy as np
import matplotlib.pyplot as plt

def extract_images(data_folder):

    for filename in os.listdir(data_folder):
        if filename.split('.')[1] == "jpg": 
            print(filename)
            imfile = os.path.join(data_folder, filename)
            img = cv2.imread(imfile, 0)
            #cv2.imshow('',img)
            #cv2.waitKey(0)
            #print(img)
            width, height = img.shape
            print(height)

            image = cv2.imread(imfile)
            template = cv2.imread('iphone.jpeg')

        ## downscale template
            scale_percent = 8 # percent of original size
            width = int(template.shape[1] * scale_percent / 100)
            height = int(template.shape[0] * scale_percent / 100)
            dim = (width, height)
            
            # resize image
            template = cv2.resize(template, dim, interpolation = cv2.INTER_AREA)
        ##
        query_img = cv2.imread('iphone.jpeg') 
        train_img = cv2.imread(imfile)

        img1 = cv2.imread('iphone.jpeg', 0)          # query Image
        img2 = cv2.imread(imfile,0)  # target Image

        # Initiate SIFT detector
        orb = cv2.ORB_create()

        # find the keypoints and descriptors with ORB
        kp1, des1 = orb.detectAndCompute(img1,None)
        kp2, des2 = orb.detectAndCompute(img2,None)

        # create BFMatcher object
        bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

        # Match descriptors.
        matches = bf.match(des1,des2)

        # Sort them in the order of their distance.
        matches = sorted(matches, key = lambda x:x.distance)

        good_matches = matches[:30]

        src_pts = np.float32([ kp1[m.queryIdx].pt for m in good_matches     ]).reshape(-1,1,2)
        dst_pts = np.float32([ kp2[m.trainIdx].pt for m in good_matches ]).reshape(-1,1,2)
        M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC,5.0)
        matchesMask = mask.ravel().tolist()
        h,w = img1.shape[:2]
        pts = np.float32([ [0,0],[0,h-1],[w-1,h-1],[w-1,0] ]).reshape(-1,1,2)

        dst = cv2.perspectiveTransform(pts,M)
        dst += (w, 0)  # adding offset

        draw_params = dict(matchColor = (0,255,0), # draw matches in green color
                    singlePointColor = None,
                    matchesMask = matchesMask, # draw only inliers
                    flags = 2)

        img3 = cv2.drawMatches(img1,kp1,img2,kp2,good_matches, None,**draw_params)

        # Draw bounding box in Red
        img3 = cv2.polylines(img3, [np.int32(dst)], True, (0,0,255),3, cv2.LINE_AA)

        cv2.imshow("result", img3)
        cv2.waitKey()
        # or another option for display output
        #plt.imshow(img3, 'result'), plt.show()
                


    #cv2.imshow('',template)
    #cv2.waitKey(0)


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