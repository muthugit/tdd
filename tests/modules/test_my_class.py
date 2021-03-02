import unittest, pytest
from tdd.modules.my_class import MyClass


class TestMyClass(unittest.TestCase):
    def test_print(self):
        obj = MyClass()
        assert obj.ping() == "pong"

    def test_sys_error(self):
        obj = MyClass()
        with pytest.raises(TypeError):
            obj.ping("unwanted") == "pong"
