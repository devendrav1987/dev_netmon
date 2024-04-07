import os

def show_current_working_directory():
    """
    Prints the current working directory.
    """
    cwd = os.getcwd()
    print(f"The current working directory is: {cwd}")

if __name__ == "__main__":
    show_current_working_directory()
