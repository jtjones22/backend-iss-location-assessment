#!/usr/bin/env python

__author__ = 'Jonathan Jones'

import requests
import turtle
import time


def part_a():
    """
    First we request data from url then turns the data into json.
    Then we loop through the dictionary 'people' and output the craft,
        name and number of astronauts
        in space currently.
    """
    url = 'http://api.open-notify.org/astros.json'
    r = requests.get(url)
    r_dict = r.json()
    for text in r_dict['people']:
        print(text['craft'], text['name'])
    print("Total number of astronauts in space: " + str(r_dict['number']))


def part_b():
    """
    First we request data fron url.
    Then turns received data into json.
    After that we extract the lat and lon as a float.
    Finally we print the results out.
    """
    url = 'http://api.open-notify.org/iss-now.json'
    r = requests.get(url)
    r_dict = r.json()
    latitude = float(r_dict['iss_position']['latitude'])
    longitude = float(r_dict['iss_position']['longitude'])
    print("Timestamp: " + str((r_dict['timestamp'])))
    print("latitude: " + str(r_dict['iss_position']['latitude']))
    print("longitude: " + str(r_dict['iss_position']['longitude']))
    return [longitude, latitude]


def part_c(coords):
    """
    First we create a window.
    Then we adjust the width and height of the window.
    After that we set the background picture to our desired
        image and also register the shape we want to import
        into the shape list.
    Lastly for the windwo we setworldcoords to
        better fit our needs, so our icon position
        is where we want it
    """
    window = turtle.Screen()
    window.setup(width=720, height=360)
    window.bgpic("./map.gif")
    window.register_shape("./iss.gif")
    window.setworldcoordinates(-175, -80, 175, 80)
    """
    We create the icon named bob and
        give bob the shape of our
        image that we registered above.
    We then take away the pen marking from the icon
        so there is no trail when it moves
        to the desired location.
    After that we extract the coords from part_b function,
        and input the return values from that function into
        the x and y.
    Lastly let the turtle module know we are done running it.
    """
    bob = turtle.Turtle()
    bob.shape("./iss.gif")
    bob.penup()
    bob.goto(coords[0], coords[1])
    turtle.done()


def part_d(lat, lon):
    """
    First we request data from the url.
    Then we convert the recieved data into json.
    After that we loop through the json data outputting
        the risetime and duration.
    Lastly we create the screen and icon named bob to output
        the location on the map that we sent in through
        parameters.
    """
    url = f"http://api.open-notify.org/iss-pass.json?lat={lat}&lon={lon}"
    r = requests.get(url)
    r_dict = r.json()
    print("\n" + "Times and duration of iss pass" + "\n")
    for text in r_dict['response']:
        print('risetime:' + time.ctime(text['risetime']))
        print('duration:' + str(text['duration']) + "\n")
    window = turtle.Screen()
    window.setup(width=720, height=360)
    window.bgpic("./map.gif")
    window.setworldcoordinates(178, -84, -178, 84)
    bob = turtle.Turtle()
    bob.penup()
    bob.shape("circle")
    bob.color("yellow")
    bob.shapesize(.2, .2, .2)
    bob.goto(86.1581, 39.7684)
    turtle.done()


def main():
    part_a()
    part_b()
    # part_c(part_b())
    # part_d(39.7684, 86.1581)


if __name__ == '__main__':
    main()
