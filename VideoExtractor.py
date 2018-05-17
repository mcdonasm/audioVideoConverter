import subprocess
import os


def main(input_dir_path, output_dir_path):
    video_files = os.listdir(input_dir_path)

    for video_file_name in video_files:
        video_file_path = os.path.join(input_dir_path, video_file_name)

        if os.path.isfile(video_file_path):

            file_name, video_file_extension = os.path.splitext(video_file_name)
            audio_file_extension = ".mp3"
            audio_file_path = os.path.join(output_dir_path, file_name + audio_file_extension)

            try:
                command = "ffmpeg -i " + video_file_path + " -f mp3  -vn -ac 1 " + audio_file_path
                subprocess.call(command, shell=True)
            except:
                print("Error caught trying to convert: " + video_file_name)


if __name__ == '__main__':
    import argparse

    program_description = "This script extracts the video file from a directory of files, as .mp3, using the ffmpeg library,\
         outputting the results into the given directory."

    input_path_description = "The path to the folder that has the input video files."

    output_path_description = "The path to the desired output folder."

    parser = argparse.ArgumentParser(description=program_description,
                                     formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('input_path', metavar="input_dir_path", help=input_path_description)
    parser.add_argument('output_path', type=int, metavar="output_dir_path",
                        help=output_path_description)

    args = parser.parse_args()

    main(args.path, args.desired_format)
