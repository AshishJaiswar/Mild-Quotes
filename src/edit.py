# Import everything needed to edit video clips
from moviepy.editor import *
import random
from glob import glob
import os


def video_editor(video_count, quote, author):
    # Import everything needed to edit video clips

    current_path = os.getcwd()
    video_path = fr"{current_path}\pexel_video.mp4"
    clip = VideoFileClip(video_path)
    clip.subclip(0, 25)

    duration = clip.duration

    # Generate a text clip. You can customize the font, color, etc.
    txt_clip = TextClip(quote, font="Gabriola",
                        fontsize=65,
                        color='white')

    quotes_by = TextClip(f"~ {author}", font="Consolas-Bold", fontsize=40,
                         color='white')

    # Say that you want it to appear 10s at the center of the screen
    txt_clip = txt_clip.set_pos('center').set_duration(duration)
    quotes_by = quotes_by.set_position(("center", 1500)).set_duration(duration)

    image_layer_path = get_layer_path()
    image_clip = ImageClip(image_layer_path).set_duration(duration)

    image = CompositeVideoClip([image_clip, txt_clip, quotes_by])

    # Overlay the text clip on the first video clip
    video = CompositeVideoClip([clip, image])

    subscribe_video_path = fr"{current_path}\assets\videos\subscribe.mp4"
    subscribe_clip = VideoFileClip(subscribe_video_path)
    video = concatenate_videoclips([video, subscribe_clip])

    audio_path = get_audio_path()
    audio_file = AudioFileClip(audio_path)
    audio = audio_file.set_end(video.duration)
    edited_audio_path = fr"{current_path}\music.mp3"
    audio.write_audiofile(edited_audio_path)
    # Write the result to a file (many options available !)
    edited_video_path = fr"{current_path}\final_output\by_{author}_{video_count}.mp4"
    video.write_videofile(edited_video_path, audio=edited_audio_path)


def get_audio_path():
    """
        Select Random videos
    """
    current_path = os.getcwd()
    path = fr"{current_path}\assets\audios\*"
    list_of_audios = glob(path)
    audio_path = random.choice(list_of_audios)
    return audio_path


def get_layer_path():
    """
        Select Random Layer
    """
    current_path = os.getcwd()
    path = fr"{current_path}\assets\images\*"
    list_of_layers = glob(path)
    layer_path = random.choice(list_of_layers)
    return layer_path
