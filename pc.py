class pc:
    
    def __init__(self, name):
        self.status = "SHUT_DOWN"
        self.name = name
    
    def power_on(self):
        self.status = "POWERED_ON"
        print(f"PC {self.name} was powered on")