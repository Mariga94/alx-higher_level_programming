#!/usr/bin/python3
"""Defines a Base class"""
import json
import csv
import turtle


class Base:
    """Represents a Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize data

        Args:
            id (int): id of object
        """
        if id is not None:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects

    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs"""
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return a class instantiate from a dictionary of attributes"""
        if dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """Return  a list of classes instantiated from
            a file of JSON strings
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dict = Base.from_json_string(jsonfile.read())
                return [cls.create(**f) for f in list_dict]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV serialization of a list of objects to a file"""
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                edit = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for item in list_objs:
                    edit.writerow(item.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of classes instantiated from a CSV file"""

        filename = cls.__name__ + "csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dict = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dict = [
                        dict([key, int(value)] for key, value in d.items())
                        for d in list_dict]
                return [cls.create(**f) for f in list_dict]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using turtle
        """
        tp = turtle.Turtle()
        tp.screen.bgcolor("#00FFFF")
        tp.pensize(1)
        tp.shape("turtle")
        tp.color("#000000")

        for r in list_rectangles:
            tp.st()
            tp.up()
            tp.goto(r.x, r.y)
            tp.down()
            for i in range(2):
                tp.forward(r.width)
                tp.left(90)
                tp.forward(r.height)
                tp.left(90)
            tp.hideturtle()

        tp.color("#00ff33")
        for s in list_squares:
            tp.st()
            tp.up()
            tp.goto(s.x, s.y)
            tp.down()
            for i in range(2):
                tp.forward(s.width)
                tp.left(90)
                tp.forward(s.height)
                tp.left(90)
            tp.hideturtle()

        tp.exitonclick()
