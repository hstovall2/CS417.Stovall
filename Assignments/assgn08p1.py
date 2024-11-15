#Hudson Stovall
#Assignment 8 Problem 1
#Command

class Square:
    def __init__(self, centerX, centerY, length):
        self.centerX = centerX
        self.centerY = centerY
        self.length = length

    def __str__(self):
        return f"({self.centerX}, {self.centerY}, {self.length})"

class Command:
    def execute(self, squares):
        raise NotImplementedError
    def undo(self, squares):
        raise NotImplementedError

class CreateCommand(Command):
    def __init__(self, squareNumber, length):
        self.squareNumber = squareNumber
        self.length = length
    def execute(self, squares):
        squares[self.squareNumber] = Square(0, 0, self.length)
    def undo(self, squares):
        del squares[self.squareNumber]


class MoveCommand(Command):
    def __init__(self, squareNumber, newX, newY):
        self.squareNumber = squareNumber
        self.newX = newX
        self.newY = newY
        self.oldX = None
        self.oldY = None
    def execute(self, squares):
        square = squares[self.squareNumber]
        self.oldX, self.oldY = square.centerX, square.centerY
        square.centerX, square.centerY = self.newX, self.newY
    def undo(self, squares):
        square = squares[self.squareNumber]
        square.centerX, square.centerY = self.oldX, self.oldY

class ScaleCommand(Command):
    def __init__(self, squareNumber, factor):
        self.squareNumber = squareNumber
        self.factor = factor
        self.oldLength = None
    def execute(self, squares):
        square = squares[self.squareNumber]
        self.oldLength = square.length
        square.length *= self.factor
    def undo(self, squares):
        square = squares[self.squareNumber]
        square.length = self.oldLength

class CommandManager:
    def __init__(self):
        self.squares = {}
        self.undoStack = []
        self.redoStack = []
    def executeCommand(self, command):
        command.execute(self.squares)
        self.undoStack.append(command)
        self.redoStack.clear()
    def undo(self):
        if self.undoStack:
            command = self.undoStack.pop()
            command.undo(self.squares)
            self.redoStack.append(command)
    def redo(self):
        if self.redoStack:
            command = self.redoStack.pop()
            command.execute(self.squares)
            self.undoStack.append(command)
    def printSquares(self):
        for number, square in self.squares.items():
            print(f"{number}: {square}")

def main():
    manager = CommandManager()
    while True:
        try:
            userInput = input("> ").strip()
            if not userInput:
                continue
            parts = userInput.split()
            commandType = parts[0].upper()
            if commandType == "C":
                squareNumber, length = int(parts[1]), float(parts[2])
                manager.executeCommand(CreateCommand(squareNumber, length))
            elif commandType == "M":
                squareNumber, x, y = int(parts[1]), float(parts[2]), float(parts[3])
                manager.executeCommand(MoveCommand(squareNumber, x, y))
            elif commandType == "S":
                squareNumber, factor = int(parts[1]), float(parts[2])
                manager.executeCommand(ScaleCommand(squareNumber, factor))
            elif commandType == "U":
                manager.undo()
            elif commandType == "R":
                manager.redo()
            elif commandType == "P":
                manager.printSquares()
            elif commandType == "X":
                break
            else:
                print("Invalid command")
        except Exception as e:
            print(f"Error: {e}")
if __name__ == "__main__":
    main()
