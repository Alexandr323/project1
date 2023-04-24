import random
# from tkinter import *
#
#
# window = Tk()
# window.geometry('700x700')
# for i in range(10):
#     for j in range(10):
#         cell = Button(text='',width=4,height=3)
#         cell.place(x = j*40,y=i*40)
#
# window.mainloop()



class Ship:
    def __init__(self,lenght,x=None,y=None,tp = 1):
        self.x = x
        self.y = y
        self.lenght = lenght
        self.tp = tp
        self.cells = [1]*self.lenght
        self.is_move = True


    def set_start_coords(self,x,y):
        if self.tp == 1 and self.x + self.lenght > 9 or self.tp == 2 and self.y + self.lenght > 9 or self.x < 2  or self.y < 2:
            raise ValueError
        self.x = x
        self.y = y

    def get_start_coords(self):
        return (self.x,self.y)

    def move(self,go):
        pass
    def is_collide(cls,ship):
        pass
    def is_out_pole(self,size):
        pass

    def __getitem__(self, item):
        return self.cells[item]
    def __setitem__(self, key, value):
        self.cells[key] = value

    def __repr__(self):
        return f"{self.lenght}"


class GamePole:
    def __init__(self,size):
        self.size = size
        self.ships = [Ship(4,tp = random.randint(1,2)),Ship(3,tp = random.randint(1,2)),Ship(3,tp = random.randint(1,2)),Ship(2,tp = random.randint(1,2)),Ship(2,tp = random.randint(1,2)),Ship(2,tp = random.randint(1,2)),Ship(1,tp = random.randint(1,2)),Ship(1,tp = random.randint(1,2)),Ship(1,tp = random.randint(1,2)),Ship(1,tp = random.randint(1,2))]

        self.board = []
        for i in range(12):
            self.board.append(["O"] * 12)

    def get_ships(self):
        return self.ships
    def place_ships(self):
        for i in self.ships:
            placed = False
            while not placed:
                x = random.randint(1, self.size-1)
                y = random.randint(1, self.size-1)
                if i.tp == 1:
                    if y + i.lenght <= self.size:
                        valid = True
                        for j in range(i.lenght):
                            if self.board[x][y + j] != "O":
                                valid = False
                        if valid:
                            for z in range(i.lenght):
                                self.board[x][y + z] = i
                            placed = True
                else:
                    if x + i.lenght <= self.size:
                        valid = True
                        for v in range(i.lenght):
                            if self.board[x + v][y] != "O":
                                valid = False
                        if valid:
                            for b in range(i.lenght):
                                self.board[x + b][y] = i
                            placed = True


    def move_ships(self):
        pass
    def show(self):
        # for row in self.board:
        #     return " ".join(row)

        print(*self.board,sep="\n")


    def get_pole(self):
        pass

game = GamePole(10)
game.place_ships()
game.show()
