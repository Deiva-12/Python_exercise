class LogEntry:
    def __init__(self, timestamp:str,level:str,message:str):
        self.timestamp:str = timestamp
        self.level:str = level
        self.message :str = message
    def __repr__(self):
        return f"Log(time='{self.timestamp}', level='{self.level}', msg='{self.message}')"
    
