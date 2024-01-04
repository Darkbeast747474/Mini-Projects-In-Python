# To Make KBC In Python

qs = [
    "Whose Founder of TATA Groups?:\n1.)Jamshed Ji Tata\t2.)Ratan Tata\n3.)Mukesh Ambani\t4.)Adani",
    "Most Populated Country In The World:\n1.)India\t2.)China\n3.)Japan\t4.)USA",  # A List of Questions Which Will be Printed U Can
    "What is the pH value of the human body?:\n1.)9.2 to 9.8\t2.)7.0 to 7.8\n3.)6.1 to 6.3\t4.)5.4 to 5.6",  # Questions can be added  to make the Game Challenging
    "Which of the following Himalayan regions is called Shivalik's?:\n1.)Upper Himalayas\t2.)Lower Himalayas\n3.)Outer Himalayas\t4.)Inner Himalayas",
    "The Grand Canyon located in which country?:\n1.)Ghana\t2.)The US\n3.)Canada\t4.)Bolivia",
]

ans = ["1","2","2","3","2",]  # The Correct Option Of The Parallel Questions Given Above {Index OF Lists OF Questions & Answers Must Be Same}

lev = [1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,]  # List Of Levels Of Price Money Icreases By Giving The Correct Answer Each Time


def ansval():
    
    """Takes The Input Of Answers To Validate
    It According To The Question."""

    i = 0   # Variable to store The Level Number
    
    mon = 0 # Variable to store The Total Amount Of Price User Has Won Till Last OF Wrong Answering
    
    for q in qs:
        
        if i == 0:
            print(f"First Question For Rs.{lev[i]}-->\n")        # identifys The Question Is First Or Not
        else:
            print(f"Next Question For Rs.{lev[i]}-->\n")
            
        print(q, "\n")  # Print the question From List 
        ua = input("Choose An Option By Numbering or Type 'Quit' To Quit:\n")   #User have to choose Desired option Between {1,2,3,4} 

        if ua in ans[i]:   #Checking the Users choice With The stored choice Parallel to It's Question Using Level index Variale
            
            #Executed IF User's choice Is Correct
            
            print("Answer IS Correct!!\n")
            if i == 4:  
                mon = lev[i]
                print("You Cleared Level 1")   #First level Is Cleared After answering  4 Previous questions Correctly
            elif i == 8:
                mon = lev[i]                                
                print("You Cleared Level 2")   #Second level Is Cleared After answering 3 Previous questions Correctly 
            elif i == 9:
                mon = lev[i]
                print("You Cleared Level 3")   #Third level Is Cleared After answering all Previous questions Correctly As It's The Final level
                
        elif ua == "Quit":           #Executes If User Quits {By typing "Quit" In Ua(User's Answer Variable)}
            
            if i == 0:
                mon = 0   #If Quits at Start 0 Prize Money            
                
            else:                       
                mon = lev[i - 1]    #If Quits after answering Certain Level Of Question
            break
        
        else:
            print("Wrong Answer!!\n")   
            if i == 4 or 8 or 9:        #If Answered Incorrectly At any level The Loop's Breaked 
                break
            
        i = i + 1   #Iterator's Value IS Incremented After Passing Each Index OF Question's List
        
    return mon  #Return The Total Amount Earned By User

if __name__ == "__main__":  #This is the Main Function 

    print("Welcome to KBC With Python!!")
    
    n = input("Enter Your Name...")
    print("+----------------------------------------+")
    
    if n == "" or n == None:
        print("A unknown user!!")   #Verify Name Of User Whether It's A empty string 
    else:
        print("Welcome To KBC!!", n, "\n")
        
        res = ansval()      #The Asks The Answers of Question From User Validates It And return The Prize Money He/She Earned
        
        print(f"Your Prize Money Is:{res}")     #Return Value Stored In a Variable Called Res N printed

    print("End OF Game!!")  # The End Of Game THe Message Is printed
