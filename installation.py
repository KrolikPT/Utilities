import os

def install():
    os.system("sudo cp utls.py /bin/utls")
    os.system("sudo cp colors.py /bin/colors.py")
    os.system("sudo cp file_creator.py /bin/file_creator.py")
    os.system("sudo chmod +x /bin/utls")
    print("Script installed!")
    print("Now you can use only: utls [OPTION]")


def uninstall():
    os.system("sudo rm /bin/utls")
    os.system("sudo rm /bin/colors.py")
    os.system("sudo rm /bin/file_creator.py")
    print("The script was removed!")