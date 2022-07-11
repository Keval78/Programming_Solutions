from __future__ import division, print_function

import os,sys
from io import BytesIO, IOBase


def ii():  return int(input())
def si():  return input()
def mi(ss=" "):  return map(int,input().strip().split(ss))
def msi(ss=" "): return map(str,input().strip().split(ss))
def li(ss=" "):  return list(mi(ss))



def read():
    sys.stdin  = open('./input.txt', 'r')  
    sys.stdout = open('./output.txt', 'w') 

def main():

    for _ in range(ii()):
        N = ii()
        # * read array of integer
        arr = li()
        K = ii()
        
        
        if N%2!=0:
            print("-1")
        else:
            freq = {}
            even_parity = 0
            odd_parity = 0
            for i in range(N):
                if arr[i] in freq:
                    freq[arr[i]]+=1
                else:
                    freq[arr[i]]=1
                
                if arr[i]%2==0:
                    even_parity+=1
                else:
                    odd_parity+=1
            
            last_key = 0
            change_even = 0
            change_odd = 0
            change_parity = 0
            for key in sorted(freq):
                # print(key, freq[key])
                if key <= K or (key>K and last_key<=K):
                    eles = key-last_key-1    
                    if eles%2==0:
                        change_even += eles//2
                        change_odd += eles//2
                    else:
                        if last_key%2==0:
                            change_odd += (eles//2) + 1
                        else:
                            change_even += (eles//2) + 1
                    last_key = key
                
                change_parity += freq[key] - 1
            
            if last_key < K:
                eles = K-last_key
                if eles%2==0:
                    change_even += eles//2
                    change_odd += eles//2
                else:
                    if last_key%2==0:
                        change_odd += (eles//2) + 1
                    else:
                        change_even += (eles//2) + 1
            
            if K > N:
                print(change_parity)
            else:
                if change_even+change_odd < change_parity:
                    print("-12")
                else:
                    if even_parity != odd_parity:
                        if even_parity > odd_parity:
                            change_parity -= even_parity-odd_parity
                            change_odd -= even_parity-odd_parity
                        else:
                            change_parity -= odd_parity-even_parity
                            change_even -= odd_parity-even_parity
                    
                    if change_parity>0:
                        if change_parity%2==0:
                            if change_parity//2 >= change_odd and change_parity//2 >= change_even:
                                print(change_parity)
                            else:
                                print("-1")
                        else:
                            
                            print("-14")
                    else:
                        if change_odd>=0 and change_even>=0:
                            print(change_parity)
                        else:
                            print("-15")
            
            
        























    


















# region fastio
# template taken from https://github.com/cheran-senthil/PyRival/blob/master/templates/template.py

BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


def print(*args, **kwargs):
    """Prints the values to a stream, or to sys.stdout by default."""
    sep, file = kwargs.pop("sep", " "), kwargs.pop("file", sys.stdout)
    at_start = True
    for x in args:
        if not at_start:
            file.write(sep)
        file.write(str(x))
        at_start = False
    file.write(kwargs.pop("end", "\n"))
    if kwargs.pop("flush", False):
        file.flush()



sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")

# endregion

if __name__ == "__main__":
    read()
    main()
    #dmain()
