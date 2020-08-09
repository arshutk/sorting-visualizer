from tkinter import *
from tkinter import ttk
from random import randrange
from windll import set_dpi_awareness
import threading

# algoritm files :
from BubbleSort import bubble_sort
from SelectionSort import selection_sort
from QuickSort import quick_sort
from InsertionSort import insertion_sort
from MergeSort import merge_sort


set_dpi_awareness()

root = Tk()
root.maxsize(900, 600)
root.geometry("700x550")
root.resizable(False, False)
root.title("Sorting Algorithms Visualizer")
root.config(background="#121212")
root.columnconfigure(0, weight=1)

# Logo :
root.iconphoto(False, PhotoImage(file="./media/logo.png"))

# Variables :
alg_slctd = StringVar()
data = []

# Functions :


def start():
    global data
    if not data:
        return

    if (algorithm_menu.get() == "Bubble Sort"):
        bubble_sort(data, draw_dataset, dash_scale.get(), sort_canvas)
        # threading.Thread(target=bubble_sort(
        # data, draw_dataset, dash_scale.get(), sort_canvas)).start()

    if (algorithm_menu.get() == "Selection Sort"):
        threading.Thread(target=selection_sort(
            data, draw_dataset, dash_scale.get(), sort_canvas)).start()

    if (algorithm_menu.get() == "Quick Sort"):
        threading.Thread(target=quick_sort(data, 0, len(
            data) - 1, draw_dataset, dash_scale.get(), sort_canvas)).start()

    if (algorithm_menu.get() == "Insertion Sort"):
        threading.Thread(target=insertion_sort(
            data, draw_dataset, dash_scale.get(), sort_canvas)).start()

    if (algorithm_menu.get() == "Merge Sort"):
        threading.Thread(target=merge_sort(
            data, draw_dataset, dash_scale.get(), sort_canvas)).start()

    draw_dataset(data, ["#98fb98" for counter in range(len(data))])


def generate():
    global data
    min_value = int(min_scale.get())
    max_value = int(max_scale.get())
    size = int(size_scale.get())

    data = []
    for element in range(size):
        data.append(randrange(min_value, max_value + 1))
    draw_dataset(data, ["#98fb98" for data in range(len(data))])


def draw_dataset(data, clrd_data):
    sort_canvas.delete("all")
    c_height = 380
    c_width = 600
    x_width = c_width / (len(data) + 2)
    offset = 30
    spacing = 10
    normalizedData = [i / max(data) for i in data]
    for itr, height in enumerate(normalizedData):
        # top - left :
        x_0 = itr * x_width + offset + spacing
        y_0 = c_height - height * 340
        # bottom - right :
        x_1 = (itr + 1) * x_width + offset
        y_1 = c_height + 1

        sort_canvas.create_rectangle(x_0, y_0, x_1, y_1, fill=clrd_data[itr])
        sort_canvas.create_text((((x_0 + x_1) // 2) - 2), y_0,
                                anchor=SW, text=str(data[itr]), fill="#F0F0F0")
    root.update_idletasks()


user_interface = Frame(root, width=600, height=200, background="#121212")
user_interface.grid(row=1, column=0, padx=10, pady=5, sticky=EW)
user_interface.columnconfigure((0, 1, 2, 3, 4), weight=1)

sort_canvas = Canvas(root, width=600, height=380,
                     background="#121212", borderwidth=0, highlightthickness=0)
sort_canvas.grid(row=0, column=0, padx=10, pady=5)

# First - Row :

Label(user_interface, text="Algorithms", background="#F0F0F0").grid(
    row=0, column=0, padx=5, pady=5, columnspan=2, sticky=EW)
algorithm_menu = ttk.Combobox(user_interface, textvariable=alg_slctd, state="readonly", values=[
    "Bubble Sort", "Selection Sort", "Quick Sort", "Insertion Sort", "Merge Sort"], background="red")
algorithm_menu.current(0)
algorithm_menu.grid(row=0, column=2, padx=5, pady=5, columnspan=2, sticky=EW)
Button(user_interface, text="Start",
       command=start, background="#F0F0F0", activebackground="#D0D0D0").grid(row=0, column=4, padx=5, pady=5, columnspan=2, sticky=EW)

# Second Row :

size_scale = Scale(user_interface, from_=10, to=25,
                   orient="horizontal", resolution=1, label="Data Size", foreground="black", background="#F0F0F0", activebackground="#C0C0C0", cursor="hand2", troughcolor="#404040", borderwidth=0, highlightthickness=0)
size_scale.grid(row=1, column=0, padx=5, pady=5, columnspan=2, sticky=EW)

min_scale = Scale(user_interface, from_=0, to=20,
                  orient="horizontal", resolution=1, label="Min-Value", foreground="black", background="#F0F0F0", activebackground="#C0C0C0", cursor="hand2", troughcolor="#404040", borderwidth=0, highlightthickness=0)
min_scale.grid(row=1, column=2, padx=5, pady=5, sticky=EW)

max_scale = Scale(user_interface, from_=20, to=100,
                  orient="horizontal", resolution=1, label="Max Value", foreground="black", background="#F0F0F0", activebackground="#C0C0C0", cursor="hand2", troughcolor="#404040", borderwidth=0, highlightthickness=0)
max_scale.grid(row=1, column=3, padx=5, pady=5, sticky=EW)

dash_scale = Scale(user_interface, from_=0.1, to=3.0,
                   orient="horizontal", resolution=0.2, digits=2, label="Delay[s]", foreground="black", background="#F0F0F0", activebackground="#C0C0C0", cursor="hand2", troughcolor="#404040", borderwidth=0, highlightthickness=0)
dash_scale.grid(row=1, column=4, padx=5, pady=5, sticky=EW)


# Third Row :

Button(user_interface, text="Generate",
       command=generate, background="#F9F9F9", activebackground="#D0D0D0").grid(row=2, column=0, padx=5, pady=5, columnspan=5, sticky=EW)


root.mainloop()
