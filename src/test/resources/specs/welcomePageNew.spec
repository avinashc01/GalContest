@import commonNew.spec

@objects
	service_offered			xpath	  /html/body/main/div/div[2]/div/div[2]
    buy_now       			xpath     //*[@id='buy-btn']/a
    pay_premium             xpath     //*[@id='pay-btn']/a
    statements        		xpath     //*[@id='statement-btn']/a
    top_up        			xpath     //*[@id='claim-btn']/a


= Content =
    @on desktop
        buy_now, pay_premium, statements,top_up:
            inside service_offered
