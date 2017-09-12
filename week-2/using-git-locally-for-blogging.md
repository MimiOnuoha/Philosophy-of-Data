# Using Git locally

## Overview
We've been using Git entirely through Github, but in reality, the best way to use it is through the command line. Let's have a quick reminder of definitions:

- **Terminal**: Also known as the command line, or shell, or console. It's an interface in which you can type and execute text based commands. It's just like Finder, but is another (often faster and more direct) way of interacting with the computer. 
- **Git**: an open-source version control system that tracks changes to a file. A tool used with the command line, useful for maintaining and referring to multiple versions of a file.
- **Github:** web hosting service for code. A place where programmers can share/store their projects and code, and interact with the code and projects of other people. 
- **Github Pages:** Public webpages hosted for free through GitHub. GitHub users can create and host both personal websites (one allowed per user) and websites related to specific GitHub projects.
- **Markdown:** a lightweight text format that exports easily to HTML (as well as other formats) and allows us to write using any plain text editor. This document is written in Markdown. 
- **Text Editor:** A program that allows us to create and edit programming language files in plain text. This is the place where we'll be writing most of our code. We'll be using Sublime Text, though you're free to use your own if you already have a favorite. 



## Setting up our computers 

We'll be using the console, or the terminal, a lot this semester, so you'll have many chances to get familiar with it. Don't worry if some of the things that we do in this guide are confusing to you, it'll all make sense in time. 

1. **Install homebrew** </br> [Homebrew](https://brew.sh/) is a package manager for your OSX (the operating system that Macs run), it will help us manage programs on the computer. </br></br> To install, copy and paste this into your terminal window: `/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"` </br></br>*Note:* if you get an error saying that you don't have permission to install this, you may have to sudo the command. That means typing in the word `sudo` before the command, and pressing return. You'll then be prompted to enter your password; type it in and press return, and be aware that as a security measure nothing may show up in the screen even though you're typing. 

2. **Use homebrew to install Ruby** </br> Type `brew install ruby` in your terminal. 

3. **Download RubyGems** </br>Go [here](https://rubygems.org/pages/download/) and download the zip of RubyGems. 

4. **Download Sublime Text** </br> Available [here](https://www.sublimetext.com).

5. **Download Macdown**  </br>
Available [here](https://macdown.uranusjr.com/)


## Using Git locally	
Right now, when you want to update your blog you've done so by navigating to github.com, finding the right folder, and editing it online. But you would much more control and flexibility if you could edit it from a program on your computer, and then just push the changes that you've made online. We're going to learn how to do that!

First, let's execute some one-time commands that will allow us to easily interface with github from the command line.

NOTE: don't do these if you're on a public computer! Also, note that these values will be stored with Git, so make sure that you're okay with the email address being public.

$ git config --global user.name "YOUR_FULL_NAME" $ git config --global user.email "YOUR_EMAIL_ADDRESS"

See below for an example: 
$ git config --global user.name "John Doe" $ git config --global user.email johndoe@example.com

## Getting our blogs set up locally

Some of these things are a little tedious, but we just have to get this set up once, and then we'll be fine for awhile. 

1. Go into your Github repo for your blog. Go to the _config file and delete the line that says `highlighter: pygments`
2. In the terminal, install bundler: `gem install bundler`
3. Install github pages: `gem install github-pages`


Phew, got that out of the way. Now we want to get our repo down on our computers. To do that, we do a thing called **cloning**. 

 - Go to Github, navigate to your blog repo, and click the button that says `Clone/Download`
 - Copy the link that it gives you. 
 - Navigate to Terminal and write `git clone` followed by the link. So it should look something like `https://github.com/YOURGITHUBUSERNAME/YOURGITHUBUSERNAME.GITHUB.IO.git`


Now if you use the handy terminal commands that you learned today, like `ls`, you'll see that you have a copy of the repo on your computer! 

## Pushing to Github
Anything you do to that repo is only going to be done locally, i.e. on your computer. But the point is that you'll want to be editing your blog and pushing things online, right? So we have to learn how to push up to the Github site. 

So a reminder: git is what allows us to constantly be saving and tracking our changes. But github is where the code that we write actually becomes public. 

Here's how git works. You make changes to a file. You tell git you want those files you've changed to be staged to be saved, or *added*. Then, you actually save those changes by *commiting* them. 

Then, to get everything online, you have to *push* them. When you're working, it looks like this:

1. `git add . ` Here you're adding all the files.
2. `git status` Not a necessary step, but this will show you the files you've added. 
2. `git commit -m "insert a message saying what you did" ` This is where you actually commit those files, or save the changes. 
3. `git push origin master` Now you're pushing things online.

That last line is important. Without it, nothing you ever do will be reflected online. When you're working with Git locally, you always have to remember the difference between what you're doing locally, on your own computer, versus what will be reflected online. 

Git is one of those things that doesn't make sense at first, but if you keep doing it, eventually it will. So keep at it! By the end of the semester, you'll be a pro. 

## Resources
- For more on git, github, and github pages, see [here](http://jmcglone.com/guides/github-pages/)
- [An introduction to git](https://sklise.com/2012/09/22/introduction-to-git/) (it's old, but very clear)