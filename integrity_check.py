import openpyxl
import tkinter as tk
from tkinter import filedialog, simpledialog

def read_column_p(file_path, sheet_name):
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook[sheet_name]

    p_column = []
    for row in sheet.iter_rows(min_row=6, min_col=16, max_col=16, values_only=True):
        p_column.append(row[0])

    return p_column

def check_column_format(p_column):
    invalid_rows = []
    for idx, value in enumerate(p_column, start=6):
        lines = str(value).split('\n')
        for line in lines:
            if not line.startswith(('#', '^', '~', '!', '%')):
                invalid_rows.append((idx, line))
                break
    return invalid_rows

def main():
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename(title="엑셀 파일선택", filetypes=[("Excel files", "*.xlsx *.xls")])

    sheet_name = simpledialog.askstring("시트 이름", "시트 이름 입력:")

    p_column = read_column_p(file_path, sheet_name)
    invalid_rows = check_column_format(p_column)

    if invalid_rows:
        print("지정 포멧과 다른 column:")
        for row in invalid_rows:
            print(f"행 번호: {row[0]}, 값: {row[1]}")
    else:
        print("column내용 이상 없음.")

if __name__ == "__main__":
    main()