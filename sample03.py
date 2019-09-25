""""
目標： usersのusersテーブルからうまいことデータをとってきて

Bobさんは15歳です
Tomさんは27歳です
Kenさんは77歳です

って出力するやーつ
"""

import sqlite3


def main():
    conn = sqlite3.connect("users.sqlite")
    cursor = conn.cursor()

    sql = "SELECT * FROM users"

    cursor.execute(sql)

    conn.commit()

    conn.close()


if __name__ == "__main__":
    main()
