"""
Program: Project1
Author: Viet Trinh
Last date modifued: 10/14/2018
Prompt:
Write a program that calculate the file with most duplication and most size wasted
Algorithm:
->Devide to smaller categories of files with the same size
->Devide to even smaller categories of files with the same content
->Count max copies and max size can be saved
->Report """

import p1utils
import time
import os

# slow search implementation:
def search(file_list):
    """Looking for duplicate files"""
    doS = {} # dictionary of size [key:value] = {size of file: List of List]}
    for i in range(len(file_list)):
        tSize = os.path.getsize(file_list[i]) 
        if not(tSize in doS): doS[tSize] = [[file_list[i]]] # add the first file_name with particular size
        elif True:
            for item in doS[tSize]: 
               if (p1utils.compare(file_list[i],item[0])): 
                   item.append(file_list[i]) # add to its orginal file's list
                   break            
               else: doS[tSize].append([file_list[i]]) # can't find original file, add as another original file 
    return doS

# faster search implementation:    
def fasterSearch(file_list):
    """Looking for duplicate files"""
    cmpDict = {} # compare Dictionary [key:value] = {size of file: {index : names}}
    for i in range(len(file_list)):
        tmp = os.path.getsize(file_list[i])
        cmpDict.setdefault(tmp,{})[len(cmpDict[tmp])] = [file_list[i]] # put names in the next index of size 
        for k in range(len(cmpDict[tmp])-1):
            if p1utils.compare(file_list[i],cmpDict[tmp][k][0]): # compare every new element with the original file
                cmpDict[tmp][k].append(file_list[i]) # if True, append list
                cmpDict[tmp].pop(len(cmpDict[tmp])-1) # after append, pop()
    return cmpDict

# find max search implementation:
def countSearch(doL):
    """Find file with the most copies, size and list them"""
    maxL = 0 # most_copies
    maxLitem = [] # most_copies_list
    maxS = 0 # most_size
    maxSitem = [] # most_size_list
    for key in doL:
        for item in doL[key]:
            tmp = len(item) # Get list value 
            if tmp>maxL:
                maxL = tmp
                maxLitem = item
            if (tmp-1)*key>maxS:
                maxS = (tmp-1)*key
                maxSitem = item              
    return [maxL,maxLitem,maxS,maxSitem] 

# find max fasterSearch implementation, almost the same with countSearch():
def countFasterSearch(doD):
    """Find file with the most copies, size and list them"""
    maxL = 0 # most_copies
    maxLitem = [] # most_copies_list
    maxS = 0 # most_size
    maxSitem = [] # most_size_list
    for key in doD:
        for item in doD[key]: 
            tmp = len(doD[key][item]) # Get dictionary value 
            if tmp>maxL:
                maxL = tmp
                maxLitem = doD[key][item]
            if (tmp-1)*key>maxS:
                maxS = (tmp-1)*key
                maxSitem = doD[key][item]              
    return [maxL,maxLitem,maxS,maxSitem] 

# report
# t0 = time.time()
# print("Runtime: %.2f secs" % (time.time() - t0))
def report(d):
    """ report seach results"""
    t0 = time.time()
    printReport(countSearch(search(d)))
    print("Runtime: %.2f secs" % (time.time() - t0))
    print(".. and now w/ a faster search implementation:")
    t0 = time.time()
    printReport(countFasterSearch(fasterSearch(d)))
    print("Runtime: %.2f secs" % (time.time() - t0))
    
# print report
def printReport(d):
    """print result"""
    print("The file with the most duplicates is:\n", d[1][0])
    print("Here are its", d[0]-1 ,"copies:")
    print('\n'.join(item for item in d[1][1:]))
    print("\nThe most disk space ("+ str(d[2])+") could be recovered, by deleting copies of this file:")
    print(d[3][0])
    print("Here are its",len(d[3])-1,"copies:")
    print('\n'.join(item for item in d[3][1:]))
    
# report(files)    
#find all files in the provided directory and report
def main():
    #find all files in the provided directory
    files = p1utils.allFiles("." + os.sep + "fullset")
    print("Number of files found: ", len(files))
    #report search(files) & (fasterSearch(files))
    report(files)
    
#program start here
if __name__ == '__main__':
    main()
