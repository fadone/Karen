import sqlite3


class CommandDatabase:

    def __init__(self):
        self.db = sqlite3.connect("database/karen.sqlite")
        self.db.execute("CREATE TABLE IF NOT EXISTS commands("
                        "id INTEGER PRIMARY KEY, "
                        "command TEXT, "
                        "response TEXT, "
                        "timestamp TEXT)")
        self.cursor = self.db.cursor()

    def add_command(self, command, response, timestamp):
        add_sql = "INSERT INTO commands (command, response, timestamp) VALUES(?, ?, ?)"
        self.db.execute(add_sql, (command, response, timestamp))
        self.db.commit()

    def print_all_commands(self):
        self.cursor.execute("SELECT * FROM commands")
        commands = self.cursor.fetchall()
        print("{:<5} {:<20} {:<50} {:<10}".format("ID", "Command", "Response", "Timestamp"))
        for idx, command, response, timestamp in commands:
            print("{:<5} {:<20} {:<50} {:<10}".format(idx, command, response, timestamp))
        self.cursor.close()

