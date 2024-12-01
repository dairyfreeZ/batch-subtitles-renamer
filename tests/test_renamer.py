import os
import unittest
from pathlib import Path
from python.runfiles import runfiles
from src.renamer import main


class TestRenamer(unittest.TestCase):
    def setUp(self):
        r = runfiles.Create()
        self.testdata_dir = Path(
            r.Rlocation("batch_subtitles_renamer/tests/testdata/matched_subs_and_vids"))

    def test_subtitle_renaming(self):
        # Change the current directory to the temporary directory
        os.chdir(self.testdata_dir)

        # Call the renamer's main function
        main()

        # Define expected groups
        other_subtitles = ["subtitle_01.srt"]
        matched_videos = [f"video_{i:02d}.mkv" for i in range(1, 13)]
        other_videos = ["video_00.mp4", "video_02.mp4"]

        # Check renamed subtitles
        for i, video in enumerate(matched_videos, start=1):
            expected_subtitle = f"video_{i:02d}.ass"
            renamed_subtitle_path = self.testdata_dir / expected_subtitle

            self.assertTrue(
                renamed_subtitle_path.exists(),
                f"{expected_subtitle} not found.")

            # Verify content matches original subtitle content
            with open(renamed_subtitle_path, "r") as renamed_file:
                self.assertEqual(
                    renamed_file.read(), f"subtitle_{i:02d}.ass",
                    f"Content mismatch for {expected_subtitle}."
                )

        # Check other subtitles remain untouched
        for subtitle in other_subtitles:
            subtitle_path = self.testdata_dir / subtitle
            self.assertTrue(subtitle_path.exists(), f"{subtitle} is missing.")
            with open(subtitle_path, "r") as subtitle_file:
                self.assertEqual(
                    subtitle_file.read(), subtitle,
                    f"{subtitle} should remain untouched."
                )

        # Check other videos remain untouched
        for video in matched_videos + other_videos:
            video_path = self.testdata_dir / video
            self.assertTrue(video_path.exists(), f"{video} is missing.")
            with open(video_path, "r") as video_file:
                self.assertEqual(
                    video_file.read(), video,
                    f"{video} should remain untouched."
                )


if __name__ == "__main__":
    unittest.main()
