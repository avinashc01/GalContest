
@objects
    header                   xpath    /html/body/div[2]/div[1]/div[2]/div/div/div   
    menu                     xpath    /html/body/div[2]/div[2]/div[2]/div/div[2]/div/div
    content_section		     xpath    /html/body/main/div/div[5]
    content_products		 xpath    /html/body/main/div/div[7]/div[1]
    content_banner           xpath    /html/body/main/div/div[7]/div[2]/div 
    footer                   xpath    /html/body/div[3]/div[2]/div/div


= Header =
    
    @on desktop
        header:
            width ~ 995px
            
    @on mobile
    	header:
    		width ~ 432px        

    
= Menu =
    
    @on desktop
        menu:
        	centered horizontally inside screen 1px
        	below header ~ 0px
            width 994px


= Content =

    @on desktop
        
        content_products:
        	below content_section ~ 40px
        	width 994px
        	
        content_banner:
        	below content_products ~ 0px
        	width 994px
        	
    @on mobile
    	
        content_products:
        	below content_section ~ 90px
        	width 431px
        	
        content_banner:
        	below content_products ~ 0px
        	width 431px
    	    			

= Footer =

	footer:
        below content_banner ~ 0px
        
       
