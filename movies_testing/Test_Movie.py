import unittest
from unittest.mock import MagicMock
from Movie_Extractor import FileExtractor
from Calculate_Time import calculate_time_hours
from Movie_Average import movie_average
from ExtractStub import ExtractorStub
from io import StringIO
from unittest.mock import patch
from Exit_Watchlist import exit_watchlist


class TestMovie(unittest.TestCase):
    ExtractorStub = ExtractorStub()
    FileExtractor = FileExtractor()

    def test_ratings_mock(self):
        choices = {"Hot Fuzz": 121, "Cast Away": 144, "The Fellowship of the Ring": 228}
        self.FileExtractor.extract_movie_ratings = MagicMock(return_value=choices)
        self.assertEqual(movie_average(choices), 8.1)

    def test_length_stub(self):
        choices = self.ExtractorStub.extract_movie_dict()
        self.assertEqual(calculate_time_hours(choices), {'Hot Fuzz': [2, 1], 'Cast Away': [2, 24], 'The Fellowship of the Ring': [3, 48]})

    def runTest(self, given_answer, expected_out):
        with patch('builtins.input', return_value=given_answer), patch('sys.stdout', new=StringIO()) as fake_out:
            exit_watchlist()
            self.assertEqual(fake_out.getvalue().strip(), expected_out)

    def test_exit_fake(self):
        self.runTest("Y", "Thank you, have a nice day!")

    def test_exit_fake_2(self):
        self.runTest("N", "Apologies, we will attempt to make improvements")


if __name__ == '__main__':
    unittest.main()
