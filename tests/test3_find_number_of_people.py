import unittest

from source.general import load_csv, find_rows


class SimpleLoadFile(unittest.TestCase):
    def setUp(self):
        self.loaded_file: list[list[str]] = load_csv("source/matura.csv")


class Test(SimpleLoadFile):
    def test_find_rows(self):
        self.assertEqual(
            find_rows(
                self.loaded_file,
                region="Lubuskie",
                sex="kobiety",
                pass_="zdało",
                year="2018",
            ),
            [["Lubuskie", "zdało", "kobiety", "2018", "6926"]],
        )
