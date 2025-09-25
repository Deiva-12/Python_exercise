"""Scenario: You receive a datacenters.json file that groups servers by their physical location. 
Your script needs to parse this file and create a single list of all servers, regardless of their datacenter."""
import json

class Server:

    def __init__(self, hostname:str, ip_address:str, status:str,
                 cpu_usage:float,memory_usage: float):
        self.hostname:str = hostname
        self.ip_address : str = ip_address
        self.status : str = status
        self.cpu_usage : float = cpu_usage
        self.memory_usage :float = memory_usage
    def __repr__(self):
                return (f"Server(hostname='{self.hostname}', ip='{self.ip_address}', "
                f"status='{self.status}', cpu={self.cpu_usage}%, mem={self.memory_usage}%)")

with open("datacenters.json","r") as file:
    data = json.load(file)

# print(data)

all_servers = []

for dc in data["datacenters"]:
      dc_name = dc["name"]
      dc_location = dc["location"]
      print(f"Name of the server : {dc_name} and location is : {dc_location}")
      for server_data in dc["servers"]:
            # print(server_data)
            server_obj = Server(hostname=server_data["hostname"],
                                ip_address=server_data["ip"],
                                status=server_data["status"],
                                cpu_usage=float(server_data["cpu"]),
                                memory_usage=float(server_data["mem"]))
            all_servers.append(server_obj)
print("----------Server list ----------")
for server in all_servers:
      print(server)
            


      
      

