import unittest
from src.file_type_detector import FileType, FileTypeDetector


class TestFileTypeDetector(unittest.TestCase):
    def test_video_file(self):
        file_type, ext = FileTypeDetector.determine_file_type("movie.mkv")
        self.assertEqual(file_type, FileType.VIDEO)
        self.assertEqual(ext, ".mkv")

    def test_subtitle_file(self):
        file_type, ext = FileTypeDetector.determine_file_type("subtitle.srt")
        self.assertEqual(file_type, FileType.SUBTITLE)
        self.assertEqual(ext, ".srt")

    def test_unknown_file(self):
        file_type, ext = FileTypeDetector.determine_file_type("document.pdf")
        self.assertEqual(file_type, FileType.UNKNOWN)
        self.assertEqual(ext, "")

    def test_no_extension(self):
        file_type, ext = FileTypeDetector.determine_file_type(
            "file_with_no_extension")
        self.assertEqual(file_type, FileType.UNKNOWN)
        self.assertEqual(ext, "")

    def test_uppercase_extension(self):
        file_type, ext = FileTypeDetector.determine_file_type("MOVIE.MKV")
        self.assertEqual(file_type, FileType.VIDEO)
        self.assertEqual(ext, ".mkv")  # Case should normalize to lowercase


if __name__ == "__main__":
    unittest.main()
