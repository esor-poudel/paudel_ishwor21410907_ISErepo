# COVER PAGE FOR ASSESSMENT

    INTRODUCTION TO SOFTWARE ENGINEERING FINAL ASSESSMENT 

    STUDENT NAME : ISHWOR PAUDEL 
    STUDENT ID : 21410907
    PRACTICAL CLASS: WEDNESDAY/ 6-8 PM 

# INTRODUCTION 

This project is to reflect the software enginnering pattern that follow good modularity design pattern, version control and testing of code. It consist of three module i.e Numerical, Generation and Main module that are design to calculate life path number, lucky colour and also to find the generation based on the birth

# Module Description 

Module generally refers to the component of the program for easy replacement. To tackle the problem statement of this project, I am designing the 3 module named Generation Module, Numerology Module and Main module which is described below:

1. ## Numerology module:

    **Module Name**: Numerical.py

    **Description**: This module handle the all the logical part of my program to check **life path number**, **identify master number** , **determining the lucky color based on the life path number** and **finding the lucky color based on the birthday**.

    **Design Decision**: I came to split my all numerical calculation of my project in Numerology module. So if there is changes required in feature of program then checking this module is enough for neccessary update/downgrade.Similarly, it consist of total 4 function named **check_if_mater_number**, **single_digit_number**, **calculate_life_path** and **find_lucky_color**. check_if_mater_number simply check of the number is mater number or not and return boolean value. single_digit_number simply check if the provided number is less than 9 or not if not it split the number and return the sum of the number. this process is continued untill the number is less than 9. At last calculate_life_path simply uses above 2 function for basic operation and calculate the life path number of the user based on thier birthday date and return the number. 

2. ## Generation Module:

    **Module Name** : Generation.py

    **Description** : this module handles to determine the generation of the user based on their birth year. It maps birthyear of the user to generation based on the rule written on the function. 

    **Design Decision**: I came to decide to implement finding the generation of the user in seperate module. This helps me to seperate my program for finding numerical and generation part of the user. I came to assumption that any developer or itself me in the future wants to change the generation logic of the program then it can be done by just editing this module. I implemented **find_user_generation** that takes birthday of the user as input argument and returns the generation of the user based on the rule determine in the function. 

3. ## Main Module:

    **Module Name** : Main.py

    **Description**: This module act as the entry point of the software that integrate all the function written in the above module. It interact with the user to ask user to input birthday and display the calculated result to the user.

    **Design Decision**: the decision to make this module is simple, this module helps to integerate all the function so that in the future it helps developer to integrate module or the function written in other module. It consit of **make_analysation** and **main** functions that interact each other for asking input and displaying the result to the user. 

# Modularity:

## How to Run the Production Code
To run the production code follow the step mentioned below

1. Make sure the python is installed in your local machine ([https://docs.python.org/3/using/windows.html]) **installation Guide for python**
2. Clone the Repository 
3. git clone <repository_url>
3. cd to cloned file 
4. Goto Main.py and type command **python -m main.py**
5. If everything goes right then you will be prompt terminal that ask for birthday 

Modularity simply means "**the quality of consisting of seperate part that, when combined, form a complete whole**". In software engineering this concept can be applied when implementing the actual coding of the project. Instead of writing whole logic in one file, it can be divided into multiple functions and files for ease of reading and maintainance purpose.So, this project consist two directory **code** and **document**. In code directory three main module named **generation.py**, **numerical.py** and **main.py** can be found. the sole purpose of this module is to implement the coding section of the project and implement the logic of the program. In other hand, **document** directory consist of **ishworpaudel_21410907_ISEREPORT.md** file that handles the documentation section of the program. This project tries to implement the key concept of the modularity that are described below briefly:

1. **Single Responsibilty principle:**
Each module performs a single and a well defined task. for example numerical module is only concerned for finding the life path number of the user whereas generation module is concerned for finding the generation of the user. This module are not concerned for validating the user input, prompting display for asking user birthday or providing the result. Main module is concerned with this part and main module is not concerned for numerical part of the program.So, the program follows the single responsibilty principle wisely. 

2. **High Cohesion**:
Each module contains multiple functions and are closely related and work together to acheive the module's goal. for example numerical module contains three functions and at each step this functions work together to break down the birthday and calculating the sum. similarly, at each step they communicate to check if the total is within the mater number [11,22,33] or not. 

3. **Low Coupling:**
Modules interact through well-defined interfaces and they are independent. This allows the freedom to changes in one module without affecting others.for example the change in generation module will not affect the another module that contains the the logic for calulating the life path number. 

4. **Encapsulation**:
In this project only the **private functions and variable** are used. furthermore, module interface are simple and easy to understand. Implementation details are hidden with modules exposing only the necessary interface for the interaction. 

5. **Abstraction:**
This module hides the complexity of the logic to the user and only provide the simple interface to the user. for example, main module contains one simple function make_analysis that analyze the user life path number based on their birthday but the user is hidden what inside the calculation of the number. 

6. **Flexibility and Extensibility:**
This module are designed to easily expand on the future.for example adding new rule on calculation of life path or finding the generation of the user requires minimal changes in the module. 

## Review Checklist 

1. **Implementation**:
- [] Does the code modification achieve its intended purpose?
- [] Is there a way to make this solution more straightforward?
- [] Does this change introduce any unnecessary compile-time or run-time dependencies?
- [] Is there a framework, API, library, or service in use that is inappropriate for this situation?
- [] Would incorporating an additional framework, API, library, or service enhance the solution?
- [] Is the code written at an appropriate level of abstraction?
- [] Is the code sufficiently modular?
- [] Can the solution be improved in terms of maintainability, readability, performance, or security?
- [] Does similar functionality already exist within the codebase, and if so, why isn’t it being reused?
- [] Are there any best practices, design patterns, or language-specific conventions that could significantly enhance this code?





