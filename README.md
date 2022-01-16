# Sasha's Automatic CTF Solver

[Pwntools](https://github.com/Gallopsled/pwntools) is a CTF framework and exploit development library. Written in Python, it is designed for rapid prototyping and development, and intended to make exploit writing as simple as possible.

This program is created using [Pwntools](https://github.com/Gallopsled/pwntools), it is able to automatically handle the first 10 challenges in OverTheWire: Bandit. If you are looking for a comprehensive explanation of my solutions, you can check out my [write-up](https://github.com/ahs4sNs3c/OverTheWire-Bandit-Writeup) for Bandit Level 0-15.

## Demo
[![Demo Video](https://img.youtube.com/vi/TiuDywTCaqM/maxresdefault.jpg)](https://www.youtube.com/embed/TiuDywTCaqM) </br>

Link: https://www.youtube.com/watch?v=TiuDywTCaqM

## Installation
Python3 is suggested, but [Pwntools](https://github.com/Gallopsled/pwntools) still works with Python 2.7. Most of the functionality of [Pwntools](https://github.com/Gallopsled/pwntools) is self-contained and Python-only. You should be able to get running quickly with
```
apt-get update
apt-get install python3 python3-pip python3-dev git libssl-dev libffi-dev build-essential
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade pwntools
```
Then, clone this repository
```
git clone https://github.com/ahs4sNs3c/automatic-bandit-solver
```
Change your working directory to the local repository and run the program
```
python main.py
```
