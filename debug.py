
import skills
import database
from skills import *

width = 80


def show_disabled_skills():
    print("-" * width)
    try:
        mod = glob.glob(join(dirname(__file__), "skills/*.py"))
        all_skills = [basename(f)[:-3] for f in mod if isfile(f) and not f.endswith('__init__.py')]
        enabled_mod = [x for x in all_skills if eval(x + ".enable")]
        disabled_mod = [x for x in all_skills if not eval(x + ".enable")]
        print("ENABLED MODULES:")
        for mod in enabled_mod:
            print("\t" + mod)
        print("DISABLED MODULES:")
        for mod in disabled_mod:
            print("\t" + mod)
    except AttributeError as e:
        print(e)
    print("-" * width)


def show_all_commands():
    print("-" * width)
    print("COMMANDS:")
    for command in skills.get_all_commands():
        print(command)
    print("-" * width)


def show_all_commands_sorted():
    print("-" * width)
    print("SORTED COMMANDS:")
    for command in sorted(skills.get_all_commands()):
        print(command)
    print("-" * width)


def show_all_commands_sorted_by_length():
    print("-" * width)
    print("SORTED COMMANDS BY LENGTH:")
    for command in sorted(skills.get_all_commands(), key=len, reverse=True):
        print(command)
    print("-" * width)


def show_commands_list():
    print("-" * width)
    print("COMMANDS LIST:")
    commands_list = sorted(skills.get_commands_list(), key=len)
    for module_func_commands in commands_list:
            print(module_func_commands)
    print("-" * width)


def show_all_configurations():
    pass


def show_commands_database():
    print("-" * width)
    commands = database.CommandDatabase()
    commands.print_all_commands()
    print("-" * width)


show_all_commands()
show_all_commands_sorted()
show_all_commands_sorted_by_length()
show_disabled_skills()
show_commands_database()
show_commands_list()
