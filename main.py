import json
from random import randint
from sys import argv

with open(argv[1]) as waypoints_fl:
    waypoints = waypoints_fl.readlines()
waypoints_fl.close()
del waypoints_fl

waypoints = list(map(lambda point: point.removeprefix("waypoint:").split(":"), waypoints))
# waypoints = list(map(lambda point: list(map(lambda index, num: (num if index != 1 else None), enumerate(point))), waypoints))


for pointdata in waypoints:
    pointdata.pop(1)

for i in waypoints:
    waypoint = dict()
    cords = tuple(i[1:4])
    id = f"{i[0]}_{cords[0]}-{cords[1]}-{cords[2]}".replace(" ","_").replace("?","")
    name = i[0]
    red = randint(1,255)
    green = randint(1,255)
    blue = randint(1,255)
    waypoint['id'] = id
    waypoint["name"] = name
    waypoint["icon"] = "journeymap:ui/img/waypoint-icon.png"
    waypoint["colorizedIcon"] = "fake:color--16627714-waypoint-icon.png"
    waypoint["x"] = cords[0]
    waypoint["y"] = cords[1]
    waypoint["z"] = cords[2]
    waypoint["r"] = red
    waypoint["g"] = green
    waypoint["b"] = blue
    waypoint["enable"] = True
    waypoint["type"] = "Normal"
    waypoint["origin"] = "journeymap"
    waypoint["dimensions"] = ["minecraft:overworld"]
    waypoint["persistent"] = True
    waypoint["showDeviation"] = False
    waypoint["iconColor"] = -1
    waypoint["customIconColor"] = False
    # print(waypoint)

    with open(f"{argv[2]}/{id}.json", "w") as waypoint_fl:
        waypoint_fl.write(json.dumps(waypoint))


    # print(f"RGB: {red} {green} {blue}")




