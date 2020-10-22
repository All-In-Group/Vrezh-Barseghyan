import mysql.connector
import config

db = mysql.connector.connect(
    host=config.db_name,
    user=config.db_username,
    passwd=config.db_password,
    port=config.db_port,
    database=config.db_workbench
)

cursor = db.cursor()

sql = "CREATE TABLE users (" \
      "first_name VARCHAR(255)," \
      "last_name VARCHAR(255)," \
      "phone_number VARCHAR(255)," \
      "email_address VARCHAR(255)," \
      "team_select VARCHAR(255)," \
      "id int AUTO_INCREMENT PRIMARY KEY," \
      "user_id int UNIQUE," \
      "task_status VARCHAR(255));"

if __name__ == "__main__":
    cursor.execute(sql)
    db.commit()