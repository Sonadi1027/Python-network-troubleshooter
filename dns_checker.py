import socket

print("================")
print("DNS Checker")
print("================")

hostname = input("Enter a website name: ")

try:
    ip_address = socket.gethostbyname(hostname)

    print("\nDNS Lookup Result: SUCCESS")
    print("Hostname:", hostname)
    print("IP Address:", ip_address)

except socket.gaierror:
    print("\nDNS Lookup Result: FAILURE")
    print("The hostname could not be resolved.")

    