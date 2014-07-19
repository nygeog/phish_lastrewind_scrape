import time
import glob
import fnmatch 
import urllib

htmlFile = '/Users/danielmsheehan/GitHub/phish_lastrewind_scrape/lastrewind2.html'

f = open(htmlFile,'r')

listofTunes = []

#YYMMDD
#listofDates = ['140716']
#listofDates = ['140712']
#listofDates = ['140426']
listofDates = ['140718']

finalListofTunes = []

for date in listofDates:
	print date
	for line in f.readlines():
	    #print line
	    if fnmatch.fnmatch(line, '*ph'+date+'*.mp3*'):
	    	line = line.replace('<li><a href="','').replace('</a></li>','').replace('> ','').replace("\n",'')#.replace('"','')
	    	listofTunes.append(line)
	    else:
	    	print '-'

#print listofTunes

for element in listofTunes:
    parts = element.split('"')
    parts = parts[0]
    finalListofTunes.append(parts)

print finalListofTunes
print 'Downloads beginning.......'
for i in finalListofTunes:
	mp3Address = "http://lastrewind.com/wp-content/uploads/2014/07/"+i
	urllib.urlretrieve(mp3Address, '/Users/danielmsheehan/Desktop/phish/'+i)
	print i + ' is downloading........'
	time.sleep(15) # delays for 15 seconds