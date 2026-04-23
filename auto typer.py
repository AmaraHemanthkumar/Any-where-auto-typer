# This code is based on the original by Amara Hemanth Kumar
from pynput.keyboard import Controller
import time
import os

def main():
    print("--- Auto-Typer ---")
    print("Make sure the tab where you want to auto-type is convenient to reach.\n")
    
    # Get file location
    L = input("Enter the full file path: ").strip()
    
    # Check if the file exists to prevent crashing
    if not os.path.exists(L):
        print("Error: File not found. Please check the path and try again.")
        return

    # Using 'with open' ensures the file is safely closed after reading, even if an error occurs
    try:
        with open(L, 'r', encoding='utf-8') as file:
            content = file.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    total_chars = len(content)
    if total_chars == 0:
        print("The file is empty. Nothing to type.")
        return

    print(f"\nFile loaded successfully! Total characters: {total_chars}")

    # Give the user options for speed or total time
    print("\nHow would you like to set the typing speed?")
    print("1. Set delay between keystrokes (Speed)")
    print("2. Set total time to finish the task (Time)")
    choice = input("Enter 1 or 2: ").strip()

    delay = 0.1 # Default delay
    if choice == '1':
        try:
            delay = float(input("Enter delay between keystrokes in seconds (e.g., 0.1): "))
        except ValueError:
            print("Invalid input. Defaulting to 0.1 seconds.")
    elif choice == '2':
        try:
            total_time = float(input(f"Enter total time to finish in seconds (e.g., 60): "))
            # Calculate the required delay per character to meet the total time limit
            delay = total_time / total_chars
            print(f"Calculated delay per character: {delay:.4f} seconds")
        except ValueError:
            print("Invalid input. Defaulting to 0.1 seconds delay.")
    else:
        print("Invalid choice. Defaulting to 0.1 seconds delay.")

    # Allow user to customize the wait time before typing starts (instead of a fixed 20 seconds)
    try:
        wait_time = int(input("\nHow many seconds do you need to click on your target window? (e.g., 5): "))
    except ValueError:
        wait_time = 5
        print("Invalid input. Defaulting to 5 seconds.")

    print("\nCAUTION!!! Please do not interfere with the mouse or keyboard while auto-typing.")
    print(f"Starting in {wait_time} seconds. Click on the target text area now!\n")
    
    time.sleep(wait_time)

    # Initialize the controller and start typing
    keyboard = Controller()
    
    # We don't need a split() function; Python can iterate directly over a string
    for char in content:
        keyboard.type(char)
        time.sleep(delay)
        
    print("\nAuto-typing task finished successfully!")

if __name__ == "__main__":
    main()
