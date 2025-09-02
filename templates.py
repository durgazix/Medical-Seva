import os

# Project structure definition
structure = {
    "src": [
        "__init__.py",
        "helper.py",
        "prompt.py"
    ],
    "research": [
        "trials.ipynb"
    ],
    "root": [
        ".env",
        "setup.py",
        "app.py",
    ]
}

def create_directories_and_files(base_path="."):
    for folder, files in structure.items():
        if folder == "root":
            # Create files at root level
            for file in files:
                file_path = os.path.join(base_path, file)
                if not os.path.exists(file_path):
                    with open(file_path, "w") as f:
                        pass
                    print(f"Created file: {file_path}")
        else:
            # Create directory
            dir_path = os.path.join(base_path, folder)
            os.makedirs(dir_path, exist_ok=True)
            print(f"Created directory: {dir_path}")
            
            # Create files inside directory
            for file in files:
                file_path = os.path.join(dir_path, file)
                if not os.path.exists(file_path):
                    with open(file_path, "w") as f:
                        pass
                    print(f"Created file: {file_path}")

if __name__ == "__main__":
    create_directories_and_files()
