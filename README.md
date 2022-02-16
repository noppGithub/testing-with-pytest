# testing-with-pytest

### Installation
- create virtual environment name .venv: `python3 -m venv .venv`
- activate the created environment: `source .venv/bin/activate`
- install `pytest`: `pip install pytest`

### Start the test
- create the file with prefix `test_` to test your class object
- type in `pytest`, press enter
- expected result

```bash
(.venv) D:\np\testing-with-pytest>pytest
========================== test session starts ===========================
platform win32 -- Python 3.8.8, pytest-7.0.1, pluggy-1.0.0
rootdir: D:\np\testing-with-pytest
collected 7 items                                                                                                                                      

test_myclass.py ......   [100%] 

=========================== 7 passed in 0.02s ============================ 
```

Credit: https://github.com/python-frederick/python-testing-101 + https://www.youtube.com/watch?v=etosV2IWBF0