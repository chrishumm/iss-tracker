#!
# iss-tracker-map.py - tracks the location of the ISS in orbit over Earth

import json
import turtle
import urllib.request
import time
import webbrowser
import geocoder


def load_astronaut_api():
    url = "http://api.open-notify.org/astros.json"
    while True:
        try:
            response = urllib.request.urlopen(url) #gets response from the server
            result = json.loads(response.read())
            break
        except:
            print("No server response")
            time.sleep(5)

    g = geocoder.ip('me')

    with open("iss.txt", "w") as file:
        file.write("There are currently " +
            str(result["number"]) + " astronauts on the ISS: \n\n")
        people = result["people"]

        for astronaut in people:
         file.write(astronaut['name'] + " - on board the " +astronaut['craft'] +".\n")

         file.write("\nYour current lat / long is: " + str(g.latlng))
        file.close()

    webbrowser.open("iss.txt")


load_astronaut_api()

# Setup the world map in turtle module
screen = turtle.Screen()
screen.setup(1280, 720)
screen.setworldcoordinates(-180, -90, 180, 90)

# load the world map image
screen.bgpic("map.gif")
screen.register_shape("iss.gif")
screen.register_shape("chris.gif")

iss = turtle.Turtle()

iss_line = turtle.Turtle()
iss_line.fillcolor('red')

iss.shape("iss.gif")


iss.setheading(45)
iss.penup()


while True:
    url = "http://api.open-notify.org/iss-now.json"
    try:
        response = urllib.request.urlopen(url)
        result = json.loads(response.read())
    except:
        print("No server response")
        break

    location = result["iss_position"]
    lat = location['latitude']
    lon = location['longitude']



    # Ouput lon and lat to the terminal
    lat, lon = float(lat), float(lon)
    print("\nLatitude: " + str(lat)+ "\nLongitude: " + str(lon))

    iss.goto(lon, lat)
    iss_line.dot()
    iss_line.penup()

    iss_line.goto(lon,lat)
    time.sleep(1)
