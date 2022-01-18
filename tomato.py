import webbrowser
import time

if __name__ == '__main__':
    total_breaks = 20
    break_count=0

    webbrowser.open("file:///Users/i312177/githubP/stock-overview/index.html")
    while(break_count<total_breaks):
        time.sleep(60*55)
        webbrowser.open("file:///Users/i312177/githubP/stock-overview/index.html")
        time.sleep(60*5)
        break_count+=1
