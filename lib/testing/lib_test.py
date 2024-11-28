# GLORY BE TO GOD,
# TESTING FILE
# BY ISRAEL MAFABI EMMANUEL


import runpy

class TestNameError:
    # name error
    def test_name_error(self):
        runpy.run_path('lib/python_name_error.py')

class TestSyntaxError:
    # syntax error
    def test_syntax_error(self):
        runpy.run_path('lib/python_syntax_error.py')

class TestTypeError:
    # type error
    def test_type_error(self): 
        runpy.run_path('lib/python_type_error.py')

class TestAssertionError:
    # assertion error
    def test_assertion_error(self):
        runpy.run_path('lib/python_assertion_error.py')