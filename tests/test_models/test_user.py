#!/usr/bin/python3
""" """
from models.user import User
import unittest
import os
import MySQLdb

conn_params = {
    'user': os.getenv("HBNB_MYSQL_USER"),
    'passwd': os.getenv("HBNB_MYSQL_PWD"),
    'host': os.getenv("HBNB_MYSQL_HOST"),
    'db': os.getenv("HBNB_MYSQL_DB"),
    'port': 3306
}

class test_User(unittest.TestCase):
    """ """
    
    cursor = None
    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User
    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == 'db', "not testing fl storage")
    def test_first_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.first_name), str)
    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == 'db', "not testing fl storage")
    def test_last_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.last_name), str)
    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == 'db', "not testing fl storage")
    def test_email(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.email), str)
    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == 'db', "not testing fl storage")
    def test_password(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.password), str)
        
    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") != 'db', "not testing db storage")
    def setUp(self):
        conn = MySQLdb.connect(**conn_params)
        test_User.cursor = conn.cursor()
        query = "CREATE DATABASE IF NOT EXISTS hbnb_test_db"
        test_User.cursor.execute(query)


    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") != 'db', "not testing db storage")
    def test_sql(self):
        
        query = "SELECT COUNT(*) FROM users"
        test_User.cursor.execute(query)
        self.assertEqual(0, list(test_User.cursor)[0][0])
    

