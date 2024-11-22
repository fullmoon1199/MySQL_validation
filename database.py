import pymysql
import openpyxl

class Database:
    def __init__(self):
        self.connection = self.connect_to_database()
        self.read_data_from_excel()

    def read_data_from_excel(self):
        workbook = openpyxl.load_workbook('./ExynosAutoV920_Validation_IR241007_103552_LA.xlsx')

        sheet = workbook['User_Scenario']

        cell_value = sheet['A5'].value

        print(f"cell_value = {cell_value}")

    def connect_to_database(self):
        connection = pymysql.connect(
            host='127.0.0.1',
            user='root',
            password='atk1703825!',
            database='validation_modi',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
        return connection

    def execute_query(self, query, params=None):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, params)
                result = cursor.fetchall()
            self.connection.commit()
        except Exception as e:
            print(f"Error executing query: {e}")
            result = []
        return result

    def close_connection(self):
        if self.connection:
            self.connection.close()

    def insert_test_case(self, tc_id, category_id, title):
        try:
            with self.connection.cursor() as cursor:
                sql = "INSERT INTO test_case (tc_id, category_id, title) VALUES (%s, %s, %s)"
                cursor.execute(sql, (tc_id, category_id, title))
            self.connection.commit()
        except Exception as e:
            print(f"Error inserting test case: {e}")

    def get_test_results(self):
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT * FROM test_result"
                cursor.execute(sql)
                results = cursor.fetchall()
            return results
        except Exception as e:
            print(f"Error getting test results: {e}")
            return []

if __name__ == "__main__":
    db = Database()
#     query = "DESC board"
#     results = db.execute_query(query)
#     for row in results:
#         print(row)
#     db.close_connection()