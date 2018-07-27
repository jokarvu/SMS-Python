import pymysql.cursors

class BaseModel:
    def __init__(self):
        # Establish connection to database
        self.connection = pymysql.connect(host = "localhost", db = "test", user = "root", password = "b15dcpt082", charset = "utf8mb4", cursorclass = pymysql.cursors.DictCursor)
        # Name of table
        self.table = ""
        # Name of columns in table
        self.columns = []
        # Hidden columns of table such as password  
        self.hidden = []
    # Select Method
    def select(self, *args):
        if args:
            # if give a list of columns to select
            tmp = ",".join(args)
        else:
            # If no column was given select all columns
            tmp = "*"
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT " + tmp + " FROM " + self.table
                cursor.execute(sql)
                res = cursor.fetchall()
        finally:
            return res
    # Delete Method
    def delete(self, condition):
        if condition:
            tmp = " AND ".join("{} = '{}'".format(key, value) for key, value in condition.items())
            try:
                with self.connection.cursor() as cursor:
                    sql = "DELETE FROM " + self.table + " WHERE " + tmp
                    res = cursor.execute(sql)
                    self.connection.commit()
            finally:
                return res if res else 0
        else:
            return 0
    # Update Method
    def update(self, condition, **kwargs):
        if kwargs:
            tmp = ", ".join("{} = '{}'".format(key, value) for key, value in kwargs.items())
            try:
                with self.connection.cursor() as cursor:
                    sql = "UPDATE " + self.table + " SET " + tmp + " WHERE " + condition
                    res = cursor.execute(sql)
                    self.connection.commit()
            finally:
                # If res was initialized
                if 'res' in locals():
                    return res
                else:
                    return 0
    # Insert Method
    def insert(self, kwargs):
        if kwargs:
            try:
                with self.connection.cursor() as cursor:
                    sql = "INSERT INTO " + self.table + "(" + ", ".join(self.columns) + ") VALUES(" + ", ".join("'{}'".format(value) for key, value in kwargs.items()) + ")"
                    res = cursor.execute(sql)
                    self.connection.commit()
            except pymysql.Error as e:
                # If has errors print error
                print(e)
            finally:
                # If res vas initialized
                if 'res' in locals():
                    return res
                else:
                    return 0
    def __del__(self):
        self.connection.close()
        