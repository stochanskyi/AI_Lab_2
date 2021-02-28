from tkinter import *
from first_task import *
from tkmacosx import Button as B


def with_zero_to_one():
    size = size_input.get()
    result_label['text'] = zero_to_one(int(size))


def second_action():
    size = size_input.get()
    set_result(generate_sorted_int_array(-10, 10, int(size)))


def third_action():
    size = size_input.get()
    set_result(generate_sorted_int_array(0, 50, int(size)))


def set_result(result):
    result_label['text'] = result


root = Tk()

root.title("Lab 2")
root.geometry("800x500")

# Task one layout

task_one_frame = Frame(root)
task_one_frame.place(relx=0.05, rely=0.05, relwidth=0.5)

task_one_title = Label(task_one_frame, text='TASK 2', font='Helvetica 14 bold')
task_one_title.pack()

task_one_description = Label(task_one_frame, text='Please select size of array and generation option')
task_one_description.pack()

task_one_size_label = Label(task_one_frame, text='n', fg='grey')
task_one_size_label.pack()
# task_one_size_label.pack(anchor="w")

size_input = Entry(task_one_frame)
size_input.pack()

button_zero_to_one = B(task_one_frame, text='with zero to one', command=with_zero_to_one)
button_zero_to_one.pack()

button_two = B(task_one_frame, text='with -10 to 10', command=second_action)
button_two.pack()

button_three = B(task_one_frame, text='with 0 to 50', command=third_action)
button_three.pack()

result_label = Label(task_one_frame, text='Result will be displayed here')
result_label.pack()

# Task two layout

task_two_frame = Frame(root)
task_two_frame.place(relx=0.5, rely=0.05, relwidth=0.5)

task_two_title = Label(task_two_frame, text='Lab 2', font='Helvetica 14 bold')
task_two_title.pack()

root.mainloop()
