from collections import defaultdict
from src.file_type_detector import FileType, FileTypeDetector


def find_first_match(filenames):
    """
    :param filenames: List of filenames.
    :return Tuple (video_files, video_ext, subtitle_files, subtitle_ext) for the first matching pair or None
    """
    video_map = defaultdict(list)
    subtitle_map = defaultdict(list)

    for name in filenames:
        type, ext = FileTypeDetector.determine_file_type(name)
        if type == FileType.VIDEO:
            video_map[ext].append(name)
        elif type == FileType.SUBTITLE:
            subtitle_map[ext].append(name)

    for video_ext, video_files in video_map.items():
        for subtitle_ext, subtitle_files in subtitle_map.items():
            if len(video_files) == len(subtitle_files):
                return video_files, video_ext, subtitle_files, subtitle_ext

    return None
