# COVER PAGE FOR ASSESSMENT

    INTRODUCTION TO SOFTWARE ENGINEERING FINAL ASSESSMENT 

    STUDENT NAME : ISHWOR PAUDEL 
    STUDENT ID : 21410907
    PRACTICAL CLASS: WEDNESDAY/ 6-8 PM 

# INTRODUCTION 

This project is to reflect the software enginnering pattern that follow good modularity design pattern, version control and testing of code. It consist of three module i.e Numerical, Generation and Main module that are design to calculate life path number, lucky colour and also to find the generation based on the birth

# Module Description 

Module generally refers to the component of the program for easy replacement. To tackle the problem statement of this project, I am designing the 3 module named Generation Module, Numerology Module and Main module which is described below:

1. Numerology module:

    **Module Name**: Numerical.py

    **Description**: This module handle the all the logical part of my program to check **life path number**, **identify master number** and **determining the lucky color based on the life path number**.

    **Design Decision**: I came to split my all numerical calculation of my project in Numerology module. So if there is changes required in feature of program then checking this module is enough for neccessary update/downgrade.Similarly, it consist of total 3 function named **check_if_mater_number**, **single_digit_number** and **calculate_life_path**. check_if_mater_number simply check of the number is mater number or not and return boolean value. single_digit_number simply check if the provided number is less than 9 or not if not it split the number and return the sum of the number. this process is continued untill the number is less than 9. At last calculate_life_path simply uses above 2 function for basic operation and calculate the life path number of the user based on thier birthday date and return the number. 

    



