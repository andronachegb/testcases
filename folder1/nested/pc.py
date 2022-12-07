class pc:
    
    def __init__(self, name):
        self.status = "SHUT_DOWN"
        self.name = name
        self.return_status()

    def return_status(self):
        print(f"Status of {self.name} is {self.status}.")
    
    def power_on(self):
        self.status = "POWERED_ON"
        print(f"PC {self.name} was powered on.")
        self.return_status()

    def restart(self):
        print(f"PC {self.name} was restarted.")
        self.return_status()

    def shut_down(self):
        self.status = "SHUT_DOWN"
        print(f"PC {self.name} was shut down.")
        self.return_status()