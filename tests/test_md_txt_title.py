from magic_ssg.asstLib import get_md_title


# def get_md_title(file_path):
#     i = 0
#     title = ""
#     # Read top 3 lines one by one.
#     with open(file_path, "r", encoding="utf8") as input_file:
#         for i in range(3):
#             for line in input_file.readlines():
#                 i += 1
#                 title = line.strip()
#                 if i == 3:
#                     break
#                 elif not len(title):
#                     continue
#                 elif (
#                     title.startswith("#")
#                     or title.startswith("##")
#                     or title.startswith("###")
#                 ):
#                     return title


# test the title with one pound key
def test_md_title_with_one_pound():
    file_path = "./tests/testfiles/test1.md"
    result = get_md_title(file_path)
    expecte_result = ""
    assert result == expecte_result


# test the title with two pound keys
def test_md_title_with_two_pound():
    file_path = "./tests/testfiles/test2-1.md"
    result = get_md_title(file_path)
    expecte_result = ""
    assert result == expecte_result


# test the title with three pound keys
def testmd_title_with_three_pound():
    file_path = "./tests/testfiles/test3.md"
    result = get_md_title(file_path)
    expecte_result = ""
    assert result == expecte_result


# test the first line is the comment line
def test_md_title_on_first_line():
    file_path = "./tests/testfiles/test4.md"
    result = get_md_title(file_path)
    expecte_result = "this is heading line1"
    assert result == expecte_result


# test the second line is the comment line
def test_md_title_on_second_line():
    file_path = "./tests/testfiles/test5.md"
    result = get_md_title(file_path)
    expecte_result = "this is heading line2"
    assert result == expecte_result


# test the third line is the comment line
def test_md_title_on_third_line():
    file_path = "./tests/testfiles/test6.md"
    result = get_md_title(file_path)
    expecte_result = "this is heading line3"
    assert result == expecte_result
