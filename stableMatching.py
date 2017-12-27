#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# An imlementation of the Gale-Shapley Algorithm 

if __name__ == "__main__":
    n = 4  # 4 men and 4 women are to get married into a stable matching
    # Therefore we have men numbered from 0 to (n-1), and women from 0 to (n-1)
    # Input list of lists, with each inner list being the preference of (wo)man i:       
    menPref = [ [0, 1, 2, 3], [0, 2, 3, 1], [0, 3, 2, 1], [3, 1, 2, 0] ]
    womenPref = [ [3, 1, 2, 0], [1, 2, 3, 0], [0, 3, 2, 1], [0, 1, 2, 3] ]
    # Create dictionaries to hold preferences and marriage assignments
    mPrefs = {}  # preferences for men to be filled in a dictionary
    wPrefs = {}  # preferences for women to be filled in a dictionary
    mSpouses = {}  # currently assigned spouses by the algorithm
    wSpouses = {}
    for i in range(n):  # for each man and woman numbered i, starting from 0 to (n-1)
        mPrefs[i] = [0, tuple(menPref[i])]  # a list whose first entry is 
          # the index of the highest untried preference and the second entry is
          # man i's preferences as a tuple (immutable list)
        mSpouses[i] = None  # no spouse initially
        wPrefs[i] = tuple(womenPref[i])  # woman i's preferences as a tuple
        wSpouses[i] = None  # no spouse initially
        
    m = 0  # start with the first man
    mUnmarried = list(range(n))  # initially every man is unmarried
    while len(mUnmarried) > 0:
        print("Unmarried men:", mUnmarried)
        print("Unmarried women:", [w for w in wSpouses.keys() if wSpouses[w] is None])
        wCand = mPrefs[m][1][mPrefs[m][0]]  #  next preferred woman candidate for the man
        wCandPref = wPrefs[wCand]  #  preferences of the candidate
        curHus = wSpouses[wCand]  #  the candidate's currently assigned husbnd, if any
        if curHus is not None:  # if a husband assignment exists
            if wCandPref.index(curHus) > wCandPref.index(m):
                  # if the current man is more preferred by the candidate
                wSpouses[wCand] = m  # assign the pair to each other
                mSpouses[m] = wCand
                print("Woman",wCand,"was previously assigned to Man",curHus)
                print("Man",m,"gets assigned to Woman",wCand,"with her pref-level:",wCandPref.index(m))
                mUnmarried.remove(m)  # the current man is no longer unmarried
                mUnmarried.append(curHus)  # previous assigned man is now unmarried
                print("Man",curHus, "is now free")
                #m = (m+1) % n  #  get the next unmarried man
            else:  # the the candidate likes her previous assignment better, do not touch her
                mPrefs[m][0] += 1 # current man's next preference will be considered later on
                print("Man",m,"is rejected by Woman",wCand,", he will consider Woman",mPrefs[m][0] ,"next")
        else:
            print("Man",m,"gets assigned to Woman",wCand,"with her pref-level:",wCandPref.index(m))
            wSpouses[wCand] = m  # assign the pair to each other
            mSpouses[m] = wCand
            mUnmarried.remove(m)  # the current man is no longer unmarried
            
        U = len(mUnmarried)
        if U : m = mUnmarried[(m+1) % U]  #  get the next unmarried man
        print()
    
    for m in mSpouses:    
        print("Man #", m, "gets married to Woman #", mSpouses[m])