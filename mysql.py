import os
import MySQLdb as db
from credentials import *
#import numpy as np
from time import strptime

def push_MySQL(sql):
    """
    Implements execution of changes on the MySQL server
    """
    #make connection with db
    d = db.connect(host, user_id, password, user_db)

    # prepare a cursor object using cursor() method
    cursor = d.cursor()
    try:
        #Execute the SQL command
        cursor.execute(sql)
    except db.Error, e:
        try:
            print "MySQL Error [%d]: %s" % (e.args[0], e.args[1])
        except IndexError:
            print "MySQL Error: %s" % str(e)
    d.close()

def pull_MySQL(sql):
    """
    Implements getting data from the MySQL server
    """
    #make connection with db
    d = db.connect(host, user_id, password, user_db)

    # prepare a cursor object using cursor() method
    cursor = d.cursor()
    try:
        #Execute the SQL command
        cursor.execute(sql)
        #create list of first field in tuple
        data = [item[0] for item in cursor.fetchall()]
        return data

    except db.Error, e:
        try:
            print "MySQL Error [%d]: %s" % (e.args[0], e.args[1])
        except IndexError:
            print "MySQL Error: %s" % str(e)
    d.close()

def get_existing_files():
    """
    Get list of all existing files
    """
    sql = "SELECT logfile,sid FROM Sessions"
    ingested = pull_MySQL(sql)
    return ingested

def truncate_table(table):
    """
    Truncate given table
    """
    sql = "TRUNCATE TABLE %s" % (table)

    push_MySQL(sql)


def get_local_logs(path_files):

    allfiles = os.listdir(path_files)
    logs = [x for x in allfiles if x.endswith("xpd")]
    return logs


class Logfile:
    def __init__(self, file_name):
        self.name = file_name
        print "start ingesting ", self.name
        full_path = path_files + self.name

        with open(full_path) as f:
            self.lis = [line.split() for line in f]        # create a list of lists

        #datetime
        month = strptime(self.lis[1][2],'%b').tm_mon
        str_month = str(month)
        if len(str_month) < 2:
            str_month = "0" + str_month
        self.datetime = self.lis[1][4] + '-' + str_month + '-' + self.lis[1][3] + ' ' + self.lis[1][5]

        #sid
        self.sid = self.lis[9][2]

        #header
        self.header = self.lis[10][0].split(',')

        #data
        self.data = list()
        for i,x in enumerate(self.lis):
            if (i > 10):
                self.data.append(x[0].split(','))

    def __del__(self):
        print "Closing " , self.name

    def log_session(self):
        """
        Implements logging of data export in Sessions table
        """
        sql = "INSERT INTO Sessions(logfile, sid, dateTested, dateIngested) VALUES ('%s', '%s', '%s', NOW())" % (self.name, self.sid, self.datetime)
        push_MySQL(sql)

    def export_raw_data(self):
        """
        Implements exporting raw data to MySQL table "Raw"
        """
        sql = "SELECT id FROM Sessions WHERE logfile = '%s'" % (self.name)
        session_id = pull_MySQL(sql)

        # Prepare SQL query to INSERT a record into the database.
        for ind in range(0, len(self.data)-1):
            sql = "INSERT INTO Raw (id, trial, clef, note, expected, hit, rt) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (str(session_id[0]), self.data[ind][1],self.data[ind][2],self.data[ind][3],self.data[ind][4],self.data[ind][5],self.data[ind][6])
            push_MySQL(sql)


#Script begins here

#truncate_table('Sessions')

#truncate_table('Raw')

ingested = get_existing_files()

logfiles = get_local_logs(path_files)

newlogfiles = [x for x in logfiles if x not in ingested]

<<<<<<< HEAD
for el in newlogfiles:
    l = Logfile(el)
    l.log_session()
    l.export_raw_data()
=======
if (len(newlogfiles) > 0):
    for el in newlogfiles:
        l = Logfile(el)
        l.log_session()
        l.export_raw_data()
else:
     print "all files are already ingested"

>>>>>>> origin/master
#print(l)


