import json
from random import randint
from sys import argv
import os

import argparse
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-f", "--file", required=True, help="file of xaeros waypoints")
    ap.add_argument("-fd", "--folder", required=True, help="The folder you want the journeymap waypoints to be saved")
    argv = vars(ap.parse_args())
    
    if os.path.isdir(argv["file"]):
        print("(ERROR) File is a folder")
        return
    if not os.path.exists(argv["file"]):
        print("(ERROR) File Does not exist")
        return
    if not os.path.isdir(argv['folder']):
        print("(ERROR) Path must be folder")
        return
    if not os.path.exists(argv['folder']):
        print("(ERROR) Folder does not exist")
        return
    
    with open(argv["file"], 'r') as waypoints_fl:
        waypoints = waypoints_fl.readlines()
    waypoints_fl.close()
    del waypoints_fl

    waypoints = list(map(lambda point: point.removeprefix("waypoint:").split(":"), waypoints))


    for pointdata in waypoints:
        pointdata.pop(1)
    try:
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

            with open(f"{argv['folder']}/{id}.json", "w") as waypoint_fl:
                waypoint_fl.write(json.dumps(waypoint))
    except Exception as err:
        print("Error while creating file. (probably wrogn format)")
        print(f"Exception: {err}")




if __name__ == "__main__":
    main()
