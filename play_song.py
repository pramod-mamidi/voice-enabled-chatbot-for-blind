from selenium import webdriver
from bs4 import BeautifulSoup as bs
import requests as r
import time
import bot
import keyboard
driver=webdriver.Chrome("chromedriver")
def spawn_program_and_die(program, exit_code=0):
    subprocess.Popen(program)
    sys.exit(exit_code)
def song(n):
    driver.get('https://wynk.in/music/detailsearch/'+n)
    s=driver.find_element_by_css_selector('#SONG_smoothScroll > li:nth-child(1) > div.railContent.w-100.float-left.pt-2 > a')
    href=s.get_attribute('href')
    print(href)
    driver.get(href)
    try:
        button=driver.find_element_by_xpath('/html/body/app-root/app-home/div[2]/div/song-info/div/div[1]/div[3]/div[2]/div[1]/button[1]')
        button.click()
    except:
        time.sleep(4)
        button=driver.find_element_by_xpath('/html/body/app-root/app-home/div[2]/div/song-info/div/div[1]/div[3]/div[2]/div[1]/button[1]')
        button.click()
    while True:
        try:
            if keyboard.is_pressed('q'):
                #driver.quit()
                spawn_program_and_die(['python','home2.py'])
                break
        except:
            break
song(bot.n)
