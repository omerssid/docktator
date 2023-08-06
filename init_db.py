import sqlite3

connection = sqlite3.connect('database.db')

# open the schema file and call executescript() method that executes multiple SQL statements at once
with open('schema.sql') as f:
    connection.executescript(f.read())

# create cursor object
cur = connection.cursor()

# Add two posts
cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('First Post', 'Content blah blah for the first post')
            )
cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Second Post', 'important stuff in here pay attention for the second post')
            )

connection.commit()
connection.close()
