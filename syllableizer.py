#!/usr/bin/python
import inflect
import sys
import os



class Syllableizer:
    '''
    Class which takes in a string and then will return a list of the string tokenized into its phonic syllables
    '''
    
    def __init__(self, dictPath):
        self.p = inflect.engine()
        self.d = {}
        self.words_list = []

        with open(dictPath) as f:
            for line in f:
                (key, val) = line.split("\t", 1)
                val = val.replace("\n", "")
                self.d[key.lower()] = val

    def isfloat(self, value):
        try:
            float(value)
            return True
        except ValueError:
            return False

    def split_words(self, usr_input):
        words = usr_input
        # separate punctiation to separate all words for tokenizing
        words = words.replace(".", " .PERIOD ")
        words = words.replace("!", " !EXCLAMATION-POINT ")
        words = words.replace("?", " ?QUESTION-MARK ")
        words = words.replace(",", " ,COMMA ")
        words = words.replace("-", " -HYPHEN ")
        words = words.replace(":", " :COLON ")
        words = words.replace(";", " ;SEMI-COLON ")
        words = words.replace("\"", " \"QUOTE ")
        words = words.replace(")", " )CLOSE-PARENTHESES ")
        words = words.replace("(", " (OPEN-PARENTHESES ")
        words = words.replace("\\", " \\ ")
        words = words.replace("/", " /SLASH ")
        words = words.replace("%", " %PERCENT ")
        words = words.replace("[", " [ ")
        words = words.replace("]", " ] ")
        words = words.split()
        for a in words:
            try:
                if a.isdigit():
                    # print ("true", a)
                    w = self.p.number_to_words(a)
                    # print w
                    self.split_words(w)

                elif self.isfloat(a):
                    (w, dec) = a.split(".", 1)
                    w = self.p.number_to_words(a)
                    # print w
                    self.split_words(w)
                else:
                    # print a
                    self.words_list.append(self.d[a.lower()])
            except:
                print "Errors, see error.txt"
                f = open("error.txt", "a+")
                f.write("Failed Word: %s\n" % a)
                f.close()

    def getList(self):
        returnList = self.words_list
        self.words_list = []
        return returnList


def main(args):
    parser = Syllableizer('cmudict-modified.txt')
    usr_input = "none"
    while (usr_input != "quit"):
        usr_input = raw_input('enter word to break apart\n')
        parser.split_words(usr_input)
        print parser.getList()


if __name__ == '__main__':
    main(sys.argv)
