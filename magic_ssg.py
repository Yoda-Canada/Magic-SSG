import argparse
import os
import shutil

DIST_FOLDER = "dist"


def get_txt_files(directory):
    txt_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.txt'):
                file_path = os.path.join(root, file)
                txt_files.append(file_path)
    return txt_files


# Look for a title

def get_title(file_path):
    i = 0
    title = ""
    # Read top 3 lines one by one.
    with open(file_path, "r", encoding="utf8") as input_file:
        for i in range(3):
            for line in input_file.readlines():
                i += 1
                title = line.strip()
                if i == 3:
                    break
                elif not len(title) or title.startswith("#"):
                    continue
                # elif len(title) or title.startswith("#"):
                else:
                    return title


# Returns bodycont with html format.
def generate_content(file_path, title):
    titled_format = "<h1>{}</h1>\n\n\n{}"
    content = ""

    with open(file_path, "r", encoding="utf8") as input_file:
        if (title == ""):
            content = input_file.read()[4:]
            content = "<p>" + content
            content = content.replace("\n\n", "</p>\n<p>")
            content = content + "</p>"
            content = titled_format.format(title, content)
            return content
        else:
            content = input_file.read()
            content = content.split("\n", 3)[3]
            content = "<p>" + content
            content = content.replace("\n\n", "</p>\n<p>")
            content = content + "</p>"
            content = titled_format.format(title, content)
            return content


def format_to_html(file_name, title, content, lang):

    html_template = """<!doctype html>
        <html lang="{currentlang}">
        <head>
            <meta charset="utf-8">
            <title>{title}</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
        </head>
        <body>
            {bodycont}
        </body>
        </html>
        """
    return html_template.format(title=title if title else file_name, bodycont=content, currentlang=lang)


def output_result(file_name, html):

    if(os.path.isdir(DIST_FOLDER)):
        shutil.rmtree(DIST_FOLDER)

    os.mkdir(DIST_FOLDER)
    file_path = DIST_FOLDER + "/" + file_name.replace(".txt", ".html")
    with open(file_path, "w", encoding="utf8") as output_file:
        output_file.write(html)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--version", action="version",
                        version="%(prog)s 0.1", help="display tool name and version.")
    parser.add_argument(
        "-i", "--input", help="specify an input file or folder to be processed.", required=True)
    parser.add_argument('-l', '--lang', nargs='?', type=str, default='en=CA',
                        help='Language of the document (default is en=CA)')
    args = parser.parse_args()
    input = args.input

    if (args.lang is not None):
        langlist = "".join(args.lang)
        lang = langlist.strip()

    all_files = []
    folder = ""

    if not input.endswith(".txt"):
        folder = input + "/"
        all_files = get_txt_files(folder)
    else:
        all_files.append(input)

    for file in all_files:
        file_path = folder + file
        title = get_title(file_path)
        bodycont = generate_content(file_path, title)
        html = format_to_html(file, title, bodycont, lang)
        output_result(file, html)


main()
