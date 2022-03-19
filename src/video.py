import requests
import json
import os


def get_pexels_data(keyword, page):
    API_KEY = "563492ad6f91700001000001ba422fdc9b6349b4909383db68a27373"
    api_url = f"https://api.pexels.com/videos/search?query={keyword}&per_page=80&orientation=portrait&page={page}"
    response = requests.get(api_url, headers={"Authorization": API_KEY})
    data = response.json()
    current_path = os.getcwd()
    with open(fr"{current_path}\json_files\{keyword}.json", "w") as file:
        file.write(json.dumps(data))
        file.close()


def get_video_link(keyword, data_index):
    video_list = []
    video_link = ""
    current_path = os.getcwd()
    with open(fr"{current_path}\json_files\{keyword}.json", "r") as file:
        data = json.loads(file.read())
        video_list = data["videos"]
        file.close()
    video_files_list = video_list[data_index]["video_files"]
    for obj in video_files_list:
        width = obj['width']
        height = obj['height']
        if width == 1080 and height == 1920:
            video_link = obj['link']
            break
    return video_link


def download_video(link):
    response = requests.get(link, stream=True)
    current_path = os.getcwd()
    with open(fr"{current_path}\pexel_video.mp4", "wb") as outfile:
        outfile.write(response.content)
        outfile.close()
