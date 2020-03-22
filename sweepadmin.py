import sqlite3
from pprint import pprint


class Config():
    def __init__(self, name):
        self.name = name


def get_command():
    retval = ""
    while retval.upper() not in ('L', 'A', 'D', 'Q'):
        print("\n\nPlease make a selection from the following choices:\n")
        print("[L]ist all configurations")
        print("[A]dd a new configuration")
        print("[D]elete a configuration")
        print("[Q]uit")
        retval = input(">>>")
    return retval.upper()


def connect_db():
    try:
        retval = sqlite3.connect('./sweeper.db')
        return retval
    except:
        print("Unable to connect to the database")
        exit(1)


def execute_command(cmd, dbc):
    if cmd == 'Q':
        exit()
    if cmd == 'L':
        list_all_configurations(dbc)
    if cmd == 'D':
        delete_config(dbc)
    if cmd == 'A':
        add_new_config(dbc)


def delete_config(dbc):
    name = input("Enter configuration name to delete: ")
    query = dbc.cursor()
    query.execute('delete from sweeper where name = ?', (name,))
    dbc.commit()


def list_all_configurations(dbc):
    query = dbc.cursor()
    query.execute('select * from sweeper;')
    for retval in query.fetchall():
        retval = dict(zip(('name', 'server', 'user', 'password', 'local path',
                           'remote path', 'action', 'file mask'), retval))
        pprint(retval)


def add_new_config(dbc):
    new_name = input("Configuration Name: ")
    query = dbc.cursor()
    query.execute('select * from sweeper where name = ?', (new_name,))
    retval = query.fetchall()

    if retval:
        print(f"{new_name} already exists. To edit, select 'E' from the menu.")
        return

    new_server = input("Server: ")
    new_user = input("User: ")
    new_password = input("Password: ")
    new_remote = input("Remote Path: ")
    new_local = input("Local Path: ")
    new_action = input("Action: ")
    new_mask = input("File Mask: ")

    query.execute('insert into sweeper values (?, ?, ?, ?, ?, ?, ?, ?)',
                  (new_name, new_server, new_user, new_password, new_remote, new_local, new_action, new_mask))
    dbc.commit()


def main():
    dbc = connect_db()
    while True:
        cmd = get_command()
        execute_command(cmd, dbc)


if __name__ == "__main__":
    main()
