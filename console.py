#!/usr/bin/python3

import cmd
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import re


class HBNBCommand(cmd.Cmd):

    __classes = {'BaseModel': BaseModel, 'User': User, 'State': State, "Amenity": Amenity, "City": City, "Place": Place, "Review": Review}
    
    prompt = '(hbnb) '

    def do_create(self, arg):
        if arg and arg in __class__.__classes.keys():
            temp = __class__.__classes[arg]()
            temp.save()
            storage.reload()
            print(temp.id)
        elif arg and arg not in __class__.__classes.keys():
            print("** class doesn't exist **")
        else:
            print("** class name is missing **")

    def do_show(self, arg=None):
        arg = parse(arg)

        if len(arg) == 2:
            fmt = "{}.{}".format(arg[0], arg[1])

            if arg[0] in __class__.__classes.keys():
                storage.reload()
                temp = storage._FileStorage__objects

                if fmt in temp.keys():
                    print(temp[fmt])
                    #storage.reload()
                else:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")

        elif len(arg) == 1 and arg[0] in __class__.__classes.keys():
            print("** instance id missing **")

        elif len(arg) == 0:
            print("** class name missing **")
            
    def do_destroy(self, arg):
        arg = parse(arg)

        if len(arg) == 2:
            fmt = "{}.{}".format(arg[0], arg[1])

            if arg[0] in __class__.__classes.keys():
                storage.reload()
                temp = storage._FileStorage__objects

                if fmt in temp.keys():
                    del(storage._FileStorage__objects[fmt])
                    storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")

        elif len(arg) == 1 and arg[0] in __class__.__classes.keys():
            print("** instance id missing **")

        elif len(arg) == 0:
            print("** class name missing **")

    def do_all(self, arg):
        arg = parse(arg)
        storage.reload()
        temp = storage._FileStorage__objects

        if len(arg) == 1:
            if arg[0] in __class__.__classes.keys():
                for k, v in temp.items():
                    if k.split('.')[0] == arg[0]:
                        print(v)
            else:
                print("** class doesn't exist **")
        elif len(arg) == 0:
            for k, v in temp.items():
                print(v)

    def do_update(self, arg):
        arg = parse(arg)
        storage.reload()
        temp = storage._FileStorage__objects

        if len(arg) == 0:
            print("** class name mising **")
        elif len(arg) == 1:
            if arg[0] not in __class__.__classes:
                print("** class doesn't exist **")
            else:
                print("** instance id missing **")
        elif len(arg) == 2:
            if arg[0] in __class__.__classes:
                fmt = "{}.{}".format(arg[0], arg[1])
                if fmt not in temp.keys():
                    print("** no instance found **")
                else:
                    print("** attribute name missing **")
            else:
                print("** class doesn't exist **")
        elif len(arg) == 3:
            if arg[0] in __class__.__classes:
                fmt = "{}.{}".format(arg[0], arg[1])
                if fmt not in temp.keys():
                    print("** no instance found **")
                else:
                    print("** value missing **")
            else:
                print("** class doesn't exist **")
        elif len(arg) >= 4:
            if arg[0] in __class__.__classes:
                fmt = "{}.{}".format(arg[0], arg[1])
                if fmt in temp.keys():
                    temp[fmt].__dict__.update({arg[2]: arg[3]})
                    storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")

    def do_count(self, arg):
        arg = parse(arg)
        storage.reload()
        temp = storage._FileStorage__objects
        count = 0
        if arg[0] in __class__.__classes:
            for k, v in temp.items():
                if k.split('.')[0] == arg[0]:
                    count += 1
        print(count)

    def do_User(self, arg):
        name = 'User'
        args = parse2(name, arg)
        if arg == ".all()":
            __class__.do_all(self, arg=name)                   
        elif arg == ".count()":
            __class__.do_count(self, arg=name)
        elif arg[0:5] == ".show":
            __class__.do_show(self, arg=args)
        elif arg[0:8] ==  ".destroy":
            __class__.do_destroy(self, arg=args)
        elif arg[0:7] == ".update":
            __class__.do_update(self, args)

    def do_Amenity(self, arg):
        name = 'Amenity'
        args = parse2(name, arg)
        if arg == ".all()":
            __class__.do_all(self, arg=name)                   
        elif arg == ".count()":
            __class__.do_count(self, arg=name)
        elif arg[0:5] == ".show":
            __class__.do_show(self, arg=args)
        elif arg[0:8] ==  ".destroy":
            __class__.do_destroy(self, arg=args)
        elif arg[0:7] == ".update":
            __class__.do_update(self, args)

    def do_BaseModel(self, arg):
        name = 'BaseModel'
        args = parse2(name, arg)
        if arg == ".all()":
            __class__.do_all(self, arg=name)                   
        elif arg == ".count()":
            __class__.do_count(self, arg=name)
        elif arg[0:5] == ".show":
            __class__.do_show(self, arg=args)
        elif arg[0:8] ==  ".destroy":
            __class__.do_destroy(self, arg=args)
        elif arg[0:7] == ".update":
            __class__.do_update(self, args)

    def do_City(self, arg):
        name = 'City'
        args = parse2(name, arg)
        if arg == ".all()":
            __class__.do_all(self, arg=name)                   
        elif arg == ".count()":
            __class__.do_count(self, arg=name)
        elif arg[0:5] == ".show":
            __class__.do_show(self, arg=args)
        elif arg[0:8] ==  ".destroy":
            __class__.do_destroy(self, arg=args)
        elif arg[0:7] == ".update":
            __class__.do_update(self, args)

    def do_Place(self, arg):
        name = 'Place'
        args = parse2(name, arg)
        if arg == ".all()":
            __class__.do_all(self, arg=name)                   
        elif arg == ".count()":
            __class__.do_count(self, arg=name)
        elif arg[0:5] == ".show":
            __class__.do_show(self, arg=args)
        elif arg[0:8] ==  ".destroy":
            __class__.do_destroy(self, arg=args)
        elif arg[0:7] == ".update":
            __class__.do_update(self, args)

    def do_Review(self, arg):
        name = 'Review'
        args = parse2(name, arg)
        if arg == ".all()":
            __class__.do_all(self, arg=name)                   
        elif arg == ".count()":
            __class__.do_count(self, arg=name)
        elif arg[0:5] == ".show":
            __class__.do_show(self, arg=args)
        elif arg[0:8] ==  ".destroy":
            __class__.do_destroy(self, arg=args)
        elif arg[0:7] == ".update":
            __class__.do_update(self, args)

    def do_State(self, arg):
        name = 'State'
        args = parse2(name, arg)
        if arg == ".all()":
            __class__.do_all(self, arg=name)                   
        elif arg == ".count()":
            __class__.do_count(self, arg=name)
        elif arg[0:5] == ".show":
            __class__.do_show(self, arg=args)
        elif arg[0:8] ==  ".destroy":
            __class__.do_destroy(self, arg=args)
        elif arg[0:7] == ".update":
            __class__.do_update(self, args)

    def do_EOF(self, line):
        """end-of-file marker to exit program cleanly\n"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True

    def emptyline(self):
        pass

    def postloop(self):
        print

def parse(arg):
    return tuple(arg.split())

def parse2(name, arg):
    strs = re.findall('\((.+?)\)', arg)
    new_str = name + ' ' + ' '.join(strs)
    new_str = new_str.replace('"', "")
    new_str = new_str.replace("'", "")
    new_str = new_str.replace(',', "")
    return new_str


if __name__ == "__main__":
    HBNBCommand().cmdloop()
