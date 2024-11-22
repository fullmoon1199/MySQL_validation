import sys
import openpyxl
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QListView, QTableWidgetItem
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import Qt
from mainwindow_ui import Ui_MainWindow
from add_result_ui import Ui_Form as AddResultForm
from add_tc_ui import Ui_Form as AddTcForm
from database import Database

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.database = Database()
        self.load_data()
        self.refresh_window()

        self.init_add_tc_form()
        self.init_results_form()

        self.ui.search_result_button.clicked.connect(self.search_test_results)

    def init_results_form(self):
        self.add_result_popup = QWidget()
        self.add_result_form = AddResultForm()
        self.add_result_form.setupUi(self.add_result_popup)
        self.ui.add_result_button.clicked.connect(self.show_add_result_popup)
        self.add_result_form.bsp_listView.clicked.connect(self.on_bsp_item_clicked)
        self.add_result_form.tc_listView.clicked.connect(self.on_tc_item_clicked)
        self.add_result_form.board_listView.clicked.connect(self.on_board_item_clicked)
        self.add_result_form.tag_listView.clicked.connect(self.on_tag_item_clicked)
        self.add_result_form.add_button.clicked.connect(self.add_result)
        self.add_result_form.add_tag_button.clicked.connect(self.add_tag)

    def refresh_window(self):
        self.load_tag_combobox()
        self.load_bsp_combobox()
        self.load_board_combobox()

    def search_test_results(self):
        bsp_name = self.ui.bsp_comboBox.currentText()
        board_name = self.ui.board_comboBox.currentText()
        release_date = self.ui.tag_comboBox.currentText()

        query = """
            SELECT test_case.tc_id, category.category_name, test_case.sub_category, test_case.title, test_case.status, test_case.domain, test_case.pre_condition, test_case.test_sequence, test_case.pass_criteria, test_case.linked_work_items, test_case.comment, result.result
            FROM test_case
            JOIN category
            ON test_case.category_id = category.category_id
            JOIN result
            ON test_case.test_case_id = result.test_case_id
            JOIN `release`
            ON result.release_id = `release`.release_id
            JOIN bsp
            ON `release`.bsp_id = bsp.bsp_id
            JOIN board
            ON `release`.board_id = board.board_id
            WHERE bsp.bsp_name = %s
            AND board.board_name = %s
            AND `release`.release_date = %s;
        """
        results = self.database.execute_query(query, (bsp_name, board_name, release_date))

        self.ui.result_tableWidget.setRowCount(0)
        self.ui.result_tableWidget.setColumnCount(12)
        self.ui.result_tableWidget.setHorizontalHeaderLabels(['ID', 'Category', 'Sub Category', 'Title', 'Status', 'Domain', 'Pre-Condition', 'Test Sequence', 'Pass Criteria', 'Linked Work Items', 'Comment', 'result'])

        for row_number, row_data in enumerate(results):
            self.ui.result_tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data.values()):
                self.ui.result_tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def load_tag_combobox(self):
        print("Loading tag combobox")
        query = """
        SELECT DISTINCT release_date
        FROM `release`
        ORDER BY release_date;
        """
        results = self.database.execute_query(query)
        self.ui.tag_comboBox.clear()
        for row in results:
            self.ui.tag_comboBox.addItem(row['release_date'])

    def load_bsp_combobox(self):
        query = "SELECT * FROM bsp"
        results = self.database.execute_query(query)
        self.ui.bsp_comboBox.clear()
        for row in results:
            self.ui.bsp_comboBox.addItem(row['bsp_name'])

    def load_board_combobox(self):
        query = "SELECT * FROM board"
        results = self.database.execute_query(query)
        self.ui.board_comboBox.clear()
        for row in results:
            self.ui.board_comboBox.addItem(row['board_name'])

    def add_tag(self):
        tag_name = self.add_result_form.tag_lineEdit.text()
        query = """
        INSERT INTO `release` (release_date, bsp_id, board_id)
        SELECT %s, bsp.bsp_id, board.board_id
        FROM bsp
        CROSS JOIN board;
        """
        self.database.execute_query(query, (tag_name,))
        self.load_tag_data()

    def find_release_id(self):
        board_id = self.add_result_form.label_3.text().split(":")[1].strip()
        bsp_id = self.add_result_form.label.text().split(":")[1].strip()
        release_date = self.add_result_form.label_4.text().split(":")[1].strip()
        print(f"Board ID: {board_id}, BSP ID: {bsp_id}, Release Date: {release_date}")
        query = """
                SELECT `release`.release_id
                FROM `release`
                JOIN bsp
                ON `release`.bsp_id = bsp.bsp_id
                JOIN board
                ON `release`.board_id = board.board_id
                WHERE bsp.bsp_name = %s AND board.board_name = %s AND `release`.release_date = %s;
                """
        result = self.database.execute_query(query, (bsp_id, board_id, release_date))
        if result:
            return result[0]['release_id']
        return None

    def load_add_tc_board_combobox(self):
        query = "SELECT * FROM board"
        results = self.database.execute_query(query)
        self.add_tc_form.add_tc_board_comboBox.clear()
        for row in results:
            self.add_tc_form.add_tc_board_comboBox.addItem(row['board_name'])

    def load_add_tc_bsp_combobox(self):
        query = "SELECT * FROM bsp"
        results = self.database.execute_query(query)
        self.add_tc_form.add_tc_bsp_comboBox.clear()
        for row in results:
            self.add_tc_form.add_tc_bsp_comboBox.addItem(row['bsp_name'])

    def load_add_tc_tag_comboBox(self):
        query = """
        SELECT DISTINCT release_date
        FROM `release`
        ORDER BY release_date;
        """
        results = self.database.execute_query(query)
        self.add_tc_form.add_tc_tag_comboBox.clear()
        for row in results:
            self.add_tc_form.add_tc_tag_comboBox.addItem(row['release_date'])

    def add_result(self):
        print("Adding result")
        if self.add_result_form.pass_button.isChecked():
            result = 'PASS'
        elif self.add_result_form.fail_button.isChecked():
            result = 'FAIL'
        elif self.add_result_form.na_button.isChecked():
            result = 'SKIP'
        else:
            return
        test_case_id = self.find_test_case_id(self.add_result_form.label_2.text().split(":")[1].strip())
        release_id = self.find_release_id()
        print(f"Result: {result}, Test Case ID: {test_case_id}, Release ID: {release_id}")
        query = """
            INSERT INTO result
            (result, release_id, test_case_id)
            VALUES (%s, %s, %s)
        """
        self.database.execute_query(query, (result, release_id, test_case_id))

    def init_add_tc_form(self):
        self.add_tc_popup = QWidget()
        self.add_tc_form = AddTcForm()
        self.add_tc_form.setupUi(self.add_tc_popup)
        self.ui.add_tc_button_2.clicked.connect(self.show_add_tc_popup)
        self.add_tc_form.add_tc_button.clicked.connect(self.add_test_case)
        self.add_tc_form.auto_tc_pushButton.clicked.connect(self.auto_add_test_case)

    def on_tag_item_clicked(self, index):
        tag_name = index.data(Qt.DisplayRole)
        print(f"tag: {tag_name}")
        self.add_result_form.label_4.setText(f"tag: {tag_name}")

    def on_board_item_clicked(self, index):
        board_name = index.data(Qt.DisplayRole)
        print(f"Board Name: {board_name}")
        self.add_result_form.label_3.setText(f"board: {board_name}")

    def on_bsp_item_clicked(self, index):
        bsp_name = index.data(Qt.DisplayRole)
        print(f"BSP Name: {bsp_name}")
        # self.load_bsp_data()
        self.load_tc_for_bsp(bsp_name)
        self.add_result_form.label.setText(f"bsp : {bsp_name}")
        self.add_result_form.label_2.setText(f"TC :")

    def on_tc_item_clicked(self, index):
        tc_id = index.data(Qt.DisplayRole)
        print(f"TC ID: {tc_id}")
        self.add_result_form.label_2.setText(f"TC : {tc_id}")

    def load_tc_for_bsp(self, bsp_name):
        query = """
                select result.result_id, result.result, result.release_id, result.test_case_id, `release`.release_date, bsp.bsp_name, board.board_name, test_case.tc_id from result
                join `release`
                on result.release_id = `release`.release_id
                join bsp
                on bsp.bsp_id = `release`.bsp_id
                join board
                on board.board_id = `release`.board_id
                join test_case
                on test_case.test_case_id = result.test_case_id
                where bsp.bsp_name = %s and board.board_name = %s and `release`.release_date = %s;
        """
        results = self.database.execute_query(query, (bsp_name, self.add_result_form.label_3.text().split(":")[1].strip(), self.add_result_form.label_4.text().split(":")[1].strip()))
        model = QStandardItemModel()
        for row in results:
            item = QStandardItem(row['tc_id'])
            model.appendRow(item)
        self.add_result_form.tc_listView.setModel(model)


    def show_add_result_popup(self):
        # self.load_tag_data()
        self.load_bsp_data()
        self.load_board_data()
        self.load_tag_data()
        self.add_result_popup.show()

    def load_board_data(self):
        query = "SELECT * FROM board"
        results = self.database.execute_query(query)
        model = QStandardItemModel()
        for row in results:
            item = QStandardItem(row['board_name'])
            item.setData(row['board_id'], 1)
            model.appendRow(item)
        self.add_result_form.board_listView.setModel(model)

    def load_bsp_data(self):
        query = "SELECT * FROM bsp"
        results = self.database.execute_query(query)
        model = QStandardItemModel()
        for row in results:
            item = QStandardItem(row['bsp_name'])
            item.setData(row['bsp_id'], 1)
            model.appendRow(item)
            print(row)
        self.add_result_form.bsp_listView.setModel(model)

    def load_tag_data(self):
        query = """
        SELECT DISTINCT release_date
        FROM `release`
        ORDER BY release_date;
        """
        results = self.database.execute_query(query)
        model = QStandardItemModel()
        for row in results:
            item = QStandardItem(row['release_date'])
            model.appendRow(item)
        self.add_result_form.tag_listView.setModel(model)

    def load_tc_list_data(self):
        query = "SELECT * FROM test_case"
        results = self.database.execute_query(query)
        model = QStandardItemModel()
        for row in results:
            item = QStandardItem(row['title'])
            model.appendRow(item)

    def add_tc(self, tc_id, category_name, sub_category_name, title, status, domain, pre_condition, test_sequence, pass_criteria, link_work, comment, board_name, bsp_name, release_date):
        board_name = self.add_tc_form.add_tc_board_comboBox.currentText()
        bsp_name = self.add_tc_form.add_tc_bsp_comboBox.currentText()
        release_date = self.add_tc_form.add_tc_tag_comboBox.currentText()
        category_query = "SELECT category_id FROM category WHERE category_name = %s"
        category_result = self.database.execute_query(category_query, (category_name,))
        if category_result:
            category_id = category_result[0]['category_id']
        else:
            insert_category_query = "INSERT INTO category (category_name) VALUES (%s)"
            self.database.execute_query(insert_category_query, (category_name,))
            category_id_query = "SELECT category_id FROM category WHERE category_name = %s"
            category_result = self.database.execute_query(category_id_query, (category_name,))
            if category_result:
                category_id = category_result[0]['category_id']
            else:
                print("Failed to retrieve category ID after insertion.")
                return
        if category_id:
            query = """
                INSERT INTO test_case
                (tc_id, category_id, sub_category, title, status, domain, pre_condition, test_sequence, pass_criteria, linked_work_items, comment)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            self.database.execute_query(query, (tc_id, category_id, sub_category_name, title, status, domain, pre_condition, test_sequence, pass_criteria, link_work, comment))
        else:
            print("Invalid category")
        query = """
                SELECT test_case_id
                FROM test_case
                WHERE tc_id = %s
                AND category_id = %s
                AND title = %s
                AND sub_category = %s
                AND status = %s
                AND domain = %s
                AND pre_condition = %s
                AND test_sequence = %s
                AND pass_criteria = %s
                AND linked_work_items = %s
                AND comment = %s
        """
        add_test_case_id = self.database.execute_query(query, (tc_id, category_id, sub_category_name, title, status, domain, pre_condition, test_sequence, pass_criteria, link_work, comment))
        print(f"Test Case ID: {add_test_case_id}")
        query = """
                SELECT `release`.release_id
                FROM `release`
                JOIN bsp
                ON `release`.bsp_id = bsp.bsp_id
                JOIN board
                ON `release`.board_id = board.board_id
                WHERE bsp.bsp_name = %s
                AND board.board_name = %s
                AND `release`.release_date = %s;
        """
        release_id = self.database.execute_query(query, (bsp_name, board_name, release_date))
        query = """
                INSERT INTO result
                (result, release_id, test_case_id)
                VALUES (%s, %s, %s)
        """
        self.database.execute_query(query, ('SKIP', release_id[0]['release_id'], add_test_case_id[0]['test_case_id']))

    def auto_add_test_case(self):
        # Load the workbook
        workbook = openpyxl.load_workbook('ExynosAutoV920_Validation_IR241007_103552_LA.xlsx')

        # Select the sheet
        sheet = workbook['User_Scenario']

        # Read data from specific cells and store in variables
        for row in sheet.iter_rows(min_row=3, max_row=46, min_col=1, max_col=17):
            tc_id = row[0].value
            category_name = row[1].value
            sub_category_name = row[2].value
            title = row[3].value
            status = row[4].value
            domain = row[5].value
            pre_condition = row[6].value
            test_sequence = row[7].value
            pass_criteria = row[8].value
            link_work = row[11].value
            comment = row[12].value
            board_name = self.add_tc_form.add_tc_board_comboBox.currentText()
            bsp_name = self.add_tc_form.add_tc_bsp_comboBox.currentText()
            release_date = self.add_tc_form.add_tc_tag_comboBox.currentText()
            self.add_tc(tc_id, category_name, sub_category_name, title, status, domain, pre_condition, test_sequence, pass_criteria, link_work, comment, board_name, bsp_name, release_date)

            # category_query = "SELECT category_id FROM category WHERE category_name = %s"
            # category_result = self.database.execute_query(category_query, (category_name,))

            # if category_result:
            #     category_id = category_result[0]['category_id']
            # else:
            #     insert_category_query = "INSERT INTO category (category_name) VALUES (%s)"
            #     self.database.execute_query(insert_category_query, (category_name,))

            #     category_id_query = "SELECT category_id FROM category WHERE category_name = %s"
            #     category_result = self.database.execute_query(category_id_query, (category_name,))
            #     if category_result:
            #         category_id = category_result[0]['category_id']
            #     else:
            #         print("Failed to retrieve category ID after insertion.")
            #         return

            # if category_id:
            #     query = """
            #         INSERT INTO test_case
            #         (tc_id, category_id, sub_category, title, status, domain, pre_condition, test_sequence, pass_criteria, linked_work_items, comment)
            #         VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            #     """
            #     self.database.execute_query(query, (tc_id, category_id, sub_category_name, title, status, domain, pre_condition, test_sequence, pass_criteria, link_work, comment))
            # else:
            #     print("Invalid category")

            # query = """
            #         SELECT test_case_id
            #         FROM test_case
            #         WHERE tc_id = %s
            #         AND category_id = %s
            #         AND title = %s
            #         AND sub_category = %s
            #         AND status = %s
            #         AND domain = %s
            #         AND pre_condition = %s
            #         AND test_sequence = %s
            #         AND pass_criteria = %s
            #         AND linked_work_items = %s
            #         AND comment = %s
            # """
            # add_test_case_id = self.database.execute_query(query, (tc_id, category_id, sub_category_name, title, status, domain, pre_condition, test_sequence, pass_criteria, link_work, comment))
            # print(f"Test Case ID: {add_test_case_id}")

            # query = """
            #         SELECT `release`.release_id
            #         FROM `release`
            #         JOIN bsp
            #         ON `release`.bsp_id = bsp.bsp_id
            #         JOIN board
            #         ON `release`.board_id = board.board_id
            #         WHERE bsp.bsp_name = %s
            #         AND board.board_name = %s
            #         AND `release`.release_date = %s;
            # """
            # release_id = self.database.execute_query(query, (bsp_name, board_name, release_date))

            # query = """
            #         INSERT INTO result
            #         (result, release_id, test_case_id)
            #         VALUES (%s, %s, %s)
            # """
            # self.database.execute_query(query, ('SKIP', release_id[0]['release_id'], add_test_case_id[0]['test_case_id']))

    def add_test_case(self):
        print("Adding test case")
        tc_id = self.add_tc_form.id_lineEdit.text()
        category_name = self.add_tc_form.category_lineEdit.text()
        sub_category_name = self.add_tc_form.sub_caregory_lineEdit.text()
        title = self.add_tc_form.title_lineEdit.text()
        status = self.add_tc_form.status_lineEdit.text()
        domain = self.add_tc_form.domain_lineEdit.text()
        pre_condition = self.add_tc_form.pre_condition_lineEdit.text()
        test_sequence = self.add_tc_form.test_sequence_lineEdit.text()
        pass_criteria = self.add_tc_form.pass_criteria_lineEdit.text()
        link_work = self.add_tc_form.link_lineEdit.text()
        comment = self.add_tc_form.comment_lineEdit.text()

        board_name = self.add_tc_form.add_tc_board_comboBox.currentText()
        bsp_name = self.add_tc_form.add_tc_bsp_comboBox.currentText()
        release_date = self.add_tc_form.add_tc_tag_comboBox.currentText()

        self.add_tc(tc_id, category_name, sub_category_name, title, status, domain, pre_condition, test_sequence, pass_criteria, link_work, comment, board_name, bsp_name, release_date)
        # category_query = "SELECT category_id FROM category WHERE category_name = %s"
        # category_result = self.database.execute_query(category_query, (category_name,))

        # if category_result:
        #     category_id = category_result[0]['category_id']
        # else:
        #     insert_category_query = "INSERT INTO category (category_name) VALUES (%s)"
        #     self.database.execute_query(insert_category_query, (category_name,))

        #     category_id_query = "SELECT category_id FROM category WHERE category_name = %s"
        #     category_result = self.database.execute_query(category_id_query, (category_name,))
        #     if category_result:
        #         category_id = category_result[0]['category_id']
        #     else:
        #         print("Failed to retrieve category ID after insertion.")
        #         return

        # if category_id:
        #     query = """
        #         INSERT INTO test_case
        #         (tc_id, category_id, sub_category, title, status, domain, pre_condition, test_sequence, pass_criteria, linked_work_items, comment)
        #         VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        #     """
        #     self.database.execute_query(query, (tc_id, category_id, sub_category_name, title, status, domain, pre_condition, test_sequence, pass_criteria, link_work, comment))
        # else:
        #     print("Invalid category")

        # query = """
        #         SELECT test_case_id
        #         FROM test_case
        #         WHERE tc_id = %s
        #         AND category_id = %s
        #         AND title = %s
        #         AND sub_category = %s
        #         AND status = %s
        #         AND domain = %s
        #         AND pre_condition = %s
        #         AND test_sequence = %s
        #         AND pass_criteria = %s
        #         AND linked_work_items = %s
        #         AND comment = %s
        # """
        # add_test_case_id = self.database.execute_query(query, (tc_id, category_id, sub_category_name, title, status, domain, pre_condition, test_sequence, pass_criteria, link_work, comment))
        # print(f"Test Case ID: {add_test_case_id}")

        # query = """
        #         SELECT `release`.release_id
        #         FROM `release`
        #         JOIN bsp
        #         ON `release`.bsp_id = bsp.bsp_id
        #         JOIN board
        #         ON `release`.board_id = board.board_id
        #         WHERE bsp.bsp_name = %s
        #         AND board.board_name = %s
        #         AND `release`.release_date = %s;
        # """
        # release_id = self.database.execute_query(query, (bsp_name, board_name, release_date))

        # query = """
        #         INSERT INTO result
        #         (result, release_id, test_case_id)
        #         VALUES (%s, %s, %s)
        # """
        # self.database.execute_query(query, ('SKIP', release_id[0]['release_id'], add_test_case_id[0]['test_case_id']))

    def find_test_case_id(self, tc_id):
        query = "SELECT test_case_id FROM test_case WHERE tc_id = %s"
        result = self.database.execute_query(query, (tc_id,))
        if result:
            return result[0]['test_case_id']
        return None

    def show_add_tc_popup(self):
        self.add_tc_popup.show()
        self.load_add_tc_bsp_combobox()
        self.load_add_tc_board_combobox()
        self.load_add_tc_tag_comboBox()

    def load_data(self):
        query = "SELECT * FROM board"
        results = self.database.execute_query(query)
        for row in results:
            print(row)

    def closeEvent(self, event):
        self.database.close_connection()
        event.accept()

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()