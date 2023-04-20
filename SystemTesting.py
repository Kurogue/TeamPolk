import unittest
from backend.db import connect
from backend.queries.add_queries import *
from backend.queries.find_queries import *
from backend.queries.delete_queries import *
from decimal import *
import time

class SystemTesting(unittest.TestCase):
    # Test that pushes the system to its limits
    def test_statement_1(self):
        start_time = time.time()
        db = connect()
        add_vehicle(db, '1sdfghjklasdfghij', 'Ford', 'Mustang', 2003, 60000, 1, 1, 1, 'no', 6, 8)

        db.close()
        self.assertEqual(db.closed, 1)
        print("--- %s seconds ---" % (time.time() - start_time))

    def test_statement_2(self):
        start_time = time.time()
        db = connect()
        for vehicle in range(1,99):
            if vehicle > 9:
                id = str(vehicle)
                id = id +'dfghjklasdfghij'
            else:
                id = str(vehicle)
                id = id +'sdfghjklasdfghij'
            
            add_vehicle(db, id, 'Ford', 'Mustang', 2003, 60000, 1, 1, 1, 'no', 6, 8)


        db.close()
        self.assertEqual(db.closed, 1)
        print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == '__main__':
    unittest.main()
