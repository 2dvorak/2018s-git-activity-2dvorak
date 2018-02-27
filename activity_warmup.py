import sys
import csv
import random

# reads csv file(argv[1])
def read_csv(csv_filename):
	with open(csv_filename,'r') as csvfile:
		# detect delimeter
		dialect = csv.Sniffer().sniff(csvfile.read())

		csvfile.seek(0)
		
		# parse csv and return a list of names
		csvreader = csv.reader(csvfile, dialect)
		name_list = list()
		for row in csvreader:
			name_list.append(row[0])
		
		return name_list

# shuffle name_list and divide into groups
# group size less than max_num(argv[2])
def shuffle(name_list, max_num):
	# how many groups?
	group_num = len(name_list) / max_num
	if len(name_list) % max_num != 0:
		group_num += 1
	
	# shuffle name_list
	random.shuffle(name_list)
	
	# list of group
	# each group is a list of names
	group_list = list()
	
	# allocated shuffled names into group
	for i in range(len(name_list)):
		# first create each group's name list
		if i < group_num:
			group_list.append([name_list[i]])
		else:
			group_list[i % group_num].append(name_list[i])
	
	return group_list

# main function
def main():
	# check arguments
	if len(sys.argv) < 3:
		print "Usage : {0} [CSV_FILE] [MAX_MEMBER_PER_GROUP]".format(sys.argv[0])
		return
	else:
		# check argv[2]
		try:
			# argv[2] less than 1
			if int(sys.argv[2]) < 1:
				print "Invalid MAX_MEMBER_PER_GROUP value : should be greater than 0"
			
			# everything looks fine, good to go
			else:
				name_list = read_csv(sys.argv[1])
				group_list = shuffle(name_list, int(sys.argv[2]))
				for i, group in enumerate(group_list):
					print "GROUP {0} :".format(i + 1),
					for name in group:
						print "'" + name + "'",
					print
					
		except Exception as ex:
			# in case argv[2] not an integer
			if type(ex).__name__ == "ValueError":
				print "Invalid MAX_MEMBER_PER_GROUP value : should be integer"
			# in case IOError. Likely typo in file name
			elif type(ex).__name__ == "IOError":
				print "IOError occured. Check your csv file name. Any typos?"
			else:
				print "Unexpected exception ocured.\n{0}: {1}".format(type(ex).__name__, ex)

# imported?
if __name__ in '__main__':
	main()
