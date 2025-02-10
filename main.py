import customtkinter as ctk

class Block:
    def __init__(self, x_cord: int, y_cord: int):
        self.x_cord: int = x_cord
        self.y_cord: int = y_cord
        self.full: int = 0

class Grid:
    def __init__(self):
        self.grid: list[Block] = list()
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                self.grid.append(Block(x_cord=i, y_cord=j))

        self.window = ctk.CTk()
        self.window.title("Block Blast")
        self.window.configure(bg_color="green")
        self.window.geometry("399x399")
        self.window.resizable(False, False)

        self.padding: dict = {"padx": 0, "pady": 0}

        self.buttons: list[ctk.CTkButton] = list()
        for i, block in enumerate(self.grid):
            button = ctk.CTkButton(
                self.window,
                text=f"{block.full}",
                fg_color="black",
                width=50,
                height=50,
                border_width=1,
                border_color="green",
                command=None
            )
            button.grid(row=block.y_cord, column=block.x_cord, **self.padding)
            self.buttons.append(button)

    def run(self):
        self.window.mainloop()

GRID_SIZE: int = 8

def main() -> None:
    grid_instance = Grid()
    grid_instance.run()

if __name__ == '__main__':
    main()
