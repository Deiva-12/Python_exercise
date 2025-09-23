import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
class Server:
    def __init__(self,hostname:str,ip_address:str,status:str,cpu_usage:float,memory_usage:float):
        self.hostname = hostname
        self.ip_address = ip_address
        self.status = status
        self.cpu_usage = cpu_usage
        self.memory_usage = memory_usage
    def __repr__(self):
        """Provides a developer-friendly string representation of the object."""
        return (f"Server(hostname='{self.hostname}', ip='{self.ip_address}', "
                f"status='{self.status}', cpu={self.cpu_usage}%, mem={self.memory_usage}%)")
    def to_dict(self):
        """Converts the object's attributes to a dictionary."""
        return self.__dict__
    
"""Exercise 1: Filtering and Sorting a Server List"""    
# Create a list of Server objects
servers = [
    Server("web-01", "192.168.1.10", "online", 25.5, 45.0),
    Server("db-01", "192.168.1.11", "offline", 0.0, 10.0),
    Server("app-01", "192.168.1.12", "online", 85.0, 60.5),
    Server("cache-01", "192.168.1.13", "online", 5.2, 22.8),
    Server("db-02", "192.168.1.14", "offline", 0.0, 10.0),
]

# --- Filtering ---
# Use a list comprehension to find all offline servers
# offline_servers = []
# for s in servers:
#     if s.status == "offline":
#         offline_servers.append(s)
# print(offline_servers)
# for server in offline_servers:
#     print(server)

offline_servers = [s for s in servers if s.status == "offline"]
logging.info("--- Offline Servers Report ---")
for server in offline_servers:
    logging.info(server)

# --- Sorting ---
# Use the sorted() function with a lambda key to sort by CPU usage in descending order
servers_sorted_by_cpu = sorted(servers, key=lambda s: s.cpu_usage, reverse=True)
logging.info("\n--- Servers Sorted by CPU Usage (High to Low) ---")

for server in servers_sorted_by_cpu:
    logging.info(server)
logging.info(f"\nServer with highest CPU usage: {servers_sorted_by_cpu[0].hostname}")
         
"""Exercise 2: Transforming Object Data"""

# Using the 'servers' list from Exercise 1
servers = [
    Server("web-01", "192.168.1.10", "online", 25.5, 45.0),
    Server("db-01", "192.168.1.11", "offline", 0.0, 10.0),
    Server("app-01", "192.168.1.12", "online", 85.0, 60.5),
]

# Use a list comprehension to transform the data
inventory_report = [f"{s.hostname} ({s.ip_address})" for s in servers]

logging.info("--- Network Inventory ---")
for entry in inventory_report:
    logging.info(entry)

"""Exercise 3: Aggregating Data from a List of Objects
Objective: Learn to calculate summary statistics (like an average) from a list of objects.
Scenario: You need to calculate the average CPU usage for all servers that are currently online."""

# Using the 'servers' list from Exercise 1
servers = [
    Server("web-01", "192.168.1.10", "online", 25.5, 45.0),
    Server("db-01", "192.168.1.11", "offline", 0.0, 10.0),
    Server("app-01", "192.168.1.12", "online", 85.0, 60.5),
    Server("cache-01", "192.168.1.13", "online", 5.2, 22.8),
]

# First, get only the online servers

online_servers = [s for s in servers if s.status == "online"]

if online_servers:
    # Get a list of just the CPU usage values
    cpu_usages = [s.cpu_usage for s in online_servers]
    
    # Calculate the average
    average_cpu = sum(cpu_usages) / len(cpu_usages)
    logging.info(f'avg : {average_cpu}')
    logging.info(f"--- Health Summary for {len(online_servers)} Online Servers ---")
    logging.info(f"Average CPU Usage: {average_cpu:.2f}%")
else:
    logging.info("No online servers found.")

# Using the 'servers' list from Exercise 1
servers_list = [
    Server("web-01", "192.168.1.10", "online", 25.5, 45.0),
    Server("db-01", "192.168.1.11", "offline", 0.0, 10.0),
    Server("app-01", "192.168.1.12", "online", 85.0, 60.5),
]

# Use a dictionary comprehension to build the dictionary
# Key: server's hostname, Value: the Server object itself
servers_dict = {s.hostname: s for s in servers_list}

print("--- Server Dictionary ---")
print(servers_dict)

# --- Fast Lookup ---
target_hostname = "app-01"
if target_hostname in servers_dict:
    app_server = servers_dict[target_hostname]
    print(f"\n--- Details for {target_hostname} ---")
    print(f"Status: {app_server.status}, CPU: {app_server.cpu_usage}%")
else:
    print(f"\nServer '{target_hostname}' not found.")


    # Using the 'servers_dict' from Exercise 4
servers_dict = {
    'web-01': Server(hostname='web-01', ip_address='192.168.1.10', status='online', cpu_usage=25.5, memory_usage=45.0),
    'db-01': Server(hostname='db-01', ip_address='192.168.1.11', status='offline', cpu_usage=0.0, memory_usage=10.0),
    'app-01': Server(hostname='app-01', ip_address='192.168.1.12', status='online', cpu_usage=85.0, memory_usage=60.5)
}

print(f"Status of web-01 before update: {servers_dict['web-01'].status}")

# --- Update the object's state ---
target_server = servers_dict.get("web-01")
if target_server:
    target_server.status = "offline"
    target_server.cpu_usage = 0.0
    print("Updated web-01 status.")

print(f"Status of web-01 after update: {servers_dict['web-01'].status}")
print(f"Full object after update: {servers_dict['web-01']}")