import argparse
import json
import asstLib


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version="%(prog)s 0.1",
        help="display tool name and version.",
    )
    parser.add_argument(
        "-i", "--input", help="specify an input file or folder to be processed."
    )
    parser.add_argument(
        "-l",
        "--lang",
        nargs="?",
        type=str,
        default="en=CA",
        help="Language of the document (default is en=CA)",
    )
    parser.add_argument("-c", "--config", help="specify a config file to be processed")
    args = parser.parse_args()
    input = args.input

    if args.config is not None:
        try:
            with open(args.config, "r", encoding="utf-8") as config_file:
                config = json.load(config_file)
                if "input" in config:
                    input = config["input"]
                else:
                    input = None
                if "lang" in config:
                    args.lang = config["lang"]
        except FileNotFoundError:
            print(f'Error: File "{args.config}" cannot be found!')
        except json.JSONDecodeError:
            print(f'Error: File "{args.config} has invalid JSON syntax!" ')

    if input is None:
        print(
            f"Error: Input is not found! Please specify a {args.config} to be processed."
        )
        exit()

    if args.lang is not None:
        langlist = "".join(args.lang)
        lang = langlist.strip()

    all_files = []
    folder = ""

    # output .md file
    if not input.endswith(".md"):
        #    folder = input + "/"
        all_files = asstLib.get_files(folder)
    else:
        all_files.append(input)

    for file in all_files:
        file_path = folder + file
        title = asstLib.get_md_title(file_path)
        bodycont = asstLib.generate_md_content(file_path, title)
        html = asstLib.format_to_html(file, title, bodycont, lang)
        asstLib.output_result(file, html)

    # output .txt file
    if not input.endswith(".txt"):

        #    folder = input + "/"
        all_files = asstLib.get_files(folder)
    else:
        all_files.append(input)

    for file in all_files:
        file_path = folder + file
        title = asstLib.get_txt_title(file_path)
        bodycont = asstLib.generate_txt_content(file_path, title)
        html = asstLib.format_to_html(file, title, bodycont, lang)
        asstLib.output_result(file, html)


main()
