import webbrowser
import time

i =0;
print("This started"+time.ctime());
while(i<3):
    time.sleep(3)
    webbrowser.open("https://www.youtube.com/watch?v=0Bk4Bjgji4c",new=1,autoraise='true')
    i = i+1;
