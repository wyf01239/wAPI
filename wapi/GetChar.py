from encodings import utf_8
utf_8
import os
# TODO: 删除不需要功能
if os.name == 'nt':
    import msvcrt
    def getch():
        try:
            return msvcrt.getch().decode()
        except:
            return None
else:
    import sys, tty, termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    def getch():
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

def wMain():
    wgch = getch()
    try:
        wgch2 = str(wgch)
    except ValueError:
        wgch2 = None
    return wgch2

def wOriginal():
    wgch = getch()
    try:
        wgch2 = wgch
    except ValueError:
        wgch2 = None
    return wgch2

def wO():
    return wOriginal()