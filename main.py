from tkinter import *
from first_task import *
from second_task import *
from tkmacosx import Button as MacosButton


def task_1_action_1():
    size = size_input.get()
    generated_array = float_array(0, 1, int(size))
    generated_array_label['text'] = generated_array
    set_first_task_result(sort_array(generated_array))


def task_1_action_2():
    size = size_input.get()
    generated_array = int_array(-10, 10, int(size))
    generated_array_label['text'] = generated_array
    set_first_task_result(sort_array(generated_array))


def task_1_action_3():

    size = size_input.get()
    generated_array = int_array(0, 50, int(size))
    generated_array_label['text'] = generated_array
    set_first_task_result(sort_array(generated_array))


def task_2_action_1():
    generated_array = get_float_matrix(0, 1)
    generated_matrix_label['text'] = generated_array
    set_second_task_result(multiply_row_on_max(generated_array))


def task_2_action_2():
    generated_array = get_int_matrix(-10, 10)
    generated_matrix_label['text'] = generated_array
    set_second_task_result(multiply_row_on_max(generated_array))


def task_2_action_3():
    generated_array = get_int_matrix(0, 20)
    generated_matrix_label['text'] = generated_array
    set_second_task_result(multiply_row_on_max(generated_array))


def task_2_action_4():
    generated_array = get_float_matrix(-10, 10)
    generated_matrix_label['text'] = generated_array
    set_second_task_result(multiply_row_on_max(generated_array))


def get_float_matrix(from_value, to_value):
    return float_matrix(
        from_value,
        to_value,
        int(n_input.get()),
        int(m_input.get())
    )


def get_int_matrix(from_value, to_value):
    return int_matrix(
        from_value,
        to_value,
        int(n_input.get()),
        int(m_input.get())
    )


def set_first_task_result(result):
    result_label['text'] = result


def set_second_task_result(result):
    result_label_two['text'] = result


root = Tk()

root.title("Lab 2")
root.geometry("1300x800")

# Task one layout

task_one_frame = Frame(root)
task_one_frame.place(relx=0.05, rely=0.05, relwidth=0.5, relheight=1)

task_one_title = Label(task_one_frame, text='TASK 1', font='Helvetica 14 bold')
task_one_title.pack()

task_one_description = Label(task_one_frame, text='Please select size of array and generation option')
task_one_description.pack()

input_frame = Frame(task_one_frame)
input_frame.pack(pady=20)

task_one_size_label = Label(input_frame, text='size', fg='grey')
task_one_size_label.pack(side=LEFT)

size_input = Entry(input_frame)
size_input.pack(side=LEFT)

button_zero_to_one = MacosButton(task_one_frame, text='with zero to one', command=task_1_action_1)
button_zero_to_one.pack(pady=10)

button_two = MacosButton(task_one_frame, text='with -10 to 10', command=task_1_action_2)
button_two.pack(pady=5)

button_three = MacosButton(task_one_frame, text='with 0 to 50', command=task_1_action_3)
button_three.pack(pady=5)

generated_array_label = Label(task_one_frame, text='Generated array will be here')
generated_array_label.pack()

result_label = Label(task_one_frame, text='Result will be displayed here')
result_label.pack(pady=20)

# Task two layout

task_two_frame = Frame(root)
task_two_frame.place(relx=0.5, rely=0.05, relwidth=0.5)

task_two_title = Label(task_two_frame, text='TASK 2', font='Helvetica 14 bold')
task_two_title.pack()

task_two_description = Label(task_two_frame, text='Please select n and m of matrix and generation option')
task_two_description.pack()

input_frame_n = Frame(task_two_frame)
input_frame_n.pack(pady=10)

task_two_n_label = Label(input_frame_n, text='n', fg='grey')
task_two_n_label.pack(side=LEFT)

n_input = Entry(input_frame_n)
n_input.pack(side=LEFT)

input_frame_m = Frame(task_two_frame)
input_frame_m.pack()

task_two_m_label = Label(input_frame_m, text='m', fg='grey')
task_two_m_label.pack(side=LEFT)

m_input = Entry(input_frame_m)
m_input.pack(side=RIGHT)

button_task_2_action_1 = MacosButton(task_two_frame, text='with zero to one', command=task_2_action_1)
button_task_2_action_1.pack(pady=10)

button_task_2_action_2 = MacosButton(task_two_frame, text='with -10 to 10 int', command=task_2_action_2)
button_task_2_action_2.pack(pady=5)

button_task_2_action_3 = MacosButton(task_two_frame, text='with 0 to 20 int', command=task_2_action_3)
button_task_2_action_3.pack(pady=5)

button_task_2_action_4 = MacosButton(task_two_frame, text='with -10 to 10 float', command=task_2_action_4)
button_task_2_action_4.pack(pady=5)

generated_matrix_label = Label(task_two_frame, text='Generated matrix will be here')
generated_matrix_label.pack()

result_label_two = Label(task_two_frame, text='Result will be displayed here')
result_label_two.pack(pady=20)

root.mainloop()
