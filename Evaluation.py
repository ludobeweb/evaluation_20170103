tablTheme = []
tablQuest = []
tablRep = []
line = ""

def fetch():
    i = 0
    with open("questions.qs","r") as qs:
        for line in qs:
            line = line.rstrip()
            if line.startswith("##"):
                tablTheme.append(line)
                tablQuest.append("")
		tablRep.append("")
		print line
                i += 1
            elif line.startswith("#"):
                tablQuest.append(line)
                tablTheme.append("")
		tablRep.append("")
		print line
                i += 1
	    elif line.startswith("-"):
	    	 tablRep.append(line)
		 tablTheme.append("")
		 tablQuest.append("")
		 print line
		 i += 1

fetch()

#print tablTheme
#print tablQuest
#print tablRep

