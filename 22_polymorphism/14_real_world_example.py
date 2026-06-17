class File:
    
    def open(self):
        print("Folder open")

class Pdf(File):

    def open(self):
        print("pdf open")

class Image(File):

    def open(self):
        print("Image open")

class Video(File):

    def open(self):
        print("Video open")

class textfile(File):

    pass

files = [Pdf(), Image(), Video(), textfile()]

for file in files:
    file.open()