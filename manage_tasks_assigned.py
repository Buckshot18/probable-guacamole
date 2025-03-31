'''Capstone project'''

'''Import date and time and import os'''
from datetime import date, datetime
import os

'''Reads Users information from the file which contains usernames and 
passwords.
Store item in to lists named list_of_usernames and list_of_passwords.
Users.txt file'''
credentials = []
user_file = open("user.txt", "r")
for line in user_file:
    line_without_whitespaces = line.strip("\n")
    split_line_into_list = line_without_whitespaces.split(", ")
    credentials.append(split_line_into_list)

list_of_usernames = []
list_of_passwords = []

for item in credentials:
    temp_username = item[0]
    temp_password = item[1]
    
    list_of_usernames.append(temp_username)
    list_of_passwords.append(temp_password)

'''Opens and read file and remove spaces from the line of information   
Tasks.txt file'''
tasks = []
with open("tasks.txt", "r") as task_file:
    for line in task_file:
        remove_whitespaces = line.replace(" ", "")
        tasks.append(line.strip().split(", "))
        

def reg_user():
    '''Display a header to let the user know what they are about to do'''
    print("***Register new user***")

    new_username = input("Please enter a new username: ")
    '''User inputs a new username'''
    while new_username in list_of_usernames:
        '''If username already exists the user is notified and asked to 
        enter a username again'''
        print("***Username already exists. Try again please***")
        new_username = input("Please enter a new username: ")
            
    new_password = input("Please enter your password: ")
    '''User inputs a new password'''    
    confirm_password = input("Confirm password: ")
    '''Ask user to confirm their password if it does not match to their 
    previous entry they will be prompted to re enter the confirmation of 
    password'''
    while confirm_password != new_password:
        print("Passwords don't match")
        confirm_password = input("Confirm password: ")
        
    print("New user added")
    '''Show a message to confirm that user is added'''
    with open("user.txt", "a") as file:
            file.write(f"\n{new_username}, {new_password}")
            list_of_usernames.append(new_username)
            list_of_passwords.append(new_password)
    '''New user information is added and saved in user.txt'''
    
def add_task():
    assign_user_to_task = input("Enter username to assign the new task: ")
    title_of_task = input("Enter title of the task: ")
    description_of_task = input("Enter description of task: ")
    due_date = input("Enter due date for task: ")
    current_date = date.today()
    task_finished = "No"
    '''Ask user for the information about the task they want to ad'''

    with open("tasks.txt", "a") as file:
        file.write(
            f"\n{assign_user_to_task}, {title_of_task}, {description_of_task},"
            f" {due_date}, {current_date}, {task_finished}")
        '''Open the file and append the information to be saved in 
        tasks.txt file'''
            
        print("***Task added to list***\n")
        '''Confirmation to th user that task is added'''
    
