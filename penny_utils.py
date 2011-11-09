import csv
import urllib
import random
from matplotlib import pyplot
#import dhtml
image_file = dhtml.join_path(crunchy.temp_dir, "graph.png")

import csv, urllib

def load_csv(url):
    d = {}
    fp = urllib.urlopen(url)
    #print 'this is fp', fp                                                   
    for row in csv.DictReader(fp):
        key = row['date']
        value = row['fish']

        x = d.get(key, [])                                                    
        x.append(value)                                                  
        d[key] = x                                                  
    return d                                                           

def make_dates_dict(fish_d):
    fishy_listy = []
    dates_d = {}                                        
    for name in fish_d:
        for x in fish_d[name]:
            key = x
            fishy_listy = dates_d.get(key, [])
            fishy_listy.append(name)
            fishy_set = set(fishy_listy)
            fishy_list = list(fishy_set)
            dates_d[key] = fishy_list
    #print 'this is dates_d', dates_d
    return dates_d

def get_fishes_by_date(fish_d, date):
  fishlist = []
  for i in date:
  	#print 'i in date', i
  	for keys in fish_d:
  		#print 'keys in fish_d', fish_d
    		if keys == i:	
        		#print 'keys ==i', i
        		fishlist.append(len(fish_d[keys]))
        		#print 'lenght of fish_d[keys]', len(fish_d[keys])
        		#print 'fishlist', fishlist
        		#print "length", len(fishlist)
        		#number_o_fish.append(len(fishlist))
        		#print 'this is number_o_fish', number_o_fish
     		else:
        #print 'EPIC FAIL'
        		pass 
     #print 'this is the fish by date', fishlist
  return fishlist

fish_d = load_csv('https://raw.github.com/ctb/edda/master/doc/beacon-2011/tutorial5/fishies.csv')
#small fish
#fish_d = load_csv('https://raw.github.com/ctb/edda/master/doc/beacon-2011/tutorial5/fishies-short.csv')
dates_d = make_dates_dict(fish_d)
pie_dates = ('1/1', '1/2')
plot_this = get_fishes_by_date(fish_d, pie_dates)
print 'plot this', plot_this
pyplot.savefig(image_file)
#dhtml.image(image_file)