import sqlite3


def main():
    with open("schema.sql", mode="r", encoding="utf-8") as f:
        sql = f.read()

    # print(sql)

    conn = sqlite3.connect('sample.db')
    cursor = conn.cursor()

    # cursor.execute(sql)
    cursor.executescript(sql)

    conn.commit()

    conn.close()


if __name__ == "__main__":
    main()
