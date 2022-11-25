#!/usr/bin/python3
import cmd
import re
from models.base_model import BaseModel
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.base_model import BaseModel
from models.user import User
from models import storage

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    '''Console (hbnb) commands '''

    def do_quit(self, line):
        '''Exits the program '''
        return True

    do_EOF = do_quit


    def do_create(self, line):
        '''Creating a new object'''
        if not len(line):
            print("** class name missing **")
            return
        if line not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        object = BaseModel()
        print(object.id)
        object.save()
        
    def do_show(self, line):
        """ show the commands """
        if not len(line):
            print("** class name missing **")
            return
        if line not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if not self.object.id:
            print("** instance id missing **")
            return
        if self.object not in HBNBCommand.classes:
            print("** no instance found**")
            return
        if line not in storage.all().keys():
            print("** no instance found **")
            return
        else:
            print(storage.all()[line])

    def do_destroy(self, line):
        """ deletes instance base on class name """
        if not len(line):
            print("** class name missing **")
            return
        if line not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if not self.object.id:
            print("** instance id missing **")
            return
        if self.object not in HBNBCommand.classes:
            print("** no instance found**")
            return
        if line not in storage.all().keys():
            print("** no instance found **")
            return
        del storage.all()[line]
        storage.save()

    def do_all(self, line):
        """ prints all """
        if not len(line):
            print([i for i in storage.all().values()])
            return
        if line not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        print([i for i in storage.all().values() if line == type(i).__name__])
        

    def do_update(self, line):
        """" updates and object """
        if not len(line):
            print("** class name missing**")
            return
        strings = split(line)
        for string in strings:
            if string.startwith('""') and string.endswith('""'):
                string = string[1:]
        if string[0] not in HBNBCommand.classes:
            print("** instance id missing **")
            return
        if len(strings) == 1:
            print("** instance id missing **")
            return
        key = strings[0] + ',' + strings[1]
        if key not in storage.all().keys():
            print("** no intance found **")
            return
        if len(strings) == 2:
            print("** attribute name missing **")
            return
        if len(strings) == 3:
            print("** value missing **")
            return
        try:
            setattr(storage.all()[key], strings[2], eval(strings[3]))
        except:
            setattr(storage.all()[key], strings[2], strings[3])
      
    def default(self, line):
        """Catch commands if nothing else matches then."""
        self.before(line)

    def before(self, line):
        """Intercepts commands to test for class.syntax()"""
        match = re.search(r"^(\w*)\.(\w+)(?:\(([^)]*)\))$", line)
        if not match:
            return line
        classname = match.group(1)
        method = match.group(2)
        args = match.group(3)
        match_uid_and_args = re.search('^"([^"]*)"(?:, (.*))?$', args)
        if match_uid_and_args:
            uid = match_uid_and_args.group(1)
            attr_or_dict = match_uid_and_args.group(2)
        else:
            uid = args
            attr_or_dict = False

        attr_and_value = ""
        if method == "update" and attr_or_dict:
            match_dict = re.search('^({.*})$', attr_or_dict)
            if match_dict:
                self.update_dict(classname, uid, match_dict.group(1))
                return ""
            match_attr_and_value = re.search(
                '^(?:"([^"]*)")?(?:, (.*))?$', attr_or_dict)
            if match_attr_and_value:
                attr_and_value = (match_attr_and_value.group(
                    1) or "") + " " + (match_attr_and_value.group(2) or "")
        command = method + " " + classname + " " + uid + " " + attr_and_value
        self.onecmd(command)
        return command
        
    def update_dict(self, classname, uid, s_dict):
        """Helper method for update() with a dictionary."""
        s = s_dict.replace("'", '"')
        d = json.loads(s)
        if not classname:
            print("** class name missing **")
        elif classname not in storage.classes():
            print("** class doesn't exist **")
        elif uid is None:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(classname, uid)
            if key not in storage.all():
                print("** no instance found **")
            else:
                attributes = storage.attributes()[classname]
                for attribute, value in d.items():
                    if attribute in attributes:
                        value = attributes[attribute](value)
                    setattr(storage.all()[key], attribute, value)
                storage.all()[key].save()




if __name__ == '__main__':
    HBNBCommand().cmdloop()
