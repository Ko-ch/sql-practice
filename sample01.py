import sqlite3

"""
目標：PythonでSQLを使ってテーブルをつくる
"""


def main():
    # conn = sqlite3.connect('users_db.sqlite')
    conn = sqlite3.connect('users.sqlite')
    cursor = conn.cursor()

    # SQLの準備
    sql = """CREATE TABLE users (
                name TEXT,
                age INTEGER
                )"""

    # SQL実行
    cursor.execute(sql)

    # コミット
    conn.commit()

    # 接続を切る
    conn.close()


if __name__ == "__main__":
    main()
