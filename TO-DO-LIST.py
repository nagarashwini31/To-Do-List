import tkinter as tk
from tkinter import PhotoImage, StringVar, END, ANCHOR

# Initialize main window
root = tk.Tk()
root.title("To-Do-List")
root.geometry("400x650+400+100")
root.resizable(False, False)

task_list = []

def addTask():
    task = task_entry.get()
    task_entry.delete(0, END)

    if task:
        with open("tasklist.txt", 'a') as taskfile:
            taskfile.write(f"{task}\n")
        task_list.append(task)
        listbox.insert(END, task)

def deleteTask():
    global task_list
    task = str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("tasklist.txt", 'w') as taskfile:
            for task in task_list:
                taskfile.write(task + "\n")
        listbox.delete(ANCHOR)

def openTaskFile():
    try:
        global task_list
        with open("tasklist.txt", "r") as taskfile:
            tasks = taskfile.readlines()
        for task in tasks:
            task = task.strip()
            if task:
                task_list.append(task)
                listbox.insert(END, task)
    except FileNotFoundError:
        with open('tasklist.txt', 'w') as file:
            pass

# Load images
try:
    Image_icon = PhotoImage(file="Image/task.png")
    root.iconphoto(False, Image_icon)
except Exception as e:
    print(f"Error loading icon: {e}")

try:
    TopImage = PhotoImage(file="Image/topbar.png")
    tk.Label(root, image=TopImage).pack()
except Exception as e:
    print(f"Error loading top bar image: {e}")

try:
    dockImage = PhotoImage(file="Image/dock.png")
    tk.Label(root, image=dockImage, bg="#32405b").place(x=30, y=25)
except Exception as e:
    print(f"Error loading dock image: {e}")

try:
    noteImage = PhotoImage(file="Image/task.png")
    tk.Label(root, image=noteImage, bg="#32405b").place(x=340, y=25)
except Exception as e:
    print(f"Error loading note image: {e}")

heading = tk.Label(root, text="ALL TASK", font="arial 20 bold", fg="white", bg="#32405b")
heading.place(x=130, y=20)

# Main input area
frame = tk.Frame(root, width=400, height=50, bg="white")
frame.place(x=0, y=180)

task_entry = tk.Entry(frame, width=18, font="arial 20", bd=0)
task_entry.place(x=10, y=7)
task_entry.focus()

add_button = tk.Button(frame, text="ADD", font="arial 20 bold", width=6, bg="#5a95ff", fg="#fff", bd=0, command=addTask)
add_button.place(x=300, y=0)

# Listbox for tasks
frame1 = tk.Frame(root, bd=3, width=700, height=280, bg="#32405b")
frame1.pack(pady=(160, 0))

listbox = tk.Listbox(frame1, font=('arial', 12), width=40, height=16, bg="#324056", fg="white", cursor="hand2", selectbackground="#5a95ff")
listbox.pack(side=tk.LEFT, fill=tk.BOTH, padx=2)

scrollbar = tk.Scrollbar(frame1)
scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

openTaskFile()

# Delete button
try:
    Delete_icon = PhotoImage(file="Image/delete.png")
    tk.Button(root, image=Delete_icon, bd=0, command=deleteTask).pack(side=tk.BOTTOM, pady=13)
except Exception as e:
    print(f"Error loading delete icon: {e}")

root.mainloop()
