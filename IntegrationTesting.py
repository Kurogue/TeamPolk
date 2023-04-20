import unittest
from unittest.mock import Mock
from backend.db import connect
from backend.queries.add_queries import *
from backend.queries.find_queries import *
from backend.queries.delete_queries import *

class IntegrationTesting(unittest.TestCase):    

    def test_integration(self):
        db_mock = connect()
        add_vehicle(db_mock, 'asdfghjklasdfghij', 'Ford', 'Mustang', 2003, 60000, 1, 1, 1, 'yes', 6, 8)
    
        
        add_handling(db_mock, 234, 'Power Steering', 'mechanical device installed on a vehicle ')
        #print handling before deleting it ([(234, 'Power Steering', 'mechanical device installed on a vehicle ')])
        print(find_all_handling(db_mock, 'Power Steering'))
        
        add_interior(db_mock, 123, 'Cloth Seasts', 'd', 'black')
        add_hasInterior(db_mock, 'asdfghjklasdfghij', 123)
        #print vehicle interior before deleting it([('Cloth Seasts', 'd')])
        print(find_vehicle_interior(db_mock, 'asdfghjklasdfghij'))

        add_vehicle(db_mock, 'asdfghjklasdfg123', 'Toyota', 'Corolla', 2022, 4500, 1, 1, 1, 'yes', 7, 2)

        delete_handling(db_mock, 234, 'Power Steering')
        delete_interior(db_mock, 123, 'Cloth Seasts')
        #print handling and interior after deleting them
        print(find_all_handling(db_mock, 'Power Steering'))
        print(find_vehicle_interior(db_mock, 'asdfghjklasdfghij'))
        
        add_customer(db_mock, 'Fiorella', '3600 E', 'frattitamayo@usf.edu', "08-05-2002", '813')
        
        #print customer just added
        print(find_all_customers(db_mock))
        delete_customer(db_mock, 'Fiorella', 'frattitamayo@usf.edu')
        
        
        delete_vehicle(db_mock, 'asdfghjklasdfg123')
        
        #Check if connection closed succesfully
        self.assertEqual(db_mock.closed, 1)


if __name__ == '__main__':
    unittest.main()