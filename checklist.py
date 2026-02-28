# This is the Checklist class for the checklist on the users dashboard
import sys
import os
# import database files
sys.path.append(os.path.join(os.path.dirname(__file__)), 'database')
import db

class Checklist:

    # checklist class constructor
    def __init__(self):

        self.task = []

        self.Get_Tasks_From_DB()


    def Get_Tasks_From_DB(self):

        tasks_db = db
