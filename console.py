#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
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
        if not len(line):
            print([i for i in storage.all().values()])
            return
        if line not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        print([i for i in storage.all().values()] if line == type(i).__name__])

    def do_update(self, line):
        """" updates and object """
        if not len(line):
            print("** class name missing**")
            return
        strings = split(line)
        for string in strings:
            if string.startwith('""') and string.endswith('""'):
                string = string[1:]
        if string[0[ not in HBNBCommand.classes:
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
    


if __name__ == '__main__':
    HBNBCommand().cmdloop()