def view_all_and_my_tasks():
    tasks = []
    '''Stored tasks that is read from tasks.txt file'''
    task_index = 0
    '''Acts as a counter to keep track of the number of tasks when they 
    are displayed'''

    if menu == 'va':
        print("***All tasks***")
    else:
        print("***Overview of your tasks***")
    '''If user chooses 'va' prints "***All tasks***" else it will print 
    "***All tasks***" '''
    
    '''Read tasks from the file'''
    with open("tasks.txt", "r") as tasks_file:
        for line in tasks_file:
            contents_list = line.strip().split(", ")
            tasks.append(contents_list)
    '''Reads each line (representing a task) from the file.
    splits the line into a list of task attributes and then appends the 
    task (as a list) to the tasks list.'''

    for task in tasks:
        task_index += 1
        (assigned_user, title_of_task, description_of_task, due_date, 
         current_date, task_finished) = task
        '''loop through the tasks
        assigned_user: The user assigned to the task.
        title_of_task: The title of the task.
        description_of_task: The description of the task.
        due_date: The due date of the task.
        current_date: The date the task was assigned.
        task_finished: Whether the task is complete Yes or No'''

        if menu == 'vm' and entered_username == assigned_user:
            print(f"Task {task_index}:\t\t\t{title_of_task}")
            print(f"Assigned to: \t\t{assigned_user}")
            print(f"Date assigned: \t\t{current_date}")
            print(f"Due date: \t\t{due_date}")
            print(f"Task Complete? \t\t{task_finished}")
            print(f"Task Description: \t{description_of_task}\n")
        elif menu != 'vm':
            print(f"Task {task_index}: \t\t{title_of_task}")
            print(f"Assigned to: \t\t{assigned_user}")
            print(f"Date assigned: \t\t{current_date}")
            print(f"Due date: \t\t{due_date}")
            print(f"Task Complete? \t\t{task_finished}")
            print(f"Task Description: \t{description_of_task}\n")
            '''if the user chose vm the tasks assigned to the user 
            will print for the user to overview
            If the user chose va it will print all the tasks with their 
            information '''

    '''Selecting a specific task or returning to the main menu'''
    selected_task = int(input("Select a task by number or enter '-1' to "
                              "return to the main menu: "))
    
    if selected_task == -1:
        return
    '''If user enters -1 it returns to the menu'''
    
    task = tasks[selected_task - 1]
    (assigned_user, title_of_task, description_of_task, due_date, current_date, 
     task_finished) = task
    '''Retrieves the selected task from the tasks list
    task is splitted into variables'''

    action = input("Enter 'm' to mark the task as complete, 'e' to edit the "
                   "task, or any other key to return: ")
    '''user is asked to "m" mark it as finished or "e" to edit task 
    information'''
    
    if action == 'm':
        task_finished = "Yes"
        task[5] = task_finished
        print("Task marked as complete.\n")
        '''if user chose m the task will update task_finished to "Yes" 
        list will update in tasks '''
    
    elif action == 'e' and task_finished != "Yes":
        edit_choice = input("Enter 'u' to edit assigned user or 'd' to edit "
                            "due date: ")
        '''user can chose e but only if the task is not completed
        task info is updated in the tasks list'''
        
        if edit_choice == 'u':
            new_user = input("Enter new assigned user: ")
            task[0] = new_user
            print("Assigned user updated.\n")
            '''user chose u to chance a assigned user, task info is 
            updated in the tasks list'''
        
        elif edit_choice == 'd':
            new_due_date = input("Enter new due date: ")
            task[3] = new_due_date
            print("Due date updated.\n")
            '''user chose d to change the due date, task info is updated
            in the task list'''
        else:
            print("Invalid choice.\n")
            '''if user inputs something else this message will let them 
            know'''
    
    '''Save the updated tasks to the file'''
    with open("tasks.txt", "w") as tasks_file:
        for task in tasks:
            tasks_file.write(", ".join(task) + "\n")

def generate_reports():
    '''Function to convert the date'''
    def convert_date(date_str):
        return datetime.strptime(date_str, '%d %b %Y').date()
    '''helps to convert the string to a date object 
    https://www.geeksforgeeks.org/python-convert-string-to-datetime-and-
    vice-versa/'''
    
    with open("task_overview.txt", "w") as task_overview_file:
        total_tasks = len(tasks)
        completed_tasks = sum(1 for task in tasks if task[5].lower() == "yes")
        uncompleted_tasks = total_tasks - completed_tasks
        overdue_tasks = sum(1 for task in tasks if task[5].lower() != 
                            "yes" and convert_date(task[3]) < date.today())
        percentage_incomplete = ((uncompleted_tasks / total_tasks) * 100 if 
                                 total_tasks > 0 else 0)
        percentage_overdue = ((overdue_tasks / total_tasks) * 100 if 
                              total_tasks > 0 else 0)
        '''statistics calculation of tasks
        total_tasks: Total number of tasks.
        completed_tasks: Number of tasks marked as complete.
        uncompleted_tasks: Number of tasks not yet completed.
        overdue_tasks: Number of incomplete tasks with a due date 
        earlier than today.
        percentage_incomplete: Percentage of incomplete tasks.
        percentage_overdue: Percentage of overdue tasks.'''
        
        task_overview_file.write("Task Overview\n")
        task_overview_file.write(f"Total tasks: {total_tasks}\n")
        task_overview_file.write(f"Completed tasks: {completed_tasks}\n")
        task_overview_file.write(f"Uncompleted tasks: {uncompleted_tasks}\n")
        task_overview_file.write(f"Overdue tasks: {overdue_tasks}\n")
        task_overview_file.write(
            f"Percentage incomplete: {percentage_incomplete:.2f}%\n")
        task_overview_file.write(
            f"Percentage overdue: {percentage_overdue:.2f}%\n")
        '''writes statistics to task_overview.txt'''
        
    with open("user_overview.txt", "w") as user_overview_file:
        total_users = len(list_of_usernames)
       
        user_overview_file.write("User Overview\n")
        user_overview_file.write(f"Total users: {total_users}\n")
        user_overview_file.write(f"Total tasks: {total_tasks}\n")
        '''finds the total numbers of users and tasks'''
        
        for username in list_of_usernames:
            user_tasks = [task for task in tasks if task[0] == username]
            user_total_tasks = len(user_tasks)
            user_percentage_total_tasks = ((user_total_tasks / total_tasks) * 
                                           100 if total_tasks > 0 else 0)
            user_completed_tasks = sum(1 for task in user_tasks if 
                                       task[5].lower() == "yes")
            user_percentage_completed_tasks = ((user_completed_tasks / 
                        user_total_tasks) * 100 if user_total_tasks > 0 else 0)
            user_uncompleted_tasks = user_total_tasks - user_completed_tasks
            user_percentage_uncompleted_tasks = ((user_uncompleted_tasks / 
                        user_total_tasks) * 100 if user_total_tasks > 0 else 0)
            user_overdue_tasks = sum(1 for task in user_tasks if task[5].lower(
                        ) != "yes" and convert_date(task[3]) < date.today())
            user_percentage_overdue_tasks = ((user_overdue_tasks / 
                        user_total_tasks) * 100 if user_total_tasks > 0 else 0)
            '''Calculate the statistics of users
            user_tasks: Tasks assigned to the user.
            user_total_tasks: Total tasks assigned to the user.
            user_percentage_total_tasks: Percentage of total tasks assigned to the user.
            user_completed_tasks: Number of completed tasks for the user.
            user_percentage_completed_tasks: Percentage of completed tasks for the user.
            user_uncompleted_tasks: Number of incomplete tasks for the user.
            user_percentage_uncompleted_tasks: Percentage of incomplete tasks for the user.
            user_overdue_tasks: Number of overdue tasks for the user.
            user_percentage_overdue_tasks: Percentage of overdue tasks for the user.'''
            
            user_overview_file.write(f"\nUsername: {username}\n")
            user_overview_file.write(f"Total tasks: {user_total_tasks}\n")
            user_overview_file.write(
                f"Percentage of total tasks: {user_percentage_total_tasks:.2f}%\n")
            user_overview_file.write(
                f"Percentage completed: {user_percentage_completed_tasks:.2f}%\n")
            user_overview_file.write(
                f"Percentage uncompleted: {user_percentage_uncompleted_tasks:.2f}%\n")
            user_overview_file.write(
                f"Percentage overdue: {user_percentage_overdue_tasks:.2f}%\n")
            '''write the statistic for each user to a file 
            user_overview.txt'''
            
    print("***Reports generated successfully! Check the task_overview.txt and "
          "user_overview.txt files.***")
    '''lets the user know that the reports has been generated'''

