## This is the file that will manage the services layer, once I add that.

## This is where I can implement my use cases, which will in turn call the other data that has been written.
## I will wait to write code here until after I have reviewed Unit 5.  I think checking out the Week 5 branch of the
## Sanskrit course demo could help here too:
## https://github.com/jjberry-508/sanskrit-508/blob/week5/app/services.py

import db.mysql_repository

class Services:

    ## Init code shamelessly ripped off from the course Sanskrit code :)
    def __init__(self):
        self.repo = db.mysql_repository.MysqlRepository()

    ### USE CASE 4: Returns the origin of the word entered ###
    def find_word_origin(self, word):
        raise NotImplementedError