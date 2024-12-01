import os
import sys
import src.utils as utils


def main():
    all_files = os.listdir(".")
    result = utils.find_first_match(all_files)
    if result is None:
        print("No matching video-subtitle pair of the same length is found.")
        sys.exit(1)

    videos, _, subtitles, subtitle_ext = result
    for i in range(len(subtitles)):
        old_name = subtitles[i]
        new_name = os.path.splitext(videos[i])[0] + subtitle_ext

        if old_name != new_name:
            try:
                os.rename(old_name, new_name)
            except OSError as e:
                print(f"Error renaming file '{old_name}' to '{new_name}': {e}")
                sys.exit(1)

    print("Succeed.")
