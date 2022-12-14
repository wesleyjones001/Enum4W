#!/usr/bin/python3

from __future__ import print_function
import sys
import os
import subprocess
import math


# Included modules

# BEGIN TERMCOLOR IMPORT
# coding: utf-8
# Copyright (c) 2008-2011 Volvox Development Team
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
# Author: Konstantin Lepa <konstantin.lepa@gmail.com>

"""ANSII Color formatting for output in terminal."""



__ALL__ = [ 'colored', 'cprint' ]

VERSION = (1, 1, 0)

ATTRIBUTES = dict(
        list(zip([
            'bold',
            'dark',
            '',
            'underline',
            'blink',
            '',
            'reverse',
            'concealed'
            ],
            list(range(1, 9))
            ))
        )
del ATTRIBUTES['']


HIGHLIGHTS = dict(
        list(zip([
            'on_grey',
            'on_red',
            'on_green',
            'on_yellow',
            'on_blue',
            'on_magenta',
            'on_cyan',
            'on_white'
            ],
            list(range(40, 48))
            ))
        )


COLORS = dict(
        list(zip([
            'grey',
            'red',
            'green',
            'yellow',
            'blue',
            'magenta',
            'cyan',
            'white',
            ],
            list(range(30, 38))
            ))
        )


RESET = '\033[0m'


def colored(text, color=None, on_color=None, attrs=None):
    """Colorize text.

    Available text colors:
        red, green, yellow, blue, magenta, cyan, white.

    Available text highlights:
        on_red, on_green, on_yellow, on_blue, on_magenta, on_cyan, on_white.

    Available attributes:
        bold, dark, underline, blink, reverse, concealed.

    Example:
        colored('Hello, World!', 'red', 'on_grey', ['blue', 'blink'])
        colored('Hello, World!', 'green')
    """
    if os.getenv('ANSI_COLORS_DISABLED') is None:
        fmt_str = '\033[%dm%s'
        if color is not None:
            text = fmt_str % (COLORS[color], text)

        if on_color is not None:
            text = fmt_str % (HIGHLIGHTS[on_color], text)

        if attrs is not None:
            for attr in attrs:
                text = fmt_str % (ATTRIBUTES[attr], text)

        text += RESET
    return text


def cprint(text, color=None, on_color=None, attrs=None, **kwargs):
    """Print colorize text.

    It accepts arguments of print function.
    """

    print((colored(text, color, on_color, attrs)), **kwargs)
# END TERMCOLOR IMPORT


globals = {}


def print_banner():
    print("+=============================================+")
    print("|          " +
          colored("[ ENUM FOR WESLEY SCRIPT ]", "green") + "         |")
    print("|          " +
          colored("[ By Hacker For Hackers! ]", "yellow") + "         |")
    print(
        "| " + colored("[ LEGAL: NO WARENTY; USE AT YOUR OWN RISK ]", "red") + " |")
    print(
        "| " + colored("[ Star this repo on wesleyjones001/Enum4w ]", "green") + " |")
    print("+=============================================+")


def execute_cmd(input: str):
    output_stream = os.popen(input)
    return output_stream.read()


def get_users():
    raw = execute_cmd('cut -d ":" -f 1 /etc/passwd')
    users = raw.splitlines()
    return users


def display_users(level: int):
    users = get_users()
    default_users = ["daemon",
                     "shutdown",
                     "operator",
                     "halt",
                     "bin",
                     "sys",
                     "sync",
                     "games",
                     "man",
                     "lp",
                     "mail",
                     "news",
                     "uucp",
                     "proxy",
                     "backup",
                     "list",
                     "irc",
                     "gnats",
                     "nobody",
                     "_apt",
                     "systemd-network",
                     "systemd-resolve",
                     "systemd-timesync",
                     "messagebus",
                     "tss",
                     "strongswan",
                     "tcpdump",
                     "usbmux",
                     "sshd",
                     "dnsmasq",
                     "avahi",
                     "rtkit",
                     "speech-dispatcher",
                     "nm-openvpn",
                     "nm-openconnect",
                     "lightdm",
                     "pulse",
                     "saned",
                     "colord",
                     "stunnel4",
                     "geoclue",
                     "redsocks",
                     "rwhod",
                     "iodine",
                     "miredo",
                     "statd",
                     "inetsim",
                     "king-phisher",
                     "vboxadd",
                     "ntpsec",
                     "Debian-snmp",
                     "sslh",
                     "_rpc",
                     "systemd-oom",
                     "polkitd",
                     "systemd-coredump"
                     ]
    print(colored("Users in /etc/passwd: ", "yellow"))
    primary = []
    secondary = []
    for user in users:
        if user in default_users and level == 2:
            secondary.append(colored(user, "blue"))
        elif user not in default_users:
            primary.append(colored(user, "green"))
    l1 = primary + secondary
    if len(l1) > 9:
        for a, b, c in zip(l1[::3], l1[1::3], l1[2::3]):
            print('{:<30}{:<30}{:<}'.format(a, b, c))
    else:
        print('\n'.join(l1))
    print()
    return


def get_top_processes_by_mem():
    tmp = execute_cmd("ps aux | sort -nrk 3,3 | head -n 10")
    lines = tmp.splitlines()
    return lines


def get_top_processes_by_cpu():
    tmp = execute_cmd("ps aux | sort -nrk 4,4 | head -n 10")
    lines = tmp.splitlines()
    return lines


