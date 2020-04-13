import os

"""
@Author Austin
Folder Organizer
"""


# TODO: add more file extension clean ups.
# TODO: Move files into folder destination.


class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


folder_location = input("Please enter your folder location: ")


def photos():
    # example C:/Users/Austin/Documents
    # check file types in folder_location
    """
    ###
    #start photo organization
    ###
    """
    photo_file_extensions = ("jpg", "jpeg", "png", "bmp", "gif")
    # prints list of photos
    dir_name = folder_location + '/photos'
    try:
        # Create target Directory
        os.mkdir(dir_name)
        print(f"{Colors.HEADER}Directory{Colors.END} {dir_name} {Colors.HEADER}Created{Colors.END} \n")
    except FileExistsError:
        # checks if folder exists
        print(f"{Colors.RED}Directory {Colors.END}{dir_name} {Colors.RED}already exists{Colors.END}\n")
    for file in os.listdir(folder_location):
        if file.endswith(photo_file_extensions):
            # prints all file types
            # Create directory
            print(f"{Colors.YELLOW}File Name:{Colors.END} {file}")
    documents()


def documents():
    dir_name = folder_location + '/documents'
    document_file_extensions = ("doc", "pdf", "txt", "ods", "XLS")
    try:
        # Create target Directory
        os.mkdir(dir_name)
        print(f"{Colors.HEADER}Directory{Colors.END} {dir_name} {Colors.HEADER}Created{Colors.END} \n")
    except FileExistsError:
        # checks if folder exists
        print(f"{Colors.RED}Directory {Colors.END}{dir_name} {Colors.RED}already exists{Colors.END}\n")
    for file in os.listdir(folder_location):
        if file.endswith(document_file_extensions):
            # prints all file types
            # Create directory
            print(f"{Colors.BLUE}File Name:{Colors.END} {file}")


photos()
