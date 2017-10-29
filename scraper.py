
import urllib2
import LawnetCaseContentFinder
import csv
import loger

counter = 0
start_point = loger.get_current_index()
with open('cases_links.csv', 'rb') as f:
    reader = csv.reader(f)
    for link in reader:
        counter = counter + 1
        if counter >= start_point:
            try:
                page_content = urllib2.urlopen(link[0])
                case = LawnetCaseContentFinder.Case(page_content)
                loger.write(case.get_file_slug(), case.get())
                print counter
                loger.log_current_index(str(counter))
            except IndexError:
                print "Not readable content"
                loger.log_ignored_case(link[0])
                loger.log_current_index(str(counter))

        else:
            print "."
