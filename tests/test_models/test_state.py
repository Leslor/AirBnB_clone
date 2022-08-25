#!/usr/bin/python3
""" """
import subprocess
import MySQLdb
import unittest
import os

conn_params = {
    'user': os.getenv("HBNB_MYSQL_USER"),
    'passwd': os.getenv("HBNB_MYSQL_PWD"),
    'host': os.getenv("HBNB_MYSQL_HOST"),
    'db': os.getenv("HBNB_MYSQL_DB"),
    'port': 3306
}


class test_state(unittest.TestCase):
    """ """
    cursor = None

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") != 'db', "not testing fl storage")
    def setUp(self):
        conn = MySQLdb.connect(**conn_params)
        test_state.cursor = conn.cursor()
        query = "CREATE DATABASE IF NOT EXISTS hbnb_test_db"
        test_state.cursor.execute(query)


    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") != 'db', "not testing fl storage")
    def test_sql(self):
        
        query = "SELECT COUNT(*) FROM states"
        test_state.cursor.execute(query)
        self.assertEqual(0, list(test_state.cursor)[0][0])

