from tkinter import *
from tkinter import messagebox
import subprocess

root=Tk()

# defined

def debugwin():
    messagebox.showwarning("!! Alert !!", """You need to have USB Debugging ON for it to work.
Go enable it in Developer Options.
                           
(If you dont have developer options, head over to Settings > About, scroll down and tap the Build Number 7 times. Now find the Developer options and enable USB Debugging.)
""")
    # debug window
    debugwin = Toplevel(root)
    debugwin.title("debug android")
    debugwin.geometry("300x175")
    debugwin.resizable(height=False, width=False)

    # defined

    def rebootaction():
        command = "adb reboot"
        subprocess.Popen(command, shell=True)

    def bootloaderaction():
        command = "adb reboot bootloader"
        subprocess.Popen(command, shell=True)

    def recoveryaction():
        command = "adb reboot recovery"
        subprocess.Popen(command, shell=True)
    # elements
    pathtext = Label(debugwin, text="Add platform-tools to PATH before or it won't work.")
    reboot = Button(debugwin, text="regular reboot", command=rebootaction)
    bootloader = Button(debugwin, text="reboot bootloader", command=bootloaderaction)
    recovery = Button(debugwin, text="reboot recovery", command=recoveryaction)

    # order
    pathtext.pack()
    reboot.pack()
    bootloader.pack()
    recovery.pack()

series = [
    "Google Pixel 7",
    "Google Pixel 6",
    "Google Pixel 5"
]

model = [
    "7 (panther)",
    "7 Pro (cheetah)",
    "7a (lynx)",
    "6 (oriole)",
    "6 Pro (raven)",
    "6a (bluejay)",
    "5 (redfin)",
    "5a (barbet)"
]

serselected = StringVar(root)
serselected.set(series[0])

modselected = StringVar(root)
modselected.set(model[0])

# elements
title = Label(root, text="unofficial lineageos installer gui")
series = Button(root, text="choose phone series")
model = Button(root, text="choose phone model")
debug = Button(root, text="debug", command=debugwin)

# order
title.pack()
series.pack()
model.pack()
debug.pack()

# root window
root.title('installerTitle')
root.geometry("200x250")
root.resizable(height=False, width=False)

root.mainloop()