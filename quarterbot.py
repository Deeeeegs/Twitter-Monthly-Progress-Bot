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

    tweet = monthname + " progress:\n" #string that will be
                                                                      # the tweet 

    #if there is a new percentage then tweet 
    if percentage != prevpercentage and ((day >= (lastdaytweeted + 4)) or (day == daysthismonth)):
       amountFill = round((day/daysthismonth) * 15)
       amountEmpty = 15-amountFill
       
       tweet += fill*amountFill
       tweet += empty*amountEmpty

       tweet += (" " + str(round(percentage)) + "%")
       api.update_status(tweet)
       
       if day == daysthismonth:
           lastdaytweeted = 3
       else:
           lastdaytweeted = day
           
       print("Tweet made on", currentdate, ":\n\n" + tweet)
       print("\nLast day tweeted:", lastdaytweeted)
       print("")
            
    prevpercentage = percentage
    prevdate = currentdate


    
    

