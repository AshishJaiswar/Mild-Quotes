from src.quotes import quote_generator, quote_formatter
from src.utility import *
from src.video import *
from src.edit import video_editor
import random
import os

# -------------------------- Quotes -----------------------------------
# default length of quote is 150. Can pass length argument into
# quote_generator
data = quote_generator()
quote = data['content']
formated_quote = quote_formatter(quote)
author = data['author']
print(author)
# ---------------------------------------------------------------------


def run():
    # ---------------------------- Keyword ----------------------------
    keyword_list = ["Hotel",
                    "City",
                    "Snow",
                    "Snow Mountain",
                    "Night Tree",
                    "United Kingdom",
                    "Famous places"]

    keyword = random.choice(keyword_list)
    print(f"Keyword: {keyword}")
    data_index = get_index(keyword)
    print(f"Data index: {data_index}")
    page_num = get_page_number(keyword)
    print(f"Page Number: {page_num}")
    # ------------------------------------------------------------------

    # -------------------------- Check Json File -----------------------
    path = os.getcwd()
    isFileExists = os.path.isfile(rf"{path}\json_files\{keyword}.json")
    if not isFileExists or data_index >= 80:
        get_pexels_data(keyword, page_num)
        reset_index(keyword)
    # ------------------------------------------------------------------

    # ----------------------------- Video Download ---------------------

    video_link = get_video_link(keyword, data_index)
    print(f"Video Link: {video_link}")

    if video_link == "":
        # Return 404 if link not found
        return 404

    download_video(video_link)
    # -----------------------------------------------------------------

    # ----------------------------- Video Edit ------------------------
    video_count = get_video_count()
    video_editor(video_count, formated_quote, author)
    print("Sucessfull :)")
    return 200
    # -----------------------------------------------------------------


if __name__ == "__main__":
    # Database Initialization
    initalize_db()
    # Start Execution
    for i in range(10):
        status = run()
        if status == 200:
            break

    # Close Database Connection
    quit_db_connection()
