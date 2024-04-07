from netmiko import ConnectHandler

def connect_to_arista_device(ip, username, password):
    """
    Connects to an Arista device and runs 'show ip int brief'.

    :param ip: IP address of the Arista device.
    :param username: Username for authentication.
    :param password: Password for authentication.
    """
    # Define device parameters
    arista_device = {
        'device_type': 'arista_eos',
        'host': ip,
        'username': username,
        'password': password,
        'port': 22,  # Optional, default is 22
        'secret': '',  # Optional, default is ''
    }

    try:
        # Establish an SSH connection to the device
        with ConnectHandler(**arista_device) as net_connect:
            # Entering enable mode
            net_connect.enable()

            # Running the 'show ip int brief' command
            output = net_connect.send_command('sh run')
            print(output)
            print("Hello")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Device IP address
    ip_address = '192.168.1.58'
    # Device login credentials
    username = 'cisco'
    password = 'cisco'

    # Connect to the device and run the command
    connect_to_arista_device(ip_address, username, password)
