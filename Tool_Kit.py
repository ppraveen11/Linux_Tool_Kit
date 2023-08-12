import os
import subprocess as sp
#from subprocess import call
import datetime
import sys


def additional_commands_menu22():
    while True:
        os.system("clear")  # Clear the terminal screen
        print("Additional Commands")
        print("===================")
        print("1. Display Date and Time")
        print("2. Network Configuration")
        print("3. Check System Information")
        print("4. Check Disk Usage")
        print("5. Check Network Connectivity")
        print("6. Web Server Setup")
        print("b. Back to main menu")
        print("q. Exit")

        choice = input("Select an option: ")

        if choice in ["1", "01"]:
            display_date_and_time()
        elif choice in ["2", "02"]:
            network_configuration()
        elif choice in ["3", "03"]:
            check_system_information()
        elif choice in ["4", "04"]:
            check_disk_usage()
        elif choice in ["5", "05"]:
            check_network_connectivity()
        elif choice in ["6", "06"]:
            web_server()
        elif choice.lower() == "b":
            main_menu22()  # Exit the loop and return to the main menu
        elif choice.lower() == "q":
            sys.exit()  # Exit the program


def disk_management_menu22():
    while True:
        os.system("clear")  # Clear the terminal screen
        print("Disk Management")
        print("==============")
        print("1. Help [Steps for creating LVM]")
        print("2. Check how many storages are attached")
        print("3. Create Physical Volume (PV)")
        print("4. Get Physical Volume details")
        print("5. Create Volume Group (VG)")
        print("6. Get Volume Group details")
        print("7. Create Logical Volume (LV)")
        print("8. Get Logical Volume details")
        print("9. Format the Logical Volume (LV)")
        print("b. Go back to main menu")

        choice = input("Select an option: ")

        if choice in ["1", "01"]:
            get_steps()
        elif choice in ["2", "02"]:
            get_physical_stroages()
        elif choice in ["3", "03"]:
            create_physical_volume()
        elif choice in ["4", "04"]:
            get_all_pvs()
        elif choice in ["5", "05"]:
            create_volume_group()
        elif choice in ["6", "06"]:
            get_vg_details()
        elif choice in ["7", "07"]:
            create_logical_volume()
        elif choice in ["8", "08"]:
            get_logical_volume()
        elif choice in ["9", "09"]:
            format_logical_volume()

        elif choice.lower() == "b":
            #main_menu_banner22() 
            main_menu22()






# Disk Management Functions

def get_steps():
    print("""
        1. Select the physical storage devices for LVM
        2. Create the Volume Group from Physical Volumes
        3. Create Logical Volumes from Volume Group
    """)
    input("\n\nPress Enter to continue...:\t")

def get_physical_stroages():
   sp.run("clear", shell=True)
   sp.run("fdisk -l", shell=True)
   input("\n\nPress Enter to continue...:\t")

def create_physical_volume():
    #To create a physical volume (PV)
    sp.run("clear", shell=True)
    device_name = input("Enter Physical storage name from you want to create physical volume [eg: /dev/sdb] :" )
    sp.run("sudo pvcreate {}".format(device_name), shell=True)
    sp.run("sudo pvdisplay {}".format(device_name), shell=True) 
    input("\n\nPress Enter to continue...:\t")

def get_all_pvs():
    sp.run("clear", shell=True)
    sp.run("sudo pvdisplay", shell=True)
    input("\n\nPress Enter to continue...:\t")

def create_volume_group():
    #To create a volume group (VG)
        sp.run("clear", shell=True)
        vg_name = input("Enter Volume Group name :")
        pv_name = input("Enter Physical Volume name :")
        sp.run("sudo vgcreate {} {}".format(vg_name, pv_name), shell=True)
        sp.run("sudo vgdisplay {}".format(vg_name), shell=True)
        input("\n\nPress Enter to continue...:\t")

