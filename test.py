import bs4, requests

with open("listings.txt", "wb") as f:
	res = requests.get("https://tampa.craigslist.org/search/sss?query=vintage%20bicycle&sort=rel").text.encode('ascII', 'ignore')
	f.write(res)

f = open("listings.txt")
f = f.read()

soup = bs4.BeautifulSoup(f, "html.parser")

times = soup.find_all("time", "result-date")

descriptions = soup.find_all("a", "result-title")

neighborhoods = soup.find_all("span", "result-hood")

area, desc, dates = [], [], []

with open("output.txt", "w+") as o:
	for z in times:
		x = z.getText()
		dates.append(x)
	
	for d in descriptions:
		t = d.getText()
		l = d["href"]
		dl = t + " " + l + " " + "\n"
		desc.append(dl)
	
	for n in neighborhoods:
		n = n.getText()
		area.append(n)
	
	for a, b, c in zip(dates, desc, area):
		output = a + "\n" + b + "\n" + c + "\n\n"
		o.write(output)
