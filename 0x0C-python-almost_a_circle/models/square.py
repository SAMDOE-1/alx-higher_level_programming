from models.rectangle import Rectangle

"""Defines a square model from rectangle"""


class Square(Rectangle):
    """Square model: rectangle equal sides"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, val):
        self.width = val
        self.height = val

    def __str__(self):
        tmp = super().__str__()
        return tmp[:tmp.rfind('/')]

    def update(self, *args, **kwargs):
        """resets the attributes of self"""

        L = len(args)
        if L:
            if L > 2:
                args = list(args)
                args.insert(1, args[1])
            return super().update(*args)
        if kwargs != {}:
            if 'size' in kwargs:
                _w = kwargs['size']
                del kwargs['size']
                kwargs['width'] = _w
            super().update(**kwargs)

    def to_dictionary(self):
        """Converts self to a dictionary"""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x, "y": self.y
        }

    def to_csv_str(self):
        """returns a csv string of self"""
        fmt = "{},{},{},{}"
        return fmt.format(*(
            self.id, self.size,
            self.x, self.y
        ))
