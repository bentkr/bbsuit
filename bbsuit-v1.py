#!/usr/bin/python3.6
### Meine imports ###
import time
import os
import sys

### Meine Klasse + Vars ###
class MariaBackup:
    username = "root"
    password = "qwe123"
    hostname = "localhost"
    database = "pythontest"
    datum = time.strftime('%Y-%m-%d')
    pfad = "/home/bent-root/Dokumente/python3/backups/"
    bkname = ("Backup-" + database + "-" + datum)

### Meine Backup Funktion ###
    def backupit(self):
        os.popen("mysqldump -u %s -p%s -h %s -e --opt -c %s | gzip -c > %s%s.zip" % (self.username, self.password, self.hostname, self.database, self.pfad, self.bkname))

    def speaker(self):
        sys.stdout.write("Das Backup Script wurde erfolgreich ausgeführt\n")
        sys.stdout.write("Das Backup befindet sich unter: \n")
        print(self.pfad)

### Erstellen einer Instanz um auf u.A Vars und Funktion zuzugreifen ###
instanz1 = MariaBackup()

### Aufruf der Funktion backupit ###
instanz1.backupit()
instanz1.speaker()
