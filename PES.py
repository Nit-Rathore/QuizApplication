import tkinter
from tkinter import*
import random
import time
from PIL import Image
from PIL import ImageTk

root = Tk()
root.title("NoBrainer")
root.geometry("800x600")
root.config(bg="light green")
root.resizable(0,0)

##########################################################################################################################################
img1 = Image.open("C:\\Users\\Spectre\\Desktop\\PES\\CSE Project\\Sem1 Project\\NoBrainer.png")
img1 = img1.resize((150,120), Image.ANTIALIAS)
img1 = ImageTk.PhotoImage(img1)

img2 = Image.open("C:\\Users\\Spectre\\Desktop\\PES\\CSE Project\\Sem1 Project\\unnamed.png")
img2 = img2.resize((150,90), Image.ANTIALIAS)
img2 = ImageTk.PhotoImage(img2)

photo= Image.open("C:\\Users\\Spectre\\Desktop\\PES\\CSE Project\\Sem1 Project\\Civics.png")
photo = photo.resize((100,75), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(photo)
photo1= Image.open("C:\\Users\\Spectre\\Desktop\\PES\\CSE Project\\Sem1 Project\\Nature.png")
photo1 = photo1.resize((100,75), Image.ANTIALIAS)
photo1 = ImageTk.PhotoImage(photo1)
photo2=Image.open('C:\\Users\\Spectre\\Desktop\\PES\\CSE Project\\Sem1 Project\\English.png')
photo2 = photo2.resize((100,75), Image.ANTIALIAS)
photo2 = ImageTk.PhotoImage(photo2)
photo3=Image.open('C:\\Users\\Spectre\\Desktop\\PES\\CSE Project\\Sem1 Project\\Sports.png')
photo3 = photo3.resize((100,75), Image.ANTIALIAS)
photo3 = ImageTk.PhotoImage(photo3)
photo4=Image.open("C:\\Users\\Spectre\\Desktop\\PES\\CSE Project\\Sem1 Project\\Mental_Ability.png")
photo4 = photo4.resize((100,75), Image.ANTIALIAS)
photo4 = ImageTk.PhotoImage(photo4)
photo5=Image.open("C:\\Users\\Spectre\\Desktop\\PES\\CSE Project\\Sem1 Project\\His.png")
photo5 = photo5.resize((100,75), Image.ANTIALIAS)
photo5 = ImageTk.PhotoImage(photo5)

##########################################################################################################################################
def Entertainment():
    ques= ["Who directed the movie '3 IDIOTS?' "," Which is the highest Grossing Film at present"," Who is India's Richest Actor?"," Who is the first Indian to win he prestigous Booker Prize",
    "Which IMD Indian Web series is 1st on IMDb ","Which country will be the focus country of the 50th- edition of International Film Festival of India (IFFI)? ",
    "Aishwarya Rai was crowned Miss World in which year? "," Who is known as father of Indian Cinema?","Which one is India's first television soap opera?"]

    choices=[["Rajkumar Hirani","Anurag Kashyap","Karan Johar","Aditya Chopda"],
    ["Infinity Wars","Avatar","Endgame","Titanic"], 
    ["Shah Rukh Khan","Amitabh Bacchan","Akshay Kumar","Me"],
    ["Kushwant Singh","Ruskin Bond","Suchetha Dalal","Arunaduthi Roy"],
    ["Scam 1992","Pataal Lok","SPECIAL OPS","Asur"],
    ["Germany","Italy","Russia","Japan"],
    ["1990","2000","1998","1994"],
    ["Dadasaheb Torne","V Shantaram","Dada Saheb Palake","Satyajit Ray"],
    ["Ramayan","Hum Log","Mahabharat","Buniyaad"]]
    answers = [0,2,0,3,0,2,3,2,1] 
    indexes = []
    user_ans= []    
    
    def gen():
        nonlocal indexes
        while(len(indexes)<9):
            x = random.randint(0,8)
            if x not in indexes:
                indexes.append(x)
            else:
                continue
    return indexes
    indexes =gen()
    q_no =1
                                            
    def calc():
        nonlocal indexes,user_ans,answers
    n = 0
    score = 0
    eoq = Label(root,text = 'END OF THE QUIZ',font = ('Consolas',20) , fg = 'purple',width = 20)
    eoq.pack()
    eoq1 = Label(root,text = 'Correct answers in Green incorrect in red', font =('Times',15), fg = 'violet')
    eoq1.pack()
    if user_ans==[]:
        for i in indexes:
            lb2 = Label(root, text = str(ques[i]) + ": " + str(choices[i][answers[i]]),justify = 'right',fg = 'red')
            lb2.pack()
        else:
                for i in indexes:
                    if user_ans[n]== answers[i]:
                        score += 1
                        lb1 = Label(root, text = str(ques[i]) + ": " + str(choices[i][answers[i]]),justify = 'right',fg = 'green')
                        lb1.pack()
                    else:
                        lb2 = Label(root, text = str(ques[i]) + ": " + str(choices[i][answers[i]]),justify = 'right',fg = 'red')
                        lb2.pack()
                    n += 1

    print(score)
    final = Label(root, text = "You've answered " + str(score) +" out of 9 questions correct", font = ("Consolas",20) ,width = 30,fg = 'blue')
    final.pack()
    quit_b = Button(root, text="PRESS TO QUIT", command=root.destroy, bg = 'yellow', fg= 'red')
    quit_b.pack()
    

    def scoreboard():
        lbl_ques.destroy()
        r1.destroy()
        r2.destroy()  
        r3.destroy()
        r4.destroy()
        time_l.destroy()
        end.destroy()
        calc()
    
    t = 600
    def timer():
        nonlocal time_l,t
        if t>0:
            minute = t//60
            second = t%60
            t-=1
            time_l.config(text = str(minute) +":"+str(second)) 
            time_l.after(1000,timer)
        elif t==0:
            scoreboard()
    time_l = Label(
        root,
        text = ""
        )
    time_l.pack()
    timer()

    def selected():
        nonlocal radiovar,user_ans
        nonlocal lbl_ques,r1,r2,r3,r4
        nonlocal q_no,time_l
        x = radiovar.get()
        user_ans.append(x)
        radiovar.set(-1)
        
        if q_no<9:
            lbl_ques['text']= ques[indexes[q_no]]
            r1['text']= choices[indexes[q_no]][0]
            r2['text']= choices[indexes[q_no]][1]
            r3['text']= choices[indexes[q_no]][2]
            r4['text']= choices[indexes[q_no]][3]
            q_no += 1
        
        elif q_no == 9:
            scoreboard()
    
    lbl_ques = Label(
        root,
        text = ques[indexes[0]],
        font = ("Times",15),
        wraplength = 350,
        width = 500
        )    
    lbl_ques.pack()
    radiovar = IntVar()
    radiovar.set(-1)

    r1 = Radiobutton(
        root,
        text = choices[indexes[0]][0],
        font = ("Times",12),
        variable = radiovar,
        value = 0,
        command = selected)
    r1.pack()

    r2 = Radiobutton(
        root,
        text = choices[indexes[0]][1],
        font = ("Times",12),
        variable = radiovar,
        value = 1,
        command = selected)
    r2.pack()

    r3 = Radiobutton(
        root,
        text = choices[indexes[0]][2],
        font = ("Times",12),
        variable = radiovar,
        value = 2,
        command = selected)
    r3.pack()

    r4 = Radiobutton(
        root,
        text = choices[indexes[0]][3],
        font = ("Times",12),
        variable = radiovar,
        value = 3,
        command = selected)
    r4.pack()

    end = Button(
        root,
        text="END QUIZ",
        command = scoreboard
    )
    end.pack()
    


def destroy_l():
    b_1.destroy()
    b_2.destroy()
    b_3.destroy()
    b_4.destroy()
    b_5.destroy()
    b_6.destroy()
    Entertainment()

#####################################################################################################################################
def Sports():
    ques= ["Which captain led Indian cricket team to win in all 3 formats of cricket","In which country was the first olympics held"," Who is the captain of Indian Football team"," What is the national sport of India"," Which team has most number of FIFA World cups"," Which player has dunked most in NBA"," Which wrestler has the most no. of golds in olympics"," Who is currently Word No.1 in tennis"," Which cricketer has scored the fastest 100 in IPL"]
    choices = [["Mahendra Singh Dhoni","Virat Kohli","Sourav Ganguly","Rahul Dravid"],
    ["Hong Kong","Greece","Athens","Seoul"],
    ["Sunil Chhetri","Gurpreet Singh","Abhisekh B","Rahul C"],
    ["Kabaddi","Cricket","Hockey","Tennis"],
    ["Brazil","Spain","Italy","Germany"],
    ["Rudy","Michael Jordan","Duncan","Tom Harry"],
    ["Yama Moto","Bruce Baumgarterner","Sushil Kumar","Kerelin"],
    ["Novak Djokovic","Andy Murray","Leander Paes","Roger Federer"],
    ["Chris Gayle","ABD","Virat Kohli","KL Rahul"]]
    answers = [0,2,0,2,0,0,1,0,0]
    
    def gen():
        nonlocal indexes
        while (len(indexes)<9):
            x = random.randint(0,8)
            if x not in indexes:
                indexes.append(x)
            else:
                continue
        return indexes
    indexes = gen()
    user_ans=[]
    q_no= 1
    
    def calc():
        nonlocal indexes,user_ans,answers
        n = 0
        score = 0
        eoq = Label(root,text = 'END OF THE QUIZ',font = ('Consolas',20) , fg = 'purple',width = 20)
        eoq.pack()
        eoq1 = Label(root,text = 'Correct answers in Green incorrect in red', font =('Times',15), fg = 'violet')
        eoq1.pack()
        if user_ans==[]:
            for i in indexes:
                lb2 = Label(root, text = str(ques[i]) + ": " + str(choices[i][answers[i]]),justify = 'right',fg = 'red')
                lb2.pack()
        else:
            for i in indexes:
                if user_ans[n]== answers[i]:
                    score += 1
                    lb1 = Label(root, text = str(ques[i]) + ": " + str(choices[i][answers[i]]),justify = 'right',fg = 'green')
                    lb1.pack()
                else:
                    lb2 = Label(root, text = str(ques[i]) + ": " + str(choices[i][answers[i]]),justify = 'right',fg = 'red')
                    lb2.pack()
                n += 1

        print(score)
        final = Label(root, text = "You've answered " + str(score) +" out of 9 questions correct", font = ("Consolas",20) ,width = 30,fg = 'blue')
        final.pack()
        quit_b = Button(root, text="PRESS TO QUIT", command=root.destroy, bg = 'yellow', fg= 'red')
        quit_b.pack()


    def scoreboard():
        lbl_ques.destroy()
        r1.destroy()
        r2.destroy()
        r3.destroy()
        r4.destroy()
        time_l.destroy()
        end.destroy()
        calc()
    
    t = 600
    def timer():
        nonlocal time_l,t
        if t>0:
            minute = t//60
            second = t%60
            t-=1
            time_l.config(text = str(minute) +":"+str(second)) 
            time_l.after(1000,timer)
        elif t==0:
            scoreboard()

    time_l = Label(
        root,
        text = ""
        )
    time_l.pack()
    timer()

    def selected():
        nonlocal radiovar,user_ans
        nonlocal lbl_ques,r1,r2,r3,r4
        nonlocal q_no,time_l
        x = radiovar.get()
        user_ans.append(x)
        radiovar.set(-1)
        if q_no<9:
            lbl_ques['text']= ques[indexes[q_no]]
            r1['text']= choices[indexes[q_no]][0]
            r2['text']= choices[indexes[q_no]][1]
            r3['text']= choices[indexes[q_no]][2]
            r4['text']= choices[indexes[q_no]][3]
            q_no += 1
        
        elif q_no == 9:
          scoreboard()

    lbl_ques = Label(
        root,
        text = ques[indexes[0]],
        font = ("Times",15),
        wraplength = 350,
        width = 500
        )    
    lbl_ques.pack()
    radiovar = IntVar()
    radiovar.set(-1)

    r1 = Radiobutton(
        root,
        text = choices[indexes[0]][0],
        font = ("Times",12),
        variable = radiovar,
        value = 0,
        command = selected)
    r1.pack()

    r2 = Radiobutton(
        root,
        text = choices[indexes[0]][1],
        font = ("Times",12),
        variable = radiovar,
        value = 1,
        command = selected)
    r2.pack()

    r3 = Radiobutton(
        root,
        text = choices[indexes[0]][2],
        font = ("Times",12),
        variable = radiovar,
        value = 2,
        command = selected)
    r3.pack()

    r4 = Radiobutton(
        root,
        text = choices[indexes[0]][3],
        font = ("Times",12),
        variable = radiovar,
        value = 3,
        command = selected)
    r4.pack()

    end = Button(
        root,
        text="END QUIZ",
        command = scoreboard
    )
    end.pack()
    


def destroy_l():
    b_1.destroy()
    b_2.destroy()
    b_3.destroy()
    b_4.destroy()
    b_5.destroy()
    b_6.destroy()
    Sports()

#########################################################################################################################################
def Literature():        
    ques = [ "Who is the author of 'To Kill a Mockingbird'?",
    "Material feminism studies inequality in terms of-",
    "Anita Desai's 'Where Shall We Go This Summer' has been compared to Virginia Woolf's-",
    "How many sonnets did Shakespeare write in all?",
    "Which is believed to be the first important revenge tragedy?",
    "Which one of these books is not written by 'Haruki Murakami'?",
    "In 1913 Tagore was awarded the Nobel Prize for literature for the English translation of?",
    "To read critically means-",
    "Which one is the world's longest novel?"
    ]

    choices = [["Harper Lee","Virginia Woolf","George Orwell","Enid Blyton"],
    ["Only Gender","Only Class","Both Class and Gender","Only Patriarchy"],
    ["To The Lighthouse","The Voyage Out","The Waves","Night and Day"],
    [152,153,154,155],
    ["Gorboduc","Hamlet","The Spanish Tragedy","Tamburlaine"],
    ["Kafka on the Shore","After Dark","1984","Men Without Women"],
    ["The Gitanjali","Fruit Gathering","Lover’s Gift","None"],
    ["Taking an opposing point of view to the ideas and opinions expressed","Skimming through the material because most of it is just padding",
    "Evaluating what you read in terms of your own research questions","Being negative about something before you read it"],
    ["A Suitable Boy","L'Astree","War and Peace","Remembrance of Things Past"]
    ]

    answers = [0,2,0,2,2,2,0,2,3]
    indexes= []
    def gen():
        nonlocal indexes
        while (len(indexes)<9):
            x = random.randint(0,8)
            if x not in indexes:
                indexes.append(x)
            else:
                continue
        return indexes
    indexes = gen()
    user_ans=[]
    q_no= 1
    
    def calc():
        nonlocal indexes,user_ans,answers
        n = 0
        score = 0
        eoq = Label(root,text = 'END OF THE QUIZ',font = ('Consolas',20) , fg = 'purple',width = 20)
        eoq.pack()
        eoq1 = Label(root,text = 'Correct answers in Green incorrect in red', font =('Times',15), fg = 'violet')
        eoq1.pack()
        if user_ans==[]:
            for i in indexes:
                lb2 = Label(root, text = str(ques[i]) + ": " + str(choices[i][answers[i]]),justify = 'right',fg = 'red')
                lb2.pack()
        else:
            for i in indexes:
                if user_ans[n]== answers[i]:
                    score += 1
                    lb1 = Label(root, text = str(ques[i]) + ": " + str(choices[i][answers[i]]),justify = 'right',fg = 'green')
                    lb1.pack()
                else:
                    lb2 = Label(root, text = str(ques[i]) + ": " + str(choices[i][answers[i]]),justify = 'right',fg = 'red')
                    lb2.pack()
                n += 1

        print(score)
        final = Label(root, text = "You've answered " + str(score) +" out of 9 questions correct", font = ("Consolas",20) ,width = 30,fg = 'blue')
        final.pack()
        quit_b = Button(root, text="PRESS TO QUIT", command=root.destroy, bg = 'yellow', fg= 'red')
        quit_b.pack()



    def scoreboard():
        lbl_ques.destroy()
        r1.destroy()
        r2.destroy()
        r3.destroy()
        r4.destroy()
        time_l.destroy()
        end.destroy()
        calc()
    
    t = 600
    def timer():
        nonlocal time_l,t
        if t>0:
            minute = t//60
            second = t%60
            t-=1
            time_l.config(text = str(minute) +":"+str(second)) 
            time_l.after(1000,timer)
        elif t==0:
            scoreboard()
    time_l = Label(
        root,
        text = ""
        )
    time_l.pack()
    timer()

    def selected():
        nonlocal radiovar,user_ans
        nonlocal lbl_ques,r1,r2,r3,r4
        nonlocal q_no,time_l
        x = radiovar.get()
        user_ans.append(x)
        radiovar.set(-1)
        if q_no<9:
            lbl_ques['text']= ques[indexes[q_no]]
            r1['text']= choices[indexes[q_no]][0]
            r2['text']= choices[indexes[q_no]][1]
            r3['text']= choices[indexes[q_no]][2]
            r4['text']= choices[indexes[q_no]][3]
            q_no += 1
        
        elif q_no == 9:
          scoreboard()
    lbl_ques = Label(
        root,
        text = ques[indexes[0]],
        font = ("Times",15),
        wraplength = 350,
        width = 500
        )    
    lbl_ques.pack()
    radiovar = IntVar()
    radiovar.set(-1)

    r1 = Radiobutton(
        root,
        text = choices[indexes[0]][0],
        font = ("Times",12),
        variable = radiovar,
        value = 0,
        command = selected)
    r1.pack()
    r2 = Radiobutton(
        root,
        text = choices[indexes[0]][1],
        font = ("Times",12),
        variable = radiovar,
        value = 1,
        command = selected)
    r2.pack()

    r3 = Radiobutton(
        root,
        text = choices[indexes[0]][2],
        font = ("Times",12),
        variable = radiovar,
        value = 2,
        command = selected)
    r3.pack()
    r4 = Radiobutton(
        root,
        text = choices[indexes[0]][3],
        font = ("Times",12),
        variable = radiovar,
        value = 3,
        command = selected)
    r4.pack()

    end = Button(
        root,
        text="END QUIZ",
        command = scoreboard
    )
    end.pack()
    


def destroy_l():
    b_1.destroy()
    b_2.destroy()
    b_3.destroy()
    b_4.destroy()
    b_5.destroy()
    b_6.destroy()
    Literature()
#########################################################################################################################################
def Nature():

    
    
    ques = [ "Pakistan developed the National conservation strategy in-",
    "Recycling of one ton of paper can save-",
    "Stilt roots are found in -",
    "The age of a tree can be determined more or less accurately by-",
    "Which of the following plants is referred to as a living fossil?",
    "Birds are known to survive in virtually all known environments. To which class do they belong?",
    "An example of a flightless, swimming bird is a",
    "What is the largest group of insects?",
    "Why do Crickets rub their wings together?"
    ]
    choices = [["1990","1991","1993","1992"],
    ["120 trees","130 trees","17 trees","18 trees"],
    ["Banyan","Maize","Mango","China rose"],
    ["finding the ratio of height to the width of the tree","counting the number of rings in the trunk","measuring the height of the tree",
    "measuring the diameter of the trunk"],
    ["Ephedra","Cycas","Ginkgo","Adiantum"],
    ["Reptiles","Aves","Agnatha","Fliers"],
    ["Gull","Quail","Penguin","Crane"],
    ["Flies","Butterflies","Bees and wasps","Beetles"],
    ["To help them fly","To keep themselves warm","To attract a male","To keep their predators away"]
    ]


    answers = [3,2,1,1,2,1,2,3,2]
    indexes= []
    def gen():
        nonlocal indexes
        while (len(indexes)<9):
            x = random.randint(0,8)
            if x not in indexes:
                indexes.append(x)
            else:
                continue
        return indexes
    indexes = gen()
    user_ans=[]
    q_no= 1 

    
    def calc():
        nonlocal indexes,user_ans,answers
        n = 0
        score = 0
        eoq = Label(root,text = 'END OF THE QUIZ',font = ('Consolas',20) , fg = 'purple',width = 20)
        eoq.pack()
        eoq1 = Label(root,text = 'Correct answers in Green incorrect in red', font =('Times',15), fg = 'violet')
        eoq1.pack()
        if user_ans==[]:
            for i in indexes:
                lb2 = Label(root, text = str(ques[i]) + ": " + str(choices[i][answers[i]]),justify = 'right',fg = 'red')
                lb2.pack()
        else:
            for i in indexes:
                if user_ans[n]== answers[i]:
                    score += 1
                    lb1 = Label(root, text = str(ques[i]) + ": " + str(choices[i][answers[i]]),justify = 'right',fg = 'green')
                    lb1.pack()
                else:
                    lb2 = Label(root, text = str(ques[i]) + ": " + str(choices[i][answers[i]]),justify = 'right',fg = 'red')
                    lb2.pack()
                n += 1
        print(score)
        final = Label(root, text = "You've answered " + str(score) +" out of 9 questions correct", font = ("Consolas",20) ,width = 30,fg = 'blue')
        final.pack()
        quit_b = Button(root, text="PRESS TO QUIT", command=root.destroy, bg = 'yellow', fg= 'red')
        quit_b.pack()

    def scoreboard():
        lbl_ques.destroy()
        r1.destroy()
        r2.destroy()
        r3.destroy()
        r4.destroy()
        time_l.destroy()
        end.destroy()
        calc()

    t = 5
    def timer():
        nonlocal time_l,t
        if t>0:
            minute = t//60
            second = t%60
            t-=1
            time_l.config(text = str(minute) +":"+str(second)) 
            time_l.after(1000,timer)
        elif t==0:
            scoreboard()
        
    time_l = Label(
        root,
        text = ""
        )
    time_l.pack()
    timer()

    def selected():
        nonlocal radiovar,user_ans
        nonlocal lbl_ques,r1,r2,r3,r4
        nonlocal q_no
        x = radiovar.get()
        user_ans.append(x)
        radiovar.set(-1)
        if q_no<9:
            lbl_ques['text']= ques[indexes[q_no]]
            r1['text']= choices[indexes[q_no]][0]
            r2['text']= choices[indexes[q_no]][1]
            r3['text']= choices[indexes[q_no]][2]
            r4['text']= choices[indexes[q_no]][3]
            q_no += 1
        
        elif q_no == 9:
            scoreboard()
            

    lbl_ques = Label(
        root,
        text = ques[indexes[0]],
        font = ("Times",15),
        wraplength = 350,
        width = 500
        )    
    lbl_ques.pack()
    radiovar = IntVar()
    radiovar.set(-1)

    r1 = Radiobutton(
        root,
        text = choices[indexes[0]][0],
        font = ("Times",12),
        variable = radiovar,
        value = 0,
        command = selected)
    r1.pack()
    r2 = Radiobutton(
        root,
        text = choices[indexes[0]][1],
        font = ("Times",12),
        variable = radiovar,
        value = 1,
        command = selected)
    r2.pack()

    r3 = Radiobutton(
        root,
        text = choices[indexes[0]][2],
        font = ("Times",12),
        variable = radiovar,
        value = 2,
        command = selected)
    r3.pack()
    r4 = Radiobutton(root,
        text = choices[indexes[0]][3],
        font = ("Times",12),
        variable = radiovar,
        value = 3,
        command = selected)
    r4.pack()

    end = Button(
        root,
        text="END QUIZ",
        command = scoreboard
    )
    end.pack()


def destroy_n():
    b_1.destroy()
    b_2.destroy()
    b_3.destroy()
    b_4.destroy()
    b_5.destroy()
    b_6.destroy()
    Nature()
##########################################################################################################################################
def _menu():
    global b_1,b_2,b_3,b_4,b_5,b_6
    def History():
        print("Hizzz")
    def Civ():
        print("Civ")
    def Nature():
        print("Nature")
    def Litreture():
        print("Shakesphere")
    def Mental_Ability():
        print("I'm dead")
    b_1= Button(root,text='\nLiterature\n\t\t',width=100,height = 75, command=destroy_l,image=photo2,bg="Blue",border=0)
    b_1.place(x=50,y=50)
    b_2=Button(root,text='\nNature\n',width=100,height = 75, command=destroy_n,image=photo1,bg="Blue",border=0) 
    b_2.place(x=100,y=0)
    b_3=Button(root,text='\nCivics\n\t\t',width=100,height = 75, command=Civ,image=photo,bg="Blue",border=0)
    b_3.place(x=0,y=100)
    b_4=Button(root,text='\nSports\n',width=100,height = 75, command=Litreture,image=photo3,bg="Blue",border=0)
    b_4.place(x=100,y=100)
    b_5=Button(root,text='\nMental Ability \n',width=100,height = 75,command=Mental_Ability,image=photo4,bg="Blue",border=0)
    b_5.place(x=0,y=200)
    b_6=Button(root,text='\nHistory\n\t\t',width=100,height = 75, command=History,image=photo1,bg="Blue",border=0)
    b_6.place(x=100,y=200)

##########################################################################################################################################

def destroy1():
    Label_img.destroy()
    Label_text.destroy()
    name.destroy()
    lbl_instructions_1.destroy()
    lbl_instructions_t.destroy()
    lbl_instructions.destroy()
    start_bt.destroy()
    click.destroy()
    _menu()
##########################################################################################################################################

Label_img = Label(
    root,
    image= img1, 
    bg ="light green")
Label_img.pack()
Label_text = Label(
    root,
    text="Welcome!",
    bg ="light green",
    font= ("Calibri",24,"bold")
)
Label_text.pack()
name = Entry(root,width=80)
name.pack()
name.insert(0,"Enter your name")
user_name = name.get()
def my_click():
    global lbl_instructions_1,lbl_instructions_t,lbl_instructions
    global start_bt
    lbl_instructions_1 = Label(
    root,
    text= "Hello "+name.get()+"," + """ Click on the start button to choose your quiz topic
            once you've read the instructions.""",
    font = (12),
    bg = "light green"
    )
    lbl_instructions_1.pack()
    lbl_instructions_t = Label(
    root,
    text= "INSTRUCTIONS",
    font= (14),
    bg = "light green"
    )
    lbl_instructions_t.pack()

    lbl_instructions =  Label(
        root,
        text="""1) The quiz contains six quiz topics
        2) You can choose one of them
        3)Each quiz contains 9 questions
        4)The quiz lasts for 15 mins after which the quiz will end automatically.
        5)The questions will be of  MCQ type.
        6)You can select an option only once, after which the next ques will be displayed. So, choose wisely.
        7)Your answers will be auto-saved as you enter them.
        Have fun and Good Luck!""",
        font = ("Comic Sans",13),
        bg = "light green",
        foreground = "Blue"
        )
    lbl_instructions.pack()

    start_bt = Button(
        root,
        image=img2,
        bg ="light green",
        relief = GROOVE,
        border = 0,
        command = destroy1
        )
    start_bt.pack()

click = Button(
    root,
    text="Click here",
    width = 10,
    relief = FLAT,
    border=0,
    bg= "Dark Blue",
    fg ="white",
    command = my_click,
    )
click.pack()





root.mainloop()
