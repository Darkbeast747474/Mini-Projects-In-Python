import time #Time Module 
from win10toast import ToastNotifier	# A Module Used To Make Toast Notifications {Only For Windows!!}

def Give_Notification():	
    
    '''Defininig A Function To Make Toast Notifications'''
    
    t = ToastNotifier()	#Toast Notification Object
    
    #Show Toast Method Of Toast Notification Object and Giving Parameters In The Following
    t.show_toast(
        title=f"Hey {Name}!!",               
        msg="Drink Some Water!!\nIt's"+time.strftime("%H:%M"),  #strftime Method To Return The Local Time tuple as a string
        duration=5,
        icon_path='Py/as.ico',
        threaded=True
    )
    
if __name__ == "__main__":
    
	Name = input('Your Name: ')
 
	print('Enter Your Focus Time--->')
	hour, minute = int(input('Enter Hours:\t')), int(input(" Minutes:")) #Input the Desired Duration Of Focus Time In hours and minutes
 
	breaks = int(input('How Many Breaks U Want?: ')) #Input For The Number Of Breaks a User Need 
 
	if hour >= 0 and hour <= 24:	#Valdating If The Hour Of Focus Isn't Too Long Than 24
		print(f"Focus Time:- {hour}:{ minute}")		#Print The Focus Time 
  
		for i in range(breaks): #Iterate through Number Of Breaks Given By User						
			time.sleep((((hour)*60+minute)*60)/breaks+1) # The Main Logic Where The Hour & Minutes are Converted To Seconds
   			# and Divied By Break+1 {As The Loop Starts From 0} And Sent To The Sleep Method Of Time Module To till Next Break
      
			Give_Notification() #Raise Notification By calling Get_Notification Function
   
	else:
		print("U Can't Focus THISSS Long or THISSS Short!!")	#Print To Notify User Bout Long Duration