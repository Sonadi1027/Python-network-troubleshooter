
import socket

print("================================")
print("       TCP PORT CHECKER")
print("================================")

host = input("Enter Hostname or IP address: ").strip()

try:
    port = int(input("Enter a port number (1-65535): "))

    if port < 1 or port > 65535:
        print("\nError: Enter a port between 1 and 65535.")

    else:
        print("\nChecking TCP connection...")

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            client.settimeout(5)
            result = client.connect_ex((host, port))

        if result == 0:
            print("\nResult: PORT OPEN")
            print(f"TCP port {port} is accepting connections on {host}.")
        else:
            print("\nResult: PORT CLOSED OR UNREACHABLE")
            print(f"Could not connect to {host} on TCP port {port}.")

except ValueError:
    print("\nError: Please enter a valid port number.")

except socket.gaierror as error:
    print("\nError: Could not resolve the hostname.")
    print("Details:", error)

except OSError as error:
    print("\nConnection error:", error)
