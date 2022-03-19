from database.database import DB


def initalize_db():
    global db
    db = DB()


def get_index(keyword):
    '''
        Select data_index from tbl_keyword table
        After getting value update the value of data_index
    '''

    result = db.retrive(
        f"SELECT ID, DATA_INDEX FROM TBL_KEYWORD WHERE KEYWORD = '{keyword}'")
    id = result[0][0]
    index = result[0][1]
    db.update(
        f"UPDATE TBL_KEYWORD SET DATA_INDEX = {index + 1} WHERE ID = {id}")
    return index


def reset_index(keyword):
    result = db.retrive(
        f"SELECT ID FROM TBL_KEYWORD WHERE KEYWORD = '{keyword}'")
    id = result[0][0]
    db.update(
        f"UPDATE TBL_KEYWORD SET DATA_INDEX = 0 WHERE ID = {id}")


def get_page_number(keyword):
    result = db.retrive(
        f"SELECT PAGE_NUMBER FROM TBL_KEYWORD WHERE KEYWORD = '{keyword}'")
    page_number = result[0][0]
    return page_number


def update_page_number(keyword):
    result = db.retrive(
        f"SELECT ID, PAGE_NUMBER FROM TBL_KEYWORD WHERE KEYWORD = '{keyword}'")
    id = result[0][0]
    page_number = result[0][1]
    db.update(
        f"UPDATE TBL_KEYWORD SET PAGE_NUMBER = {page_number + 1} WHERE ID = {id}")


def get_video_count():
    '''
        Select count from tbl_video table
        After getting value update the value of count
    '''

    result = db.retrive(
        f"SELECT COUNT FROM TBL_VIDEO WHERE ID = 1")
    count = result[0][0]
    db.update(
        f"UPDATE TBL_VIDEO SET COUNT = {count + 1} WHERE ID = 1")
    return count


def quit_db_connection():
    db.quit_connection()
