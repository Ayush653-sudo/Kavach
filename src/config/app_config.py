class AppConfig:
    DATABASE_PATH=r"C:\Users\atomar\projects\KAVACH\src\database_layer\KAVACH.db"
    LOG_FILE_PATH = "logs.log"
    COMMON_PASSWORD_FILE = r"C:\Users\atomar\projects\KAVACH\src\database_layer\common_password.txt"
    SECRET_KEY = "kAVACHHIKAVAH"
    PROMPT_PATH = r"C:\Users\atomar\projects\KAVACH\src\config\prompts\prompts.yaml"
    LOGPROMPT_PATH = r"C:\Users\atomar\projects\KAVACH\src\config\prompts\logprompts.py"
    MAXIMUM_LOGIN_ATTEMPTS = 3
    REGULAR = "Regular"
    Admin = "Admin"
    FETCHED = "Fetched"
    UPDATED = "Updated"
    INITIAL = "Initial"

    DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    LOWERCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                            'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                            'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                            'z']

    UPPERCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                            'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                            'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                            'Z']

    SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
               '*', '(', ')', '<']

