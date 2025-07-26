from datetime import datetime

#function to read tasks from tasks.txt
def read_tasks(file_path):
    tasks = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                if '|' in line:  # check if the line is formatted properly with |
                    title, date_str = line.strip().split('|') #This removes spaces and splits the title and date into cleaner formats
                    title = title.strip() #remove spaces from title and below from dates
                    date_str = date_str.strip()
                    tasks.append((title, date_str)) #saves the title and dates into a list
    except FileNotFoundError:
        print(f"File {file_path} not found.")
    return tasks


#Checking if the function reads all tasks correctly

    '''if __name__ == "__main__":
    tasks = read_tasks('tasks.txt')
    print(tasks) '''

#Filter tasks for today
def filter_tasks_for_today(tasks):
    today = datetime.now().date().isoformat()
    return [task for task in tasks if task[1] == today] #we loop throuch each task and check if the date matches today's date (2nd item in the tuple), if it does we return that task.

#Function to display today's tasks
def display_tasks(tasks):
    today = datetime.now().date() # Get today's date

    if not tasks:
        print(f"\n+---------------------------------------------------------+")
        print(f"|           No tasks for today({today}).           |") # If there are no tasks for today, we print this message
        print(f"+---------------------------------------------------------+")
        return
    print(f"\n+---------------------------------------------------------+")
    print(f"|            Tasks for today ({today}):                |") #date will be displayed with the sentence
    print(f"+---------------------------------------------------------+")

    for index, (title, date) in enumerate(tasks, start=1): #loop through each task and automatically number the tasks starting from 1, giving it an index
        print(f"  {index}. {title}") 
        print(f"  🔔 Reminder sent for task: {title} on {date}") #this would be where a reminder will be stimulated, in a real application this would be where you send an email or notification
        print(f"+---------------------------------------------------------+")

#Run the reminder

if __name__ == "__main__":  #Although i can run the below code without the main block, it is a good practise to use the python structure and ensures that the code only runs when the script is executed directly, not when imported as a module.
    tasks = read_tasks('tasks.txt')
    today_tasks = filter_tasks_for_today(tasks)
    display_tasks(today_tasks)

    #Ive used a simple box style formatting to make the output more visually appealing and easier to read.