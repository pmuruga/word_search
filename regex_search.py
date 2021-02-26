import numpy as np
import re
import os
from tqdm.auto import tqdm

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

class wordSearch:

    def __init__(self):
        self.words = []
        with open("words2.txt",'r') as f:
            for line in f:
                if len(line.strip()) > 2 or line.strip() in ['a','i','at','an','as','ax','ad','am','in','hi','if','is','it']:
                    self.words.append(line.strip())

        self.words = np.array(self.words)

    def query(self, s, len_fixed = True):
        regex = re.compile(s)
        ret = []
        for i in self.words:
            if len_fixed:
                if regex.fullmatch(i):
                    ret.append(i)
            else:
                if regex.match(i):
                    ret.append(i)
        return ret
    
    def is_reducible(self,length):
        candidates = np.array([i for i in self.words if len(i) == length])
        possible = []
        for i in tqdm(range(len(candidates))):
            possible.append(self.countdown(candidates[i],length))

        ret = []
        for t, word in zip(possible,candidates):
            if t:
                ret.append(word)
        return ret
        
    def countdown(self, word, length):
        if length == 1:
            if word in self.words:
                return True
            return False

        candidates = np.array([word[:i]+word[i+1:] for i in range(len(word)) if word[:i]+word[i+1:] in self.words])
        return any(list(map(self.countdown,candidates,len(candidates)*[length-1])))

ws = wordSearch()
w = ws.is_reducible(8)
print(w)