@import commonNew.spec

@objects
	service_offered			xpath	  /html/body/main/div/div[2]/div/div[2]
    buy_now       			xpath     //*[@id='buy-btn']/a
    pay_premium             xpath     //*[@id='pay-btn']/a
    statements        		xpath     //*[@id='statement-btn']/a
    top_up        			xpath     //*[@id='claim-btn']/a
    
    service_offered_mobile  xpath     /html/body/main/div/div[1]/div
    buy_now_mobile			xpath     /html/body/main/div/div[1]/div/div[1]
    pay_premium_mobile      xpath     /html/body/main/div/div[1]/div/div[2]
    statements_mobile       xpath     /html/body/main/div/div[1]/div/div[3]
    track_mobile            xpath     /html/body/main/div/div[1]/div/div[4]
    
    


= Content =
    @on desktop
        buy_now, pay_premium, statements,top_up:
            inside service_offered
            
    @on mobile
        buy_now_mobile, pay_premium_mobile, statements_mobile,track_mobile:
            inside service_offered_mobile
                     
