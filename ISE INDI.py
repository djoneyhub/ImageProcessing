#modules used
import cv2
import numpy as np

#IMAGE HANDLING
im = cv2.imread("/Users/djoneeeeyyy/Desktop/fruits.png") #upload image
cv2.imshow("fruits",im) #TO SHOW IMAGE
cv2.destroyAllWindows()

#main menu
def main_menu():
    print("====================WELCOME TO====================")
    print("===============COLOR DETECTING SYSTEM=============")
    print("=======Created by Adjani Udayana TP061651=========")
    print("press the following keys to choose color to detect:")
    print("1. Yellow")
    print("2. Red")
    print("3. Purple")
    print("4. Orange")
    print("5. Green")
    print("6. Exit")
    choice = input("choice: ")

    if choice == "1":
        
        print("here are the yellows \^-^/")
        #COLOR DETECTING AND MASK CREATION
        #HSV is used
        hsv = cv2.cvtColor(im,cv2.COLOR_BGR2HSV) #convert color space

        #setting lower and upper bound for yellow
        low_bound = np.array([20, 100, 100]) 
        up_bound = np.array([30, 255, 255])


        #find colors within range
        mask = cv2.inRange (hsv,low_bound,up_bound)

        #REMOVING MASK
        #define kernel size
        kern = np.ones((7,7), np.uint8)

        #remove unnecessary noise
        mask = cv2.morphologyEx (mask, cv2.MORPH_CLOSE, kern)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kern)

        #segmenting detected area
        seg_img = cv2.bitwise_and(im, im, mask = mask)

        # Find contours from the mask
        contours, hierarchy = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        output = cv2.drawContours(seg_img, contours, -1, (0, 0, 255), 3)

        # Showing the output
        cv2.imshow("yellow image", output)
        

    elif choice == "2":
        print("here is the red! \^-^/")
        #COLOR DETECTING AND MASK CREATION
        #HSV is used
        hsv = cv2.cvtColor(im,cv2.COLOR_BGR2HSV) #convert color space

        #setting lower and upper bound for red
        r_low_bound = np.array([0,50,50]) 
        r_up_bound = np.array([10,255,255])
        
        #find colors within range
        mask = cv2.inRange (hsv,r_low_bound,r_up_bound)

        #REMOVING MASK
        #define kernel size
        kern = np.ones((7,7), np.uint8)

        #remove unnecessary noise
        mask = cv2.morphologyEx (mask, cv2.MORPH_CLOSE, kern)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kern)

        #segmenting detected area
        seg_img = cv2.bitwise_and(im, im, mask = mask)

        # Find contours from the mask
        contours, hierarchy = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        output = cv2.drawContours(seg_img, contours, -1, (0, 0, 255), 3)

        # Showing the output
        cv2.imshow("red image", output)
        

        

    elif choice == "3":
        print("here is the purple \^-^/")
        #COLOR DETECTING AND MASK CREATION
        #HSV is used
        hsv = cv2.cvtColor(im,cv2.COLOR_BGR2HSV) #convert color space

        #setting lower and upper bound for purple
        p_low_bound = np.array([70,50,50]) 
        p_up_bound = np.array([180,255,255])


        #find colors within range
        mask = cv2.inRange (hsv,p_low_bound,p_up_bound)

        #REMOVING MASK
        #define kernel size
        kern = np.ones((7,7), np.uint8)

        #remove unnecessary noise
        mask = cv2.morphologyEx (mask, cv2.MORPH_CLOSE, kern)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kern)

        #segmenting detected area
        seg_img = cv2.bitwise_and(im, im, mask = mask)

        # Find contours from the mask
        contours, hierarchy = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        output = cv2.drawContours(seg_img, contours, -1, (0, 0, 255), 3)

        # Showing the output
        cv2.imshow("purple image", output)
        


    elif choice == "4":
        print("here is the orange! \^-^/")
        #COLOR DETECTING AND MASK CREATION
        #HSV is used
        hsv = cv2.cvtColor(im,cv2.COLOR_BGR2HSV) #convert color space

        #setting lower and upper bound for orange
        o_low_bound = np.array([10,100,5]) 
        o_up_bound = np.array([20,255,255])


        #find colors within range
        mask = cv2.inRange (hsv,o_low_bound,o_up_bound)

        #REMOVING MASK
        #define kernel size
        kern = np.ones((7,7), np.uint8)

        #remove unnecessary noise
        mask = cv2.morphologyEx (mask, cv2.MORPH_CLOSE, kern)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kern)

        #segmenting detected area
        seg_img = cv2.bitwise_and(im, im, mask = mask)

        # Find contours from the mask
        contours, hierarchy = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        output = cv2.drawContours(seg_img, contours, -1, (0, 0, 255), 3)

        # Showing the output
        cv2.imshow("orange image", output)
        
        

    elif choice == "5":
        print("here are the greens! \^-^/")
        #COLOR DETECTING AND MASK CREATION
        #HSV is used
        hsv = cv2.cvtColor(im,cv2.COLOR_BGR2HSV) #convert color space

        #setting lower and upper bound for green
        g_low_bound = np.array([40,100,5]) 
        g_up_bound = np.array([70,255,255])


        #find colors within range
        mask = cv2.inRange (hsv,g_low_bound,g_up_bound)

        #REMOVING MASK
        #define kernel size
        kern = np.ones((7,7), np.uint8)

        #remove unnecessary noise
        mask = cv2.morphologyEx (mask, cv2.MORPH_CLOSE, kern)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kern)

        #segmenting detected area
        seg_img = cv2.bitwise_and(im, im, mask = mask)

        # Find contours from the mask
        contours, hierarchy = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        output = cv2.drawContours(seg_img, contours, -1, (0, 0, 255), 3)

        # Showing the output
        cv2.imshow("green image", output)
        

    elif choice == "6":
        exit()

        
    else:
        
        print("wrong input try again")
        main_menu()


main_menu()
        
