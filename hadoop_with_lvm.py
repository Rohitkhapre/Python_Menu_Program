import os
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

speak("hello Rohit... welcome to your Terminal.. I am your voice assistant. Please tell me how may I help you...")
print("\t\t\t Hey Rohit! Welcome to my TUI that makes life simple") 

while True:
    print("""              
    1. Check available disk
    2. Create a physical volume
    3. Create a volume group
    4. Create a logical volume
    5. Format a logical volume partition
    6. Mount the logical volume to a folder
    7. Show the mount space
    8. Start the datanode
    9. Show running Java processes
    10. Show the report of connected datanodes
    11. Increase the size of a logical volume
    12. Resize LVM while datanode connected
    13. Start Docker services
    14. Show available Docker images
    15. Launch Docker OS
    16. Show running Docker OS
    17. Exit
    """)
    
    choice = input("Enter your choice: ")

    if choice == "1":
        os.system('ssh -i docker3.pem ec2-user@100.25.158.237 "sudo fdisk -l"')
    elif choice == "2":
        os.system('ssh -i docker3.pem ec2-user@100.25.158.237 "sudo pvcreate /dev/xvdb /dev/xvdc"')
        os.system('ssh -i docker3.pem ec2-user@100.25.158.237 "sudo pvdisplay"')
    elif choice == "3":
        VGname = input("Enter volume group name: ")
        os.system('ssh -i docker3.pem ec2-user@100.25.158.237 "sudo vgcreate {} /dev/sdc /dev/sdb"'.format(VGname))
        os.system('ssh -i docker3.pem ec2-user@100.25.158.237 "sudo vgdisplay"')
    elif choice == "4":
        RequiredSize = input("Enter required size: ")
        LVname = input("Enter logical volume name: ")
        os.system('ssh -i docker3.pem ec2-user@100.25.158.237 "sudo lvcreate --size {} --name {} myvg"'.format(RequiredSize, LVname))
        os.system('ssh -i docker3.pem ec2-user@100.25.158.237 "sudo lvdisplay"')
    elif choice == "5":
        os.system('ssh -i docker3.pem ec2-user@100.25.158.237 "sudo mkfs.ext4 /dev/myvg/vklv"')
    elif choice == "6":
        mountpoint = input("Enter mount point: ")
        os.system('ssh -i docker3.pem ec2-user@100.25.158.237 "sudo mount /dev/myvg/vklv /{}"'.format(mountpoint))
        os.system('ssh -i docker3.pem ec2-user@100.25.158.237 "sudo df -Th"')
    elif choice == "7":
        os.system('ssh -i docker3.pem ec2-user@100.25.158.237 "sudo df -Th"')
    elif choice == "8":
        os.system('ssh -i docker3.pem ec2-user@100.25.158.237 "sudo hadoop-daemon.sh start datanode"')
    elif choice == "9":
        os.system('ssh -i docker3.pem ec2-user@100.25.158.237 "sudo jps"')
    elif choice == "10":
        os.system('ssh -i docker3.pem ec2-user@100.25.158.237 "sudo hadoop dfsadmin -report"')
    elif choice == "11":
        SizeOfLv = input("Enter the size of logical volume: ")
        os.system('ssh -i docker3.pem ec2-user@100.25.158.237 "sudo lvresize -L {} /dev/myvg/vklv"'.format(SizeOfLv))
        os.system('ssh -i docker3.pem ec2-user@100.25.158.237 "sudo lvs"')
    elif choice == "12":
        os.system('ssh -i docker3.pem ec2-user@100.25.158.237 "sudo resize2fs -f /dev/myvg/vklv"')
    elif choice == "13":
        os.system('ssh -i docker3.pem ec2-user@100.25.158.237 "sudo systemctl start docker"')
    elif choice == "14":
        os.system('ssh -i docker3.pem ec2-user@100.25.158.237 "sudo docker images"')
    elif choice == "15":
        os.system('ssh -i docker3.pem ec2-user@100.25.158.237 "sudo docker run -itd centos"')
    elif choice == "16":
        os.system('ssh -i docker3.pem ec2-user@100.25.158.237 "sudo docker ps"')
    elif choice == "17":
        speak("Thank you for using me. I am always here to help. Goodbye...")
        break
    else:
        speak("Option not supported. Please try again.")

