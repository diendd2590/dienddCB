**1. Level 0 - > 1**
  **Current password:** bandit0
  **Target password:** 6y2kwnwK6grgvwvpvLaa2T1cpFEKOhNR

  **Command used:**
  -To connect: `ssh bandit0@bandit.labs.overthewire.org -p 2220` 
  -To solve: `cat readme`

    **Key concepts learned:** 
    -cat: used to print the contents of a file to the terminal
---
**2.Level 1 - > 2** 
 **Current password:** 6y2kwnwK6grgvwvpvLaa2T1cpFEKOhNR
 **Target password:** PK8fYLZg2hnHSz83plBL1iEPKdD3QToB

 **Command used:**
 -To connect: `ssh bandit1@bandit.labs.overthewire.org -p 2220`
 -To solve: 2 ways | 1.`cat ./-` | 2. `cat < -`

 **Key concepts learned:** In a Linux terminal (like Ubuntu), a single `-` is usually understood as a command flag/option     indicator (for example, `-la` in `ls -la`). Because of this, a file named strictly `-` is easily misunderstood by the         terminal as an option or as standard input (`stdin`).
 To solve this, we need a method to help the system differentiate between a filename and a command flag:
 1. **Using Relative Paths (`cat ./-`)**: 
   Adding `./` explicitly tells the terminal to look for the file named `-` in the current working directory (`./`).            Furthermore, we can combine this with the `Tab` key to auto-complete the filename.
 2. **Using Input Redirection (`cat < -`)**: 
   The `<` operator redirects the contents of the file named `-` directly into `cat` for reading.
---
**3.Level 2 -> 3**
 **Current password:** PK8fYLZg2hnHSz83plBL1iEPKdD3QToB
 **Target password:** 7ZZ2LFrykP2zEyvBl4m3clcL7tGYJPME

 **Command used:** 
 -To connect: `ssh bandit2@bandit.labs.overthewire.org -p 2220`
 -To solve: 2 ways | 1.`cat ./-- + tab` | 2. `cat < "--spaces in this file--"`

 **Key concepts learned:**
 This level teaches us how to deal with filenames that contain spaces. Here are the two methods I used:
  1. **Using `./` with `Tab` Auto-completion:**
 Type `cat ./--spaces` and press `Tab`. The terminal will automatically add backslashes (`\`) to escape the spaces and auto-  complete the matching filename.
  2. **Using Input Redirection (`<`) with Double Quotes (`""`):**
  Run `cat < "--spaces in this filename--"`. Wrapping the filename inside double quotes forces the terminal to treat the       whole phrase as a single filename instead of separate words.

 ---
 **4.Level 3 -> 4**
 **Current password:** 7ZZ2LFrykP2zEyvBl4m3clcL7tGYJPME
 **Target password:** xzTXq1rDJQVVAzdv5cHq1TQytTWufAMq

 **Command used:** 
 -To connect: `ssh bandit3@bandit.labs.overthewire.org -p 2220`
 -To solve: 2 ways: 
   +) `cd inhere` -> `cat ./...Hid + tab`
   +) `ls -A inhere` -> `cat inhere/...Hid + tab` -> (this way, no need to cd to inhere btw; equal steps)

  **Key concepts learned:**
  This level teaches us how to find hidden files and understand special directory symbols:
  * `.` = Current directory
  * `..` = Parent directory
  Here is the explanation for the two ways to solve this level:
  * **Way 1 (Standard approach):** Use `ls -la` to display all hidden files inside the directory, then use `cat` to read the   `...Hiding-From-You` file.
  * **Way 2 (Faster approach):** Avoid changing directories with `cd`. Instead, use `ls -A inhere` to view hidden files from   the outside, then read it directly using its relative path: `cat inhere/...Hiding-From-You`.

  ---
  **5.Level 4 -> 5**
  **Current password:**xzTXq1rDJQVVAzdv5cHq1TQytTWufAMq
  **Target password:** 6C7h9GD8M6ai5nr7wo1RonrzFjj9yIrG

  **Command used:**
  -To connect: ssh bandit4@bandit.labs.ovethewire.org -p 2220
  -To solve: `file inhere/*` -> `cat inhere/-file07`

  **Key concepts learned:**
   This level teaches us how to identify file formats using the file command.
   When we encounter a lot of files in a directory, checking or reading them one by one using cat is really inefficient.        Instead, we can combine the file command with a wildcard * to check all file types at once, like file inhere/*.
   Here, * means all files inside the inhere directory. Once we run this, we can easily spot the only ASCII text file           containing the password.
   
 ---
 **6.Level 5 -> 6**
  **Current password:** 6C7h9GD8M6ai5nr7wo1RonrzFjj9yIrG
  **Target password:** pXa26xhMWaC2SvDotA4r9EgZkulOeSB

  **Command used:**
  -To connect: ssh bandit5@bandit.labs.ovethewire.org -p 2220
  -To solve: `cd inhere` -> `cat ./maybehere07/.file2`

  **Key concepts learned:**
  This level teaches us how to use the find command with specific criteria, especially file size. Here is the command we       need: `find inhere -size 1033c` .
  We can also append 2>/dev/null at the end to suppress all 'Permission denied' error messages, keeping our output clean.
