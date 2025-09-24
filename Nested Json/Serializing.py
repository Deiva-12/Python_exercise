import json

class Server:

    def __init__(self,hostname:str,ip_address:str,status:str,
                 cpu_usage:float,memory_usage:float, region:str,location:str):
        
        self.hostname:str = hostname
        self.ip_address :str = ip_address
        self.status :str = status
        self.cpu_usage:float = cpu_usage
        self.memory_usage:float = memory_usage
        self.region = region
        self.loaction :str = location

    def to_dict(self):
        return self.__dict__
    
server_list = [
    Server("web-01", "192.168.1.10", "online", 25.5, 45.0, "us-est-1","us"),
    Server("db-01", "192.168.1.11", "offline", 0.0, 10.0,"us-est-1","us"),
    Server("aa_01","192.167.89.1.1","ofline",2.1,10.4,"us-est-1","us")
]


server_data_for_json = [s.to_dict() for s in server_list] # comprehensions

# server_data_for_json = []
# for s in server_list:
#    server_data_for_json.append(s.__dict__)
with open("backup.json", 'w')as file:
    json.dump(server_data_for_json, file, indent=4)
print("Server data has been serialized to backup.json")