def get_vg_details():
    sp.run("clear", shell=True)
    vg_name = input("Enter Volume Group name :")
    sp.run("sudo vgdisplay {}".format(vg_name), shell=True)
    input("\n\nPress Enter to continue...:\t")


def create_logical_volume():
     sp.run("clear", shell=True)
     lv_name = input("Enter New Logical Volume name :")
     vg_name = input("Enter Volume Group Name(VG) :")
     size    = input("Enter the size of Logical Volume(LV) :")
     sp.run("sudo lvcreate --size {} --name {} {}".format(size, lv_name, vg_name), shell=True)
     sp.run("sudo lvdisplay {}/{}".format(vg_name, lv_name), shell=True)
     choice = input("Do you want to format this logical volume now? [y/N]")
     if choice.lower() == 'y':
        format_logical_volume("{}/{}".format(vg_name, lv_name))
     input("\n\nPress Enter to continue...:\t")   


def format_logical_volume(lv_name=""):
     sp.run("clear", shell=True)
     lv_name = input("Enter the Logical Volume name (eg: vg_name/lv_name) :")
     file_system =  input("Enter the file system (ext2, ext3, ext4, minix, xfs, cramfs) :")
     sp.run("sudo mkfs.{} /dev/{}".format(file_system, lv_name), shell=True)   
     input("\n\nPress Enter to continue...:\t")

def get_logical_volume():
    sp.run("clear", shell=True)
    lv_name = input("Enter Logical Volume Name (eg: vg_name/lv_name) : ")
    sp.run("sudo lvdisplay /dev/{}".format(lv_name), shell=True)
    input("\n\nPress Enter to continue...:\t")

def mount_logical_volume():
    sp.run("clear", shell=True)
    lv_name = input("Enter the Logical Volume name (eg: vg_name/lv_name) :")
    mount_path = input("Enter absolute path of directory for mounting :")
    sp.run("mkdir -p {}".format(mount_path), shell=True)
    sp.run("sudo mount /dev/{} {}".format(lv_name, mount_path), shell=True)
    sp.run("sudo lsblk /dev/{}".format(lv_name), shell=True)  
    input("\n\nPress Enter to continue...:\t")





# Additional Commands Functions


def display_date_and_time():
    now = datetime.datetime.now()
    print("Current date and time:", now)
    print("hello")
    input("\n\nPress Enter to continue...:\t")

def network_configuration():
    print("Network Configuration:")
    sp.run("ip addr", shell=True)
    input("\n\nPress Enter to continue...:\t")


def check_system_information():
    sp.run("uname -a", shell=True)
    input("\n\nPress Enter to continue...:\t")

def check_disk_usage():
    sp.run("df -h", shell=True)  
    input("\n\nPress Enter to continue...:\t")

def check_network_connectivity():
    sp.run("ping -c 4 www.google.com", shell=True)
    input("\n\nPress Enter to continue...:\t")

def web_server():
    sp.run("sudo yum install httpd", shell=True)
    sp.run("sudo systemctl start httpd", shell=True)
    input("\n\nPress Enter to continue...:\t")

def main_menu_banner(): 
    sp.run(["python", "4mtest4.py"], shell=False)
    input("\n\nPress Enter to continue...:\t")
    


def display_banner22():
    print("**************************************")
    print("*            Linux Toolkit           *")
    print("**************************************")

def main_menu22():
    while True:
        os.system("clear")  # Clear the terminal screen
        display_banner22()

        print("\nHey, what do you want to do?")
        print("""
            1. Disk Management
            2. Execute Linux Commands
            0. Exit
            """)

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Not a valid integer! Please try again...")
            continue

        if choice == 1:
            disk_management_menu22()
        elif choice == 2:
            additional_commands_menu22()
        elif choice == 0:
            print("\n\nGoodbye! Thank you for using Linux Toolkit.")
            sys.exit()

if __name__ == "__main__":
    print("Welcome To Manage LVM")
    main_menu22()


