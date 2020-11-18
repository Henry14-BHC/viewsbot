# viewsbot
it's a framework to have bot views in YouTube. Instructions are given. Have fun to code.


i developed this using python.

line 1: i have downloaded and imported selenium webdriver from that i imported driver to my project.
(you need to download using pip in cmd and for sure need chromium driver in order to access chrome browse.There are different drivers for different browsers)
line 2: i've imported time to sleep my program to pause , for video to end in this program
line 3: used for loop to play this no. of times as we want . i did it for 2 times if you want to do more than that just change the range (0,2) to (0, NO. OF TIMES YOU WANT)
line 4 & 5 : i've set my browser to open in logged in status. if this line is excluded the browser will open in unsigned status.
line 7  : to open chrome there i accessed chromium driver with help of webdriver. and option  is mentioned to open the browser in logged in status.
line 8 : inorder to search in the browser the bot have to identify the searchbox so with the help of webdriver it finds the searchbox by xpath(it can be find in inspect in chrome)
line 9  : the searchbox become active. for the next step bot has to type the key word, so i used send_keys function in  driver to induced the keyword  
line 11 : to search the keyword entered i used the same procedure as in line 8
line 12 : search button becomes active to click it i used click function in driver
line 14,15 : opened the result i want and clicked it
line 17 : i put my program to sleep for 100 sec as the video length (change the no. 100 to your requirment)
line 18: i closed the browswer after the video played completly

and the loop goes on untill the range is completed

line 19: i quit the driver cause my task is performed and satisfied me and i dony want to run the driver in the background


thank you!!!!!!!
