# Unofficial LineageOS Installer GUI
# by arm64 and Yeet1000
#
# View at https://github.com/thepyrite/Unofficial-LineageOS-installer
# All Rights Reserved
# 2023

from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import subprocess

messagebox.showwarning("!! Alert !!", """This program won't work if platform-tools isn't in PATH.

Please visit https://developer.android.com/tools/releases/platform-tools and download the platform-tools. Follow instructions on the GitHub page to learn how to properly set it up.

If it's already set up, you can proceed to the installer.""")

root=Tk()

# defined

def debugwin():
    messagebox.showwarning("!! Alert !!", """You need to have USB Debugging ON for these to work.
Go enable it in Developer Options.
                           
(If you don't have developer options, head over to Settings > About, scroll down and tap the Build Number 7 times. Now find the Developer options and enable USB Debugging.)
""")
    # debug window
    debugwin = Toplevel(root)
    debugwin.title("Android Debug")
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
    reboot = Button(debugwin, text="Regular reboot", command=rebootaction)
    bootloader = Button(debugwin, text="Reboot bootloader", command=bootloaderaction)
    recovery = Button(debugwin, text="Reboot recovery", command=recoveryaction)

    # order
    pathtext.pack()
    reboot.pack()
    bootloader.pack()
    recovery.pack()

def extrawin():
    messagebox.showwarning("!! Alert !!", "These are extras you can select AFTER finishing the LineageOS installation on your device.")

    extrawin = Toplevel(root)
    extrawin.title("Extra")
    extrawin.geometry("150x175")
    extrawin.resizable(height=False, width=False)

    #elements
    extratext = Label(extrawin, text="Extra options")
    advancedmode = Checkbutton(extrawin, text='Advanced mode', onvalue=1, offvalue=0)
    verbose = Checkbutton(extrawin, text='Verbose mode', onvalue=1, offvalue=0)

    #order
    extratext.pack()
    advancedmode.pack()
    verbose.pack()

serieslist = [
    "Google Pixel 7",
    "Google Pixel 6",
    "Google Pixel 5"
]

models = [
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
series = ttk.Combobox(state="readonly", values=serieslist)
series.set("Select device series")

model = ttk.Combobox(state="readonly", values=models)
model.set("Select device model")

status = Label(root, text="Device status: unavailable")

proceed = Button(root, text="Proceed to installation")

title = Label(root, text="Installer")
debug = Button(root, text="Debug", command=debugwin)
extras = Button(root, text="Extra options", command=extrawin)

# order
title.pack()
series.pack()
model.pack()
status.pack()
proceed.pack()
debug.pack()
extras.pack()

# root window
root.title('Installer')
root.geometry("200x250")
root.resizable(height=False, width=False)
icon_data = base64.b64decode(iconb64)
actualicon = PhotoImage(data=icon_data)
root.iconphoto(True, actualicon)
root.mainloop()