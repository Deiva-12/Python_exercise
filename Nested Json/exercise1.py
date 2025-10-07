import  json

class Detail_l:
    def __init__(self,date:str,time:str,status:str,message:str):
        self.date : str = date
        self.time : str = time
        self.status : str = status
        self.message : str = message

   
    
    def to_dict(self):
        return self.__dict__
    
class Detail_u:
    def __init__(self,appname:str,com_location:str,reports:str):
        self.appname : str = appname
        self.com_location : str = com_location
        self.reports :str = reports if reports else []

    def to_dict(self):
        return {"appname":self.appname,
                "com_location" : self.com_location,
                "report":[n.to_dict() for n in self.reports] }
    def __repr__(self):
        return f"Detail_u({self.appname},{self.com_location},Detail_l={len(self.reports)})"

    
detail_report = [
        Detail_l("2025-09-23","09:46:06","INFO","Querying database for user list."),
        Detail_l("2025-09-21","09:46:01","ERROR","Querying database for user list.")
    ]

server_detail_report = []
for m in detail_report:
    server_detail_report.append(m.__dict__)
print(server_detail_report) 
with open("backup_report.json","w") as file:
    json.dump(server_detail_report, file , indent=4)
           
