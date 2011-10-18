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
  # write code HERE to fill in fishlist
  for keys in fish_d:
     #print 'first try at keys', keys
     #print 'date?', date
     if keys == date:
        #print 'keys?', keys
        #print 'date?', date
        fishlist.append(fish_d[keys])
        #print 'this is the dates', fishlist
     else:
        #print 'EPIC FAIL'
        pass 
     #print 'this is the fish by date', fishlist
  return fishlist

def get_dates_by_fish(dates_d, fish):
   datelist = []
   for stuff in dates_d:
      #print 'stuff', stuff
      #print 'fish', fish
      if stuff == fish:
         datelist.append(dates_d[stuff])
      else:
         #print 'Fail'
         pass
   return datelist

def get_fishes_by_datelist(fish_d, input):
    datelist = []
    print 'this is input', input
    for i in fish_d:
        #print 'this is i', i
        if i == input:
            datelist.append(fish_d[i])
        else:
            pass
            #print ' slap my ass and call me sally'
    return i, datelist
            
def get_dates_by_fishlist(dates_d, inner):
    fishlist = []
    for i in dates_d:
        print 'this is i in dates_d', i
        if i == inner:
            fishlist.append(dates_d[i])
        else:
            #print 'Crap-o-la'
            pass
        return i, fishlist

#small fish
#fish_d = load_csv('https://raw.github.com/ctb/edda/master/doc/beacon-2011/tutorial5/fishies-short.csv')

#big fish
fish_d = load_csv('https://raw.github.com/ctb/edda/master/doc/beacon-2011/tutorial5/fishies.csv')

dates_d = make_dates_dict(fish_d)

#print 'this is dates_d', dates_d
#print 'this is fish_d', fish_d
print 'fishlist', get_fishes_by_date(fish_d, '1/1')
print 'datelist', get_dates_by_fish(dates_d, 'plaice')

#get_fishes_by_datelist(fish_d, datelist)
print 'new function', get_fishes_by_datelist(fish_d, '1/1')
# get_dates_by_fishlist(dates_d, fishlist)
print 'other new function', get_dates_by_fishlist(dates_d, 'plaice')
