# Getting Started with Flask

## Background

- **Flask** is a microframework used to build REST APIs in Python. 
- A REST API (also called a RESTful API) is an application programming interface that conforms to the specifications of the REST architectural pattern. It isn't a protocol or a standard, though.  
- There a tons of frameworks and libraries to build REST APIs in all major programming languages

## Python Intro
- Since Flask is a Python Library, knowing a little Python will be helpful.  Check out these resources if you're new to Python:
  - [Python Tutorial in 30 Minutes](https://youtu.be/WEm3EUdicDg)
  - [Hands On Python Tutorial](https://anh.cs.luc.edu/handsonPythonTutorial/)
  - [RealPython's Python Learning Path](https://realpython.com/learning-paths/python3-introduction/)

## Anaconda Python
- [Anaconda Documentation - Installation](https://docs.anaconda.com/anaconda/install/index.html)
  - You can use other Python installations, but Anaconda will be used throughout these examples
- [Anaconda Navigator](https://docs.anaconda.com/navigator/index.html)
  - A GUI included in Anaconda Distribution that allows you to manage your Anaconda install.  You can:
    - launch applications 
    - manage conda packages, environments, and channels
- [Conda Cheat Sheet](https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf)
  - `conda` is the command line interface to your Anaconda install.  
  - You can do the same things with the CLI that you can with Navigator. 

### Anaconda Environments

Anaconda allows you to maintain a collection of siloed Python Environments, each with their own install of specific python version and added libraries.  This is useful if you're working on multiple projects that each might need different versions of Python or some particular library. 

Some commands related to environments:

- `conda create -n webdev python=3.9`
  - create a new environment named `webdev` based on Python version 3.9
- `conda env list`
  - list all Anaconda environments on the current system
- `conda activate webdev`
  - active (switch to) another anaconda environment, in this case, the one named webdev.  If you have an environment named mlenv, you could switch to that one with `conda activate mlenv`. 
- `conda list` 
  - lists all the packages in the active Anaconda environment. 

## Visual Studio Code

We'll use VS Code as our IDE for these examples.  

You'll need to make sure VS Code is using the correct interpreter from the conda environment you've created for these examples.  One way to do this is to press `cmd-shift-p` (on mac) to open the VS Code command palette, search for `python select interpreter`, and choose the correct conda environment. 
