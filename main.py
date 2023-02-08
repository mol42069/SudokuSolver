import numpy as np
import tkinter as tk

entry = []


def generate_entry_array(grid):
    global entry
    # creating all entry-boxes

    for i in range(0, 9):
        line = []
        for x in range(0, 9):
            line.append(tk.Text(grid, height=2, width=4, font=("Arial", 30)).grid(row=i, column=x))
        entry.append(line)

    return entry


def get_input():
    global entry
    print(entry)
    inputs = []
    for y, row in enumerate(entry):
        line = []
        print(row)
        for x, column in enumerate(row):
            print(column)
            inp = column.get(1.0, 'end-1c')
            if inp > 9:
                print('ERROR WRONG INPUT: ' + inp + ' at: ' + y + ' : ' + x)
            if inp == '':
                line.append(99)
            else:
                line.append(inp)

        print(line)


def generate_solved():
    pass


def solve():
    get_input()


def main():
    root = tk.Tk()
    root.title('SS')
    root.geometry('900x1000')
    grid = tk.Frame(root)
    grid.grid(rowspan=50, columnspan=10)

    generate_entry_array(grid)

    button = [tk.Button(grid, text='QUIT', command=root.destroy).grid(column=1, row=20),
              tk.Button(grid, text='SOLVE', command=solve).grid(column=0, row=20)]

    root.mainloop()


if __name__ == '__main__':
    main()
