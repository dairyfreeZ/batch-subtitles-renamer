from enum import Enum


class FileType(Enum):
    VIDEO = "video"
    SUBTITLE = "subtitle"
    UNKNOWN = "unknown"


class FileTypeDetector:
    """
    A library to determine the type of a file based on its extension.
    Currently supports video and subtitle file types.
    """

    # Supported file extensions for each type
    VIDEO_EXTENSIONS = {
        '.avi',
        '.flv',
        '.mkv',
        '.mov',
        '.mp4',
        '.webm',
        '.wmv'}
    SUBTITLE_EXTENSIONS = {'.ass', '.srt', '.ssa', '.sub', '.vtt'}

    @classmethod
    def determine_file_type(cls, file_name):
        """
        Determines the type of a file based on its extension.

        :param file_name: str, the name of the file (e.g., "movie.mkv")
        :return: FileType, the type of the file (FileType.VIDEO, FileType.SUBTITLE, or FileType.UNKNOWN)
        """
        # Extract file extension
        extension = cls._get_file_extension(file_name)

        if extension in cls.VIDEO_EXTENSIONS:
            return FileType.VIDEO, extension
        elif extension in cls.SUBTITLE_EXTENSIONS:
            return FileType.SUBTITLE, extension
        else:
            return FileType.UNKNOWN, ''

    @staticmethod
    def _get_file_extension(file_name):
        """
        Extracts the file extension from a file name.

        :param file_name: str, the name of the file
        :return: str, the file extension (e.g., ".mkv")
        """
        if '.' not in file_name:
            return ''
        return file_name[file_name.rfind('.'):].lower()
