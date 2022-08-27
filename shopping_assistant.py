def shopping_assistant():
    import speech_recognition as sr
    import pyttsx3
    import webbrowser
    engine=pyttsx3.init("sapi5")
    voices=engine.getProperty("voices")
    engine.setProperty("rate",155)
    def speak(command):
        engine.say(command)
        engine.runAndWait()
    def acceptcommand():
        r=sr.Recognizer()
        with sr.Microphone() as source:
            audio=r.listen(source)
            try:
                statement=r.recognize_google(audio,language='en-in')
            except Exception as e:
                speak("Pardon me! Can you say that again!")
                return "None"
            return statement
    speak("Hello!I am your Shopping Assistant!")
    while True:
            speak("Tell me the product category")
            statement=acceptcommand().lower()
            if statement==0:
                continue
            elif "phone" in statement or "mobile" in statement:
                speak("Opening the best selling websites")
                webbrowser.open_new_tab("https://www.croma.com/search/?q=phone%3Arelevance%3AZAStatusFlag%3Atrue%3AexcludeOOSFlag&text=phone")
                webbrowser.open_new_tab("https://www.reliancedigital.in/smartphones/c/S101711?searchQuery=:relevance&page=0")
                webbrowser.open_new_tab("https://www.flipkart.com/search?q=mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")
                webbrowser.open_new_tab("https://www.amazon.in/s?k=mobiles&crid=TTIVQ59KAMNQ&sprefix=mobile%2Caps%2C683&ref=nb_sb_noss_1")
                break
            elif "headset" in statement or "earphone" in statement:
                 speak("Opening the best selling websites")
                 webbrowser.open_new_tab("https://www.amazon.in/gp/browse.html?node=1388921031&ref_=nav_em_sbc_tvelec_headphones_0_2_9_4")
                 webbrowser.open_new_tab("https://www.flipkart.com/audio-video/headset/earphones/wired-earphones/pr?sid=0pm,fcn,821,fof&q=headphones&otracker=categorytree")
                 webbrowser.open_new_tab("https://www.reliancedigital.in/headphones-headsets/c/S101021")
                 webbrowser.open_new_tab("https://www.croma.com/audio-video/headphones-earphones/c/1012")
                 break
            elif "laptop" in statement or "laptops" in statement:
                 speak("Opening the best selling websites")
                 webbrowser.open_new_tab("https://www.flipkart.com/search?q=laptops&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")
                 webbrowser.open_new_tab("https://www.amazon.in/s?k=laptops&crid=DGE5QVHY7OBC&sprefix=laptos%2Caps%2C1584&ref=nb_sb_noss_2")
                 webbrowser.open_new_tab("https://www.croma.com/computers-tablets/laptops/c/20")
                 webbrowser.open_new_tab("https://www.reliancedigital.in/laptops/c/S101210")
                 break
            elif "grocery" in statement:
                speak("Opening the best selling websites")
                webbrowser.open_new_tab("https://www.jiomart.com/groceries")
                webbrowser.open_new_tab("https://www.bigbasket.com/")
                webbrowser.open_new_tab("https://www.amazon.in/s?k=snacks&crid=2FU5KJPNYV0PR&sprefix=snacks%2Caps%2C398&ref=nb_sb_noss_1")
                webbrowser.open_new_tab("https://dailybasket.com/products/in/category/Kitchen-Essentials?page=1")
                webbrowser.open_new_tab("https://groceryraja.com/")
                webbrowser.open_new_tab("https://nammamaligai.com/")
                break
            elif "food" in statement or "drinks" in statement:
                speak("Opening the best selling websites")
                webbrowser.open_new_tab("https://www.zomato.com/")
                webbrowser.open_new_tab("https://www.swiggy.com/")
                webbrowser.open_new_tab("https://www.dunzo.com/chennai")
                webbrowser.open_new_tab("https://www.ubereats.com/")
                webbrowser.open_new_tab("https://www.grubhub.com/delivery/cuisine/indian")
                break
            elif "books" in statement:
                speak("Opening the best selling websites")
                webbrowser.open_new_tab("https://www.amazon.in/s?k=amazon+bookscom&i=stripbooks&hvadid=82601146486761&hvbmt=bb&hvdev=c&hvqmt=e&tag=msndeskstdin-21&ref=pd_sl_9gmjeem7t0_b")
                webbrowser.open_new_tab("https://www.flipkart.com/books-store")
                webbrowser.open_new_tab("https://www.buybooksindia.com/")
                webbrowser.open_new_tab("https://www.noolulagam.com/")
                break
            elif "home appliance" in statement:
               speak("Opening the best selling websites")
               webbrowser.open_new_tab("https://www.reliancedigital.in/?msclkid=a6913e8eefb1172f15e45d868c295798&utm_source=bing&utm_medium=cpc&utm_campaign=RD_Search_Brand&utm_term=reliance%20digital&utm_content=Reliance%20Digital%20Brand%20search%20campaign")
               webbrowser.open_new_tab("https://www.flipkart.com/home-appliance-store?otracker=nmenu_sub_Appliances_0_Small%20Home%20Appliances&otracker=nmenu_sub_TVs%20%26%20Appliances_0_Small%20Home%20Appliances")
               webbrowser.open_new_tab("https://www.amazon.com/s?k=amazon+home+appliances&adgrpid=1333709110763139&hvadid=83357045250378&hvbmt=be&hvdev=c&hvlocphy=163971&hvnetw=o&hvqmt=e&hvtargid=kwd-83357776357370%3Aloc-90&hydadcr=21776_13321822&tag=mh0b-20&ref=pd_sl_6sm0uxxtz9_e")
               break
            elif "furnitures" in statement:
                speak("Opening the best selling websites")
                webbrowser.open_new_tab("https://www.amazon.com/s?k=meridian+furniture+xander+collection+modern&adgrpid=1330410580837792&hvadid=83150888503515&hvbmt=bb&hvdev=c&hvlocphy=163971&hvnetw=o&hvqmt=b&hvtargid=kwd-83151659578369%3Aloc-90&hydadcr=19424_10615781&tag=mh0b-20&ref=pd_sl_3zl9xtf6ec_b")
                webbrower.open_new_tab("https://www.flipkart.com/furniture-store")
                break
            elif "bags" in statement:
                speak("Opening the best selling websites")
                webbrowser.open_new_tab("https://www.amazon.in/gp/browse.html?node=2917430031&ref_=nav_em_sbc_sportslugg_backpacks_0_2_14_17")
                webbrowser.open_new_tab("https://www.flipkart.com/bags-wallets-belts/bags-backpacks/pr?sid=reh,4d7&q=bags&otracker=categorytree")
                webbrowser.open_new_tab("https://www.reliancedigital.in/bags-cases-sleeves/c/S101010")
                webbrowser.open_new_tab("https://www.myntra.com/handbags-and-bags")
                webbrowser.open_new_tab("https://meesho.com/bags/pl/4pjvf")
                break
            elif "toys" in statement:
                speak("Opening the best selling websites")
                webbrowser.open_new_tab("https://www.amazon.in/gp/browse.html?node=1350380031&ref_=nav_em_sbc_tbk_toys_games_0_2_15_2")
                webbrowser.open_new_tab("https://www.flipkart.com/toysclp-store?otracker=nmenu_sub_Baby%20%26%20Kids_0_Toys")
                webbrowser.open_new_tab("https://www.meesho.com/kids-playing-toys/p/6ltbr")
                webbrowser.open_new_tab("https://www.myntra.com/toys")
                break
            elif "sports" in statement:
                 speak("Opening the best selling websites")
                 webbrowser.open_new_tab("https://www.decathlon.com/")
                 webbrowser.open_new_tab("https://www.amazon.in/s?k=sports&crid=3R267HFWRCPG9&sprefix=sports%2Caps%2C5992&ref=nb_sb_noss_2")
                 webbrowser.open_new_tab("https://www.flipkart.com/sports/pr?sid=abc&q=sports&otracker=categorytree")
                 break
            elif "baby" in statement or "toddler" in statement:
                speak("Opening the best selling websites")
                webbrowser.open_new_tab("https://www.amazon.in/s?k=baby&rh=n%3A1571274031&dc&ds=v1%3Ajms0Gl96QXoIf7sge63yOOn3juFeD7LUdkf0zLU6xPo&crid=3UV7Y1U4Z0MRO&qid=1661508923&rnid=3576079031&sprefix=bab%2Caps%2C855&ref=sr_nr_n_1")
                webbrowser.open_new_tab("https://www.firstcry.com/")
                webbrowser.open_new_tab("https://www.flipkart.com/search?q=baby&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")
                break
            elif "health" in statement or "medicine" in statement:
                speak("Opening the best websites")
                webbrowser.open_new_tab("https://www.netmeds.com/")
                webbrowser.open_new_tab("https://www.apollopharmacy.in/?campaignid=424652229&adgroupid=1361196886287324&keyword=netmeds&device=c&adtype=&product_id=&msclkid=873006d831f41106218d65d099a7d766&utm_source=bing&utm_medium=cpc&utm_campaign=Apollo_Non-Brand_Pharmacy_Competitors_Same_Day&utm_term=netmeds&utm_content=Netmeds")
                webbrowser.open_new_tab("https://pharmeasy.in/")
                break
            elif "holiday" in statement or "vacation" in statement:
                speak("Opening the best selling websites")
                webbrowser.open_new_tab("https://www.trivago.in/?__wr=21&tc=102&themeId=280&sem_keyword=trivago&sem_creativeid=72636688147314&sem_matchtype=be&sem_network=o&sem_device=c&sem_campaignid=191340818&sem_adgroupid=3930406455&sem_targetid=40966707859&cipc=br&cip=9119110005&msclkid=c2e50849f2bd17216b0d6b413beac8")
                webbrowser.open_new_tab("https://www.oyorooms.com/")
                webbrowser.open_new_tab("https://www.airbnb.co.in/a/stays/?account_id=31003615&campaign_id=303117718&ad_id=80951624440020&ad_group_id=1295224714906336&keyword_id=kwd-80951555865320:loc-90&device=c&c=.pi2.pk303117718_1295224714906336&ghost=true&msclkid=676cc188ecb31350eaa8a28026822a5e&utm_source=bing&utm_medium=cpc&utm_campaign=IND%3ADTM%3ASRC%3ABRD%2BAirbnb%5BEXACT%5D&utm_term=airbnb&utm_content=Airbnb%3A%2BExact")
            elif "travel" in statement or "trip" in statement:
                speak("Opening the best websites")
                webbrowser.open_new_tab("https://www.redbus.in/")
                webbrowser.open_new_tab("https://www.makemytrip.com/flights/?cmp=SEM|M|DF|B|Brand|B_M_Makemytrip_Search_Exact|Brand_Top_5_Exact|Expanded|&s_kwcid=AL!1631!3!!e!!o!!makemytrip&ef_id=98c902a0be941851198c61a8744cfc24:G:s")
            elif "skin care" in statement or "beauty" in statement:
                speak("Opening the best selling websites")
                webbrowser.open_new_tab("https://www.amazon.in/s?k=skin+care&rh=n%3A1374407031&ref=nb_sb_noss")
                webbrowser.open_new_tab("https://www.nykaa.com/skin/c/8377")
                webbrowser.open_new_tab("https://www.myntra.com/skin-care?f=gender%3Amen%20women%2Cwomen")
                break
            elif "shoes" in statement or "boots" in statement:
                speak("Opening the best selling websites")
                webbrowser.open_new_tab("https://www.amazon.in/shoes/s?k=shoes")
                webbrowser.open_new_tab("https://www.myntra.com/shoes")
                webbrowser.open_new_tab("https://www.flipkart.com/q/shoes")
                break
            elif "footwear" in statement:
                speak("Opening the best selling websites")
                webbrowser.open_new_tab("https://meesho.com/footwear/pl/mq5ta")
                webbrowser.open_new_tab("https://www.amazon.in/footwear/s?k=footwear")
                webbrowser.open_new_tab("https://www.flipkart.com/footwear/pr?sid=osp")
                webbrowser.open_new_tab("https://www.myntra.com/footwear")
                break
            elif "camera" in statement:
                speak("Opening the best selling websites")
                webbrowser.open_new_tab("https://www.flipkart.com/cameras/pr?sid=jek,p31&otracker=categorytree")
                webbrowser.open_new_tab("https://www.croma.com/cameras-accessories/professional-cameras/c/548")
                webbrowser.open_new_tab("https://www.amazon.in/camera-photography/b?ie=UTF8&node=1388977031")
                webbrowser.open_new_tab("https://www.reliancedigital.in/cameras/c/S1011")
                break
            elif "watches" in statement or "watch" in statement:
                speak("Opening the best selling websites")
                webbrowser.open_new_tab("https://www.reliancedigital.in/wearable-technology/c/S101722")
                webbrowser.open_new_tab("https://www.amazon.in/Watches/b?ie=UTF8&node=1350387031")
                webbrowser.open_new_tab("https://www.flipkart.com/watches/pr?sid=r18")
                webbrowser.open_new_tab("https://www.myntra.com/watches")
                break
            elif "stop" in statement:
                speak("Thank you")
                break
import tkinter
from tkinter import *
import tkinter.font as tkFont
window=Tk()
window.attributes("-fullscreen",True)
window.configure(bg="purple")
label1=Label(window,text="SHOPPING ASSISTANT",font=("Bold Italic",60),padx=65,pady=65,bg="light blue").pack()
Button1=Button(window,text="LAUNCH",font=("Italic",30),padx=50,pady=50,bg="light green",command=shopping_assistant).pack(side=LEFT)
Button2=Button(window,text="STOP",font=("Italic",30),padx=50,pady=50,bg="light green",command=window.destroy).pack(side=RIGHT)
img=PhotoImage(file="img.png")
label2=Label(window,image=img,padx=25,pady=25).pack()
window.mainloop()
