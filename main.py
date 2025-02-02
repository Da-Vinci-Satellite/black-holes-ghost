######################### This is the assignment coding section #######################
import matplotlib.pyplot as plt
#Disclaimer
'''If you are not familiar with coding, do not worry. We will help you along
the way so that you can understand what is going on and get familiar with coding
We will also explain the whole code to you along the way so that you do not have to
stress about it.
'''
# Instructions
'''
* If you are a beginner to programming, go to the 'beginner.py' files on the top left section of your computer inside the 'Files' document. You will do the same tasks as the people who already know a bit of coding but we will guide you along the way

* If you are confident with your coding skills, change the coding_experience variable to True and then go to the 'expert.py' file in the 'Files' section of the interface (which will be on the top left corner of your screen)
'''

coding_experience = True  # Change this to True if you know coding

if coding_experience is False:
  import beginner as beg
  plt.close()
  # check for task 1
  checker = input(
    f'Which assignment would you like to check? Enter the NUMBER!:\n')
  try:
    checker_int = int(checker)
  except ValueError:
    print('You need to give a NUMBER ONLY. Do not write Task1 or add spaces!')
  if checker_int == 1:
    print("Calculating")
    print(f'The mass of the black hole required is {beg.m_age()} [kg]')
    print('Task 1 Complete, continue with Task 2')
  if checker_int == 2:
    plt.figure()
    print('Generating the scatter plot')
    fig, ax = plt.subplots(1, 2)
    ax[0].plot(beg.t_ev_mass_values, beg.mass_values)
    ax[0].scatter(
      beg.t_ev_mass_values,
      beg.mass_values,
      color=['#377eb8', '#ff7f00', '#e41a1c', '#984ea3', '#a65628'])
    ax[0].set_title('Mass vs Evaporation Time')
    ax[0].set_xlabel('Evaporation Time [Yrs]')
    ax[0].set_ylabel('Mass in [kg]')
    ax[1].loglog(beg.t_ev_mass_values, beg.mass_values)
    ax[1].scatter(
      beg.t_ev_mass_values,
      beg.mass_values,
      color=['#377eb8', '#ff7f00', '#e41a1c', '#984ea3', '#a65628'])
    ax[1].set_title('Mass vs Evaporation Time Log-Log Plot')
    ax[1].set_xlabel('Log Evaporation Time [Yrs]')
    ax[1].set_ylabel('Log Mass in [kg]')
    plt.subplots_adjust(left=0.1,
                        bottom=0.1,
                        right=0.9,
                        top=0.9,
                        wspace=0.4,
                        hspace=0.4)
    fig.show()
    print('We have plotted the scatter plot; now we can move to Task 3')
  if checker_int == 3:
    plt.figure()
    fig, ax = plt.subplots(1, 2)
    ax[0].plot(beg.time_list,
               beg.m_age_values,
               color='red',
               label='Your Values')
    ax[0].vlines(beg.current_age,
                 ymin=min(beg.m_age_values),
                 ymax=max(beg.m_age_values),
                 label='Current age of Universe',
                 color='blue',
                 linestyle='--')
    ax[0].set_title('Mass vs Evaporation Time')
    ax[0].set_xlabel('Log Evaporation Time [Yrs]')
    ax[0].set_ylabel('Log Mass in [kg]')
    ax[0].legend()
    ax[1].loglog(beg.time_list,
                 beg.m_age_values,
                 color='red',
                 label='Your Values')
    ax[1].vlines(beg.current_age,
                 ymin=min(beg.m_age_values),
                 ymax=max(beg.m_age_values),
                 label='Current age of Universe',
                 color='blue',
                 linestyle='--')
    ax[1].set_title('Mass vs Evaporation Time Log-Log Plot')
    ax[1].set_xlabel('Log Evaporation Time [Yrs]')
    ax[1].set_ylabel('Log Mass in [kg]')
    ax[1].legend()
    plt.subplots_adjust(left=0.1,
                        bottom=0.1,
                        right=0.9,
                        top=0.9,
                        wspace=0.4,
                        hspace=0.4)
    fig.show()
else:
  import expert as ex
  plt.close()
  # check for task
  '''
  This has been left blank for you to complete. If you find it convenient     you can just copy and paste the code from the beginner section of the main
  to automate the process.
  '''
