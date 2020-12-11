import os
import shutil

tf = "demofile.txt"


class Task:

    @staticmethod
    def appnd(file, c):
        f = open(file, "a")
        f.write(c)
        f.close()

    @staticmethod
    def rdrsrc(file):
        f = open(file, "r")
        rdd=f.read()
        f.close()
        return rdd

    @staticmethod
    def rd(file):
        if os.path.exists(file):
            return Task.rdrsrc(file)
        else:
            print("The file does not exist")

    @staticmethod
    def rm(f):
        if os.path.exists(f):
            os.remove(f)
        else:
            print("The file does not exist")

    @staticmethod
    def mk(name):
        if os.path.exists(name):
            print("The file exist")
        else:
            open(name, "x").close()

    @staticmethod
    def cp(f1, fp2):
        shutil.copyfile(f1, fp2)

    @staticmethod
    def cl(f):
        Task.rm(f)
        Task.mk(f)

    @staticmethod
    def cmd2():
        a = input("enter cmd").upper()
        b = input("enter some file path(or unrecognized)or text(if cmd is ap)")
        c = input("enter some file path")
        if a == "CL":
            Task.cl(c)
        if a == "RM":
            Task.rm(c)
        if a == "CP":
            Task.cp(c,b)
        if a == "CR":
            Task.mk(b)
        if a == "RD":
            print(Task.rd(c))
        if a == "AP":
            Task.appnd(c,b)
