# Subject: AISC 1000_02 (Prof. Tim Nguyen)
# Assignment: Application Excercise 04S21
# Student Name & Number: Keval Padsala (500199506)
# Student Name & Number: Alifiya Pipewala (500201710)
# Student Name & Number: Ria Sharma (500195363)
# Student Name & Number: Archit Verma (500195589)


import os, sys, random, re, io


################# <------------- start main region -------------> #################

class AppExc4():

    def q1(self):

        print_menu = lambda: print("COMMAND MENU\nlist - Display all contacts\nview - View a contact\nadd - Add a contact\ndel - Delete a contact\nexit - Exit program")
        print("\n\nContact Manager")

        CONTACT_FILE = "./contacts.txt"
        
        print_menu()
        f = open(CONTACT_FILE, 'a+')
        
        def list_(f):
            f.seek(0)
            line_count = 0
            line = f.readline()
            while line:
                if line_count%3==0:
                    print("{}. {}".format(line_count//3+1, line.strip()))
                line = f.readline()
                line_count += 1
                
        def view(f):
            f.seek(0)
            print("Number:",end=" ")
            num = ii()

            flag = True
            line_count = 0
            line = f.readline()
            while line:
                if line_count//3==num-1:
                    print("{} {}".format("Name:", line.strip()))
                    print("{} {}".format("Email:", f.readline().strip()))
                    print("{} {}".format("Phone:", f.readline().strip()))
                    flag = False
                    break
                line = f.readline()
                line_count += 1
                
            if flag:
                print("Your Entry: {} couldn't found in the file.".format(num))
            
        def add(f):
            print("Name:",end=" ")
            print("Email:",end=" ")
            print("Phone:",end=" ")
            
            f.write(si()+"\n")
            f.write(si()+"\n")
            f.write(si()+"\n")
                
        def del_(f):
            f.seek(0)
            print("Number:",end=" ")
            num = ii()
            
            line_count = 0
            d = f.readlines()
            open(CONTACT_FILE, 'w').close()
            for i in d:
                if line_count//3!=num-1:
                    f.write(i)
                line_count += 1
            
            if line_count+1==len(d):
                print("Your Entry: {} couldn't found in the file.".format(num))



        run_more = True
        while run_more:                                         #Loop to run APP again...
            inp = si().lower()
            if inp == 'list':
                list_(f)
            elif inp == 'view':
                view(f)
            elif inp == 'add':
                add(f)
            elif inp == 'del':
                del_(f)
            elif inp == 'exit':
                print("Bye!")
                run_more = False
        f.close()

    def q2(self):
        print("\n\nQUESTION 2")
        REVIEW_FILE = "./reviews.txt"
        f = open(REVIEW_FILE, 'r')
        
        lines = " ".join(f.readlines())
        word_list = lines.split()
        
        stop_words = ['a', 'about', 'above', 'after', 'again', 'against', 'all', 'am', 'an', 'and', 'any', 'are', "aren't", 'as', 'at', 'be', 'because', 'been', 'before', 'being', 'below', 'between', 'both', 'but', 'by', "can't", 'cannot', 'could', "couldn't", 'did', "didn't", 'do', 'does', "doesn't", 'doing', "don't", 'down', 'during', 'each', 'few', 'for', 'from', 'further', 'had', "hadn't", 'has', "hasn't", 'have', "haven't", 'having', 'he', "he'd", "he'll", "he's", 'her', 'here', "here's", 'hers', 'herself', 'him', 'himself', 'his', 'how', "how's", 'i', "i'd", "i'll", "i'm", "i've", 'if', 'in', 'into', 'is', "isn't", 'it', "it's", 'its', 'itself', "let's", 'me', 'more', 'most', "mustn't", 'my', 'myself', 'no', 'nor', 'not', 'of', 'off', 'on', 'once', 'only', 'or', 'other', 'ought', 'our', 'ours', 'ourselves', 'out', 'over', 'own', 'same', "shan't", 'she', "she'd", "she'll", "she's", 'should', "shouldn't", 'so', 'some', 'such', 'than', 'that', "that's", 'the', 'their', 'theirs', 'them', 'themselves', 'then', 'there', "there's", 'these', 'they', "they'd", "they'll", "they're", "they've", 'this', 'those', 'through', 'to', 'too', 'under', 'until', 'up', 'very', 'was', "wasn't", 'we', "we'd", "we'll", "we're", "we've", 'were', "weren't", 'what', "what's", 'when', "when's", 'where', "where's", 'which', 'while', 'who', "who's", 'whom', 'why', "why's", 'with', "won't", 'would', "wouldn't", 'you', "you'd", "you'll", "you're", "you've", 'your', 'yours', 'yourself', 'yourselves']
        ##reference :- https://pypi.org/project/stop-words/ (To get a stopwords.)
        
        for word in word_list:                                  #remove stopwords and special characters
            if word.lower() in stop_words or not word.isalnum():
                word_list.remove(word)
        
        for i in range(len(word_list)):                          #remove special characters
            word_list[i] = re.sub('[^A-Za-z0-9]+', '', word_list[i])
        
        
        print(word_list)

def main():
    print("**** Application Exercise 04 ****")
    appExc4 = AppExc4()
    appExc4.q1()
    appExc4.q2()



################# <------------- end main region -------------> #################
###### normal io ######

def ii():  return int(input())
def si():  return input()
def mi(ss=" "):  return map(int,input().strip().split(ss))
def msi(ss=" "): return map(str,input().strip().split(ss))
def li(ss=" "):  return list(mi(ss))

def read():
    sys.stdin  = open('../input.txt', 'r')
    sys.stdout = open('../output.txt', 'w')


if __name__ == "__main__":
    read()
    main()



