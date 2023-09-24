# Unofficial LineageOS Installer GUI
# by arm64 and Yeet1000
#
# View at https://github.com/thepyrite/Unofficial-LineageOS-installer
# All Rights Reserved
# 2023

from tkinter import *
from tkinter import messagebox
import subprocess

root=Tk()

# defined

def debugwin():
    messagebox.showwarning("!! Alert !!", """You need to have USB Debugging ON for these to work.
Go enable it in Developer Options.
                           
(If you don't have developer options, head over to Settings > About, scroll down and tap the Build Number 7 times. Now find the Developer options and enable USB Debugging.)
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

def extrawin():
    messagebox.showwarning("!! Alert !!", "These are extras you can select AFTER finishing the LineageOS installation on your device.")

    extrawin = Toplevel(root)
    extrawin.title("extra options")
    extrawin.geometry("150x175")
    extrawin.resizable(height=False, width=False)

    #elements
    extratext = Label(extrawin, text="extra options")
    advancedmode = Checkbutton(extrawin, text='advanced mode', onvalue=1, offvalue=0)
    verbose = Checkbutton(extrawin, text='verbose mode', onvalue=1, offvalue=0)

    #order
    extratext.pack()
    advancedmode.pack()
    verbose.pack()

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

# elements
title = Label(root, text="unofficial lineageos installer gui")
series = Button(root, text="choose phone series")
model = Button(root, text="choose phone model")
debug = Button(root, text="debug", command=debugwin)
extras = Button(root, text="extra options", command=extrawin)

# order
title.pack()
series.pack()
model.pack()
debug.pack()
extras.pack()

# root window
root.title('unofficial lineage installer gui')
root.geometry("200x250")
root.resizable(height=False, width=False)

root.mainloop()