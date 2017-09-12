# An introduction to the command line and working with Github Pages

## Overview
The command line is a powerful way for us to interface with our computers, and we'll be making use of it quite a bit in class this semester. 

Allison Parrish has one of the best and most concise overviews to the command line that I've seen. By this point, you should have read her [guide](http://rwet.decontextualize.com/book/unix/). If you haven't please look at it, and refer to it often. 

## Useful Commands
A useful note: If you type "man" before any command, as in `man pwd`, you'll get the manual entry that tells you all about the command and how it's used. If you type "info" before any command, you'll get information about it. Just type `q` when you want to quit the manual or info screen. 

Note also that "folder" and "directory" signify the same thing. "Recursive" in Unix terms refers to all folders that are in a folder.

| Command        | Description          | 
| ------------- |:-------------|
| ls     | lists all the files in a directory   | 
| ls -a| list all files including hidden ones     | 
| pwd      | shows the folder you're currently in     |   
| cd [folder]| change directory (to a folder in your working one), e.g. `cd Documents`      | 
| cd | change to home directory     |    
| cd../ | navigate up to a previous directory       | 
| sudo [command]	| Run command with admin privileges      | 
| mkdir [directory] | make a new directory      |
| rmdir [directory] | remove an empty directory |
| rm -R [directory] | remove a directory and its contents|
| touch [file] | create a new file     |
| rm [file]| remove a file    | 
| clear| clears the screen  |
| history| history of typed commands |
| CTRL + c| end whatever process you are running |
| python -m SimpleHTTPServer 5000 | Start up a Python local server (then navigate to the URL `localhost:5000`)  |
| pbcopy < [file]| copy contents of file onto clipboard |
| mdfind [term]	| Spotlight search for files e.g. `mdfind syllabus` |
| cat [file]|  concatenate contents of file to terminal window |
| grep [term] [file]| Search for all lines that contain the term, e.g. `grep "syllabus" file.txt` |
| grep -r [term] [file]| Recursively search for all lines that contain the term, e.g. `grep "syllabus" file.txt` |
| grep -v [term] [file]| Search for all lines that do not contain the term |
| [command] > [file] | write output to new file (this will overwrite anything that was previously there |
|[command] >> [file] | append output to new file (no overwriting) |
|[command] < [file]	| Tell command to read content from a file

See this [Terminal Cheat Sheet](https://github.com/0nn0/terminal-mac-cheatsheet) for more. 


## Github Pages
The best way to work with Git and with Github Pages is through the command line. We'll be using Git in bits and pieces this semester, but there are some commands that will be espeecially useful for your blog if you want to be able to develop locally (aka work on things on your own computer before making them public online). 

### Getting set up to develop locally
1. First, you've got to install Jekyll. If you've already installed Ruby Gems (which we did last week), then you can do this by just typing this in terminal: `gem install github-pages`. If it doesn't work, you may have to try `sudo gem install -n /usr/local/bin github-pages`

2. Clone down your fork by typing this in terminal: `git clone https://github.com/yourusername/yourusername.github.io.git`

3. Serve the site locally with this command: `jekyll serve`. You can view your site by navigating to here in the browser: http://127.0.0.1:4000/


### New posts, committing changes, and the Git workflow

So you've written a new blog on your computer, and you'd now like it to go live. You need to push it to Github, and the way you do it is the same way you would push any change to github: 

1. Make sure you're in the right directory. 
2. **Get the status of what changes you've made**: `git status`. 
3. **Add the changes you've made**: `git add .`
4. **Commit the changes you've just added**: `git commit -m [insert a message here detailing what you just did]`
5. **Push to the website** `git commit origin master`

With that last line of code, you've ensured that the things that you've been doing just on your computer are now on the cloud, viewable online. 

