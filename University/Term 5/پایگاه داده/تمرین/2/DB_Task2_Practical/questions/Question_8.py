# Question 8 :
import sqlite3
from rich.console import Console
from rich.table import Table
import hashlib
import json
import os

if __name__ == "__main__":
# ---------------------------------------------
    PATH_TO_DB = '/Users/parsa/Desktop/University/Term 5/پایگاه داده/تمرین/DB_Task2_Practical/databases'
    JSON_PATH = '/Users/parsa/Desktop/University/Term 5/پایگاه داده/تمرین/DB_Task2_Practical/answer'
# ---------------------------------------------
    i = 8
    try:
        conn = sqlite3.connect(f"{PATH_TO_DB}/northwind.db")
        cursor = conn.cursor()
        console = Console()
        if os.path.exists(f"{JSON_PATH}/query_hashes.json"):
            with open(f"{JSON_PATH}/query_hashes.json", "r", encoding="utf-8") as f:
                data = json.load(f)
        else:
            data = {}

        console.print("Show the top 5 most expensive products with ProductName and UnitPrice, sorted by UnitPrice descending.", style="bold green")

        # --- Fill in your SQL query here ---
        answer = '''
        SELECT 
    ProductName,
    UnitPrice
FROM Products
ORDER BY UnitPrice DESC
LIMIT 5;
        '''
        # -----------------------------------
        insert_delete_update = False
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
