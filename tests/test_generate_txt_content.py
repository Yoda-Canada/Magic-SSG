from magic_ssg.asstLib import generate_txt_content


def test_generate_txt_content():
    file_path = "./tests/testfiles/test.txt"
    title = "THIS IS TITLE TEST"
    result = generate_txt_content(file_path, title)
    expecte_result = """<h1>THIS IS TITLE TEST</h1><p>1.	Git clone
                        2	git init
                        3.	git add .
                        4.	git commit -am "make it better"
                        5.	git push origin main</p>"""

    assert result == expecte_result
