import boto3

def create_key_pair(key_name):
    ec2 = boto3.resource('ec2', region_name='us-east-1')

    # Check if the key pair already exists
    key_pairs = ec2.key_pairs.filter(KeyNames=[key_name])
    if list(key_pairs):
        print(f"Key pair '{key_name}' already exists.")
    else:
        key_pair = ec2.create_key_pair(KeyName=key_name)
        print(f"Key pair '{key_name}' created successfully.")
        print(f"Save the private key:\n{key_pair.key_material}")

def launch_instance(key_name, security_group_name):
    ec2 = boto3.resource('ec2', region_name='us-east-1')

    # Get the security group ID from the name
    security_group_id = get_security_group_id_by_name(security_group_name)

    # Launch the instance
    instance = ec2.create_instances(
        ImageId='ami-0c55b159cbfafe1f0',  # Replace this with your desired AMI ID
        MinCount=1,
        MaxCount=1,
        InstanceType='t2.micro',
        KeyName=key_name,
        SecurityGroupIds=[security_group_id]
    )[0]

    instance.wait_until_running()
    instance.reload()

    print(f"Instance with ID '{instance.id}' launched successfully.")
    print(f"Public IP Address: {instance.public_ip_address}")
    print(f"Instance State: {instance.state['Name']}")
    print(f"Instance Type: {instance.instance_type}")

def create_security_group(group_name, description):
    ec2 = boto3.client('ec2', region_name='us-east-1')

    # Create the security group
    response = ec2.create_security_group(
        GroupName=group_name,
        Description=description
    )

    security_group_id = response['GroupId']
    print(f"Security Group '{group_name}' created with ID: {security_group_id}")

    # Ask for ports to allow
    allowed_ports = input("Enter the ports to allow (e.g., 22,80,443): ").strip()
    if allowed_ports:
        ports = [int(port.strip()) for port in allowed_ports.split(",")]
        for port in ports:
            ec2.authorize_security_group_ingress(
                GroupId=security_group_id,
                IpPermissions=[
                    {
                        'IpProtocol': 'tcp',
                        'FromPort': port,
                        'ToPort': port,
                        'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
                    }
                ]
            )
        print(f"Inbound TCP ports {allowed_ports} allowed to the security group.")

    return security_group_id

def list_instances():
    ec2 = boto3.client('ec2', region_name='us-east-1')

    # Get and print the list of instances
    response = ec2.describe_instances()
    instances = response['Reservations']

    print("Instances:")
    for instance in instances:
        instance_id = instance['Instances'][0]['InstanceId']
        instance_state = instance['Instances'][0]['State']['Name']
        instance_ip = instance['Instances'][0].get('PublicIpAddress', 'N/A')
        instance_type = instance['Instances'][0]['InstanceType']
        print(f"Instance ID: {instance_id}, State: {instance_state}, Public IP: {instance_ip}, Instance Type: {instance_type}")

def get_security_group_id_by_name(group_name):
    ec2 = boto3.client('ec2', region_name='us-east-1')
    response = ec2.describe_security_groups(Filters=[{'Name': 'group-name', 'Values': [group_name]}])
    security_groups = response['SecurityGroups']
    if security_groups:
        return security_groups[0]['GroupId']
    else:
        raise ValueError(f"Security group '{group_name}' not found.")

def list_security_groups():
    ec2 = boto3.client('ec2', region_name='us-east-1')

    # Get and print the list of security groups
    response = ec2.describe_security_groups()
    security_groups = response['SecurityGroups']

    print("Security Groups:")
    for group in security_groups:
        group_name = group['GroupName']
        group_desc = group['Description']
        print(f"Group Name: {group_name}, Description: {group_desc}")

def delete_instance(instance_id):
    ec2 = boto3.resource('ec2', region_name='us-east-1')

    # Terminate the instance
    instance = ec2.Instance(instance_id)
    instance.terminate()
    print(f"Instance with ID '{instance_id}' has been terminated.")

def show_running_instances():
    ec2 = boto3.resource('ec2', region_name='us-east-1')

    # Get and print running instances
    instances = ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])

    print("Running Instances:")
    for instance in instances:
        print(f"Instance ID: {instance.id}, Public IP: {instance.public_ip_address}, Instance Type: {instance.instance_type}")

def stop_instance(instance_id):
    ec2 = boto3.resource('ec2', region_name='us-east-1')

    # Stop the instance
    instance = ec2.Instance(instance_id)
    instance.stop()
    print(f"Instance with ID '{instance_id}' has been stopped.")

def start_instance(instance_id):
    ec2 = boto3.resource('ec2', region_name='us-east-1')

    # Start the instance
    instance = ec2.Instance(instance_id)
    instance.start()
    print(f"Instance with ID '{instance_id}' has been started.")

if __name__ == "__main__":
    while True:
        print("1. Create Key Pair")
        print("2. Launch Instance")
        print("3. Create Security Group")
        print("4. List Instances")
        print("5. List Security Groups")
        print("6. Delete Instance")
        print("7. Show Running Instances")
        print("8. Stop Instance")
        print("9. Start Instance")
        print("10. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            key_name = input("Enter the key pair name: ")
            create_key_pair(key_name)
        elif choice == "2":
            key_name = input("Enter the key pair name: ")
            security_group_name = input("Enter the security group name: ")
            launch_instance(key_name, security_group_name)
        elif choice == "3":
            group_name = input("Enter the security group name: ")
            description = input("Enter the security group description: ")
            security_group_id = create_security_group(group_name, description)
        elif choice == "4":
            list_instances()
        elif choice == "5":
            list_security_groups()
        elif choice == "6":
            instance_id = input("Enter the instance ID to delete: ")
            delete_instance(instance_id)
        elif choice == "7":
            show_running_instances()
        elif choice == "8":
            instance_id = input("Enter the instance ID to stop: ")
            stop_instance(instance_id)
        elif choice == "9":
            instance_id = input("Enter the instance ID to start: ")
            start_instance(instance_id)
        elif choice == "10":
            break
        else:
            print("Invalid choice. Please try again.")

