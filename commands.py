class Command:
    def __init__(self, id, method, description, command):
        self.id = id
        self.method = method
        self.description = description
        self.command = command

    def run(self):
        self.method()
    
    def __str__(self):
        print("Description: {0}\nCommand: {1}\n".format(self.description, self.command))
    
    def getOutputList(self):
        return [self.command, self.description]

class CommandHandler:
    def __init__(self):
        self.commands = []
    
    def runCommand(self, command):
        if len(command) == 0:
            return
        try:
            id = [x for x in self.commands if x.command == command][0].id
        except IndexError:
            return -1
        
        if isinstance(id, list):
            from terminal import Log
            Log.w("Specify Command!")
            return

        self.commands[id].run()
        return 1
    
    def addCommand(self, command):
        command.id = len(self.commands)
        self.commands.append(command)

class CommandHandlerSpeech(CommandHandler):
    def __init__(self):
        super()
        self.commands = []

    def runCommand(self, command):
        from terminal import Log
        Log.w(command)
        if command is None:
            return -1
        
        try:
            id = [x for x in self.commands if command in x.command][0].id
        except IndexError:
            return -1
        
        self.commands[id].run()
        return 1