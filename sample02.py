"""
目標：users.sqlite に INSERT文を発行する
"""

import sqlite3


def main():
    conn = sqlite3.connect('users_db.sqlite')
    cursor = conn.cursor()

    sql = "INSERT INTO users (name, age) VALUES('Bob', 15);"
    conn.execute(sql)

    sql = "INSERT INTO users (name, age) VALUES('Tom', 27);"
    conn.execute(sql)

    sql = "INSERT INTO users (name, age) VALUES('Ken', 77);"
    conn.execute(sql)

    conn.commit()

    conn.close()


if __name__ == "__main__":
    main()
