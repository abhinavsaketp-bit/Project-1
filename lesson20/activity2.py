def match_word(words):
    count=0
    List=[]
    for word in words:
        if len(word)>1 and word[0]==word[-1]:
            count=+1
            List.append(word)
    print("The first and last words are both matching: ", List)
    return count

matching=match_word(["hi","GGs","GOOD LUCK!","Bye","123 loading ...","12321","malayalam"])
print("The number of words/Numbers matching are/is: ", matching)



             