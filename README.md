# Downloads-Folder-Organizer
This Python project is designed to run on Windows OS only. It is an automated file organizer that listens for changes in your Downloads folder (or any specified source directory) and moves files to their respective directories based on the file type.
It supports a wide range of file types, including images, videos, audio files, documents, and ebooks. 

This project uses the watchdog library to monitor directory changes and perform actions accordingly.

### Features
- Automatic File Sorting: Automatically sorts files from your Downloads folder into specified folders for music, pictures, videos, documents, and ebooks.
Wide Range of File Types Supported: Includes predefined lists of file extensions for various media and document types.
- Customizable Paths: Easily customizable source and destination directories.
Conflict Resolution: When a file with the same name exists in the destination, it renames the moved file to avoid overwriting.
- Logging: Logs every file move action for audit and debug purposes.
### Installation
Before running this script, ensure you have Python installed on your system and install the required packages.

Make sure to change the hard-coded root and destination file path.

### Prerequisites
-Python 3.6 or newer
-watchdog library for monitoring file system events.

You can install the watchdog library using pip:

```bash
Copy code
pip install watchdog
Clone the Project
```

Clone this repository to your local machine:

```bash
Copy code
git clone
```
### Automate
Follow the instructions below to run the script automatically at system start-up.

1. Open Command Prompt in the program folder.
2. Install **pyinstaller**:
```bash
pip install pyinstaller
```
3. Save your .py file as an executable .exe. Replace main.py with actuall file name if differs.
```bash
 py -m PyInstaller --onefile main.py
```
4. Locate main.exe file in the newly created 'dist' folder. Create a shortcut and copy it.
5. Slect ⊞ Win + R on your keybard to open the "Run Program Or File" Window and type **shell:startup** under **Open**.
Paste a copied shortcut into the Startup folder for the program to run automatically on startup. The program will terminate if Command Prompt is closed.

## Disclaimer and Future Improvements
This project is currently in a developmental stage, and ongoing updates are anticipated as part of the learning and enhancement process. 
The primary objective is to evolve the script to trigger actions based on the detection of new downloads, rather than requiring it to run continuously or be initiated at system startup. 
This approach aims to improve efficiency and responsiveness.

Additionally, there are plans to extend compatibility and optimize the script for macOS and Linux environments, broadening its applicability and utility across different operating systems.

Your contributions, suggestions, and feedback are welcome as we strive to improve and expand the functionality of this tool.

Feel free to customize and extend the code as needed for your specific use case.
``` javascript

Replace `your-username` with your actual GitHub username in the repository URL.

```

