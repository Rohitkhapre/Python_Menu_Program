import subprocess
import os
import time

def list_docker_images():
    print(subprocess.getoutput("docker images"))

def pull_docker_image():
    imageName = input("Enter Image Name: ")
    imageVersion = input("Enter Version (Press Enter for the latest version): ")
    if imageVersion:
        imageName = f"{imageName}:{imageVersion}"
    print(subprocess.getoutput(f"docker pull {imageName}"))

def run_docker_container():
    ImageName = input("Enter Image Name: ")
    ConName = input("Enter Container Name (optional): ")
    command = input("Enter the command to run in the container (press Enter for interactive bash): ") or "/bin/bash"
    
    docker_run_command = ["docker", "run", "-it", "--name", ConName, ImageName, command]
    subprocess.run(docker_run_command)

def list_docker_containers():
    print(subprocess.getoutput("docker ps -a"))

def delete_docker_container():
    container_id = input("Enter the Container ID to delete: ")
    print(subprocess.getoutput(f"docker stop {container_id}"))
    print(subprocess.getoutput(f"docker rm {container_id}"))

if __name__ == "__main__":
    while True:
        print("1. List Docker Images")
        print("2. Pull Docker Image")
        print("3. Run Docker Container")
        print("4. List Docker Containers")
        print("5. Delete Docker Container")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            list_docker_images()
        elif choice == "2":
            pull_docker_image()
        elif choice == "3":
            run_docker_container()
        elif choice == "4":
            list_docker_containers()
        elif choice == "5":
            delete_docker_container()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

