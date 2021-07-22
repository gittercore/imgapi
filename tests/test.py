import json
import unittest
import importlib.util
import os

class TestWorkers(unittest.TestCase):
    def module_from_file(self, module_name, file_path):
        spec = importlib.util.spec_from_file_location(module_name, file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module

    def test_punch(self):
        """
        Test punch
        """
        with open(f"{os.getcwd()}/config.json") as f:
            data = json.load(f)
        punch = self.module_from_file("hug", "../workers/punch/punch.py")
        self.assertEqual(bool(punch.punch(data["punch"]["input"][0],data["punch"]["input"][1],1)), True)

if __name__ == '__main__':
    unittest.main()