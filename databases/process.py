log_file = open("um-server-01.txt") #This is opening the um-server-01.txt


def sales_reports(log_file):  #a function is started and it is going to be in log_file whitch is = to the .txt above
    for line in log_file:     #a for loop is started in the log_file meaning the .txt
        line = line.rstrip() #line is going to = line.rstrip and rstrip means rstrip() method removes any trailing characters (characters at the end a string), space is the default trailing character to remove.
        day = line[0:3]    #day now = line.rstrip
        if day == "Mon":  #if day == Tue whitch is the equavalnt to const in java
            print(line)   #basicly console.log if it is Tue


sales_reports(log_file)  #this is just telling it to run the function
