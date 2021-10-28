 <h1 align="center">Magic Static Site Generator</h1>



&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Magic-SSG is a simple Static Site Generator tool, and it can help you to generate .html from . txt files. Current version is 0.1 .

<img align="left" src="static\img\contract.png" width="50px" height="50px" />

## Features

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; So far, this tool has the following functions:

- Allows the user to specify an input file or folder to open a .txt file and generate a .html file.
- Automatically identify titles and content.
- Specify a different output directory using --output or -o.
- Allow the input to be a deep tree of files and folders.
- Allow user to check the tool's version.
- Allow the language input and SSG can generate the lang attribute on the root <html> element
- Allow user to supply a JSON formatted configuration file

<img align="left" src="static\img\install2.png" width="50px" height="50px" />

## Installation

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Make sure you have installed Python version 3.8.5 or above.

<img align="left" src="static\img\about.png" width="50px" height="50px" />

## How to use

1. Generate a .html file from a file or folder:

   > ` python magic_ssg.py -i/--input <file name or folder name>`

2. Specify a different output directory using --output or -o.

   > python magic_ssg.py --input <input file name or folder name> --output <out put folder>

3. Check the tool's version

   > ` python magic_ssg.py –v/--version`

4. Display how to use the tool

   > ` python magic_ssg.py –h`

5. Input the language
   > ` python magic_ssg.py -i file_name -l language`

6. Input a JSON config file
   > ` python magic_ssg.py -c file_name`

<img align="left" src="static\img\Example.png" width="50px" height="50px" />

## Example 1

### Full list of features:

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/lvd5ao4h7r1bm1prpk4g.png)

### input file:

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/r2lv22xz6b8byl84cn8r.png)

### output file:

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/r08erike6kspvnx3yd9u.png)

<img align="left" src="static\img\Example.png" width="50px" height="50px" />

## Example 2

### Convert a file named test.txt and select language- Fr

> `python magic_ssg.py -i test.txt -l Fr`

<img align="left" src="static\img\Example.png" width="50px" height="50px" />

## Example 3

> `python magic_ssg.py -c ssg-config.json`
> 
### input file

```js
// ssg-config.json
{
    "input": "./test.txt",
    "lang": "en-CA"
}
```

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/r2lv22xz6b8byl84cn8r.png)

### output file

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/r08erike6kspvnx3yd9u.png)