def print_top_processes_by_mem():
    print()
    print(colored("Top 10 processes by MEM usage: ", "yellow"))
    print(execute_cmd("ps aux | head -n 1").strip())
    ps = get_top_processes_by_mem()
    ps2 = []
    for i in ps:
        ps2.append(i[:120] + " ...")
    print(colored('\n'.join(ps2), "green"))


def print_top_processes_by_cpu():
    print()
    print(colored("Top 10 processes by CPU usage: ", "yellow"))
    print(execute_cmd("ps aux | head -n 1").strip())
    ps = get_top_processes_by_cpu()
    ps2 = []
    for i in ps:
        ps2.append(i[:120] + " ...")
    print(colored('\n'.join(ps2), "green"))


def get_files_in_root():
    files = os.listdir("/")
    return files


def print_files_in_root():
    files = get_files_in_root()
    default_files = ["run",
                     "mnt",
                     "root",
                     "sbin",
                     "lib64",
                     "sys",
                     "lib",
                     "lost+found",
                     "home",
                     "proc",
                     "tmp",
                     "media",
                     "bin",
                     "boot",
                     "srv",
                     "lib32",
                     "usr",
                     "opt",
                     "var",
                     "libx32",
                     "etc",
                     "initrd.img",
                     "vmlinuz",
                     "dev",
                     "initrd.img.old",
                     "vmlinuz.old",
                     "afs"
                     ]
    interesting_files = [".dockerenv"]
    t1 = []
    t2 = []
    for file in files:
        if file.lower() in interesting_files:
            t1.append(file)
        elif file.lower() not in default_files:
            t2.append(file)
    result = colored('\t\t'.join(t1), "red") + colored('\t\t'.join(t2), "green")
    print()
    print(colored("Uncommon files in root: ", "yellow"))
    print(result)
    return


def analyze_root_files():
    global globals
    files = get_files_in_root()
    if ".dockerenv" in files:
        globals["IsDockerEnv"] = True
    # TODO: Add more checks later
    return


def print_root_files_analysis():
    analyze_root_files()
    global globals
    print()
    print(colored("Root file analysis", "yellow"))
    if "IsDockerEnv" in globals.keys():
        if globals["IsDockerEnv"] == True:
            print(colored("Likely a container (Docker)", "green"))
    else:
        print("None")
    return


def get_user_home_dirs():
    dirs = os.listdir("/home")
    t1 = []
    for dir in dirs:
        t1.append("/home/" + dir)

    if os.access("/root", os.R_OK):
        t1.append("/root")
    return t1


def analyze_user_home_dirs():
    global globals
    dirs = get_user_home_dirs()
    important_files = [".ssh"]
    boring_if_empty = ["Desktop", "Documents", "Downloads",
                       "Videos", "Music", "Pictures", "Public", "Templates"]
    users_files = [[]]
    globals["CheckSSHKeysInHomeDirectories"] = []
    print()
    print(colored("Analyzing user home directories", "yellow"))
    null_print = True
    for dir in dirs:
        tmp = []
        if os.access(dir, os.R_OK):
            for file in os.listdir(dir):
                filepath = f"{dir}/{file}"
                if file in boring_if_empty:
                    if len(os.listdir(filepath)) == 0:
                        continue
                elif file in important_files:

                    if file == ".ssh":
                        print(colored("Found .ssh directory in " + dir, "green"))
                        globals["CheckSSHKeysInHomeDirectories"].append(
                            filepath)
                        null_print = False
                else:
                    tmp.append(filepath)
        users_files.append(tmp)
    if null_print:
        print("None.")


def check_if_ssh_key(filename: str):
    try:
        with open(filename, "r") as file:
            contents = file.read()
            if "-----BEGIN OPENSSH PRIVATE KEY-----" in contents and "-----END OPENSSH PRIVATE KEY-----" in contents:
                return True
    except:
        print("Cant read file.")
    return False


def cache_files():
    global globals
    print()
    string = colored(
        "Caching all readable files in system.\nBe patient this could take awhile..." + "", "white")
    print(string)
    globals["SystemFiles"] = execute_cmd(
        "find / -readable  2> /dev/null").splitlines()
    print(colored("Done. Won't have to do that again!", "green"))
    return


def check_ssh_keys():
    global globals
    dirs_to_check = []
    print()
    print(colored("Finding SSH keys", "yellow"))
    found_key = False
    if "CheckSSHKeysInHomeDirectories" in globals.keys():
        dirs_to_check += globals["CheckSSHKeysInHomeDirectories"]
    for dir in dirs_to_check:
        for file in os.listdir(dir):
            if check_if_ssh_key(f"{dir}/{file}"):
                print(
                    colored(f"Found SSH Private Key in {dir}/{file} Readable!!", "green"))
                found_key = True
    if not found_key:
        print("No keys found")


def run():
    print_banner()
    print()
    args = sys.argv
    enum_level = 1
    if "-c" in args:
        if (args.index("-c")+1) >= len(args):
            print("Specify enum level [ 1-4 ]")
            return
        enum_level = int(args[args.index("-c")+1])

    if enum_level >= 1:
        display_users(enum_level)
    print_top_processes_by_cpu()
    print_top_processes_by_mem()
    print_files_in_root()
    print_root_files_analysis()
    analyze_user_home_dirs()
    cache_files()
    check_ssh_keys()
    pass


if __name__ == "__main__":
    run()
    exit()
