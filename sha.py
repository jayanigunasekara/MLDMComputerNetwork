import logging
import os
import hashlib
import socket


class Sha(object):
    
    def __init__(self, filename, folder, output_file="Library.txt"):
        
        self.log = logging.getLogger(__name__)
        self.log.info("Initializing sha module.")
        if not os.path.exists(folder):
            raise NotADirectoryError("The given output path '{0}' is not a valid directory".format(folder))
        if not os.path.exists(folder + "/" + output_file):
            f = open(folder + "/" + output_file, "x")
        f = open(folder + "/" + output_file, "r+")
        f.truncate(0)
        self.folder = folder
        self.output_file = folder + "/" + output_file
        self.log.info("Given output directory: '{0}'".format(self.folder))
        fl = open(self.output_file, "w")
        fl.write("IP Address - " + socket.gethostbyname((socket.gethostname())) + "\n")
        fl.write("File Name - " + os.path.split(filename)[1] + "\n")
        fl.write("File Size - " + str(os.path.getsize(filename)) + "\n")
        fl.write("Book Size - 2048" + "\n")
        bookcount = 0
        for file in os.listdir(os.fsencode(os.path.dirname(os.path.realpath(__file__)) + "/" + self.folder)):
            bookcount = bookcount + 1
        fl.write("Number of books -" + str(bookcount) + "\n")

    def calc_sha(self):

        dir_path = os.path.dirname(os.path.realpath(__file__)) + "/" + self.folder
        directory = os.fsencode(dir_path)
        for file in os.listdir(directory):
            filename = os.fsdecode(file)
            print(filename)
            chunk_path = dir_path + "/" + filename
            with open(chunk_path,"rb") as f:
                bytes = f.read() # read entire file as bytes
                readable_hash = hashlib.sha1(bytes).hexdigest();
                print(readable_hash)
                f = open(self.output_file, "a")
                f.write(filename + " - " + readable_hash + "\n")
