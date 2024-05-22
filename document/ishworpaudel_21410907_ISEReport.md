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

# Review Checklist 

## Implementation
### Functionality:
- Does the life path calculation correctly sum and reduce the digits of the day, month, and year of birth?
- Does the code correctly identify master numbers (11, 22, 33) and avoid reducing them further?
- Does the generation determination function correctly classify the birth year into the appropriate generation?
### Simplification:
- Can the life path calculation logic be simplified?
- Can the generation determination logic be simplified?
### Dependencies:
- Does the code rely only on necessary libraries and frameworks?
- Could any additional frameworks, APIs, libraries, or services improve the solution?
### Abstraction and Modularity:
- Are the life path calculation and generation determination functions clearly separated?
- Is the code at the right abstraction level, avoiding unnecessary complexity?
- Is the code modular enough, with each function having a single responsibility?
## Logic Errors and Bugs
### Correctness:
- Can you think of any use case in which the life path calculation does not behave as intended?
- Can you think of any inputs or external events that could break the generation determination?
## Error Handling and Logging
### Error Handling:
- Is error handling done correctly for invalid date formats?
- Are error messages user-friendly and informative?
### Logging:
- Should any logging or debugging information be added or removed?
- Are there sufficient log events for easy debugging?
## Dependencies
### Documentation:
- Were updates to documentation, configuration, or readme files made as required by this change?
### Compatibility:
- Are there any potential impacts on other parts of the system or backward compatibility?
## Security and Data Privacy
### Vulnerabilities:
- Does the code introduce any security vulnerabilities related to user input?
- Is user input validated, sanitized, and escaped to prevent security attacks?
### Sensitive Data:
- Is sensitive data handled and stored securely?
## Performance
### Impact:
- Does the life path calculation and generation determination code perform efficiently?
- Is there potential to significantly improve performance?
## Usability and Accessibility
### Design:
- Is the proposed solution well-designed from a usability perspective?
- Is the code well-documented and easy to understand?
## Testing and Testability
### Coverage:
- Is the life path calculation and generation determination code testable?
- Have automated tests been added or updated to cover these functions?
- Do the existing tests reasonably cover the code change (unit/integration/system tests)?
- Are there some test cases, input, or edge cases that should be tested in addition?
## Readability
### Understandability:
- Is the code easy to understand, especially the life path calculation and generation determination logic?
- Which parts were confusing and why?
## Improvement:
- Can the readability of the code be improved by smaller methods or better names for functions and variables?
- Is the code located in the right file/folder/package?
- Do you think certain methods should be restructured for more intuitive control flow?
- Is the data flow understandable?
## Comments:
- Are there redundant or outdated comments?
- Could some comments convey the message better?
- Would more comments make the code more understandable?
- Could some comments be removed by making the code itself more readable?
## Dead Code:
- Is there any commented-out code?

# Test Design

1. ## Black Box Testing

### Equivalence Partitioning
Equivalence Partitioning is the technique of dividing the input data into partitions of equivalent data from which test cases can be derived. For this program, for each module test design based on equivalence partitioning are done which are described below.

### Boundary Value Analysis 
Boundary value analysis involves creating test cases that focus on the boundaries of the input partitions. For this test design technique generation module will be used which is also described below.

## Module : "validate_user_birthday"
**Equivalence Partitioning**

1. Valid date in correct format: "12/25/1990"
2. Invalid format (missing slashes): "12251990"
3. Invalid format (wrong order): "1990/12/25"
4. Non-numeric input: "ab/cd/efgh"
5. Valid date with single digits: "1/1/2000"

**Boundary Value Analysis:**

1. Date with minimal valid length: "01/01/1900"
2. Date with maximal valid length: "12/31/2099"
3. Date less than year 1901 : "11/04/1800"
4. Date more than year 2024 : "08/08/2029"

## Module : "calculate_life_path"
**Equivalence Partitioning**

1. Birthday with no master numbers: "02/03/1987" (Life Path Number: 3)
2. Birthday with master number in day: "11/15/1980" (Life Path Number: 8)
3. Birthday with master number in month: "12/11/2000" (Life Path Number: 7)
4. Birthday with master number in year: "03/03/2009" (Life Path Number: 8)
5. Birthday with master numbers in day and month: "11/11/2020" (Life Path Number: 8)

## Module: "check_if_mater_number"
**Equivalence Partitioning:**

1. Non-master number: 4 (returns False)
2. Master number: 11 (return True)
3. Borderline non-master number: 10 (return False)
4. Borderline non-master number: 12 (return False)

## Module: "find_lucky_color"
**Equivalence Partitioning:**

1. Valid life path number: 3 (Yellow)
2. Valid life path number: 8 (Magenta)
3. Invalid life path number: 0 (Unknown)
4. Invalid life path number: 100 (Unknown)

## Module: "find_user_generation"
**Equivalence Partitioning:**

1. Year within Silent Generation: 1935
2. Year within Baby Boomer: 1955
3. Year within Generation X: 1975
4. Year within Millennial: 1990
5. Year within Generation Z: 2005
6. Year within Generation Alpha: 2020
7. Year outside defined generations: 1900

**Boundary Value Analysis:**

1. First year of Silent Generation: 1928
2. Last year of Silent Generation: 1945
3. First year of Baby Boomer: 1946
4. Last year of Baby Boomer: 1964
5. First year of Generation X: 1965
6. Last year of Generation X: 1980
7. First year of Millennial: 1981
8. Last year of Millennial: 1996
9. First year of Generation Z: 1997
10. Last year of Generation Z: 2012
11. First year of Generation Alpha: 2013
12. Last year of Generation Alpha: 2025

## Test case design Table is Given below**

#### Module: `validate_user_birthday`

