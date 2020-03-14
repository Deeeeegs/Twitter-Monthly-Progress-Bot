from datetime import datetime
from calendar import monthrange
from calendar import month_name

import pytz
import twitter
import tweepy



consumerK = "3aOb8SjxLWSOFl9j8TDtHW1bQ"
consumerS = "x7bha2KZ4j3K2WT3iMQ91OdRCm34mpWqezB9aExbnmKHJyjplh"
accessK = "984326022903447552-GHx4YWRCbjkipUoxksbbzcwhwognFYi"
accessS = "PwRn2TlJ297dimL1VHTBtYzDuhO9T0uYXsMtr48n36DfE"

auth = tweepy.OAuthHandler(consumerK, consumerS)

auth.set_access_token(accessK, accessS)

api = tweepy.API(auth, wait_on_rate_limit=True,
                 wait_on_rate_limit_notify=True)

pst = pytz.timezone('America/Los_Angeles')

empty = "░"
fill = "▓"

prevpercentage = 0
lastdaytweeted = 4
prevdate = 0


while(True):
    currentdate = datetime.date(datetime.now(tz=pst)) #get the current date

    if(currentdate != prevdate):
        print("New date:", currentdate)
        
    month = currentdate.month 
    day = currentdate.day
    year = currentdate.year

    daysthismonth = monthrange(year, month)[1] #get the num of days this month

    percentage = day/daysthismonth * 100 #calc percentage of month done

    monthname = month_name[month] #get the string value of the current month

    tweet = monthname + " progress:\n" #string that will be the tweet                                                                      

    #if there is a new percentage then tweet 
    if percentage != prevpercentage and ((day >= (lastdaytweeted + 4)) or (day == daysthismonth)):
       amountFill = round((day/daysthismonth) * 15) # calculate how many filled bars we need
       amountEmpty = 15-amountFill #calculate how many empty bars we need
       
       tweet += fill*amountFill #add the filled bars to the tweet string
       tweet += empty*amountEmpty #add the emptybars to the tweet string

       tweet += (" " + str(round(percentage)) + "%") #add the percentage to the tweet string
       api.update_status(tweet) #send out the tweet
       
       if day == daysthismonth: #if it is the last day of the month reset lastdaytweeted to 3
           lastdaytweeted = 3
       else:
           lastdaytweeted = day #else set the lastdaytweeted to the current day 
           
       print("Tweet made on", currentdate, ":\n\n" + tweet)
       print("\nLast day tweeted:", lastdaytweeted)
       print("")
            
    prevpercentage = percentage #set the previous percentage to the current percentage
    prevdate = currentdate #set the previous date to the current date


    
    

