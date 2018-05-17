import subprocess
import os

video_files_dir_path = "test_files/video"
audio_files_dir_path = "test_files/audio"

video_files = os.listdir(video_files_dir_path)

for video_file_name in video_files:
    video_file_path = os.path.join(video_files_dir_path, video_file_name)

    if os.path.isfile(video_file_path):

        file_name, video_file_extension = os.path.splitext(video_file_name)
        audio_file_extension = ".mp3"
        audio_file_path = os.path.join(audio_files_dir_path, file_name + audio_file_extension)

        command = "ffmpeg -i " + video_file_path + " -f mp3  -vn -ac 1 " + audio_file_path
        subprocess.call(command, shell=True)
