#!/usr/bin/env python
#author: Don Johnson
#email: <dj@codetestcode.io>
# -*- coding: utf-8 -*-
import string

def subStringSearch(key,source):
    charList = []
    indexPosList = []
    for each_element in key:
        charList.append(each_element)

    for eachItem in charList:
        if eachItem in source:
            indexPosList.append(int(source.index(eachItem)))

    return indexPosList


def returnPhrasePos(phrase, source):
     getIndexPos = subStringSearch(phrase,source)
     results = ""
     for indecies in getIndexPos:
          results += source[indecies]
     return results




def main():

    testCharLower = "abcdefghijklmnopqrstuvwxyz "
    testCharUpper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
    testCharDigits = "0123456789 "
    multiLineString = """
                       EEEEEEEEEEEEEEEEE
                        c EEEEEEEEEEEEEE
                        EEEEEEE a EEEEEE
                        EEEEE t EEEEEEEE
                      """



    print(returnPhrasePos("Good Work","I Love Working at Guidance Software."))
    print(returnPhrasePos("keep it simple stupid",testCharLower))
    print(returnPhrasePos("cat",multiLineString))


if __name__ == "__main__":
    main()
