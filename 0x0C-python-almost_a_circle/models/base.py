#!/usr/bin/python3
"""define class base"""


class Base:
    """the base of all other classes in this project"""

    __nb_objects = 0

    def __init__(self, id=None):
        """initialization function

        Args:
            id (_type_, optional): _description_. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if not list_dictionaries or list_dictionaries is None:
            return "[]"
        else:
            import json
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        import json
        file = f"{cls.__name__}.json"
        with open(file, 'w') as f:
            if not list_objs:
                f.write('[]')
            else:
                lis = []
                for obj in list_objs:
                    lis.append(obj.to_dictionary())
                f.write(cls.to_json_string(lis))

    @staticmethod
    def from_json_string(json_string):
        import json
        """returns the list of the JSON string representation json_string"""
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        from models.rectangle import Rectangle
        from models.square import Square
        if dictionary.get('width'):
            r = Rectangle(5, 6)
            r.update(**dictionary)
            return r
        if dictionary.get('size'):
            s = Square(5)
            s.update(**dictionary)
            return s

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        from os.path import exists
        import json
        file = f"{cls.__name__}.json"
        if not exists(file):
            return []
        else:
            with open(file, 'r') as f:
                return [cls.create(**instance) for instance in
                        cls.from_json_string(cls.to_json_string(
                            json.load(f)))]
