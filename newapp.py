from bs4 import BeautifulSoup
import requests
#url of the website
url="https://www.worldometers.info/coronavirus/"
#taking specifically only english language
headers = {"Accept-Language": "en-US,en;q=0.5"}
response=requests.get(url,headers=headers)
data=response.text

soup=BeautifulSoup(data,"html.parser")

infos=soup.findAll("div",{"class":"maincounter-number"},"span")

totalcases=infos[0].text
print("Total cases: " +totalcases)

deaths=infos[1].text
print("Total Deaths: "+deaths)

recoverd=infos[2].text
print("Total Recovered: "+recoverd)

allinfos=soup.findAll("tr")
for info in allinfos:
	sub_infos=info.findAll("td")
	for sub_info in sub_infos:
		if sub_info.text=="Bangladesh":
			bd_total_cases=(sub_infos[1].text)
			if(sub_infos[2]):
				bd_new_cases="0"
			else:
				bd_new_cases=sub_infos[2].text
			bd_total_deaths=sub_infos[3].text
			bd_recovered=sub_infos[5].text

print("Bangladesh Total Cases: "+bd_total_cases+ "\n"+ "Bangladesh New Cases: "+bd_new_cases+"\n"+"Bangladesh Total Deaths: "+bd_total_deaths+"\n"+"Bangladesh Total Recovered: "+bd_recovered)
			

			
		


# print(len(allinfos))
# for info in allinfos:
# 	if info.text=="Bangladesh":
# 		print("found")

# 	else:
# 		print("Not found")