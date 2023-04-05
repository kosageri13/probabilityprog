# -*- coding: utf-8 -*-
"""
E programot magam kódoltam, nem másoltam vagy írtam át más kódját, 
és nem adtam át másnak.
Kósa Gergely
"""
# B. task. Zipf's law.

# "The Zipf's law states that in certain parts of a natural language, the frequency of occurrence of a word is inversely proportional to its rank in the frequency (occurrence) table. Thus, the most common word is almost twice as common as the second most common word, and three times as common as the third-ranked word, etc." (cf. Wikipedia)

# If this rule holds for a text, the frequency function graph is a line plotted in a coordinate system where both axes are logarithmically scaled.

# The task is to write a function that graphically verifies this rule for the text file given as a command-line argument by drawing the frequencies in a log-log coordinate system. The Python built-in split and strip functions are useful for word segmentation and punctuation removal.

# The program should be executable with the test.txt text file (which is in the same folder as the program file) as follows:

import re
import matplotlib.pyplot as plt
import sys
filename=sys.argv[1]
def zipf(filename):
    frequency = {}
     
    with open(filename, 'r') as content:
        text_string = content.read()
        
        words = re.findall(r'\b[A-Za-z][a-z]{0,1000}\b', text_string)
        a=len(words)    
        for word in words:
            
            count = frequency.get(word,0)
            frequency[word] = count + 1
     
        most_frequent = dict(sorted(frequency.items(), key=lambda elem: elem[1], reverse=True))
     
        top_count = 0
        D=[]   
        C=[]
        for idx, (words, frequency) in enumerate(most_frequent.items()):
          
            if idx == 0:
                top_count = frequency
            D.append((frequency/top_count))
            C.append(top_count/frequency)
            print(words,frequency,round(frequency/top_count, 2))
        print(D)
        E=[]
        for i in D:
            result=int(max(C))*i
            E.append(result)
        print(max(C),E)
        plt.loglog(E)
        plt.show()

def main():
    zipf(filename)
    
if __name__=="__main__":
    main()
    
            