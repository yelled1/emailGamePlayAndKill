# emailGamePlayAndKill
Restrict my son's games (mindlesscraft &amp; steam) to 45~min after an email from mom/dad in Python

THIS has been updated with rEstrictore.py script to reflect 2.7 upgrade on Ubuntu 14.04 LTS / works on 16.04 LTS as well

This was tested under Ubuntu 14 & 16
Unfortunately, I cannot give you too much help if something is not working. I will try but may or may not help.

Restrictor has a email account that gets emails from mom & dad (sender1 & sender2)

SrcDict = { 
    'imp' : "imap.zoho.com",         # Look this up from email provider or just create an account that zoho for free
    'usr': 'myGameBoyy@zoho.com',    # My son's account number
    'pwd': 'passmePls',              # email to the account
    'sendr1' : "<restrictiveMom@yahoo.com>", # this is mom's account 
    'sendr2' : "<gameCrasherDad@gmail.com>"  # this is dad's account
}
# above email names (copy it from email from zoho account after sending a test mail)

And setup a crontab by crontab -e: with root privileages
# 2,7,12,17,22,27,32,37,42,47,52,57 * * * * sleep 54 ; /usr/bin/python $HOME/rEstrictore.py >> /tmp/Killer.log 2>&1 &
Obviously do NOT let your child get hold of root privileges
after that, check the log file
tmp/Killer.log
No java or Steam activity v8.2 at 27-Oct-2016     15:27
No java or Steam activity v8.2 at 27-Oct-2016     15:32
No java or Steam activity v8.2 at 27-Oct-2016     15:37
No java or Steam activity v8.2 at 27-Oct-2016     15:42
No java or Steam activity v8.2 at 27-Oct-2016     15:47
If you see that, then your good. 
Send a test email. You will see updated msges.
