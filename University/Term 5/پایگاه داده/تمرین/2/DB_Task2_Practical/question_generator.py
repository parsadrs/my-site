import sqlite3
import random

if __name__ == "__main__":
# ---------------------------------------------
    QUESTIONS_DB_PATH = "./databases"
    STUDENT_NUMBER_PATH = "./config"
    QUESTIONS_PATH = "./questions"
# ---------------------------------------------
    with open(f'{STUDENT_NUMBER_PATH!s}/Student_Number.txt', 'r') as f:
        Student_Number = f.read().replace("\n", "").strip()
    print(f"Student Number: {1402012268156!s}")
    random.seed(1402012268156)
    try:
        conn = sqlite3.connect(f'{QUESTIONS_DB_PATH!s}/questions.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM questions;")
        rows = cursor.fetchall()
        r1 = random.randint(0, 9)
        r2 = random.randint(10, 18)
        r3 = random.randint(19, 28)
        r4 = random.randint(29, 38)
        r5 = random.randint(39, 48)
        r6 = random.randint(49, 58)
        r7 = random.randint(59, 68)
        r8 = random.randint(69, 78)
        r9 = random.randint(79, 83)
        rr = random.randint(0,4)
        r10 = rr + 84
        r11 = rr + 89
        r12 = random.randint(95, 99)
        selected_questions = [rows[r1], rows[r2], rows[r3], rows[r4], rows[r5],
                              rows[r6], rows[r7], rows[r8], rows[r9]]
        random.shuffle(selected_questions)
        selected_questions += [rows[r10],rows[r11],rows[r12]]
        print("Selected Questions:")
        for i in selected_questions:
            print(i)
        print(len(selected_questions))
        for iq, q in enumerate(selected_questions):
            with open(f'{QUESTIONS_PATH!s}/Question_{iq!s}.py', 'w') as f:
                f.write(f'# Question {iq!s} :\n')
                f.write("""import sqlite3
from rich.console import Console
from rich.table import Table
import hashlib
import json
import os

if __name__ == "__main__":
# ---------------------------------------------
    PATH_TO_DB = './../databases'
    JSON_PATH = './../answer'
# ---------------------------------------------"""+f"\n    i = {iq!s}\n" + """    try:
        conn = sqlite3.connect(f"{PATH_TO_DB}/northwind.db")
        cursor = conn.cursor()
        console = Console()
        if os.path.exists(f"{JSON_PATH}/query_hashes.json"):
            with open(f"{JSON_PATH}/query_hashes.json", "r", encoding="utf-8") as f:
                data = json.load(f)
        else:
            data = {}

        console.print(\""""+q[1]+"""\", style="bold green")

        # --- Fill in your SQL query here ---
        answer = '''
        
        '''
        # -----------------------------------
        insert_delete_update = """+ str(True if q[0] > 84 else False) +"""
        # Be careful with insert/delete/update queries that modify the database! 
        # It is recommended to back up your database before running such queries.
        if insert_delete_update:
            cursor.execute(answer)
            conn.commit()
            cursor.execute("SELECT * FROM Customers;")
        else:
            cursor.execute(answer)
        rows = cursor.fetchall()
        hash_value = hashlib.sha256(str(rows).encode()).hexdigest()

 
        columns = [description[0] for description in cursor.description]
        table = Table(show_header=True, header_style="bold magenta")
        for col in columns:
            table.add_column(col)
        for row in rows:
            table.add_row(*[str(cell) for cell in row])
        console.print(table)


        if "Q" + str(i) not in data:
            data["Q" + str(i)] = {}
        data["Q" + str(i)]["answer"] = answer.strip()
        data["Q" + str(i)]["hash"] = hash_value

    except Exception as e:
        print(f"Error connecting to database or executing query: {e!s}")
        hash_value = "Failed"
        data["Q" + str(i)]["hash"] = hash_value

    finally:
        with open(f"{JSON_PATH}/query_hashes.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

        if conn:
            conn.close()
""")

    except Exception as e:
        print(f"Error connecting to database: {e!s}")
    finally:
        if conn:
            conn.close()