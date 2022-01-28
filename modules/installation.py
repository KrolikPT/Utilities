import os

def install():
    os.system("sudo cp utls.py /bin/utls")
    os.system("sudo mkdir /bin/modules")
    os.system("sudo cp modules/* /bin/modules/")
    os.system("sudo chmod +x /bin/utls")
    print("Script installed!")
    print("Now you can use only: utls [OPTION]")


def uninstall():
    os.system("sudo rm /bin/utls")
    os.system("sudo rm -rf /bin/modules/*")
    print("The script was removed!")