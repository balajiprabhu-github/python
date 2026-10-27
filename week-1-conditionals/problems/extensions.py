"""
Problem: File Extensions (extensions.py)

In extensions.py, implement a program that prompts the user for the name of a file
and then outputs that file’s media type (MIME type).

Requirements:
- Case-insensitively and ignoring leading/trailing spaces:
    - .gif               -> image/gif
    - .jpg or .jpeg      -> image/jpeg
    - .png               -> image/png
    - .pdf               -> application/pdf
    - .txt               -> text/plain
    - .zip               -> application/zip
- If the file’s name ends with some other suffix or has no suffix at all,
  output: application/octet-stream
"""

def main():
    # TODO: Prompt the user for a file name
    ...

    # TODO: Determine the media type and print the result
    ...


if __name__ == "__main__":
    main()
