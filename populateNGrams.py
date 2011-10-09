import redis, os, sys

def verify():
	if len(sys.argv) == 1:
		print 'Usage: python populateNGrams.py /path/to/NGram/data'
		sys.exit()

def populate():
	rs = redis.Redis('localhost')
	topdirs = [d for d in os.listdir(sys.argv[1])]
	for topdir in topdirs:
		currDir = os.path.join(os.path.abspath(sys.argv[1]), topdir)
		if topdir == '1gms':
			pass
			# fsock = open(currDir + '/vocab', 'r')
			# print 'Processing 1gms/vocab'
			# for line in fsock:
			#	frags = line.split()
			#	rs.zadd('en:1gms', frags[0], frags[1])
		else:
			os.chdir(os.path.abspath(currDir))
			filesOfInterest = [f for f in os.listdir(os.getcwd()) if 'gm-' in f]
			for f in filesOfInterest:
				fsock = open(f, 'r')
				print 'Processing %s/%s' % (topdir, f)
				for line in fsock:
					frags = line.split()
					fName = 'en:%s' % topdir
					rs.zadd(fName, ' '.join(frags[:-1]), frags[-1])			
				
			

verify()
populate()	

