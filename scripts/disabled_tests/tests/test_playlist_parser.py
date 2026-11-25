import json
import os
import tempfile
from unittest import TestCase

from playlist_parser import parse_all_files, DisableNodeProcessingException


class Test(TestCase):

    def test_parse_file(self):
        test_data_dir = os.path.join(os.path.dirname(__file__), 'data')
        input_file = os.path.join(test_data_dir, 'playlist_input.xml')
        expected_out_file = os.path.join(test_data_dir, 'playlist_out.json')
        with open(expected_out_file) as f:
            expected = json.load(f)
        actual = [excl.to_scheme() for excl in parse_all_files([input_file])]
        self.assertEqual(expected, actual)

    def test_misspelled_variation_raises_exception(self):
        xml_content = """<?xml version='1.0' encoding='UTF-8'?>
<playlist>
    <test>
        <testCaseName>Test_Invalid_Variation</testCaseName>
        <disables>
            <disable>
                <comment>https://github.com/adoptium/aqa-tests/issues/1</comment>
                <variation>misspelled-variation</variation>
            </disable>
        </disables>
        <variations>
            <variation>Mode101</variation>
        </variations>
    </test>
</playlist>
"""
        with tempfile.NamedTemporaryFile('w', delete=False, suffix='.xml') as temp_f:
            temp_f.write(xml_content)
            temp_path = temp_f.name
        try:
            with self.assertRaises(DisableNodeProcessingException):
                parse_all_files([temp_path])
        finally:
            os.unlink(temp_path)

    def test_forbidden_newline_in_comment_raises_exception(self):
        xml_content = """<?xml version='1.0' encoding='UTF-8'?>
<playlist>
    <test>
        <testCaseName>Test_Forbidden_Newline</testCaseName>
        <disables>
            <disable>
                <comment>https://github.com/adoptium/aqa-tests/issues/1\nwith newline</comment>
            </disable>
        </disables>
    </test>
</playlist>
"""
        with tempfile.NamedTemporaryFile('w', delete=False, suffix='.xml') as temp_f:
            temp_f.write(xml_content)
            temp_path = temp_f.name
        try:
            with self.assertRaises(DisableNodeProcessingException):
                parse_all_files([temp_path])
        finally:
            os.unlink(temp_path)

