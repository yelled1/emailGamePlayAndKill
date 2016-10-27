#!/usr/bin/python
# by mailhyoon@gmail.com S. H. Yoon
# This script kills attempts to launch MindelessCraft
# Without an email from Mom or Dad
# Below is how to put on : sudo crontab -e
# 2,7,12,17,22,27,32,37,42,47,52,57 * * * * sleep 54 ; /usr/bin/python /home/MyHome/tRestrictor.py >> /tmp/Killer.log 2>&1 &
# sudo apt-get install python-dateutil # run this on terminal
import email, imaplib #, time, rfc822
import psutil, subprocess, signal, re
import datetime as D
from   dateutil import parser, tz
from   RestrictSrc import SrcDict

def Killer(minSince, Dte, playMin=44.):    
    if minSince > playMin: # only kill if playMin is not over 45min in above case
        print 'Kill Time:\t%12.2f mins %12.2f hrs\tlastEmail: %s'  %(minSince, minSince/60., Dte)
        for proc in psutil.process_iter():
            if proc.name.lower() == 'java': 
                for each in proc.cmdline:
                    if 'minecraft' in each.lower():
                        print '\tkilling|%s|%s' %(proc.name, each[:60])
                        proc.kill()
            if re.search('steam', proc.name.lower()) > 0:
                print '\tkilling|%s' %(proc.name)
                proc.kill()
    print 'All Done:\t%12.2f mins %12.2f hrs\tlastEmail: %s'  %(minSince, minSince/60., Dte)
    return

utc_zone = tz.gettz('UTC')
ctm  = D.datetime.now(utc_zone)
cdte = D.datetime.now().strftime('%d-%b-%Y')
chrm = D.datetime.now().strftime('%H:%M')

if map(lambda x: x.name.lower(), psutil.process_iter()).count('java')  == 0 and \
   map(lambda x: x.name.lower(), psutil.process_iter()).count('steam') == 0:
    print 'No java or Steam activity v8.2 at %s     %s' %(cdte, chrm)
    exit()
 
# You have setup a IMAP enabled account / gmail works ok but zoho is better
imp = SrcDict['imp']
usr = SrcDict['usr']
pwd = SrcDict['pwd']
sendr1  = SrcDict['sendr1']
sendr2  = SrcDict['sendr2']

# connecting to the IMAP server
m = imaplib.IMAP4_SSL(imp)
m.login(usr,pwd)
m.select("INBOX") # use m.list() to get all the mailboxes
 
searStr     = """((SENTSINCE "%s") (OR (FROM "%s") (FROM "%s")))""" %(cdte, sendr1, sendr2)
resp, items = m.search(None, searStr)
items = items[0].split() # getting the mails id
if len(items) == 0:  # if no email found then just kill minecraft
    print "No Mail Found Just Kill it!"
    Killer(999, "Auto Kill NO Mail found")
    exit()
for emailid in items: # Ok email found
    resp, data = m.fetch(emailid, "(RFC822)") 
    email_body = data[0][1] # getting the mail content
    mail = email.message_from_string(email_body) # parsing the mail content to get a mail object
    #if mail.get_content_maintype() != 'multipart': continue
    frm = mail["From"]
    sub = mail["Subject"]
    dte = mail["date"]
    btm = parser.parse(dte).astimezone(utc_zone)
    dtm = ctm-btm
    print "%-37s %-12s\t%s\t%8.2f" %(frm, sub, dte, dtm.total_seconds()/60.)
Killer(dtm.total_seconds()/60., dte)
