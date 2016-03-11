#Plays your fav Song after every hour during office timings.
#Total 8 times

def take_a_break():
    import webbrowser
    import time
    count=1
    no_of_breaks=8
    print("start time:",time.ctime())
    while(count<=no_of_breaks):
        time.sleep(1*6*60)
        #opens your fav video after 1 hour
        webbrowser.open("https://patents.google.com/")
        count=count+1



take_a_break()
