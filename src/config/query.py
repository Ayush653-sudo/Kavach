
class QueryConfig:
    """This class contains all the queries of the project."""

    User_Registration_TABLE_CREATION = """
        CREATE TABLE IF NOT EXISTS users(
            username TEXT PRIMARY KEY,
            hashed_password TEXT,
            phone_number TEXT,
            email_address TEXT,
            role TEXT,
            status TEXT
    
        )
    """

    CREATE_USER_CREDENTIALS = """
          INSERT INTO users(
            username,
            hashed_password,
            phone_number,
            email_address,
            role,
            status 
        ) VALUES(?, ?, ?, ?,?,?)
    
    """
    
    GET_ALL_USERS = """
    
    SELECT * FROM users
    
    """
    GET_USERS = """
    SELECT username,phone_number,email_address,role,status 
    FROM users
    """
    update_USERS = """
        UPDATE users SET status = ?
        WHERE username = ?
        """


    #Key table

    KEY_TABLE_CREATION = """
           CREATE TABLE IF NOT EXISTS keys(
               username TEXT PRIMARY KEY,
               key Text,
               FOREIGN KEY(username) REFERENCES users(username) ON DELETE CASCADE
           )
       """

    INSERT_KEY_INTO_TABLE = """
    INSERT INTO keys(
            username,
            key 
        ) VALUES(?, ?)   
    """
    GET_ALL_KEY = """
     SELECT * FROM keys WHERE username = ?
    
    """
    # password table

    PASSWORD_TABLE_CREATION = """
             CREATE TABLE IF NOT EXISTS passwords( id TEXT PRIMARY KEY,
                user_name TEXT,
                website_url TEXT,
                password TEXT,
                password_type TEXT,
                last_updated TIMESTAMP,
                FOREIGN KEY(user_name) REFERENCES users(username) ON DELETE CASCADE)

            """
    INSERT_PASSWORD_INTO_TABLE = """
     INSERT INTO passwords(
                id,
                user_name,
                website_url,
                password,
                password_type,
                last_updated)VALUES(?, ?,?,?,?,?) 
    
    """
    GET_ALL_PASSWORD = """
         SELECT id,user_name,website_url,password_type,last_updated FROM passwords WHERE user_name = ?

        """
    GET_ENCRYP_PASSWORD_AND_KEY = """
          SELECT passwords.password , keys.key FROM passwords
          INNER JOIN keys on keys.username = passwords.user_name
          Where passwords.id = ? AND passwords.user_name = ?

          """
    UPDATE_PASSWORD = """
         UPDATE passwords SET password = ?,
         last_updated = ? 
         WHERE user_name = ? AND id = ?
    """
    DELETE_PASSWORD_FROM_TABLE = """
           DELETE FROM passwords
           WHERE id = ?
       """

#  audit password table

    CREATE_AUDIT_PASSWORD_TABLE = """
               CREATE TABLE IF NOT EXISTS audits(
                id TEXT,
                password_id TEXT,
                operation TEXT,
                datetime TIMESTAMP,
                user_name TEXT,
                FOREIGN KEY(password_id) REFERENCES passwords(id) ON DELETE CASCADE)

    """
    INSERT_AUDIT_PASSWORD_INTO_TABLE = """
     INSERT INTO audits(
                id,
                password_id,
                operation,
                datetime,
                user_name)VALUES(?, ?,?,?,?) 
    
    """
    GET_AUDIT = """
            SELECT id, password_id, operation,datetime
            FROM audits WHERE password_id = ? AND operation = ? AND user_name = ?
                           """





