# Convert camera response curves from the Database of Response Functions
# The input data can be gotten here:
# 	http://www.cs.columbia.edu/CAVE/software/dorf/response/dorfCurves.zip

dorfs = open('./dorfCurves.txt').readlines()

for i in range(len(dorfs)/6):
  redname = dorfs[i*6].strip('\r\n')
  if(redname[-3:] == 'Red'):
    greenname = dorfs[(i+1)*6].strip('\r\n')
    if(greenname[-5:] == 'Green'):
      bluename = dorfs[(i+2)*6].strip('\r\n')
      if(bluename[-4:] == 'Blue'):
	# We've found a set of Red/Green/Blue curves
	name = redname[:-3]
	ri = map(float, dorfs[i*6+3].strip('\r\n').split('   '))
	ro = map(float, dorfs[i*6+5].strip('\r\n').split('   '))
	gi = map(float, dorfs[(i+1)*6+3].strip('\r\n').split('   '))
	go = map(float, dorfs[(i+1)*6+5].strip('\r\n').split('   '))
	bi = map(float, dorfs[(i+2)*6+3].strip('\r\n').split('   '))
	bo = map(float, dorfs[(i+3)*6+5].strip('\r\n').split('   '))
	gio = zip(gi, go)
	if name == 'agfacolor-hdc-100-plusCD':
	  for l in gio:
	    print '%f %f' % l