def statistics():
    '''Generate reports if the files do not exist'''
    if not os.path.exists("task_overview.txt") or not os.path.exists(
        "user_overview.txt"):
        generate_reports()
    
    '''Display task overview statistics'''
    with open("task_overview.txt", "r") as task_overview_file:
        for line in task_overview_file:
            print(f"{line.strip()}")
    print()
    '''Display user overview statistics'''
    with open("user_overview.txt", "r") as user_overview_file:
        for line in user_overview_file:
            print(f"{line.strip()}")
    print() 

'''====Login Section===='''
'''Users receive prompts to enter their information to log in, then 
confirms the information with the lists, if the entered information 
matches then they are granted with entry if not they receive a prompt 
message to try again from the start.'''                       
print("*********Login**********") 
while True:

    entered_username = input("Enter username: ")        
    entered_password = input("Enter password: ")
    
    if entered_username in list_of_usernames:
        index_of_user = -1
        for i in range(0, len(list_of_usernames)):
            if list_of_usernames[i] == entered_username:
                index_of_user = i 
            
        if entered_password == list_of_passwords[index_of_user]:
            print("***Login successful***")
            break
        else:
            print("***Login unsuccessful, wrong username or password."
                  " Please try again.***")
 
'''Presents the menu for the user with the available options. option 
r, ds and gr is locked to admin only.
The menu will display after every desired task is complete until e is
entered.'''
menu = ""
while menu != "e":
    menu = input('''Select one of the following options:
r -\t register a user (Admins only)
a -\t add task
va -\t view all tasks
vm -\t view my tasks
gr - \t generate reports (Admins only)
ds - \t statistics (Admins only)
e - \t exit
: ''').lower().strip()
    
    if menu == 'r' and entered_username == "admin":
        reg_user()
        '''reg_user function is called by user input 'r' only for admins'''
               
    elif menu == 'a':
        add_task()
        '''add_task function is called by users input 'a' '''

    elif menu == 'va' or menu == 'vm':
        view_all_and_my_tasks()
        '''view_all_and_my_tasks can be called by va and vm both these 
        options is integrated into the function '''
        
    elif menu == 'gr' and entered_username == "admin":
        generate_reports()
        '''generate_reports is called by users input 'gr' only admins'''
        
    elif menu == 'ds' and entered_username == "admin":
        statistics()
        '''statistics is called by users input 'ds' only admins'''
        
    elif menu == 'e':
       print("***Goodbye***")
       '''if user inputs 'e' the program exits'''
    
    else: 
        print("***Invalid input. Please try again***")
        
'''Close all open documents''' 
user_file.close()
task_file.close()        
