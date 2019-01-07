#!/usr/bin/env python3

class File(object):
    a=1
    def __init__(self,user):
        self.user=user
    def tag(self,file_name):
        self.file_name=file_name
        print('%s' % self.file_name)
        a=self.name
        print(a)
file=File('liyang')
if __name__=='__main__':
    file.tag(2)

