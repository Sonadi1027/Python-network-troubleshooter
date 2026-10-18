import subprocess

print("=======================================")
print("   PYTHON NETWORK TROUBLESHOOTING TOOL")
print("=======================================")

host = input("Enter an IP address or hostname to ping: ")

print("\nChecking Network Connectivity...")

try:
    result = subprocess.run(
        ["ping", "-n", "4", host],
        capture_output=True, 
        text=True,
        timeout=15
    )

    if result.returncode == 0:
        print("\nResult: SUCCESS")
        print("The host responded to the ping test.")

    else:
        print("\nResult: FAILURE")
        print("The host did not respond successfully")

    print("\nPing details:")
    print(result.stdout)

except subprocess.TimeoutExpired:
    print("\nResult: TIMEOUT")

except FileNotFoundError:
    print("\nError: 'ping' command not found.")