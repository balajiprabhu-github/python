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
    user_input = input("File name: ")

    filename = user_input.strip().lower()
    
    if filename.endswith(".gif"):
        print("image/gif")
    elif filename.endswith((".jpg", ".jpeg")):
        print("image/jpeg")
    elif filename.endswith(".png"):
        print("image/png")
    elif filename.endswith(".pdf"):
        print("application/pdf")
    elif filename.endswith(".txt"):
        print("text/plain")
    elif filename.endswith(".zip"):
        print("application/zip")
    else:
        print("application/octet-stream")

if __name__ == "__main__":
    main()
