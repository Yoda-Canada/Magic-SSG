import re

with open('test2.md', 'r') as f:
    line = ''.join(f.readlines())

    htmlContent = re.sub(
        '\*\*([^\s\*.]{1}.*?)\*\*|__([^\s_.]{1}.*?)__', r'<strong>\1</strong>', line)
    htmlContent = re.sub(
        '\*([^\s\*.]{1}.*?)\*|_([^\s\_.]{1}.*?)_', r'<em>\2</em>', htmlContent)
    htmlContent = re.sub(
        '(\n|(\n<p>))\s{0,3}((---)|(\*\*\*))\s{0,3}((</p>\n)|\n)', r'\n<hr/>\n', htmlContent)

    print(htmlContent, end='')
