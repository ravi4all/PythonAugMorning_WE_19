Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> for i in range(5):
	print(i)

	
0
1
2
3
4
>>> for i in range(5):
	print(i,end='')

	
01234
>>> for i in range(5):
	print(i,end=' ')

	
0 1 2 3 4 
>>> import datetime
>>> datetime.datetime.now()
datetime.datetime(2019, 8, 25, 12, 57, 55, 195291)
>>> datetime.datetime.now().date()
datetime.date(2019, 8, 25)
>>> datetime.datetime.now().time()
datetime.time(12, 58, 18, 588165)
>>> from datetime import datetime
>>> datetime.now()
datetime.datetime(2019, 8, 25, 12, 58, 57, 589638)
>>> date = datetime.now().date()
>>> print(date)
2019-08-25
>>> date.strftime("%d/%m/%y")
'25/08/19'
>>> date.strftime("%d/%m/%y,%p")
'25/08/19,AM'
>>> date.strftime("%d/%m/%y,%a")
'25/08/19,Sun'
>>> date = datetime.now().time()
>>> time = datetime.now().time()
>>> print(time)
13:00:46.335819
>>> time.strftime("%H:%M:%S,%p")
'13:00:46,PM'
>>> import calendar
>>> calendar.month(2019,8)
'    August 2019\nMo Tu We Th Fr Sa Su\n          1  2  3  4\n 5  6  7  8  9 10 11\n12 13 14 15 16 17 18\n19 20 21 22 23 24 25\n26 27 28 29 30 31\n'
>>> print(calendar.month(2019,8))
    August 2019
Mo Tu We Th Fr Sa Su
          1  2  3  4
 5  6  7  8  9 10 11
12 13 14 15 16 17 18
19 20 21 22 23 24 25
26 27 28 29 30 31

>>> print(calendar.calendar(2019))
                                  2019

      January                   February                   March
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
    1  2  3  4  5  6                   1  2  3                   1  2  3
 7  8  9 10 11 12 13       4  5  6  7  8  9 10       4  5  6  7  8  9 10
14 15 16 17 18 19 20      11 12 13 14 15 16 17      11 12 13 14 15 16 17
21 22 23 24 25 26 27      18 19 20 21 22 23 24      18 19 20 21 22 23 24
28 29 30 31               25 26 27 28               25 26 27 28 29 30 31

       April                      May                       June
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
 1  2  3  4  5  6  7             1  2  3  4  5                      1  2
 8  9 10 11 12 13 14       6  7  8  9 10 11 12       3  4  5  6  7  8  9
15 16 17 18 19 20 21      13 14 15 16 17 18 19      10 11 12 13 14 15 16
22 23 24 25 26 27 28      20 21 22 23 24 25 26      17 18 19 20 21 22 23
29 30                     27 28 29 30 31            24 25 26 27 28 29 30

        July                     August                  September
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
 1  2  3  4  5  6  7                1  2  3  4                         1
 8  9 10 11 12 13 14       5  6  7  8  9 10 11       2  3  4  5  6  7  8
15 16 17 18 19 20 21      12 13 14 15 16 17 18       9 10 11 12 13 14 15
22 23 24 25 26 27 28      19 20 21 22 23 24 25      16 17 18 19 20 21 22
29 30 31                  26 27 28 29 30 31         23 24 25 26 27 28 29
                                                    30

      October                   November                  December
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
    1  2  3  4  5  6                   1  2  3                         1
 7  8  9 10 11 12 13       4  5  6  7  8  9 10       2  3  4  5  6  7  8
14 15 16 17 18 19 20      11 12 13 14 15 16 17       9 10 11 12 13 14 15
21 22 23 24 25 26 27      18 19 20 21 22 23 24      16 17 18 19 20 21 22
28 29 30 31               25 26 27 28 29 30         23 24 25 26 27 28 29
                                                    30 31

>>> import os
>>> os.getcwd()
'C:\\Python37'
>>> os.chdir("C:\Users\asus\Music")
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> os.chdir(r"C:\Users\asus\Music")
>>> os.getcwd()
'C:\\Users\\asus\\Music'
>>> os.listdir()
['5-Varlaam Varlaam Vaa-SenSongsMp3.Co.mp3', 'BIGGEST BASS DROP EVER! (EXTREME BASS TEST!!!).mp3', 'Billian-Billian-Guri.mp3', 'Cristiano Ronaldo - Faded Best Moments 2017 • 100.000 Subscribers.mp3', 'desktop.ini', 'Dub Theri Step with Lyrics   Theri   Vijay, Samantha, Amy Jackson   Atlee   G.V.Prakash Kumar.ogg', 'Ek Pal Ka Jeena-(Mr-Jatt.com).mp3', 'Kaththi Theme…The Sword of Destiny - Full Audio.ogg', 'music_1.ogg', 'Na Ja.mp3', 'Shape of You.mp3', 'Street Fighter V Soundtrack - Main Menu.ogg', "Street Fighter V Soundtrack - Ryu's Theme.ogg", 'StreetFighter.mp3', 'Vedalam - The Theri Theme Lyric   Ajith Kumar, Shruti Haasan   Anirudh.ogg']
>>> import random
>>> song = random.choice(os.listdir())
>>> os.startfile(song)
>>> import glob
>>> glob.glob('*.mp3')
['5-Varlaam Varlaam Vaa-SenSongsMp3.Co.mp3', 'BIGGEST BASS DROP EVER! (EXTREME BASS TEST!!!).mp3', 'Billian-Billian-Guri.mp3', 'Cristiano Ronaldo - Faded Best Moments 2017 • 100.000 Subscribers.mp3', 'Ek Pal Ka Jeena-(Mr-Jatt.com).mp3', 'Na Ja.mp3', 'Shape of You.mp3', 'StreetFighter.mp3']
>>> os.system('notepad')
0
>>> 
