# cakeRr
Cake Robot Relations - input your CakeHR workdays faster

Script to make working with cakeHR faster.
1. Set your custom hours in the script.
1. `python3 cakeRr.py`
1. Place your cursor on the start hour of a day (do not click).
1. <kbd>w</kbd> to enter weekday, <kbd>f</kbd> friday, <kbd>e</kbd> to pass to the next day, <kbd>ESC</kbd> to quit.

You will need python3 and:
```bash
pip3 install pyautogui pynput
```
On Windows replace `pip3` with `pip`.

Enjoy!

_Why pyautogui when pyinput has everything I need? I just made a first version of the script with it, and it has very interesting image analysis functions for the future. It has no mouse & keyboard listener though so pyinput is required._
