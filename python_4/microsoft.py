from sys import stdout as console


# Handling 'exit' command
class SessionClosed(Exception):

    def __init__(self, value):
        self.value = value

# definition
# Interface

# Command = collection.namedtuple('Command', ['function', 'args'])


class Command:

    def execute(self):
        raise NotImplementedError()

    def cancel(self):
        raise NotImplementedError()

    def name(self):
        raise NotImplementedError()


# rm command
class RmCommand(Command):

    def execute(self):
        console.write("executed \"rm\" command\n")

    def cancel(self):
        console.write("canceled \"rm\" command\n")

    def name(self):
        return "rm"


# bold command
class BoldCommand(Command):

    def execute(self):
        console.write("executed \"bold\" command\n")

    def cancel(self):
        console.write("canceled \"bold\" command\n")

    def name(self):
        return "bold"


# undo command
class UndoCommand(Command):

    def __init__(self, history, trash):
        self.history = history
        self.trash = trash

    def execute(self):
        try:
            cmd = self.history.pop()
            self.trash.append(cmd)
            console.write("Undo command \"{0}\"\n".format(cmd.name()))
            cmd.cancel()

        except IndexError:
            console.write("ERROR: HISTORY is empty\n")

    def name(self):
        return "undo"


# redo command
class RedoCommand(Command):

    def __init__(self, history, trash):
        self.history = history
        self.trash = trash

    def execute(self):
        try:
            cmd = self.trash.pop()
            self.history.append(cmd)
            console.write("Redo command \"{0}\"\n".format(cmd.name()))
            cmd.execute()
        except IndexError:
            console.write("ERROR: TRASH is empty\n")

    def name(self):
        return "redo"


# history command
class HistoryCommand(Command):
    def __init__(self, history):
        self.history = history

    def execute(self):
        for i, cmd in enumerate(self.history):
            console.write("{0}: {1}\n".format(i, cmd.name()))

    def name(self):
        print("history")


# exit command
class ExitCommand(Command):

    def execute(self):
        raise SessionClosed("Good bay!\n")

    def name(self):
        return "exit"

# available commands



# Shell
def main():
    history = []
    trash = []
    commands = {'rm': RmCommand(), 'bold': BoldCommand(), 'undo':
                UndoCommand(history, trash), 'redo': RedoCommand(history, trash),
                'history': HistoryCommand(history), 'exit': ExitCommand()}
    try:
        while True:
            console.flush()
            console.write("pysh >> ")

            cmd = input()

            try:
                command = commands[cmd]
                command.execute()
                if (not isinstance(command, UndoCommand) and not
                        isinstance(command, RedoCommand) and not
                        isinstance(command, HistoryCommand)):
                    trash.clear()
                    history.append(command)

            except KeyError:
                console.write("ERROR: Command \"{}\" not found\n".format(cmd))

    except SessionClosed as e:
        console.write(e.value)

if __name__ == "__main__":
    main()
