# Infinity and Black Holes
In this exercise, we will be looking at black holes and their behaviour after a long time. You will get to learn about black holes in general, information theory, and basic laws of our universe. You will also get a chance to simulate how our basic laws can be broken at extreme cases.
## Learning Objectives
1. Get acquainted with descriptions of a black hole, its structures and behaviour'
2. Visualize how the black hole changes over time
3. Discuss the information theory, mass conservation laws and enegery conservation laws considering black hole evaporation

## Background Information
Black holes grow by absorbing matter from their surroundings. They 'eat' stars and other bodies that come too close, and as the matter falls into the black hole, it forms an accretion disk around it. The matter in the disk heats up and emits radiation, which can be detected by astronomers. The more matter a black hole absorbs, the bigger it gets and the stronger its gravitational pull becomes. This gravitational pull can be so strong that even light cannot escape from it, which is why black holes are called 'black'.

[Hawking radiation](https://en.wikipedia.org/wiki/Hawking_radiation) is a theoretical form of radiation emitted by black holes. According to the theory, nothing escapes a black hole. Close to the event horizon of a black hole, a local observer must accelerate to keep from falling in. An accelerating observer sees a thermal bath of particles that pop out of the local acceleration horizon, turn around, and free-fall back in. The condition of local thermal equilibrium implies that the consistent extension of this local thermal bath has a finite temperature at infinity, which implies that some of these particles emitted by the horizon are not reabsorbed and become outgoing Hawking radiation
 

Over time, this radiation causes black holes to lose mass and energy, and as a result, they shrink and eventually decay. The rate of decay is dependent on the black hole's mass, with smaller black holes decaying faster than larger ones.
 

It is important to note that the existence of Hawking radiation has not been directly observed, but its effects have been indirectly inferred through observations of black holes and theoretical calculations. The time for the evaporation of a black hole is given by the following equation:
![image](image.png)
## Assignment Description
For this assignment, we will assume that black holes have a good saturation that they do not feed (get larger) and they only emit radiation (and do nothing else.) We will be calculating the necessary time for a set of black holes to decay. We will assume that there exists 5 black holes that have the same mass as the Earth, Jupiter, the Sun, Sagittarius A* (the black hole at the center of our galaxy) and Phoenix A (the most massive black hole ever discovered) This will be more applicable for Task 2. 
```
A fun fact about Phoenix A is that it is twice the size of the Triangulum galaxy and that it has a circumference that would take 71 days and 14 hours to travel at light speed.
```
## Task 1: Mass for Lifeitme of the Universe
This part of the assignment requires you to calculate the mass required for a black hole to have an evaporation of the current age of the universe which is **13.7 billion years** old. You will be required to note this value down and then discuss it with the group afterwards. Start by inverting the equation given so that you can have M as a function of t_ev. You can use logarithms, or just square roots - whichever you prefer. They will result in the same answer.

## Task 2: Reference Values
The assignment steps that you need to reproduce is given below. If you follow these instructions carefully, you should be able to understand how much time it takes for black holes to evaporate.

```
If you are an expert, we assume that you already know the procedure that you have to follow. Therefore, you may disregard the list below. If you are stuck or you are not an expert, follow the procedure described below.
```

1. Start by making a list of all of the mass values. Name this list **mass_values** for further use. This might already be done for you, check your console.
2. Generate a list of time evaporation values called **time_evaporate** and calculate the evaporation time of all of the black holes with the given mass.
3. Scatter plot the results to confirm. These scatter plots should show the time in the x-axis and the mass values on the y-axis, and the results should be increasing as a function of M to the power of 3. This might already be done for you, check your console.

## Task 3: Evaporation Time
This part of the assignment is to re-configure the equation given to you so that you can get the mass of the black hole as a function of evaporation time. This way, you will be able to see the time it takes for a black hole to evaporate and how big the value is. Follow the steps below so you can replicate the results:

```
If you are an expert, we assume that you already know the procedure that you have to follow. Therefore, you may disregard the list below. If you are stuck or you are not an expert, follow the procedure described below.
```

1. Start by inverting the equation given so that you can have M as a function of t_ev. You should already have this from task 1
2. Make a list of time sample values called **time_list**. This list needs to have the following properties:
> The list needs to start from 0, and it needs to end at 10^50 years with equal steps in between.
> The list can be made as a log-scale list (so you would only need to report the values between 0 and 50 and not 10^0 and 10^50)
3. Create a list called **m_age_values** to report all of the values of masses that you get from inverting the equation and using **time_list**
4. Generate a log-log plot of the mass versus the time. What can you infer about the mass, and what can you infer about the evaporation time. This might already be done for you, check your console.