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
        console.write("You are executed \"rm\" command\n")

    def cancel(self):
        console.write("You are canceled \"rm\" command\n")

    def name(self):
        return "rm"


# bold command
class BoldCommand(Command):

    def execute(self):
        console.write("You are executed \"bold\" command\n")

    def cancel(self):
        console.write("You are canceled \"bold\" command\n")

    def name(self):
        return "bold"


# undo command
class UndoCommand(Command):

    def execute(self):
        try:
            cmd = HISTORY.pop()
            TRASH.append(cmd)
            console.write("Undo command \"{0}\"\n".format(cmd.name()))
            cmd.cancel()

        except IndexError:
            console.write("ERROR: HISTORY is empty\n")

    def name(self):
        return "undo"


# redo command
class RedoCommand(Command):

    def execute(self):
        try:
            cmd = TRASH.pop()
            HISTORY.append(cmd)
            console.write("Redo command \"{0}\"\n".format(cmd.name()))
            cmd.execute()
        except IndexError:
            console.write("ERROR: TRASH is empty\n")

    def name(self):
        return "redo"


# history command
class HistoryCommand(Command):

    def execute(self):
        i = 0
        for cmd in HISTORY:
            console.write("{0}: {1}\n".format(i, cmd.name()))
            i = i + 1

    def name(self):
        print("history")


# exit command
class ExitCommand(Command):

    def execute(self):
        raise SessionClosed("Good bay!\n")

    def name(self):
        return "exit"

# available commands
COMMANDS = {'rm': RmCommand(), 'bold': BoldCommand(), 'undo':
            UndoCommand(), 'redo': RedoCommand(), 'history': HistoryCommand(),
            'exit': ExitCommand()}

HISTORY = list()
TRASH = list()


# Shell
def main():
    try:
        while True:
            console.flush()
            console.write("pysh >> ")

            cmd = input()

            try:
                command = COMMANDS[cmd]
                command.execute()
                if (not isinstance(command, UndoCommand) and not
                        isinstance(command, RedoCommand) and not
                        isinstance(command, HistoryCommand)):
                    TRASH = list()
                    HISTORY.append(command)

            except KeyError:
                console.write("ERROR: Command \"{}\" not found\n".format(cmd))

    except SessionClosed as e:
        console.write(e.value)

if __name__ == "__main__":
    main()
