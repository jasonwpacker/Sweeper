Sweeper is a Python implementation of a standard sFTP sweeper.

A sweeper is typically set to run on a periodic schedule, connecting to a set 
sFTP site to check for the presence of new files and download them for processing.

This application leverages Sqlite3 as a basic database to hold configuration records that consist of:
* Name = the name of the configuration and the parameter you pass to the Sweep app when triggering it
* Server = the FQDN or IP address of the server you need to connect to
* User = the username that has rights to that server
* Passwd = the password for that user
* Local = the path on the local machine where the files will be downloaded to, or uploaded from
* Remote = the path on the sFTP server to receive files from or send files to
* Action = currently "download" or "upload" to determine the direction the files flow
* Mask = the file mask used to determime which files are downloaded, like "*.pgp" to only pull down PGP encrypted files

The sweep.py application takes the name of the configuration you want to use as its
only parameter and performs the actions determined by the configuration record 
associated with that name. A second application, sweepadmin.py lets you connect 
to the database to maintain those configuration records from the command line.

Version History:

0.0.1 - the current commit, a baseline minimum viable product as I get my feet back in the water of releasing my own code rather than writing closed source stuff for my employer
