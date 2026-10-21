
import subprocess
import sys

def run_tool(filename):
    subprocess.run([sys.executable, filename])
    input("\nPress Enter to return to the main menu...")

def main():
    while True:
        print("\n================================")
        print("  PYTHON NETWORK TROUBLESHOOTER")
        print("================================")
        print("1. Ping Test")
        print("2. DNS Checker")
        print("3. TCP Port Checker")
        print("4. Exit")

        choice = input("\nEnter your choice (1-4): ").strip()

        if choice == "1":
            run_tool("ping_tool.py")

        elif choice == "2":
            run_tool("dns_checker.py")

        elif choice == "3":
            run_tool("port_checker.py")

        elif choice == "4":
            print("\nThank you for using the tool!")
            print("Exiting...")
            break

        else:
            print("\nInvalid choice. Please enter 1, 2, 3, or 4.")
            input("Press Enter to try again...")

if __name__ == "__main__":
    main()
