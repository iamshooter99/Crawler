import pandas as pd
import requests
from bs4 import BeautifulSoup
result=requests.get("https://dmoz-odp.org/Sports/Events/")
print(result.status_code)
parsed=BeautifulSoup(result.content,"html.parser")
subcategories=parsed.find(id='subcategories-div')
Event=subcategories.find_all(class_='browse-node')
Event_link=subcategories.find_all("a")
Event_titles=[" ".join(Events.get_text().strip().replace("  ","").split()) for Events in Event]
Event_links=[str(linkEvent).split('"')[1] for linkEvent in Event_link]
title_10=[]
link_10=[]
for i in range(0,10):
	title_10.append(Event_titles[i])
	link_10.append(Event_links[i])

list=pd.DataFrame({'Title': title_10,'Links':link_10})
list.to_csv("lists.csv")
