from tkinter import *
from tkinter import messagebox
from tkinter.colorchooser import *

from Player import Player


class Board(Tk):
    def __init__(self, first: Player, second: Player):
        super().__init__()
        self.title("X-O")

        self.first = first
        self.second = second
        self.turn_number = 1

        self.first.color = askcolor(title="בחר צבע לשחקן מספר 1")[1]
        self.second.color = askcolor(title="בחר צבע לשחקן מספר 2")[1]

        self.main_frame = Frame(self)

        self.empty = "|"
        self.types = ["X", "O"]
        self.arr_2d = [[self.empty for i in range(3)] for i in range(3)]
        self.buttons_size = 10
        self.buttons = [[Button(self.main_frame, text="-", width=self.buttons_size, height=int(self.buttons_size/2)) for i in range(3)] for i in range(3)]

        self.label = Label(self, width=30, height=1, text="תור {}".format(self.first.name))

        self.setup_buttons()
        self.main_frame.pack(side=BOTTOM)
        self.label.pack(side=TOP)

        messagebox.showinfo(
            "הודעה",
            "{} מתחיל".format(self.first.name)
        )

    def next_turn(self) -> None:
        self.turn_number += 1
        self.label.configure(text="תור {}".format(self.get_now_player().name))

    def get_now_player(self) -> Player:
        if self.turn_number % 2 == 1:
            return self.first
        return self.second

    def setup_buttons(self) -> None:
        self.buttons[0][0].grid(row=0, column=0)
        self.buttons[0][0].configure(command=lambda: self.set(0, 0, self.get_now_player()))

        self.buttons[0][1].grid(row=0, column=1)
        self.buttons[0][1].configure(command=lambda: self.set(0, 1, self.get_now_player()))

        self.buttons[0][2].grid(row=0, column=2)
        self.buttons[0][2].configure(command=lambda: self.set(0, 2, self.get_now_player()))

        self.buttons[1][0].grid(row=1, column=0)
        self.buttons[1][0].configure(command=lambda: self.set(1, 0, self.get_now_player()))

        self.buttons[1][1].grid(row=1, column=1)
        self.buttons[1][1].configure(command=lambda: self.set(1, 1, self.get_now_player()))

        self.buttons[1][2].grid(row=1, column=2)
        self.buttons[1][2].configure(command=lambda: self.set(1, 2, self.get_now_player()))

        self.buttons[2][0].grid(row=2, column=0)
        self.buttons[2][0].configure(command=lambda: self.set(2, 0, self.get_now_player()))

        self.buttons[2][1].grid(row=2, column=1)
        self.buttons[2][1].configure(command=lambda: self.set(2, 1, self.get_now_player()))

        self.buttons[2][2].grid(row=2, column=2)
        self.buttons[2][2].configure(command=lambda: self.set(2, 2, self.get_now_player()))

    def show(self) -> None:
        self.mainloop()

    def set(self, row: int, col: int, player: Player) -> None:
        if self.arr_2d[row][col] in self.types:
            self.next_turn()
            self.next_turn()
        else:
            self.arr_2d[row][col] = player.player_type
            self.buttons[row][col].configure(text=player.player_type, bg=player.color)
            if self.is_winner():
                messagebox.showinfo("!ניצחון", "!!!{} ניצח".format(player.name))
                exit(0)
            elif self.is_full(): #There is no any winner...
                messagebox.showinfo("...אוייי", "...שוויון")
                exit(0)

            self.next_turn()

    def __str__(self) -> str:
        text = ""
        for i in self.arr_2d:
            for j in i:
                text += j
            text += "\n"
        return text

    def is_winner(self) -> bool:
        return self.check_diagonally() or self.check_direct()

    def check_direct(self) -> bool:
        for i in self.arr_2d:
            if "X" in i or "O" in i:
                if self.equals(i):
                    return True
        for i in self.get_columns():
            if "X" in i or "O" in i:
                if self.equals(i):
                    return True
        return False

    def check_diagonally(self) -> bool:
        if self.empty in self.arr_2d[0][0] or self.empty in self.arr_2d[1][1] or self.empty in self.arr_2d[2][2] or \
           self.empty in self.arr_2d[0][2] or self.empty in self.arr_2d[1][1] or self.empty in self.arr_2d[2][0]:
            return False
        if self.equals([self.arr_2d[0][0], self.arr_2d[1][1], self.arr_2d[2][2]]):
            return True
        elif self.equals([self.arr_2d[0][2], self.arr_2d[1][1], self.arr_2d[2][0]]):
            return True

        return False

    def get_columns(self) -> list:
        arr = []
        for i in range(3):
            arr.append([])
            for j in range(3):
                arr[i].append(self.arr_2d[j][i])

        return arr

    def is_full(self) -> bool:
        for arr in self.arr_2d:
            if self.empty in arr:
                return False
        return True

    def find_second(self, player: Player) -> str:
        if player.player_type == "X":
            return "O"
        return "X"

    @staticmethod
    def equals(arr: list) -> bool:
        return len(set(arr)) <= 1
