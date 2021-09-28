import argparse
import os
import shutil
import re

DIST_FOLDER = "dist"


def get_files(directory):
    txt_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if type_of_supported_file(file):   #if it is not False, then it is something out of supported
                file_path = os.path.join(root, file)
                txt_files.append(file_path)

    return files


# Look for a title

def get_txt_title(file_name):
    i = 0
    title = ""
    # Read top 3 lines one by one.
    with open(file_name, "r", encoding="utf8") as input_file:
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

def get_grand_title(file_name): #should be good for both .md and .txt
    title = ""

    with open(file_name, "r", encoding="utf8") as input_file:
        line = input_file.readline()
        while line in ["/n", "/r/n"]:  # loop in case first few lines are empty by mistake
            line = input_file.readline()
        if not line.startswith("#") \
                or (input_file.readline() in ["/n", "/r/n"]
                    and input_file.readline() in ["/n", "/r/n"]):
            return False  # if line does not starts with # or at least has next 2 lines empty, then it is not a title
        title = line.strip()
        title = title.strip("#")

    return title


# Returns bodycont with html format.
def generate_txt_content(file_path, title):
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

def generate_md_content(file_path):
    with open(file_path, "r", encoding="utf8") as input_file:
        content = input_file.read()

        # # TODO code block recognision
        # content = re.sub(r'(```\s+```)',
        #                  lambda s: "<pre>{}</pre>".format(s[0][3:-3]), #[3:-3] ``` elements
        #                  content)
        content = content.split("\n", 3)[3]
        content = "<p>" + content
        content = content.replace("\n\n", "</p>\n<p>")
        content = content + "</p>"

    #The re.sub() toolevaluates a pattern and, for each valid match, it calls a method (or lambda):
        # source https://www.thepoorcoder.com/regex-substitution-solution/
        # https://www.thegeekstuff.com/2014/07/advanced-python-regex/
        #bold
        content = re.sub(r'(__[^\r\n\_].*?__)|(\*\*[^\r\n\*].*?\*\*)', # regexp explained lower
                         lambda s: "<b>{}</b>".format(s[0][2:-2]),  # instead of string to replace with, we are passing a
                         content)

        #(__[ ^\r\n\_].* ?__) | (\ * \ *[^ \r\n\ *].* ?\ * \ *) explained
        #two underscores, then any character exept then new line or one more underscore, then one or more of any
        # characters followed by two underscores. OR same combination, but with * instead of _

        #italic
        content = re.sub(r'(_[^\r\n\_].*?_)|(\*[^\r\n\*].*?\*)', lambda s: "<i>{}</i>".format(s[0][1:-1]), content)


        #header
        headerTag = lambda s: '{endpTag}<h{size}>{regexContent}</h{size}>{pTag}'.format(
            endpTag="</p>\n\n" if s.group(1) == "\n" else "", size=s.group(2).count('#'), regexContent=s.group(3),
            pTag="\n\n<p>" if s.group(4) == "\n" else "")
        content = re.sub(r'(|(?<!\n)\n|<p>)(#{1,5})\s(.*)(<\/p>|(?<!<\/p>)\n|$)', headerTag, content)

    return content

def format_to_html(file_name, title, content):

    html_template = """<!doctype html>
        <html lang="en">
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
    return html_template.format(title=title if title else file_name, bodycont=content)


def output_result(file_name, html):

    if(os.path.isdir(DIST_FOLDER)):
        shutil.rmtree(DIST_FOLDER)

    os.mkdir(DIST_FOLDER)
    file_path = DIST_FOLDER + "/" + file_name.replace(".txt", ".html").replace(".md", ".html")
    with open(file_path, "w", encoding="utf8") as output_file:
        result = output_file.write(html)
    return result

def type_of_supported_file(file_name):
    if file_name.endswith(".md"):
        return "md"
    if file_name.endswith(".txt"):
        return "txt"
    return False

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--version", action="version",
                        version="%(prog)s 0.1", help="display tool name and version.")
    parser.add_argument(
        "-i", "--input", help="specify an input file or folder to be processed.", required=True)
    args = parser.parse_args()
    input = args.input

    all_files = []
    folder = ""


    if not type_of_supported_file(input): #then it is probably a directory
        folder = input + "/"
        all_files = get_files(folder)
    else:
        all_files.append(input)

    for file in all_files:
        bodycont = ""
        file_path = folder + file
        title = get_grand_title(file_path)
        if type_of_supported_file(file) == 'txt':
            bodycont = generate_txt_content(file_path, title)
        elif type_of_supported_file(file) == 'md':
            bodycont = generate_md_content(file_path)
        html = format_to_html(file, title, bodycont)
        ret = output_result(file, html)
        if ret:
            print("success!")


main()
