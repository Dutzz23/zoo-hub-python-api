from config import database


def test_database():
    try:
        database.admin.command('ping')
        print('Database test successful')
    except Exception as e:
        print(e)
        print('Database test failed. Exception: ', e)
