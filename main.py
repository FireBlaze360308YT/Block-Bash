import customtkinter as ctk


class Block:
    def __init__(self, x_cord: int, y_cord: int):
        self.x_cord: int = x_cord
        self.y_cord: int = y_cord
        self.full: int = 0


class Grid:
    def __init__(self, grid_size: int):
        self.grid_size = grid_size
        self.grid: list[Block] = list()
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                self.grid.append(Block(x_cord=i, y_cord=j))

        button_width = 50
        button_height = 50
        padding = 0
        window_width = self.grid_size * button_width + (self.grid_size - 1) * padding
        window_height = self.grid_size * button_height + (self.grid_size - 1) * padding

        self.window = ctk.CTk()
        self.window.title("Block Blast")
        self.window.configure(bg_color="black")
        self.window.geometry(f"{window_width}x{window_height}")
        self.window.resizable(False, False)

        self.padding: dict = {"padx": 0, "pady": 0}

        self.buttons: list[ctk.CTkButton] = list()
        for i, block in enumerate(self.grid):
            button = ctk.CTkButton(
                self.window,
                text=f"{block.x_cord},{block.y_cord},{block.full}",
                fg_color="black",
                width=button_width,
                height=button_height,
                border_width=1,
                border_color="green",
                command=None
            )
            button.grid(row=block.y_cord, column=block.x_cord, **self.padding)
            self.buttons.append(button)

    def run(self):
        self.window.mainloop()


def main() -> None:
    grid_size = 8
    grid_instance = Grid(grid_size)
    grid_instance.run()


if __name__ == '__main__':
    main()
