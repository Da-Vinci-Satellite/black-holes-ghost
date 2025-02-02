######################### This is the assignment coding section.
import numpy as np

'''
Structure Explanation

For each of the tasks, you will receive an explanation on what every variable does and how to
operate with them and why they are used. Also, you will be getting hints along the way on how to
Do the coding yourself.

Most of the work will be already done for you, and this exercise will be like a puzzle
where you would only have to change some code.

All of the code that you are expected to change will be indicated in triple quotation marks like this one! CHANGE THIS!
'''

##########################################

########## This is the task 1 ############

##########################################

# Variables
task1_value = -1 # This is the value that we should be changing in the code automatically
current_age = 1.37e+10 # This is the current age of the universe
pi  = np.pi # This is the pi constant that is used in all equations
G  = 6.67430e-11 # This is the universal gravitational constant.
c = 299792458 # Speed of light in [m/s]
h_reduced = 6.582119569e-16 # This is the reduced plank constant given by h bar

# Functions For Mass with Time
def m_age(t_ev=current_age): #
  '''
  This is a function that will allow you to calculate required mass 
  How it works is that you change the value as you see in the equation and then you are all set
  Whenever you run the code, you should be able to see your result here
  If want to write exponents, do variable**(exponent)
  If you want to multiply, you have to use the asterisk sign *
  The place where you want to use evaporation time, type t_ev
  '''
  task1_value = '''! CHANGE THIS !'''
  return task1_value

##########################################

########## This is the task 2 ############

##########################################
# Mass Values Needed
mass_earth = 5.972e+24 # This is the mass of the Earth in kilograms
mass_jupiter = 1.898e+27 # This is the mass of the Jupiter in kg
mass_sun = 1.989e+30 # This is the mass of the Sun in kg
mass_sagA = 8.26e+36 # This is the mass of the Sagittarius A* in kg
mass_phoA = mass_sun * 100e+6 # This is the mass of the largest known black hole, in kg

# List of masses
'''
Lists are a list of values that you can immediately access and manipulate.
Python is weird, and it starts counting from 0. So if you wanted to access the value of
In the list below for Earth, you would have to call mass_values[0]
'''
mass_values = [mass_earth, mass_jupiter, mass_sun, mass_sagA, mass_phoA] #This is a list of the values of the masses

# Function for Evaporation time
def t_evaporate(mass):
  # How it works is that you change the the code so that you have the evaporation time       equation here
  # Whenever you run the code, you should be able to see your result here
  # If want to write exponents, do variable**(exponent)
  # If you want to multiply, you have to use the asterisk sign *
  # The place where you want to use evaporation time, type t_ev
  return '''! CHANGE THIS !'''

'''
A loop is just an iterative (so it does the same for all of the things inside one range of values) process. In python, you can use loops to apply a formula to a number in a list so that you can convert all of the list to another set of values

This is done with the for i in (condition): marker in the code. We mark i as the placeholder number where the code will understand what to iterate over. We usually loop over a list of values by not indicating the place of the value we want to change but instead putting the placeholder i wherever you would normally try to access the value.


So, instead of writing mass_values[0], mass_values[1],... to get the values, we will use a for loop with placeholder i  as mass_values[i] and let Python change the i value automatically.
'''
t_ev_mass_values = []
# Looping through the list of mass values to calculate the evaporation times
for i in range(len(mass_values)):
  time = '''! CHANGE THIS !'''
  t_ev_mass_values.append(time)

# The plotting will be done automatically once you press RUN

##########################################

########## This is the task 3 ############

##########################################
# Now that you have a function called m_age, you can make use of it for this task!

# Making a list of time sample values
time_list = '''! CHANGE THIS!''' # Hint: Look at np.arange and how to use it
m_age_values = '''! CHANGE THIS! ''' # Hint: you can use m_age and time_list for this


'''Plotting for Task 3 is done automatically for you.'''
