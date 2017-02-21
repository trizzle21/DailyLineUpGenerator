import urllib.request

urllist = []


for i in sys.argv:
	urllist.push('https://sports.yahoo.com/dailyfantasy/api/resource/dailyfantasy.players;contestId='+ sys.argv)


for contest in urllist:	
	with urllib.request.urlopen(contest) as response:
   		json = response.read()
