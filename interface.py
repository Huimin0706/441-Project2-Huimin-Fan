import tkinter as tk
from tkinter import messagebox

from world import World


class GraphInterface:

    def __init__(self):

        self.__world = World(2)
        self.__graph = self.__world.getGraph()

        self.__path = []
        self.__currentStep = 0
        self.__photo = None

        self.__window = tk.Tk()
        self.__window.title("Graph Search")

        # Start node input
        tk.Label(
            self.__window,
            text="Start Node ID: (0-7)"
        ).grid(row=1, column=0, padx=30, pady=20)

        self.__startEntry = tk.Entry(self.__window)
        self.__startEntry.grid(row=1, column=1, padx=30, pady=20)

        # Search buttons
        tk.Button(
            self.__window,
            text="Solve BFS",
            command=self.solveBFS
        ).grid(row=2, column=0, padx=30, pady=20)

        tk.Button(
            self.__window,
            text="Solve DFS",
            command=self.solveDFS
        ).grid(row=2, column=1, padx=30, pady=20)

        # Image display
        self.__imageLabel = tk.Label(self.__window)
        self.__imageLabel.grid(
            row=3,
            column=0,
            columnspan=2,
            pady=40
        )

        # Information label
        self.__infoLabel = tk.Label(
            self.__window,
            text="No solution loaded."
        )

        self.__infoLabel.grid(
            row=4,
            column=0,
            columnspan=2
        )

        # Navigation buttons
        tk.Button(
            self.__window,
            text="Previous",
            command=self.previousState
        ).grid(row=5, column=0, pady=10)

        tk.Button(
            self.__window,
            text="Next",
            command=self.nextState
        ).grid(row=5, column=1, pady=10)

    def solveBFS(self):

        try:
            startId = int(self.__startEntry.get())

            ######
            #NOTE: This is where it is calling your function
            ######
            self.__path = self.__graph.bfs(startId)
            self.__currentStep = 0
            print(f"Path for BFS: {self.__path}")
            if len(self.__path) == 0:
                messagebox.showinfo(
                    "No Solution",
                    "No goal node was found."
                )
                return

            self.showCurrentState()

        except ValueError:
            messagebox.showerror(
                "Invalid Input",
                "Please enter a valid node ID."
            )

    def solveDFS(self):

        try:
            startId = int(self.__startEntry.get())

            ######
            #NOTE: This is where it is going to call your function
            ######
            self.__path = self.__graph.dfs(startId)
            self.__currentStep = 0
            print(f"Path for DFS: {self.__path}")
            if len(self.__path) == 0:
                messagebox.showinfo(
                    "No Solution",
                    "No goal node was found."
                )
                return

            self.showCurrentState()

        except ValueError:
            messagebox.showerror(
                "Invalid Input",
                "Please enter a valid node ID."
            )

    def showCurrentState(self):

        if len(self.__path) == 0:
            return

        nodeId = self.__path[self.__currentStep]

        node = self.__graph.getNode(nodeId)

        # Try to load the state image; fall back to text if missing.
        imagePath = node.getImg()
        try:
            self.__photo = tk.PhotoImage(file=imagePath)
            self.__imageLabel.config(image=self.__photo, text="")
        except Exception:
            self.__photo = None
            self.__imageLabel.config(
                image="",
                text=(f"State {nodeId}\n"
                      f"Vacuum at cell {node.getVacuumPos()}\n"
                      f"Cells: {node.getCells()}")
            )

        # Determine the action that led to this state (if any).
        actionText = "START"
        if self.__currentStep > 0:
            prevId = self.__path[self.__currentStep - 1]
            prevNode = self.__graph.getNode(prevId)
            for action, destId in prevNode.getConnections():
                if destId == nodeId:
                    actionText = action
                    break

        goalText = ""
        if node.getIsGoal():
            goalText = " (GOAL)"

        self.__infoLabel.config(
            text=(
                f"Step {self.__currentStep + 1}/{len(self.__path)}"
                f"    Node ID: {nodeId}"
                f"    Previous Action: {actionText}"
                f"{goalText}"
            )
        )

    def nextState(self):

        if len(self.__path) == 0:
            return

        if self.__currentStep < len(self.__path) - 1:
            self.__currentStep += 1
            self.showCurrentState()

    def previousState(self):

        if len(self.__path) == 0:
            return

        if self.__currentStep > 0:
            self.__currentStep -= 1
            self.showCurrentState()

    def run(self):
        self.__window.mainloop()


if __name__ == "__main__":
    gui = GraphInterface()
    gui.run()