**Category: Valid Date Format**

| Category      | Test Data    | Expected Result |
|---------------|--------------|-----------------|
| Valid Format  | "12/25/1990" | True            |
| Valid Format  | "01/01/2000" | True            |

**Category: Invalid Date Format**

| Category       | Test Data    | Expected Result |
|----------------|--------------|-----------------|
| Missing Slashes| "12251990"   | False           |
| Wrong Order    | "1990/12/25" | False           |
| Non-Numeric    | "ab/cd/efgh" | False           |

#### Module: `calculate_life_path`

**Category: Birthdays with No Master Numbers**

| Category          | Test Data    | Expected Result |
|-------------------|--------------|-----------------|
| No Master Numbers | "02/03/1990" | 6               |
| No Master Numbers | "01/01/2000" | 4               |

**Category: Birthdays with Master Numbers**

| Category                       | Test Data    | Expected Result |
|--------------------------------|--------------|-----------------|
| Master Number in Day           | "11/15/1980" | 8               |
| Master Number in Month         | "12/11/2000" | 7               |
| Master Number in Year          | "03/03/1922" | 1               |
| Master Numbers in Day and Month| "11/11/2020" | 6               |

**Category: Boundary Dates**

| Category           | Test Data    | Expected Result |
|--------------------|--------------|-----------------|
| First Day of the Year | "01/01/2000" | 4           |
| Last Day of the Year  | "12/31/2000" | 1           |

#### Module: `check_if_mater_number`

**Category: Non-Master Numbers**

| Category     | Test Data | Expected Result |
|--------------|-----------|-----------------|
| Non-Master   | 4         | False           |
| Non-Master   | 10        | False           |
| Non-Master   | 12        | False           |

**Category: Master Numbers**

| Category     | Test Data | Expected Result |
|--------------|-----------|-----------------|
| Master       | 11        | True            |
| Master       | 22        | True            |
| Master       | 33        | True            |

#### Module: `find_lucky_color`

**Category: Valid Life Path Numbers**

| Category         | Test Data | Expected Result |
|------------------|-----------|-----------------|
| Valid Life Path  | 3         | "Yellow"        |
| Valid Life Path  | 11        | "Silver"        |

**Category: Invalid Life Path Numbers**

| Category           | Test Data | Expected Result |
|--------------------|-----------|-----------------|
| Invalid Life Path  | 0         | "Unknown"       |
| Invalid Life Path  | 100       | "Unknown"       |

#### Module: `find_user_generation`

**Category: Valid Generations**

| Category           | Test Data | Expected Result      |
|--------------------|-----------|----------------------|
| Silent Generation  | 1935      | "Silent Generation"  |
| Baby Boomer        | 1955      | "Baby Boomer"        |
| Generation X       | 1975      | "Generation X"       |
| Millennial         | 1990      | "Millennial"         |
| Generation Z       | 2005      | "Generation Z"       |
| Generation Alpha   | 2020      | "Generation Alpha"   |

**Category: Invalid Generations**

| Category            | Test Data | Expected Result     |
|---------------------|-----------|---------------------|
| Year Outside Range  | 1900      | "Unknown Generation"|

**Category: Boundary Years**

| Boundary                       | Test Data | Expected Result      |
|--------------------------------|-----------|----------------------|
| Between [1901-1945]            | 1928     | "Silent Generation"  |
| Between [1946-1964]            | 1946     | "Baby Boomer"        |
| Between [1965-1979]            | 1975     | "Generation X"       |
| Between [1980-1994]            | 1985     | "Millennial"         |
| Between [1995-2009]            | 2005     | "Generation Z"       |
| Between [2010-2024]            | 2021     | "Generation Alpha"   |

#### Module: `single_digit_number`

| Category           | Test Data | Expected Result      |
|--------------------|-----------|----------------------|
| 0 > sum > 9        | 7         | return 7             |
| sum > 9            | 23        | return 2+3 = 5       |
| sum = 11,22,33     | 22        | return 22            |


2. ## White Box Testing 

**Module: `Validate_user_birthday`**


| Path                                             | Test Data       | Expected Result      |
|--------------------------------------------------|-----------------|----------------------|
| Enters in for and  if statement                  | 20/20/2020      | return True          |
| Enters in else part                              | 20202020        | return False         |
| Enter in another IF for checking length          | 20/20           | return False         |
| Enter in IF statement for checking digit         | ee/ff/abcd      | return False         |
| Enter in IF statement for validating year        | 20/10/1800      | return False         |


**Module: `calculate_life_path`**


| Path                                             | Test Data                       | Expected Result                            |
|--------------------------------------------------|---------------------------------|--------------------------------------------|
| map the user input to three variables            | day=20 month=05 year =1990      | goto function single_digit_number          |
| check for master number                          | day=11 month=05 year =1990      | return True                                |
| check the single digit number                    | day=12                          | return False and give sum of 1+2 =         |


**Module: `find_lucky_color`**


| Path                                             | Test Data       | Expected Result      |
|--------------------------------------------------|-----------------|----------------------|
| map the color with corresponding key value pair  | 1:Red           | return Red           |
| Get the life path number                         | 3               | return Yellow        |


**Module: `find_user_generation`**


| Path                                             | Test Data                    | Expected Result                            |
|--------------------------------------------------|------------------------------|--------------------------------------------|
| Enter into for loop                              | year = 1800                  | return Unknown                             |
| Enter into if statement                          | year= 1995                   | return Generation Z                        |


# Test Implementation and Test Execution

Testing the code plays important role to check if all the function works as expected as the user want before the code is sent for the live. So for this project a test file is created to check all the function work as expected or not. To run the test file simply go to the `test.py` file and run the code (**python test.py**)


