from magic_ssg.asstLib import get_txt_title


# test the title in the first line
def test_get_txt_title1():
    file_path = "./tests/testfiles/Silver_Blaze.txt"
    result = get_txt_title(file_path)
    expecte_result = "Silver Blaze"
    assert result == expecte_result


# test the title in the second line and it is centered
def test_get_txt_title2():
    file_path = "./tests/testfiles/The_Naval_Treaty.txt"
    result = get_txt_title(file_path)
    expecte_result = "The Naval Treaty"
    assert result == expecte_result


# test the title in the Third line
def test_get_txt_title3():
    file_path = "./tests/testfiles/The_Adventure_of_the_Speckled_Band.txt"
    result = get_txt_title(file_path)
    expecte_result = "THE ADVENTURE OF THE SPECKLED BAND"
    assert result == expecte_result


# test the first line is the comment line
def test_get_txt_title4():
    file_path = "./tests/testfiles/The_Red_Headed_League.txt"
    result = get_txt_title(file_path)
    expecte_result = None
    assert result == expecte_result


# test the first line is the first sentence of the first paragraph.
def test_get_txt_title5():
    file_path = "./tests/testfiles/The_Adventure_of_the_Six_Napoleans.txt"
    result = get_txt_title(file_path)
    expecte_result = None
    assert result == expecte_result, " It isn't a bug, and it need to enhance."
