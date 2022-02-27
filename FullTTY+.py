## Script para shell full TTY interactiva

from pynput.keyboard import Key, Controller
from time import sleep

keyboard = Controller()

sleep(3)
keyboard.type("python3"+" -c 'import pty; pty.spawn(\"/bin/bash\")'")
keyboard.press(Key.enter)
keyboard.release(Key.enter)
sleep(1)
keyboard.type('export TERM=screen-256color')
keyboard.press(Key.enter)
keyboard.release(Key.enter)
sleep(1)


keyboard.press(Key.ctrl)
keyboard.press('z')
keyboard.release(Key.ctrl)
keyboard.release('z')


keyboard.type('stty raw -echo && fg')
keyboard.press(Key.enter)
keyboard.release(Key.enter)
keyboard.type('reset')
keyboard.press(Key.enter)
keyboard.release(Key.enter)
sleep(0.5)
keyboard.type('export TERM=screen-256color')
keyboard.press(Key.enter)
keyboard.release(Key.enter)
keyboard.type('export TERM=screen')
keyboard.press(Key.enter)
keyboard.release(Key.enter)











'''python3 -c "import pty; pty.spawn("/bin/bash")"
# python3 -c 'import pty; pty.spawn("/bin/bash")'
	
#  export TERM=screen-256color

# CTRL Z


# echo $TERM
#stty raw -echo

# fg
[INTRO]
export TERM=screen

'''
