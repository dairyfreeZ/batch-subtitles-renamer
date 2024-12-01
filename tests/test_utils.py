import unittest
from src.utils import find_first_match


class TestFindFirstMatch(unittest.TestCase):
    def test_matching_pair_found(self):
        filenames = [
            "movie1.mkv", "subtitle1.srt", "movie2.mp4",
            "subtitle2.srt", "extra.txt", "movie3.mov", "subtitle3.ass"
        ]
        result = find_first_match(filenames)
        self.assertIsNotNone(result)

        video_files, video_ext, subtitle_files, subtitle_ext = result
        self.assertEqual(video_files, ["movie1.mkv"])
        self.assertEqual(video_ext, ".mkv")
        self.assertEqual(subtitle_files, ["subtitle3.ass"])
        self.assertEqual(subtitle_ext, ".ass")

    def test_no_matching_pair(self):
        filenames = ["movie1.mkv", "subtitle1.srt", "subtitle2.srt"]
        result = find_first_match(filenames)
        self.assertIsNone(result)

    def test_empty_input(self):
        filenames = []
        result = find_first_match(filenames)
        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()
