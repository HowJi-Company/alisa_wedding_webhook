import unittest

from insert_table_info.excel_to_firestore import (
    _normalize_table_id,
    _normalize_table_name,
)


class ExcelTableIdTests(unittest.TestCase):
    def test_accepts_main_table_label(self) -> None:
        self.assertEqual(_normalize_table_id("主桌", 2), "主桌")
        self.assertEqual(_normalize_table_name("主桌", None), "主桌")

    def test_accepts_integer_table_number(self) -> None:
        self.assertEqual(_normalize_table_id(12, 3), 12)
        self.assertEqual(_normalize_table_id("12", 3), 12)

    def test_rejects_other_text_and_decimal_numbers(self) -> None:
        with self.assertRaises(ValueError):
            _normalize_table_id("貴賓桌", 4)
        with self.assertRaises(ValueError):
            _normalize_table_id("1.5", 4)


if __name__ == "__main__":
    unittest.main()
