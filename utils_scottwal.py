"""
Module: beginnng_case

Purpose: Reusable Module for My Analytics Projects

Description: This module provides a byline for my analytics projects. 
When we work hard to write useful code, we want it to be reusable.
A good byline could be used in every Python analytics project we do.
While the example here used fictional dogs, this template can be modified
and used to complete many Analytics projects, so sayeth Professor Case!

Author: Scott Wal

TODO: Change the module name in this opening docstring
TODO: Change the author in this opening docstring
"""

#####################################
# Import Modules
#####################################

# Import helpful modules from the Python Standard library
# See more at: https://docs.python.org/3/library/

import statistics  # provides mean(), stdev() and more....

#####################################
# Declare Global Variables
#####################################

# declare a boolean variable (has a value True or False)
# TODO: Add another or replace this with your own boolean variable
is_dog_green: bool = True

# declare an integer variable 
# TODO: Add or replace this with your own integer variable
age_of_dog: int = 55

# declare a floating point variable
# TODO: Add or replace this with your own floating point variable
average_dog_age: float = 45.7

# declare a list of strings
# TODO: Add or replace this with your own list  
dog_types: list = ["Three-Legged", "Two-Legged", "One-Legged"]

# declare a list of numbers so we can illustrate statistics skills
# TODO: Add or replace this with your own numeric list  
dog_weights_in_kg: list = [98.5, 101.5, 15.6, 150.0, 2.3]

# Calculate basic statistics using built-in Python functions and the statistics module
# TODO: Replace these variable names with the variable name of your own numeric list DID WITH STEP 7 BYLINE UPDATE
min_weight: float = min(dog_weights_in_kg)  
max_weight: float = max(dog_weights_in_kg)  
mean_weight: float = statistics.mean(dog_weights_in_kg)  
stdev_weight: float = statistics.stdev(dog_weights_in_kg)

# Use a Python formatted string (f-string) to show information
# TODO: Modify the text in the byline to fit your information
# TODO: Modify the variables in the byline to use your variable names
byline: str = f"""
---------------------------------------------------------
Stellar Analytics: Delivering Professional Insights
---------------------------------------------------------
Is dog green:  {is_dog_green}
Age of Dog:         {age_of_dog}
Dog Type:             {dog_types}
Weight of Dog: {dog_weights_in_kg}
Minimum Dog Weight: {min_weight}
Maximum Dog Weight: {max_weight}
Mean Dog Weight: {mean_weight:.2f}
Standard Deviation of Dog Weight: {stdev_weight:.2f}
"""

#####################################
# Define global functions (resuable instructions)
#####################################

def get_byline() -> str:
    '''
    Get a byline for my analytics projects.
       
    Returns a string byline that illustrates my specific skills.

    A function is a block of code that performs a task.
    This function just returns our byline.
    We can call this (or other functions) in later modules 
    so we can write it once and reuse it. 
    We use a type hint to indicate this function returns a string
    (that is, it has a Python type of str).
    It doesn't need any additional information passed in, 
    so there's nothing needed inside the parentheses.
    Everything afer the colon must be indented consistently (usually 4 spaces)
    '''
    return byline

#####################################
# Define main function for this module.
#####################################

def main() -> None:
    '''
    Print results of get_byline() when main() is called.

    This function just prints the byline to the console when we run this as a script.
    The type hint indicates this function doesn't return anything when called 
    (that is, it has a Python type of None).
    It doesn't need any additional information passed in, 
    so there's nothing inside the parentheses.
    Everything afer the colon must be indented consistently (usually 4 spaces)
    '''

    print("Starting........")
    print(get_byline())
    print("Complete.......")

#####################################
# Conditional Execution
#####################################

# If we are running this file as a script then call main()
# and verify our code works as expected.

if __name__ == '__main__':
    main()

#TODO: Run this as a script and verify all code works as intended.
