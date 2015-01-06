#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import time
import sys

if sys.version[0]=="2":
    input = raw_input

def robot():
    while True:
        response = input("Robo: What is my purpose?\nRick: ").lower().split(" ")
        if all(x in response for x in ["pass","butter"]):
            print("*passes butter*")
            input("Rick: ")
            time.sleep(1.5)
            while True:
                response = input("Robo: What is my purpose?\nRick: ").lower().split(" ")
                if all(x in response for x in ["you","pass","butter"]):
                    print("Robo: Oh my god.")
                    input("Rick: ")
                    break
            break

if __name__ == "__main__":
    robot()



