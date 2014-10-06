import time
import glob
import fnmatch 
import urllib
####################################################
# SAVE MOST RECENT http://lastrewind.com/wp-content/uploads/2014/07/ as HTML page somewhere
####################################################
htmlFile = '/Users/danielmsheehan/GitHub/phish_lastrewind_scrape/lastrewind201409.html' #Save the HTML file of last rewind's word press content pages http://lastrewind.com/wp-content/uploads/2014/07/ and then pull it in
####################################################
# MODIFY FOLDER LOCATION OF WHERE YOU WANNA SAVE MP3's
####################################################
mp3SaveLocation = '/Users/danielmsheehan/Desktop/phish/' #this is where you want to save the friggin mp3's yo
####################################################
# MODIFY LIST OF DATES
####################################################
#YYMMDD This is not a 'list' as it actually doesn't loop through correctly if it has two items, gotta fix it but, meh.
listofDates = ['140831']

##########################phish##########################
# Shouldn't have to modify anything below here
####################################################
f = open(htmlFile,'r')

listofTunes = [] #create empty intermediate list of tunes
finalListofTunes = [] #create empty list to be final list of Tunes, yo

for date in listofDates: #this code grabs all the lines with .mp3 in them. Vlad the Impaler
	print date
	for line in f.readlines():
	    #if fnmatch.fnmatch(line, '*ph'+date+'*.mp3*'):
	    if fnmatch.fnmatch(line, '*.mp3*'):
	    	line = line.replace('<li><a href="','').replace('</a></li>','').replace('> ','').replace("\n",'').replace('http://lastrewind.com/wp-content/uploads/2014/09/','')#.replace('"','')
	    	listofTunes.append(line)
	    else:
	    	print '-' #print - if nothing in line has .mp3

for element in listofTunes:
    parts = element.split('"') #split the list items b/c each tune is listed twice
    parts = parts[0] #each tune is listed twice so only keep the first 
    finalListofTunes.append(parts)

print finalListofTunes #this is the final list of tunes
print 'Downloads beginning.......'
for i in finalListofTunes: #This grabs and downloads the content
	mp3Address = "http://lastrewind.com/wp-content/uploads/2014/07/"+i
	mp3Address = "http://lastrewind.com/wp-content/uploads/2014/08/"+i
	mp3Address = "http://lastrewind.com/wp-content/uploads/2014/09/"+i
	urllib.urlretrieve(mp3Address, mp3SaveLocation+i)
	print i + ' is downloading........'
	time.sleep(15) # delays for 15 seconds, not trying to bring down the web site.


#TO DO 

#1 add zip and copy to dropbox ZipFile
#2 add to iTunes
#3 timer delay morning start
