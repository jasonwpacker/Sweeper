import sys
import sqlite3
from pprint import pprint
import pysftp
import fnmatch
import os


def validate_invocation():
    if len(sys.argv) != 2:
        print("Usage: python sweep.py <configuration>")
        exit(1)
    return sys.argv[1]


def read_config(config_name):
    dbc = sqlite3.connect('./sweeper.db')
    c = dbc.cursor()
    c.execute("Select * from sweeper where name = ?", (config_name,))
    retval = c.fetchall()
    if not retval:
        print(f"No configuration exists under the name {config_name}")
        exit(1)
    return retval


def do_the_thing(config):
    cnopts = pysftp.CnOpts('./keyfile')
    # cnopts.hostkeys.load('./keyfile')
    with pysftp.Connection(config[1], username=config[2], password=config[3], cnopts=cnopts) as sftp:
        sftp.cwd(config[4])
        os.chdir(config[5])
        if(config[6] == 'download'):
            for item in sftp.listdir():
                if fnmatch.fnmatch(item, config[7]):
                    sftp.get(item)
        if(config[6] == 'upload'):
            for item in sftp.listdir():
                if fnmatch.fnmatch(item, config[7]):
                    sftp.put(item)


def main():
    config_name = validate_invocation()
    config = read_config(config_name)
    pprint(config)
    do_the_thing(config[0])


if __name__ == "__main__":
    main()
