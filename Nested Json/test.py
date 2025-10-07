import json

with open("datacenters.json","r") as file:
    data = json.load(file)
dc = data["datacenters"]
# print(type(dc))
# print(data.keys())
offline_se = 0
for m in dc:
    # if m["name"] == "sa-east-1" :
    #     print(m["servers"])
    #     for n in m["servers"]:
    #         # print(n)
    #         if n["status"] == "online":
    #             print(n)

    # if m["location"] == "Oregon, USA":
    #     print(m["servers"])
    #     for l in m['servers']:
    #         # print(l)
    #         if l['status'] == 'offline':
    #             print(l)
    #             print(l['mem'])
    # print(m['servers'])
    for s in m["servers"]:
        # print(s)
        if s["status"] == "online":
            offline_se+=1
            print(s)
print(offline_se)

