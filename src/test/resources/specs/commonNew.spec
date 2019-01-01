
@objects
    header                   xpath    /html/body/div[2]/div[1]/div[2]/div/div/div   
    header-logo              xpath    /html/body/div[2]/div[1]/div[2]/div/div/div/div/div/div/div[1]/div[3]/a/img
    menu                     xpath    /html/body/div[2]/div[2]/div[2]/div/div[2]/div/div
    content_banner           xpath    //*[@id='owl-banner']/div[1]/div/div[1]/div/div/div/div/div[1]
    content_section		     xpath    /html/body/main/div/div[5]
    content_products		 xpath    /html/body/main/div/div[7]/div[1]
    content_banner2          xpath    /html/body/main/div/div[7]/div[2]/div 
    footer                   xpath    /html/body/div[3]/div[2]/div/div


= Header =
    
    @on desktop
        header:
            width ~ 995px

    
= Menu =
    
    @on desktop
        menu:
        	centered horizontally inside screen 1px
        	below header ~ 0px
            width 994px


= Content =


    @on desktop
        content_banner:
        	below menu ~ 0px
            centered horizontally inside screen 1px
            width 994px
            
        content_section:
        	below content_banner ~ 100px
        	width 994px
        	
        content_products:
        	below content_section ~ 40px
        	width 994px
        	
        content_banner2:
        	below content_products ~ 0px
        	width 994px		


= Footer =
    footer:
        height ~ 1144px
        below content_banner2 ~ 0px
        width 994px
