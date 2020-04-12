import os


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    YELLOW = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def main():
    photos()


def photos():
    # example C:/Users/Austin/Documents
    folder_location = input("Please enter your folder location: ")
    # check file types in folder_location
    photo_file_extensions = ("jpg", "jpeg", "png", "bmp", "gif")
    # prints list of photos
    dir_name = folder_location + '/photos'
    try:
        # Create target Directory
        os.mkdir(dir_name)
        print("Directory ", dir_name, " Created ")
    except FileExistsError:
        # checks if folder exists
        print("Directory ", dir_name, " already exists")
    for file in os.listdir(folder_location):
        if file.endswith(photo_file_extensions):
            # prints all file types
            # Create directory
            print(f"{bcolors.YELLOW}File Name:{bcolors.ENDC} {file}")


main()
