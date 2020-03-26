from bs4 import BeautifulSoup
from tkinter import *
from tkinter.font import Font
import requests
turn=0
#setting the window for the gui app
window=Tk()
window.geometry('580x440')
window.configure(background="#355664")
window.title("Coronavirus Update App")
#url of the website
url="https://www.worldometers.info/coronavirus/"
#taking specifically only english language
headers = {"Accept-Language": "en-US,en;q=0.5"}
response=requests.get(url,headers=headers)
data=response.text

soup=BeautifulSoup(data,"html.parser")

infos=soup.findAll("div",{"class":"maincounter-number"},"span")

#finding world infos
totalcases=infos[0].text
print("Total cases: " +totalcases)

deaths=infos[1].text
print("Total Deaths: "+deaths)

recoverd=infos[2].text
print("Total Recovered: "+recoverd)

#finding bangladesh infos
allinfos=soup.findAll("tr")
for info in allinfos:
	sub_infos=info.findAll("td")
	for sub_info in sub_infos:
		#separating only bangldesh infos
		if sub_info.text=="Bangladesh" and turn==0:
			bd_total_cases=(sub_infos[1].text)
			print(bd_total_cases)
			if(sub_infos[2]):
				bd_new_cases=sub_infos[2].text
			else:
				bd_new_cases="0"
			bd_total_deaths=sub_infos[3].text
			bd_recovered=sub_infos[5].text
			turn=1
		
print("Bangladesh Total Cases: "+bd_total_cases+ "\n"+ "Bangladesh New Cases: "+bd_new_cases+"\n"+"Bangladesh Total Deaths: "+bd_total_deaths+"\n"+"Bangladesh Total Recovered: "+bd_recovered)

#setting the font for the gui app text
my_font = Font(family="Antique Olive", size=16)

#inserting all the text in the gui app
title_label=Label(window,text="Covid 19 Update",bg="#355664",fg="white",font=my_font).pack()
world_total_cases_label=Label(window,text="World Total Cases: "+ totalcases,fg="white",bg="#355664",font=my_font).pack()
world_total_deaths_label=Label(window,text="World Total Deaths: "+ deaths,fg="white",bg="#355664",font=my_font).pack()
world_total_recovered_label=Label(window,text="World Total Recovered: " + recoverd,fg="white",bg="#355664",font=my_font).pack()
bd_total_cases_label=Label(window,text="Bangladesh Total Cases: " + bd_total_cases,fg="white",bg="#355664",font=my_font).pack()
bd_new_cases_label=Label(window,text="Bangladesh New Cases: " + bd_new_cases,fg="white",bg="#355664",font=my_font).pack()
bd_total_deaths_label=Label(window,text="Bangladesh Total Deaths: " + bd_total_deaths,fg="white",bg="#355664",font=my_font).pack()
bd_total_recovered_label=Label(window,text="Bangladesh Total Recovered: " + bd_recovered,fg="white",bg="#355664",font=my_font).pack()

window.mainloop()
			