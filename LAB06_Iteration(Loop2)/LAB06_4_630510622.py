# 630510622
#ธนกฤต สมุทร (Thanakrit Samut)
#section 002
#Lab6_4

# find max_score runnerup_score and Average
def main():
    first_round = True
    all_score = 0
    runner_up = 0
    #line 8 to 10 set value
    num = int(input("Total students: "))#number of students 
    print("Enter score: ")
    for i in range (num):#enter score 'num' times
        score = int(input())
        if(first_round == True):#This loop will do only 1 times to get score to max for compare another score
            max_ = score
            first_round = False#when first_round is false loop will not get in if
        else:#first_round == False // another round (2 to num)
            if(max_ < score):# check if max_ is lower than new score change max_ to runnerup and get new score to max_
                runner_up = max_
                max_ = score
            elif(max_ > score):#nothing to do with max_ because max_ is maximum score but check the runnerup
                if(runner_up <= score):#if runnerup least than new score ,new score is runnerup 
                    runner_up = score
        all_score += score#plus all score to use when finding average
    Average = (all_score/num)#find average
    if(max_ != runner_up and runner_up != 0):#show the max runnerup and average
        print("---")    
        print("Max score is: %.2f"%max_)
        print("Runner up is: %.2f"%runner_up)
        print("Average is: %.2f"%Average)
    else:#(max_ == runner_up or runner_up == 0)//max = runnerup , have only 1 student score 
        print("---")   
        print("Max score is: %.2f"%max_)
        print("Runner up is: None")
        print("Average is: %.2f"%Average)
    

if __name__ == "__main__":
    main()