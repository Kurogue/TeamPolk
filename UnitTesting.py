import unittest
from backend.db import connect
from backend.queries.add_queries import *
from backend.queries.find_queries import *
from backend.queries.delete_queries import *
from decimal import *
#from backend.queries.vehicle_queries import *

class UnitTesting(unittest.TestCase):

    # Test that statement 1 opens the database connection correctly
    def test_statement_1(self):
        db = connect()
        add_vehicle(db, 'asdfghjklasdfghij', 'Ford', 'Mustang', 2003, 60000, 1, 1, 1, 'no', 6, 8)
        self.assertIsNotNone(db)
        delete_vehicle(db, 'asdfghjklasdfghij')

    # Test that statement 2 prepares the database query correctly    
    def test_statement_2(self):
        db = connect()
        expected_vehicle_info = 'asdfghjklasdfghij', 'Ford', 'Mustang', Decimal('2003'), 60000
        #db = connect()
        add_vehicle(db, 'asdfghjklasdfghij', 'Ford', 'Mustang', '2003', 60000, 1, 1, 1, 'no', 6, 8)
        actual_vehicle_info = find_vehicle(db, 'asdfghjklasdfghij')
        self.assertEqual(expected_vehicle_info, actual_vehicle_info)
        delete_vehicle(db, 'asdfghjklasdfghij')
        
    def test_statement_3(self):
        # Test that statement 3 closes the database connection correctly
        db = connect()
        self.assertRaises(Exception, db.close(), db)

    def test_statement_4(self):
        #Test that statement 4 excecutes series of functions in order
        db = connect()
        add_vehicle(db, 'asdfghjklasdfghij', 'Ford', 'Mustang', '2003', 60000, 1, 1, 1, 'no', 6, 8)

        expected_vehicle_info = find_vehicle_audio(db,'asdfghjklasdfghij')

        add_audio(db, 3, 'AM', 'Amplitude Modified Radio Waves')
        
        self.assertEqual(expected_vehicle_info, ('AM', 'Amplitude Modified Radio Waves'))
        delete_vehicle(db, 'asdfghjklasdfghij')


if __name__ == '__main__':
    unittest.main()