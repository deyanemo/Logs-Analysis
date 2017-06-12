#!/usr/bin/env python2
import psycopg2


class MyDB():

    """
    ------------------------------------------------------------
    |Small Description for creating an instance of the Database |
    ------------------------------------------------------------

    # Create an instance of the Database connection

        deyanemo = MyDB()

    # Call The _db_cur Method to execute command

        deyanemo._db_cur.execute("select * from log limit 1;")

    #And fetchone or fetchall

        res = deyanemo._db_cur.fetchall()

    # print result

        print(res)
    """
    _db_connection = None
    _db_cur = None

    def __init__(self):
        """This function initilize the connection with the
             database"""
        try:
            self._db_connection = psycopg2.connect("dbname=news")
            self._db_cur = self._db_connection.cursor()
        except psycopg2.Error as e:
            raise e

    def close(self):
        """ This Function Closes the conecttion with the
            datsabase"""
        try:
            self._db_connection.close()
            print("Database Closed Savely")
        except psycopg2.Error as e:
            raise e

    def query(self, command):
        """ This Function Execute a SQL query
        Please not : Expection one argument as a command"""
        try:
            self._db_cur.execute(command)
            result = self._db_cur.fetchall()
            return result
        except psycopg2.Error as e:
            raise e
