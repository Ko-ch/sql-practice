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

    results = cursor.execute(sql)

    users = results.fetchall()

    for name, age in users:
        print(f"{name}さんは{age}歳です")

        # print(f"{users[0][0]}さんは{users[0][1]}歳です")
        # print(f"{users[1][0]}さんは{users[1][1]}歳です")
        # print(f"{users[2][0]}さんは{users[2][1]}歳です")

    conn.commit()

    conn.close()


if __name__ == "__main__":
    main()
