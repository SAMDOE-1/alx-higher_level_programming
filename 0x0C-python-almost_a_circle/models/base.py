#!/usr/bin/python3
import json
import turtle as ttl
from random import random as rn
from time import sleep

"""Defines the base model for all our classes"""


class Base:

    """The Base model for all our classes
    It manages creation of id"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    def validate_size(self, name, val, low=1):
        if not isinstance(val, int):
            raise TypeError(f"{name} must be an integer")
        if val < low:
            op = ">" if low else ">="
            raise ValueError(f"{name} must be {op} {low}")

    def to_csv_str(self):
        """a default csv serializer"""
        return str(self.id)

    def to_json_string(list_dicts: list):
        """Convert to Json strings"""
        if list_dicts is None or list_dicts == []:
            return "[]"
        return json.dumps(list_dicts)

    def from_json_string(json_str):
        """Returns the parsed object"""
        if json_str is None or json_str == '':
            return []
        return json.loads(json_str)

    @classmethod
    def create(cls, **kwargs):
        """Create an instance from a dict"""
        _dummy = cls(1, 1, 1)
        _dummy.update(**kwargs)
        return _dummy

    @classmethod
    def create_csv(cls, *args):
        """Create an instance from a dict"""
        _dummy = cls(1, 1, 1)
        _dummy.update(*args)
        return _dummy

    @classmethod
    def save_to_file(cls, lst_objs: list):
        """save instances to a file"""
        json_str = ""
        if lst_objs is None:
            json_str = "[]"
        else:
            list_dicts = [x.to_dictionary() for x in lst_objs]
            json_str = Base.to_json_string(list_dicts)
        fname = cls.__name__ + ".json"
        with open(fname, "w") as f:
            f.write(json_str)

    @classmethod
    def load_from_file(cls):
        """Loads instances from a file"""
        try:
            fname = cls.__name__ + ".json"
            json_str = ""
            with open(fname, 'r') as f:
                json_str = f.read()
            list_dicts = cls.from_json_string(json_str)
            return list(map(
                lambda x: cls.create(**x),
                list_dicts
            ))
        except FileNotFoundError as fe:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes list of objects"""
        fname = cls.__name__ + ".csv"
        if list_objs is None or list_objs == []:
            csv_str = ''
        else:
            csv_str = '\n'.join(map(
                lambda x: x.to_csv_str(),
                list_objs
            ))
        with open(fname, 'w') as f:
            f.write(csv_str)

    @classmethod
    def load_from_file_csv(cls):
        """de-serializes a csv file"""
        fname = cls.__name__ + ".csv"
        try:
            csv_lines = []
            # read lines from file as array
            with open(fname, 'r') as f:
                csv_lines = f.readlines()
            # split lines by (,)
            # and convert elems to int
            csv_lines = map(
                lambda line: map(int, line.split(",")),
                csv_lines
            )
            return list(map(
                lambda x: cls.create_csv(*x),
                csv_lines
            ))
        except FileNotFoundError as fe:
            return []

    def _draw_shape(shape, pen=ttl.Turtle()):
        """Draws a shape using gui"""
        pen.fillcolor(rn(), rn(), rn())
        pen.up()
        pen.setpos(shape.x * 10, shape.y * 10)
        pen.down()
        sizes = (shape.width * 10, shape.height * 10) * 2

        pen.begin_fill()
        for i in range(4):
            pen.forward(sizes[i])
            pen.right(90)
        pen.end_fill()

    def draw(squares, rectangles):
        """Draw a list of squares and rectangles"""
        shapes = (*squares, *rectangles)
        wn = ttl.Screen()
        wn.title('Squares and Rectangles')
        wn.bgcolor('white')
        pen = ttl.Turtle()
        pen.setpos(0, 0)
        for shape in shapes:
            _draw_shape(shape, pen)
        sleep(10)
        ttl.bye()
