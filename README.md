# Magic-SSG
1.  add a new function named "get_md_body", and it can parse .md file to get header and paragraphs.

        >     def get_md_body(file, out):

    >        with open(file, 'r', encoding=encode) as f:
    >            for lines in f.readlines():
    >                # adding header
    >                if lines.startswith("#"):
    >                    out.extend([indent(tabDepth) + o_tag('h1') +
    >                                lines.lstrip("#").strip() + clo_tag(),
    >                                indent(tabDepth) + o_tag('p')])  # opening first paragraph
    >
    >            # the line has italic markdown
    >
    >        pline1 = re.sub(r'(_[^\r\n\_].*?_)|(\*[^\r\n\*].*?\*)',
    >                            lambda s: "<i>{}</i>".format(s[0][1:-1]), lines)
    >            out.append(indent(tabDepth + 1) +
    >                       pline1)
    >
    >            # the line has bold markdown
    >
    >            pline2 = re.sub(r'(__[^\r\n\_].*?__)|(\*\*[^\r\n\*].*?\*\*)',
    >                            lambda s: "<b>{}</b>".format(s[0][2:-2]), lines)
    >
    >         out.append(indent(tabDepth + 1) + pline2.rstrip())
    >
    > out.append(indent(tabDepth) + clo_tag())
    > return 1

2.  add elif statement changed the following
    >        if title.endswith(".txt"):
    >            body = getbody(title, Lines)
    >        elif title.endswith(".md"):
    >            body = get_md_body(title, Lines)S
