import unittest
from database import create_connection, execute_query

class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.connection = create_connection()

    def test_connection(self):
        self.assertIsNotNone(self.connection)

    def test_execute_query(self):
        create_table_query = """
        CREATE TABLE IF NOT EXISTS test_table (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL
        )
        """
        execute_query(self.connection, create_table_query)
        self.assertTrue(True)  # If no exceptions are raised, the test passes

if __name__ == '__main__':
    unittest.main()
