 <h1 align="center">CONTRIBUTING</h1>
 <img align="left" src="static\img\install2.png" width="50px" height="50px" />

## Installation

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Make sure you have installed Python version 3.8.5 or above.

## Contribut issue

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Welcome to file any issue. Please check the issue list and follow the README.md and CONTRIBUTTING.md. 

#### Usage

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;To format the **whole** project, run`.\check.sh`. This script will run Black and Flake8 against `magic_ssg/`.

#### How to apply Black to format Python code
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Black can be **installed** by running: ` pip install black `
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Easy to **run** with: `black {source_file_or_directory}` or `python -m black {source_file_or_directory}`

#### How to apply a linter - Flake8
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Flake 8 can be **installed** by running: `python -m pip install flake8`
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Easy to **run** with: `flake8 path/to/code/to/check.py ` or ` flake8 path/to/code/ `

#### Testing

I suggest to use [Pytest](https://docs.pytest.org/en/6.2.x/) as our testing framework. You can intall it using the following command in your command line:
- `pip install -U pytest`                                                        

Check that you installed the correct version:
- `pytest --version`

If you want contribute to the test part, please find my automation tests in MAGIC-SSG/tests/ folder and test files name format is (`test_*.py` or `*_test.py`).
