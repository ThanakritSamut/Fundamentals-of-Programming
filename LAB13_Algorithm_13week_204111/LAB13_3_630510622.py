#630510622
#ธนกฤต สมุทร (Thanakrit Samut)
#section 002
#Lab13_3
import string
def word_count(text):
    text = text.lower()#result must be lower
    frequency = dict()#frequency of word
    lst = text.split("\n")#split text when text has line
    lst2 = []
    result = []
    index = 0
    remove = string.punctuation + string.whitespace
    for row in lst:
        #print(row)
        result.extend(row.split(" "))#split word with whitespace
    for j in result:#result = split "\n" and split word
        if(j not in remove):#if j aren't punctiation or whitespace word to new list (maybe word has some punctuation)
            lst2.append(j)
    for i in lst2:#get punctuation out (side of word)
        result = i.strip(string.punctuation)
        lst2[index] = result#get word without punctuation side of word
        index += 1

    for i in lst2:
        count = 1 + frequency.get(i,0)#count word in text 
        frequency[i] = count
    return frequency#return in dict

def main():
    #text =   "2(l):p.4"
    text = '''
"He doesn't want to pay $40,000 for a new car, but his wife doesn't seem to care."
'''
    print(word_count(text))

if __name__ == "__main__":
    main()