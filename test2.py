import bs4, requests, webbrowser, smtplib#, os, ui

with open("listings.txt", "wb") as f:
	res = requests.get("https://tampa.craigslist.org/search/sss?query=vintage%20bicycle&sort=rel").text.encode('ascII', 'ignore')
	f.write(res)

f = open("listings.txt")
f = f.read()

soup = bs4.BeautifulSoup(f, "html.parser")

area, desc, dates = [], [], []

for z in soup.find_all("time", "result-date"):
	dates.append(str(z))
	
for d in soup.find_all("a", "result-title"):
	desc.append(str(d))
	
for n in soup.find_all("span", "result-hood"):
	area.append(str(n))

with open("output.html", "w+") as o:	
	for a, b, c in zip(dates, desc, area):
		output = a + "\n" + b + "\n" + c + "<br><br>"
		o.write(output)

#file = os.path.abspath("output.html")

#w = ui.WebView()

#w.load_url(file)

#w.present()

#o = open("output.html")

#info: http://naelshiab.com/tutorial-send-email-python/

#server = smtplib.SMTP('smtp.gmail.com', 587)
#server.starttls()
#server.login("matthewpleasant@gmail.com", "Great$cott83")
#msg = o.read()

#server.sendmail("matthewpleasant@gmail.com", "matthewpleasant@gmail.com", msg)
#server.quit()