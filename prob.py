from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import mysql.connector
from datetime import date, datetime, timedelta
#connection to mysql server
cnx = mysql.connector.connect(user='sql10380326', password='fNNmKU1TUt', host='sql10.freemysqlhosting.net', database='sql10380326')
cursor = cnx.cursor()

def connecttomysql():
    name = input()
    set_target_user = ("INSERT INTO target_user "
               "(name) "
               "VALUES (%(name)s)")   

    data_user = {
      'name': name, 
    }   
    
    cursor.execute(set_target_user, data_user)

    
    cnx.commit()
    
    cursor.close()
    cnx.close()    
     


#collectin data
def colectdata():
    options = Options()
    options.add_argument("--allow-running-insecure-content");
    options.add_argument("no-sandbox");
    options.add_argument("headless");
    options.add_argument("start-maximized");
    options.add_argument("window-size=1900,1080");
    options.add_argument("no-sandbox")
    #options.add_argument("headless")
    options.add_argument("start-maximized")
    options.add_argument("--no-sandbox");
    options.add_argument("--ignore-certificate-errors");
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36')
        
    capabilities = {
    'browserName': 'chrome',
    'chromeOptions':  {
       'useAutomationExtension': False,
       'forceDevToolsScreenshot': True,
       'args': ['--start-maximized', '--disable-infobars']
     }
    }    
        
        
        
        
        
        
        

    
    driver = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\chromedriver.exe', options=options)

    print("Digite nome de usuário")
    user = input()
    print(user)

    site = "https://porofessor.gg/pt/live/br/"

    partidaaovivo = site + user
    print(partidaaovivo)
    time.sleep(1)
    driver.get(partidaaovivo)
    driver.title
    print(driver.title)

    time.sleep(5)
    try:
        # time vermelho champions:
        top_red_champion = driver.find_element_by_xpath(
            '//*[@id="liveContent"]/div[1]/ul[2]/li[1]/div/div[2]/div[1]/div/div[1]/div[1]/img').get_attribute("alt")
        jg_red_champion = driver.find_element_by_xpath(
            '//*[@id="liveContent"]/div[1]/ul[2]/li[2]/div/div[2]/div[1]/div/div/div[1]/img').get_attribute("alt")
        mid_red_champion = driver.find_element_by_xpath(
            '//*[@id="liveContent"]/div[1]/ul[2]/li[3]/div/div[2]/div[1]/div/div[1]/div[1]/img').get_attribute("alt")
        adc_red_champion = driver.find_element_by_xpath(
            '//*[@id="liveContent"]/div[1]/ul[2]/li[4]/div/div[2]/div[1]/div/div/div[1]/img').get_attribute("alt")
        sup_red_champion = driver.find_element_by_xpath(
            '//*[@id="liveContent"]/div[1]/ul[2]/li[5]/div/div[2]/div[1]/div/div/div[1]/img').get_attribute("alt")

    except:
        print("O jogador não está em partida!")
        time.sleep(3)
        quit()

    # Comando STORE para gravar o Texto
    # TOP_red:
    txt_top_red_champion_store = open("top_red_champion.txt", "w")
    txt_top_red_champion_store.write(top_red_champion)
    txt_top_red_champion_store.close()
    txt_top_red_champion_store_r = open("top_red_champion.txt", "r")
    txt_top_red_champion_store_text_r = txt_top_red_champion_store_r.read()

    # JG_red
    txt_jg_red_champion_store = open("jg_red_champion.txt", "w")
    txt_jg_red_champion_store.write(jg_red_champion)
    txt_jg_red_champion_store.close()
    txt_jg_red_champion_store_r = open("jg_red_champion.txt", "r")
    txt_jg_red_champion_store_text_r = txt_jg_red_champion_store_r.read()
    # MID_red
    txt_mid_red_champion_store = open("mid_red_champion.txt", "w")
    txt_mid_red_champion_store.write(mid_red_champion)
    txt_mid_red_champion_store.close()
    txt_mid_red_champion_store_r = open("mid_red_champion.txt", "r")
    txt_mid_red_champion_store_text_r = txt_mid_red_champion_store_r.read()
    # ADC_red
    txt_adc_red_champion_store = open("adc_red_champion.txt", "w")
    txt_adc_red_champion_store.write(adc_red_champion)
    txt_adc_red_champion_store.close()
    txt_adc_red_champion_store_r = open("adc_red_champion.txt", "r")
    txt_adc_red_champion_store_text_r = txt_adc_red_champion_store_r.read()

    # SUP_red
    txt_sup_red_champion_store = open("sup_red_champion.txt", "w")
    txt_sup_red_champion_store.write(sup_red_champion)
    txt_sup_red_champion_store.close()
    txt_sup_red_champion_store_r = open("sup_red_champion.txt", "r")
    txt_sup_red_champion_store_text_r = txt_sup_red_champion_store_r.read()

    # time azul champions:
    top_blue_champion = driver.find_element_by_xpath(
        '//*[@id="liveContent"]/div[1]/ul[1]/li[1]/div/div[2]/div[1]/div/div[1]/div[1]/img').get_attribute("alt")
    jg_blue_champion = driver.find_element_by_xpath(
        '//*[@id="liveContent"]/div[1]/ul[1]/li[2]/div/div[2]/div[1]/div/div/div[1]/img').get_attribute("alt")
    mid_blue_champion = driver.find_element_by_xpath(
        '//*[@id="liveContent"]/div[1]/ul[1]/li[3]/div/div[2]/div[1]/div/div[1]/div[1]/img').get_attribute("alt")
    adc_blue_champion = driver.find_element_by_xpath(
        '//*[@id="liveContent"]/div[1]/ul[1]/li[4]/div/div[2]/div[1]/div/div/div[1]/img').get_attribute("alt")
    sup_blue_champion = driver.find_element_by_xpath(
        '//*[@id="liveContent"]/div[1]/ul[1]/li[5]/div/div[2]/div[1]/div/div/div[1]/img').get_attribute("alt")

# Comando STORE para gravar o Texto
    # TOP_BLUE:
    txt_top_blue_champion_store = open("top_blue_champion.txt", "w")
    txt_top_blue_champion_store.write(top_blue_champion)
    txt_top_blue_champion_store.close()
    txt_top_blue_champion_store_r = open("top_blue_champion.txt", "r")
    txt_top_blue_champion_store_text_r = txt_top_blue_champion_store_r.read()

    # JG_BLUE
    txt_jg_blue_champion_store = open("jg_blue_champion.txt", "w")
    txt_jg_blue_champion_store.write(jg_blue_champion)
    txt_jg_blue_champion_store.close()
    txt_jg_blue_champion_store_r = open("jg_blue_champion.txt", "r")
    txt_jg_blue_champion_store_text_r = txt_jg_blue_champion_store_r.read()
    # MID_BLUE
    txt_mid_blue_champion_store = open("mid_blue_champion.txt", "w")
    txt_mid_blue_champion_store.write(mid_blue_champion)
    txt_mid_blue_champion_store.close()
    txt_mid_blue_champion_store_r = open("mid_blue_champion.txt", "r")
    txt_mid_blue_champion_store_text_r = txt_mid_blue_champion_store_r.read()
    # ADC_BLUE
    txt_adc_blue_champion_store = open("adc_blue_champion.txt", "w")
    txt_adc_blue_champion_store.write(adc_blue_champion)
    txt_adc_blue_champion_store.close()
    txt_adc_blue_champion_store_r = open("adc_blue_champion.txt", "r")
    txt_adc_blue_champion_store_text_r = txt_adc_blue_champion_store_r.read()

    # SUP_BLuE
    txt_sup_blue_champion_store = open("sup_blue_champion.txt", "w")
    txt_sup_blue_champion_store.write(sup_blue_champion)
    txt_sup_blue_champion_store.close()
    txt_sup_blue_champion_store_r = open("sup_blue_champion.txt", "r")
    txt_sup_blue_champion_store_text_r = txt_sup_blue_champion_store_r.read()

    # time azul nicks:
    top_blue_nick = driver.find_element_by_xpath(
        '//*[@id="liveContent"]/div[1]/ul[1]/li[1]/div/div[1]/a')
    jg_blue_nick = driver.find_element_by_xpath(
        '//*[@id="liveContent"]/div[1]/ul[1]/li[2]/div/div[1]/a')
    mid_blue_nick = driver.find_element_by_xpath(
        '//*[@id="liveContent"]/div[1]/ul[1]/li[3]/div/div[1]/a')
    adc_blue_nick = driver.find_element_by_xpath(
        '//*[@id="liveContent"]/div[1]/ul[1]/li[4]/div/div[1]/a')
    sup_blue_nick = driver.find_element_by_xpath(
        '//*[@id="liveContent"]/div[1]/ul[1]/li[5]/div/div[1]/a')

    # STORE PARA OS NICKS azul:
    # TOP_azul:
    txt_top_blue_nick_store = open("top_blue_nick.txt", "w")
    txt_top_blue_nick_store.write(top_blue_nick.text)
    txt_top_blue_nick_store.close()
    txt_top_blue_nick_store_r = open("top_blue_nick.txt", "r")
    txt_top_blue_nick_store_text_r = txt_top_blue_nick_store_r.read()

    # JG azul:
    txt_jg_blue_nick_store = open("jg_blue_nick.txt", "w")
    txt_jg_blue_nick_store.write(jg_blue_nick.text)
    txt_jg_blue_nick_store.close()
    txt_jg_blue_nick_store_r = open("jg_blue_nick.txt", "r")
    txt_jg_blue_nick_store_text_r = txt_jg_blue_nick_store_r.read()

    # MID azul:
    txt_mid_blue_nick_store = open("mid_blue_nick.txt", "w")
    txt_mid_blue_nick_store.write(mid_blue_nick.text)
    txt_mid_blue_nick_store.close()
    txt_mid_blue_nick_store_r = open("mid_blue_nick.txt", "r")
    txt_mid_blue_nick_store_text_r = txt_mid_blue_nick_store_r.read()

    # ADC: azul:
    txt_adc_blue_nick_store = open("adc_blue_nick.txt", "w")
    txt_adc_blue_nick_store.write(adc_blue_nick.text)
    txt_adc_blue_nick_store.close()
    txt_adc_blue_nick_store_r = open("adc_blue_nick.txt", "r")
    txt_adc_blue_nick_store_text_r = txt_adc_blue_nick_store_r.read()

    # SUP azul:
    txt_sup_blue_nick_store = open("sup_blue_nick.txt", "w")
    txt_sup_blue_nick_store.write(sup_blue_nick.text)
    txt_sup_blue_nick_store.close()
    txt_sup_blue_nick_store_r = open("sup_blue_nick.txt", "r")
    txt_sup_blue_nick_store_text_r = txt_sup_blue_nick_store_r.read()








































































    # NICKS red:

    top_red_nick = driver.find_element_by_xpath(
        '//*[@id="liveContent"]/div[1]/ul[2]/li[1]/div/div[1]/a')
    jg_red_nick = driver.find_element_by_xpath(
        '//*[@id="liveContent"]/div[1]/ul[2]/li[2]/div/div[1]/a')
    mid_red_nick = driver.find_element_by_xpath(
        '//*[@id="liveContent"]/div[1]/ul[2]/li[3]/div/div[1]/a')
    adc_red_nick = driver.find_element_by_xpath(
        '//*[@id="liveContent"]/div[1]/ul[2]/li[4]/div/div[1]/a')
    sup_red_nick = driver.find_element_by_xpath(
        '//*[@id="liveContent"]/div[1]/ul[2]/li[5]/div/div[1]/a')

    # STORE PARA OS NICKS red:
    # TOP_red:
    txt_top_red_nick_store = open("top_red_nick.txt", "w")
    txt_top_red_nick_store.write(top_red_nick.text)
    txt_top_red_nick_store.close()
    txt_top_red_nick_store_r = open("top_red_nick.txt", "r")
    txt_top_red_nick_store_text_r = txt_top_red_nick_store_r.read()

    # JG red:
    txt_jg_red_nick_store = open("jg_red_nick.txt", "w")
    txt_jg_red_nick_store.write(jg_red_nick.text)
    txt_jg_red_nick_store.close()
    txt_jg_red_nick_store_r = open("jg_red_nick.txt", "r")
    txt_jg_red_nick_store_text_r = txt_jg_red_nick_store_r.read()

    # MID red:
    txt_mid_red_nick_store = open("mid_red_nick.txt", "w")
    txt_mid_red_nick_store.write(mid_red_nick.text)
    txt_mid_red_nick_store.close()
    txt_mid_red_nick_store_r = open("mid_red_nick.txt", "r")
    txt_mid_red_nick_store_text_r = txt_mid_red_nick_store_r.read()

    # ADC: red:
    txt_adc_red_nick_store = open("adc_red_nick.txt", "w")
    txt_adc_red_nick_store.write(adc_red_nick.text)
    txt_adc_red_nick_store.close()
    txt_adc_red_nick_store_r = open("adc_red_nick.txt", "r")
    txt_adc_red_nick_store_text_r = txt_adc_red_nick_store_r.read()

    # SUP red:
    txt_sup_red_nick_store = open("sup_red_nick.txt", "w")
    txt_sup_red_nick_store.write(sup_red_nick.text)
    txt_sup_red_nick_store.close()
    txt_sup_red_nick_store_r = open("sup_red_nick.txt", "r")
    txt_sup_red_nick_store_text_r = txt_sup_red_nick_store_r.read()

    # taxa de vitoria time azul com o campeão:
    top_red_win_champion = driver.find_element_by_xpath(
        '//*[@id="liveContent"]/div[1]/ul[1]/li[1]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]')
    jg_red_win_champion = driver.find_element_by_xpath(
        '//*[@id="liveContent"]/div[1]/ul[1]/li[2]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]')
    mid_red_win_champion = driver.find_element_by_xpath(
        '//*[@id="liveContent"]/div[1]/ul[1]/li[3]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]')
    adc_red_win_champion = driver.find_element_by_xpath(
        '//*[@id="liveContent"]/div[1]/ul[1]/li[4]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]')
    sup_red_win_champion = driver.find_element_by_xpath(
        '//*[@id="liveContent"]/div[1]/ul[1]/li[5]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]')
    # store

    # TOP red
    txt_top_red_win_champion = open("txt_top_red_win_champion.txt", "w")
    txt_top_red_win_champion.write(top_red_win_champion.text)
    txt_top_red_win_champion.close()
    txt_top_red_win_champion_r = open("txt_top_red_win_champion.txt", "r")
    txt_top_red_win_champion_r_text = txt_top_red_win_champion_r.read()

    # JG red

    txt_jg_red_win_champion = open("txt_jg_red_win_champion.txt", "w")
    txt_jg_red_win_champion.write(jg_red_win_champion.text)
    txt_jg_red_win_champion.close()
    txt_jg_red_win_champion_r = open("txt_jg_red_win_champion.txt", "r")
    txt_jg_red_win_champion_r_text = txt_jg_red_win_champion_r.read()

    # MID red

    txt_mid_red_win_champion = open("txt_mid_red_win_champion.txt", "w")
    txt_mid_red_win_champion.write(mid_red_win_champion.text)
    txt_mid_red_win_champion.close()
    txt_mid_red_win_champion_r = open("txt_mid_red_win_champion.txt", "r")
    txt_mid_red_win_champion_r_text = txt_mid_red_win_champion_r.read()

    # ADC red
    txt_adc_red_win_champion = open("txt_adc_red_win_champion.txt", "w")
    txt_adc_red_win_champion.write(adc_red_win_champion.text)
    txt_adc_red_win_champion.close()
    txt_adc_red_win_champion_r = open("txt_adc_red_win_champion.txt", "r")
    txt_adc_red_win_champion_r_text = txt_adc_red_win_champion_r.read()

    # SUP red

    txt_sup_red_win_champion = open("txt_sup_red_win_champion.txt", "w")
    txt_sup_red_win_champion.write(sup_red_win_champion.text)
    txt_sup_red_win_champion.close()
    txt_sup_red_win_champion_r = open("txt_top_red_win_champion.txt", "r")
    txt_sup_red_win_champion_r_text = txt_top_red_win_champion_r.read()

    # taxa de vitoria time vermelho com o campeão:
    top_red_win_champion = driver.find_element_by_xpath(
        '//*[@id="liveContent"]/div[1]/ul[2]/li[1]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]')
    jg_red_win_champion = driver.find_element_by_xpath(
        '//*[@id="liveContent"]/div[1]/ul[2]/li[2]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]')
    mid_red_win_champion = driver.find_element_by_xpath(
        '//*[@id="liveContent"]/div[1]/ul[2]/li[3]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]')
    adc_red_win_champion = driver.find_element_by_xpath(
        '//*[@id="liveContent"]/div[1]/ul[2]/li[4]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]')
    sup_red_win_champion = driver.find_element_by_xpath(
        '//*[@id="liveContent"]/div[1]/ul[2]/li[5]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]')

    # TOP RED
    txt_top_red_win_champion = open("txt_top_red_win_champion.txt", "w")
    txt_top_red_win_champion.write(top_red_win_champion.text)
    txt_top_red_win_champion.close()
    txt_top_red_win_champion_r = open("txt_top_red_win_champion.txt", "r")
    txt_top_red_win_champion_r_text = txt_top_red_win_champion_r.read()

    # JG RED

    txt_jg_red_win_champion = open("txt_jg_red_win_champion.txt", "w")
    txt_jg_red_win_champion.write(jg_red_win_champion.text)
    txt_jg_red_win_champion.close()
    txt_jg_red_win_champion_r = open("txt_jg_red_win_champion.txt", "r")
    txt_jg_red_win_champion_r_text = txt_jg_red_win_champion_r.read()

    # MID RED

    txt_mid_red_win_champion = open("txt_mid_red_win_champion.txt", "w")
    txt_mid_red_win_champion.write(mid_red_win_champion.text)
    txt_mid_red_win_champion.close()
    txt_mid_red_win_champion_r = open("txt_mid_red_win_champion.txt", "r")
    txt_mid_red_win_champion_r_text = txt_mid_red_win_champion_r.read()

    # ADC RED
    txt_adc_red_win_champion = open("txt_adc_red_win_champion.txt", "w")
    txt_adc_red_win_champion.write(adc_red_win_champion.text)
    txt_adc_red_win_champion.close()
    txt_adc_red_win_champion_r = open("txt_adc_red_win_champion.txt", "r")
    txt_adc_red_win_champion_r_text = txt_adc_red_win_champion_r.read()

    # SUP red

    txt_sup_red_win_champion = open("txt_sup_red_win_champion.txt", "w")
    txt_sup_red_win_champion.write(sup_red_win_champion.text)
    txt_sup_red_win_champion.close()
    txt_sup_red_win_champion_r = open("txt_top_red_win_champion.txt", "r")
    txt_sup_red_win_champion_r_text = txt_top_red_win_champion_r.read()

    # Kda do cara com o campeão - Time Azul:
    top_red_champion_kda = driver.find_element_by_xpath(
        '//*[@id="liveContent"]/div[1]/ul[1]/li[1]/div/div[2]/div[1]/div/div[1]/div[2]/div[2]/div[1]')
    jg_red_champion_kda = driver.find_element_by_xpath(
        '//*[@id="liveContent"]/div[1]/ul[1]/li[2]/div/div[2]/div[1]/div/div[1]/div[2]/div[2]/div[1]')
    mid_red_champion_kda = driver.find_element_by_xpath(
        '//*[@id="liveContent"]/div[1]/ul[1]/li[3]/div/div[2]/div[1]/div/div[1]/div[2]/div[2]/div[1]')
    adc_red_champion_kda = driver.find_element_by_xpath(
        '//*[@id="liveContent"]/div[1]/ul[1]/li[4]/div/div[2]/div[1]/div/div[1]/div[2]/div[2]/div[1]')
    sup_red_champion_kda = driver.find_element_by_xpath(
        '//*[@id="liveContent"]/div[1]/ul[1]/li[5]/div/div[2]/div[1]/div/div[1]/div[2]/div[2]/div[1]')

    # STORE KDA

    # TOPred
    txt_top_red_champion_kda = open("top_red_champion_kda.txt", "w")
    txt_top_red_champion_kda.write(top_red_champion_kda.text)
    txt_top_red_champion_kda.close()
    txt_top_red_champion_kda_r = open("top_red_champion_kda.txt", "r")
    txt_top_red_champion_kda_r_text = txt_top_red_champion_kda_r.read()

    # JGred
    txt_jg_red_champion_kda = open("jg_red_champion_kda.txt", "w")
    txt_jg_red_champion_kda.write(jg_red_champion_kda.text)
    txt_jg_red_champion_kda.close()
    txt_jg_red_champion_kda_r = open("jg_red_champion_kda.txt", "r")
    txt_jg_red_champion_kda_r_text = txt_jg_red_champion_kda_r.read()

    # MIDred
    txt_mid_red_champion_kda = open("mid_red_champion_kda.txt", "w")
    txt_mid_red_champion_kda.write(mid_red_champion_kda.text)
    txt_mid_red_champion_kda.close()
    txt_mid_red_champion_kda_r = open("mid_red_champion_kda.txt", "r")
    txt_mid_red_champion_kda_r_text = txt_mid_red_champion_kda_r.read()

    # ADCred

    txt_adc_red_champion_kda = open("adc_red_champion_kda.txt", "w")
    txt_adc_red_champion_kda.write(adc_red_champion_kda.text)
    txt_adc_red_champion_kda.close()
    txt_adc_red_champion_kda_r = open("adc_red_champion_kda.txt", "r")
    txt_adc_red_champion_kda_r_text = txt_adc_red_champion_kda_r.read()

    # supred
    txt_sup_red_champion_kda = open("sup_red_champion_kda.txt", "w")
    txt_sup_red_champion_kda.write(sup_red_champion_kda.text)
    txt_sup_red_champion_kda.close()
    txt_sup_red_champion_kda_r = open("sup_red_champion_kda.txt", "r")
    txt_sup_red_champion_kda_r_text = txt_sup_red_champion_kda_r.read()

    # Kda do cara com o campeão - Time Vermelho:
    top_red_champion_kda = driver.find_element_by_xpath(
        '//*[@id="liveContent"]/div[1]/ul[2]/li[1]/div/div[2]/div[1]/div/div[1]/div[2]/div[2]/div[1]')
    jg_red_champion_kda = driver.find_element_by_xpath(
        '//*[@id="liveContent"]/div[1]/ul[2]/li[2]/div/div[2]/div[1]/div/div[1]/div[2]/div[2]/div[1]')
    mid_red_champion_kda = driver.find_element_by_xpath(
        '//*[@id="liveContent"]/div[1]/ul[2]/li[3]/div/div[2]/div[1]/div/div[1]/div[2]/div[2]/div[1]')
    adc_red_champion_kda = driver.find_element_by_xpath(
        '//*[@id="liveContent"]/div[1]/ul[2]/li[4]/div/div[2]/div[1]/div/div[1]/div[2]/div[2]/div[1]')
    sup_red_champion_kda = driver.find_element_by_xpath(
        '//*[@id="liveContent"]/div[1]/ul[2]/li[5]/div/div[2]/div[1]/div/div[1]/div[2]/div[2]/div[1]')

    # STORE KDA

    # TOPRED
    txt_top_red_champion_kda = open("top_red_champion_kda.txt", "w")
    txt_top_red_champion_kda.write(top_red_champion_kda.text)
    txt_top_red_champion_kda.close()
    txt_top_red_champion_kda_r = open("top_red_champion_kda.txt", "r")
    txt_top_red_champion_kda_r_text = txt_top_red_champion_kda_r.read()

    # JGRED
    txt_jg_red_champion_kda = open("jg_red_champion_kda.txt", "w")
    txt_jg_red_champion_kda.write(jg_red_champion_kda.text)
    txt_jg_red_champion_kda.close()
    txt_jg_red_champion_kda_r = open("jg_red_champion_kda.txt", "r")
    txt_jg_red_champion_kda_r_text = txt_jg_red_champion_kda_r.read()

    # MIDRED
    txt_mid_red_champion_kda = open("mid_red_champion_kda.txt", "w")
    txt_mid_red_champion_kda.write(mid_red_champion_kda.text)
    txt_mid_red_champion_kda.close()
    txt_mid_red_champion_kda_r = open("mid_red_champion_kda.txt", "r")
    txt_mid_red_champion_kda_r_text = txt_mid_red_champion_kda_r.read()

    # ADCRED

    txt_adc_red_champion_kda = open("adc_red_champion_kda.txt", "w")
    txt_adc_red_champion_kda.write(adc_red_champion_kda.text)
    txt_adc_red_champion_kda.close()
    txt_adc_red_champion_kda_r = open("adc_red_champion_kda.txt", "r")
    txt_adc_red_champion_kda_r_text = txt_adc_red_champion_kda_r.read()

    # supRED
    txt_sup_red_champion_kda = open("sup_red_champion_kda.txt", "w")
    txt_sup_red_champion_kda.write(sup_red_champion_kda.text)
    txt_sup_red_champion_kda.close()
    txt_sup_red_champion_kda_r = open("sup_red_champion_kda.txt", "r")
    txt_sup_red_champion_kda_r_text = txt_sup_red_champion_kda_r.read()

    # Main lane - Time azul:
    top_red_mainrole = driver.find_element_by_xpath(
        '//*[@id="liveContent"]/div[1]/ul[1]/li[1]/div/div[2]/div[3]/div[1]/div[2]/div[2]/span')
    jg_red_mainrole = driver.find_element_by_xpath(
        '//*[@id="liveContent"]/div[1]/ul[1]/li[2]/div/div[2]/div[3]/div[1]/div[2]/div[2]/span')
    mid_red_mainrole = driver.find_element_by_xpath(
        '//*[@id="liveContent"]/div[1]/ul[1]/li[3]/div/div[2]/div[3]/div[1]/div[2]/div[2]/span')
    adc_red_mainrole = driver.find_element_by_xpath(
        '//*[@id="liveContent"]/div[1]/ul[1]/li[4]/div/div[2]/div[3]/div[1]/div[2]/div[2]/span')
    sup_red_mainrole = driver.find_element_by_xpath(
        '//*[@id="liveContent"]/div[1]/ul[1]/li[5]/div/div[2]/div[3]/div[1]/div[2]/div[2]/span')

    def showinfo():  # mostrar jogadores e campeoes
        print("Jogadores Time Azul:")
        print(txt_top_blue_nick_store_text_r, "-",
              txt_top_blue_champion_store_text_r, )
        print(txt_jg_blue_nick_store_text_r, "-",
              txt_jg_blue_champion_store_text_r)
        print(txt_mid_blue_nick_store_text_r, "-",
              txt_mid_blue_champion_store_text_r, )
        print(txt_adc_blue_nick_store_text_r, "-",
              txt_adc_blue_champion_store_text_r, )
        print(txt_sup_blue_nick_store_text_r, "-",
              txt_sup_blue_champion_store_text_r, )

        print("Jogadores Time Vermelho:")
        print(txt_top_red_nick_store_text_r, "-",
              txt_top_red_champion_store_text_r, )
        print(txt_jg_red_nick_store_text_r, "-",
              txt_jg_red_champion_store_text_r, )
        print(txt_mid_red_nick_store_text_r, "-",
              txt_mid_red_champion_store_text_r, )
        print(txt_adc_red_nick_store_text_r, "-",
              txt_adc_red_champion_store_text_r, )
        print(txt_sup_red_nick_store_text_r, "-",
              txt_sup_red_champion_store_text_r, )

    showinfo()

    # identificação de jogador para coleta de infomações dos ultimos 30 dias com o campeao:

    # ir para a pagina do perfil do TOPred

    def wukongtesttop():
        maybewukong = txt_top_red_champion_store_text_r
        if maybewukong == "Wukong":
            top_red_champion = "monkeyking"
            leaguegraph_main_profile_stats = "https://www.leagueofgraphs.com/pt/summoner/champions/"

            top_lane = "/top"  # aqui estão identificadas as lanes
            top_red_leaguegraph_profile = leaguegraph_main_profile_stats + \
                                           top_red_champion.lower() + "/" + "br/" + txt_jg_red_nick_store_text_r + top_lane
            driver.get(top_red_leaguegraph_profile)
            time.sleep(5)

    wukongtesttop()

    # ENTRA NO PERFIL DO TOP COM O CAMPEAO
    leaguegraph_main_profile_stats = "https://www.leagueofgraphs.com/pt/summoner/champions/"

    top_lane = "/top"  # aqui estão identificadas as lanes
    top_red_leaguegraph_profile = leaguegraph_main_profile_stats + \
                                   top_red_champion.lower() + "/" + "br/" + txt_top_red_nick_store_text_r + top_lane
    driver.get(top_red_leaguegraph_profile)
    time.sleep(5)

    print("Coletando informações de", txt_top_red_nick_store_text_r)
    # script de coleta de informações jogador, indentificação de elemento + store:
    # coleta games jogados no mês com o campeao:...
    try:
        player_gamesjogados_month = driver.find_element_by_xpath(
            '//*[@id="graphDD54"]')
        txt_top_red_gamesjogados_month = open(
            "top_red_gamesjogados_month.txt", "w")
        txt_top_red_gamesjogados_month.write(player_gamesjogados_month.text)
        txt_top_red_gamesjogados_month.close()
        txt_top_red_gamesjogados_month_r = open(
            "top_red_gamesjogados_month.txt", "r")
        txt_top_red_gamesjogados_month_text_r = txt_top_red_gamesjogados_month_r.read()
        print("Jogos com", txt_top_red_champion_store_text_r,
              "nos últimos 30 dias:", txt_top_red_gamesjogados_month_text_r)

        # coleta porcentagem de vitoria no mês com campeão
        player_wr_champion_month = driver.find_element_by_xpath(
            '//*[@id="graphDD55"]')
        txt_top_red_wr_champion_month = open(
            "txt_top_red_wr_champion_month.txt", "w")
        txt_top_red_wr_champion_month.write(player_wr_champion_month.text)
        txt_top_red_wr_champion_month.close()
        txt_top_red_wr_champion_month_r = open(
            "txt_top_red_wr_champion_month.txt", "r")
        txt_top_red_wr_champion_month_text_r = txt_top_red_wr_champion_month_r.read()
        print("Taxa de vitória:", txt_top_red_wr_champion_month_text_r)

        # taxa de vitórias em lutas em equipe mes: ...

        player_tfwr_champion_month = driver.find_element_by_xpath(
            '//*[@id="graphDD23"]')
        txt_top_red_tfwr_champion_month = open(
            "txt_top_red_tfwr_champion_month.txt", "w")
        txt_top_red_tfwr_champion_month.write(player_tfwr_champion_month.text)
        txt_top_red_tfwr_champion_month.close()
        txt_top_red_tfwr_champion_month_r = open(
            "txt_top_red_tfwr_champion_month.txt", "r")
        txt_top_red_tfwr_champion_month_text_r = txt_top_red_tfwr_champion_month_r.read()
        print("Taxa de Vitória de Team Fights",
              txt_top_red_tfwr_champion_month_text_r)

        # taxa de vitoria em 1v1: ...

        player_1v1wr_champion_month = driver.find_element_by_xpath(
            '//*[@id="graphDD24"]')
        txt_top_red_1v1wr_champion_month = open(
            "txt_top_red_1v1wr_champion_month.txt", "w")
        txt_top_red_1v1wr_champion_month.write(player_1v1wr_champion_month.text)
        txt_top_red_1v1wr_champion_month.close()
        txt_top_red_1v1wr_champion_month_r = open(
            "txt_top_red_1v1wr_champion_month.txt", "r")
        txt_top_red_1v1wr_champion_month_r_text = txt_top_red_1v1wr_champion_month_r.read()
        print("Taxa de vitória de 1v1", txt_top_red_1v1wr_champion_month_r_text)
        # taxa de participação nas lutas:

        player_tfp_champion_month = driver.find_element_by_xpath(
            '//*[@id="graphDD26"]')
        txt_top_red_tfp_champion_month = open(
            "txt_top_red_tfp_champion_month.txt", "w")
        txt_top_red_tfp_champion_month.write(player_tfp_champion_month.text)
        txt_top_red_tfp_champion_month.close()
        txt_top_red_tfp_champion_month_r = open(
            "txt_top_red_tfp_champion_month.txt", "r")
        txt_top_red_tfp_champion_month_r_text = txt_top_red_tfp_champion_month_r.read()
        print("Taxa de participação em TFs", txt_top_red_tfp_champion_month_r_text)

    except:
        pass
        # ENTRA NO PERFIL DO TOP NA ROTA
    leaguegraph_main_profile_stats = "https://www.leagueofgraphs.com/pt/summoner/champions/"

    top_lane = "/top"  # aqui estão identificadas as lanes
    top_red_leaguegraph_profile = leaguegraph_main_profile_stats + \
                                   "/" + "br/" + txt_top_red_nick_store_text_r + top_lane
    driver.get(top_red_leaguegraph_profile)
    time.sleep(5)
    try:
        player_gamesjogados_month = driver.find_element_by_xpath(
            '//*[@id="graphDD54"]"]')
        txt_top_red_rota_gamesjogados_month = open(
            "top_red_rota_gamesjogados_month.txt", "w")
        txt_top_red_rota_gamesjogados_month.write(player_gamesjogados_month.text)
        txt_top_red_rota_gamesjogados_month.close()
        txt_top_red_rota_gamesjogados_month_r = open(
            "top_red_rota_gamesjogados_month.txt", "r")
        txt_top_red_rota_gamesjogados_month_text_r = txt_top_red_rota_gamesjogados_month_r.read()
        print("Jogos na rota", top_lane,
              "nos últimos 30 dias:", )

        # coleta porcentagem de vitoria na rota
        player_wr_champion_month = driver.find_element_by_xpath(
            '//*[@id="graphDD55"]')
        txt_top_red_rota_champion_month = open(
            "txt_top_red_rota_champion_month.txt", "w")
        txt_top_red_rota_champion_month.write(player_wr_champion_month.text)
        txt_top_red_rota_champion_month.close()
        txt_top_red_rota_champion_month_r = open(
            "txt_top_red_rota_champion_month.txt", "r")
        txt_top_red_rota_champion_month_text_r = txt_top_red_rota_champion_month_r.read()
        print("Taxa de vitória:", txt_top_red_rota_champion_month_text_r)

        # taxa de vitórias em lutas em equipe mes:

        player_tfwr_champion_month = driver.find_element_by_xpath(
            '//*[@id="graphDD23"]')
        txt_top_red_rota_tfwr_champion_month = open(
            "txt_top_red_rota_tfwr_champion_month.txt", "w")
        txt_top_red_rota_tfwr_champion_month.write(
            player_tfwr_champion_month.text)
        txt_top_red_rota_tfwr_champion_month.close()
        txt_top_red_rota_tfwr_champion_month_r = open(
            "txt_top_rota_red_tfwr_champion_month.txt", "r")
        txt_top_red_rota_tfwr_champion_month_text_r = txt_top_red_rota_tfwr_champion_month_r.read()
        print("Taxa de Vitória de Team Fights",
              txt_top_red_rota_tfwr_champion_month_text_r)

        # taxa de vitoria em 1v1:

        player_1v1wr_champion_month = driver.find_element_by_xpath(
            '//*[@id="graphDD24"]')
        txt_top_red_rota_1v1wr_champion_month = open(
            "txt_top_red_rota_1v1wr_champion_month.txt", "w")
        txt_top_red_rota_1v1wr_champion_month.write(
            player_1v1wr_champion_month.text)
        txt_top_red_rota_1v1wr_champion_month.close()
        txt_top_red_rota_1v1wr_champion_month_r = open(
            "txt_top_red_rota_1v1wr_champion_month.txt", "r")
        txt_top_red_rota_1v1wr_champion_month_r_text = txt_top_red_rota_1v1wr_champion_month_r.read()
        print("Taxa de vitória de 1v1", txt_top_red_rota_1v1wr_champion_month_r_text)
        # taxa de participação nas lutas:

        player_tfp_champion_month = driver.find_element_by_xpath(
            '//*[@id="graphDD26"]')
        txt_top_red_rota_tfp_champion_month = open(
            "txt_top_red_rota_tfp_champion_month.txt", "w")
        txt_top_red_rota_tfp_champion_month.write(player_tfp_champion_month.text)
        txt_top_red_rota_tfp_champion_month.close()
        txt_top_red_rota_tfp_champion_month_r = open(
            "txt_top_red_rota_tfp_champion_month.txt", "r")
        txt_top_red_rota_tfp_champion_month_r_text = txt_top_red_rota_tfp_champion_month_r.read()
        print("Taxa de participação em TFs",
              txt_top_red_rota_tfp_champion_month_r_text)

    except:
        pass

    # TOP red - Mobalytics
    mobalytics_main_profile_stats = "https://app.mobalytics.gg/lol/profile/br/"
    top_red_mobalytics_profile = mobalytics_main_profile_stats + \
                                  txt_top_red_nick_store_text_r + "/" + "champions?champion=" + top_red_champion
    driver.get(top_red_mobalytics_profile)
    time.sleep(5)

    try:
        top_red_champion_alltime_wr = driver.find_element_by_xpath(
            '//*[@id="app-content"]/div[1]/div[4]/div[2]/div/div[3]/div/div[2]/div[2]/div[4]/div/div[3]')
        txt_top_red_champion_alltime_wr = open(
            "top_red_champion_alltime_wr.txt", "w")
        txt_top_red_champion_alltime_wr.write(top_red_champion_alltime_wr.text)
        txt_top_red_champion_alltime_wr.close()
        txt_top_red_champion_alltime_wr_r = open(
            "top_red_champion_alltime_wr.txt", "r")
        txt_top_red_champion_alltime_wr_r_text = txt_top_red_champion_alltime_wr_r.read()
        print("Winrate na season:", txt_top_red_champion_alltime_wr_r_text)

        # top red kda season
        top_red_champion_kda = driver.find_element_by_xpath(
            '//*[@id="app-content"]/div[1]/div[4]/div[2]/div/div[3]/div/div[2]/div[2]/div[5]')
        txt_top_red_champion_kda = open("top_red_champion_kda.txt", "w")
        txt_top_red_champion_kda.write(top_red_champion_kda.text)
        txt_top_red_champion_kda.close()
        txt_top_red_champion_kda_r = open("top_red_champion_kda.txt", "r")
        txt_top_red_champion_kda_r_text = txt_top_red_champion_kda_r.read()
        print("KDA com o champion:", txt_top_red_champion_kda_r_text)

        # vision score
        top_red_champion_ward = driver.find_element_by_xpath(
            '//*[@id="app-content"]/div[1]/div[4]/div[2]/div/div[3]/div/div[2]/div[2]/div[7]')
        txt_top_red_champion_ward = open("txt_top_red_champion_ward", "w")
        txt_top_red_champion_ward.write(top_red_champion_ward.text)
        txt_top_red_champion_ward.close()
        txt_top_red_champion_ward_r = open("txt_top_red_champion_ward", "r")
        txt_top_red_champion_ward_r_text = txt_top_red_champion_ward_r.read()
        print("Placar de visão:", txt_top_red_champion_ward_r_text)

        # numero de jogos com o campeao
        top_red_gamesplayed_champion = driver.find_element_by_xpath(
            '//*[@id="app-content"]/div[1]/div[4]/div[2]/div/div[3]/div/div[2]/div[2]/div[3]')
        txt_top_red_gamesplayed_champion = open(
            "top_red_gamesplayed_champion.txt", "w")
        txt_top_red_gamesplayed_champion.write(top_red_gamesplayed_champion.text)
        txt_top_red_gamesplayed_champion.close()
        txt_top_red_gamesplayed_champion_r = open(
            top_red_gamesplayed_champion.txt, "r")
        txt_top_red_gamesplayed_champion_r_text = txt_top_red_gamesplayed_champion_r.read()
        print("Total de jogos:", txt_top_red_gamesplayed_champion_r_text)
    except:
        pass

    # ir para a pagina do leaguegraphs do JG red

    leaguegraph_main_profile_stats = "https://www.leagueofgraphs.com/pt/summoner/champions/"
    print("Coletando informações de", txt_jg_red_nick_store_text_r)
    jg_lane = "/jungle"  # aqui estão identificadas as lanes

    def wukongtestjg():
        maybewukong = txt_jg_red_champion_store_text_r
        if maybewukong == "Wukong":
            jg_red_champion = "monkeyking"

    wukongtesttop()

    jg_red_leaguegraph_profile = leaguegraph_main_profile_stats + \
                                  jg_red_champion.lower() + "/" + "br/" + txt_jg_red_nick_store_text_r + jg_lane
    driver.get(jg_red_leaguegraph_profile)
    time.sleep(5)
    # script de coleta de informações jogador, indentificação de elemento + store:
    # coleta games jogados no mês com o campeao:

    # coleta games jogados no mês com o campeao: JG
    try:
        player_gamesjogados_month = driver.find_element_by_xpath(
            '//*[@id="graphDD54"]')
        txt_jg_red_gamesjogados_month = open(
            "jg_red_gamesjogados_month.txt", "w")
        txt_jg_red_gamesjogados_month.write(player_gamesjogados_month.text)
        txt_jg_red_gamesjogados_month.close()
        txt_jg_red_gamesjogados_month_r = open(
            "jg_red_gamesjogados_month.txt", "r")
        txt_jg_red_gamesjogados_month_text_r = txt_jg_red_gamesjogados_month_r.read()
        print("Jogos com", txt_jg_red_champion_store_text_r,
              "nos últimos 30 dias:", txt_jg_red_gamesjogados_month_text_r)

        # coleta porcentagem de vitoria no mês com campeão
        player_wr_champion_month = driver.find_element_by_xpath(
            '//*[@id="graphDD55"]')
        txt_jg_red_wr_champion_month = open(
            "txt_jg_red_wr_champion_month.txt", "w")
        txt_jg_red_wr_champion_month.write(player_wr_champion_month.text)
        txt_jg_red_wr_champion_month.close()
        txt_jg_red_wr_champion_month_r = open(
            "txt_jg_red_wr_champion_month.txt", "r")
        txt_jg_red_wr_champion_month_text_r = txt_jg_red_wr_champion_month_r.read()
        print("Taxa de vitória:", txt_jg_red_wr_champion_month_text_r)
        # taxa de vitórias em lutas em equipe mes:

        player_tfwr_champion_month = driver.find_element_by_xpath(
            '//*[@id="graphDD23"]')
        txt_jg_red_tfwr_champion_month = open(
            "txt_jg_red_tfwr_champion_month.txt", "w")
        txt_jg_red_tfwr_champion_month.write(player_tfwr_champion_month.text)
        txt_jg_red_tfwr_champion_month.close()
        txt_jg_red_tfwr_champion_month_r = open(
            "txt_jg_red_tfwr_champion_month.txt", "r")
        txt_jg_red_tfwr_champion_month_text_r = txt_jg_red_tfwr_champion_month_r.read()
        print("Taxa de Vitória de Team Fights",
              txt_jg_red_tfwr_champion_month_text_r)

        # taxa de vitoria em 1v1:

        player_1v1wr_champion_month = driver.find_element_by_xpath(
            '//*[@id="graphDD24"]')
        txt_jg_red_1v1wr_champion_month = open(
            "txt_jg_red_1v1wr_champion_month.txt", "w")
        txt_jg_red_1v1wr_champion_month.write(player_1v1wr_champion_month.text)
        txt_jg_red_1v1wr_champion_month.close()
        txt_jg_red_1v1wr_champion_month_r = open(
            "txt_jg_red_1v1wr_champion_month.txt", "r")
        txt_jg_red_1v1wr_champion_month_r_text = txt_jg_red_1v1wr_champion_month_r.read()
        print("Taxa de vitória de 1v1", txt_jg_red_1v1wr_champion_month_r_text)

        # taxa de participação nas lutas:

        player_tfp_champion_month = driver.find_element_by_xpath(
            '//*[@id="graphDD26"]')
        txt_jg_red_tfp_champion_month = open(
            "txt_jg_red_tfp_champion_month.txt", "w")
        txt_jg_red_tfp_champion_month.write(player_tfp_champion_month.text)
        txt_jg_red_tfp_champion_month.close()
        txt_jg_red_tfp_champion_month_r = open(
            "txt_jg_red_tfp_champion_month.txt", "r")
        txt_jg_red_tfp_champion_month_r_text = txt_jg_red_tfp_champion_month_r.read()
        print("Taxa de participação em TFs", txt_jg_red_tfp_champion_month_r_text)
    except:
        pass

    # ENTRA NA PAGINA DO JG NA LANE

    leaguegraph_main_profile_stats = "https://www.leagueofgraphs.com/pt/summoner/champions/"

    jg_lane = "/jungle"  # aqui estão identificadas as lanes
    jg_red_leaguegraph_profile = leaguegraph_main_profile_stats + \
                                  "/" + "br/" + txt_jg_red_nick_store_text_r + jg_lane
    driver.get(jg_red_leaguegraph_profile)
    time.sleep(5)
    try:
        player_gamesjogados_month = driver.find_element_by_xpath(
            '//*[@id="graphDD54"]')
        txt_jg_red_rota_gamesjogados_month = open(
            "jg_red_rota_gamesjogados_month.txt", "w")
        txt_jg_red_rota_gamesjogados_month.write(player_gamesjogados_month.text)
        txt_jg_red_rota_gamesjogados_month.close()
        txt_jg_red_rota_gamesjogados_month_r = open(
            "jg_red_rota_gamesjogados_month.txt", "r")
        txt_jg_red_rota_gamesjogados_month_text_r = txt_jg_red_rota_gamesjogados_month_r.read()
        print("Jogos na rota", jg_lane,
              "nos últimos 30 dias:", txt_jg_red_rota_gamesjogados_month_text_r)

        # coleta porcentagem de vitoria no mês com campeão
        player_wr_champion_month = driver.find_element_by_xpath(
            '//*[@id="graphDD55"]')
        txt_jg_red_rota_champion_month = open(
            "txt_jg_red_rota_champion_month.txt", "w")
        txt_jg_red_rota_champion_month.write(player_wr_champion_month.text)
        txt_jg_red_rota_champion_month.close()
        txt_jg_red_rota_champion_month_r = open(
            "txt_jg_red_rota_champion_month.txt", "r")
        txt_jg_red_rota_champion_month_text_r = txt_jg_red_rota_champion_month_r.read()
        print("Taxa de vitória:", txt_jg_red_rota_champion_month_text_r)

        # taxa de vitórias em lutas em equipe mes:

        player_tfwr_champion_month = driver.find_element_by_xpath(
            '//*[@id="graphDD23"]')
        txt_jg_red_rota_tfwr_champion_month = open(
            "txt_jg_red_rota_tfwr_champion_month.txt", "w")
        txt_jg_red_rota_tfwr_champion_month.write(
            player_tfwr_champion_month.text)
        txt_jg_red_rota_tfwr_champion_month.close()
        txt_jg_red_rota_tfwr_champion_month_r = open(
            "txt_jg_rota_red_tfwr_champion_month.txt", "r")
        txt_jg_red_rota_tfwr_champion_month_text_r = txt_jg_red_rota_tfwr_champion_month_r.read()
        print("Taxa de Vitória de Team Fights",
              txt_jg_red_rota_tfwr_champion_month_text_r)

        # taxa de vitoria em 1v1:

        player_1v1wr_champion_month = driver.find_element_by_xpath(
            '//*[@id="graphDD24"]')
        txt_jg_red_rota_1v1wr_champion_month = open(
            "txt_jg_red_rota_1v1wr_champion_month.txt", "w")
        txt_jg_red_rota_1v1wr_champion_month.write(
            player_1v1wr_champion_month.text)
        txt_jg_red_rota_1v1wr_champion_month.close()
        txt_jg_red_rota_1v1wr_champion_month_r = open(
            "txt_jg_red_rota_1v1wr_champion_month.txt", "r")
        txt_jg_red_rota_1v1wr_champion_month_r_text = txt_jg_red_rota_1v1wr_champion_month_r.read()
        print("Taxa de vitória de 1v1", txt_jg_red_rota_1v1wr_champion_month_r_text)
        # taxa de participação nas lutas:

        player_tfp_champion_month = driver.find_element_by_xpath(
            '//*[@id="graphDD26"]')
        txt_jg_red_rota_tfp_champion_month = open(
            "txt_jg_red_rota_tfp_champion_month.txt", "w")
        txt_jg_red_rota_tfp_champion_month.write(player_tfp_champion_month.text)
        txt_jg_red_rota_tfp_champion_month.close()
        txt_jg_red_rota_tfp_champion_month_r = open(
            "txt_jg_red_rota_tfp_champion_month.txt", "r")
        txt_jg_red_rota_tfp_champion_month_r_text = txt_jg_red_rota_tfp_champion_month_r.read()
        print("Taxa de participação em TFs",
              txt_jg_red_rota_tfp_champion_month_r_text)

    except:
        pass

    # JG red - Mobalytics

    mobalytics_main_profile_stats = "https://app.mobalytics.gg/lol/profile/br/"
    jg_red_mobalytics_profile = mobalytics_main_profile_stats + \
                                 txt_jg_red_nick_store_text_r + "/" + "champions?champion=" + jg_red_champion
    driver.get(jg_red_mobalytics_profile)
    time.sleep(5)
    try:
        # winrate season jg red
        jg_red_champion_alltime_wr = driver.find_element_by_xpath(
            '//*[@id="app-content"]/div[1]/div[4]/div[2]/div/div[3]/div/div[2]/div[2]/div[4]/div/div[3]')
        txt_jg_red_champion_alltime_wr = open(
            "jg_red_champion_alltime_wr.txt", "w")
        txt_jg_red_champion_alltime_wr.write(jg_red_champion_alltime_wr.text)
        txt_jg_red_champion_alltime_wr.close()
        txt_jg_red_champion_alltime_wr_r = open(
            "jg_red_champion_alltime_wr.txt", "r")
        txt_jg_red_champion_alltime_wr_r_text = txt_jg_red_champion_alltime_wr_r.read()
        print("Winrate da season:", txt_jg_red_champion_alltime_wr_r_text)

        # jg red kda season
        jg_red_champion_kda = driver.find_element_by_xpath(
            '//*[@id="app-content"]/div[1]/div[4]/div[2]/div/div[3]/div/div[2]/div[2]/div[5]')
        txt_jg_red_champion_kda = open("jg_red_champion_kda.txt", "w")
        txt_jg_red_champion_kda.write(jg_red_champion_kda.text)
        txt_jg_red_champion_kda.close()
        txt_jg_red_champion_kda_r = open("jg_red_champion_kda.txt", "r")
        txt_jg_red_champion_kda_r_text = txt_jg_red_champion_kda_r.read()
        print("KDA na season", txt_jg_red_champion_kda_r_text)

        # vision score -JG
        jg_red_champion_ward = driver.find_element_by_xpath(
            '//*[@id="app-content"]/div[1]/div[4]/div[2]/div/div[3]/div/div[2]/div[2]/div[7]')
        txt_jg_red_champion_ward = open("txt_jg_red_champion_ward", "w")
        txt_jg_red_champion_ward.write(jg_red_champion_ward.text)
        txt_jg_red_champion_ward.close()
        txt_jg_red_champion_ward_r = open("txt_jg_red_champion_ward", "r")
        txt_jg_red_champion_ward_r_text = txt_jg_red_champion_ward_r.read()
        print("Placar de visão:", txt_jg_red_champion_ward_r_text)

        # numero de jogos com o campeao  JG
        jg_red_gamesplayed_champion = driver.find_element_by_xpath(
            '//*[@id="app-content"]/div[1]/div[4]/div[2]/div/div[3]/div/div[2]/div[2]/div[3]')
        txt_jg_red_gamesplayed_champion = open(
            "jg_red_gamesplayed_champion.txt", "w")
        txt_jg_red_gamesplayed_champion.write(jg_red_gamesplayed_champion.text)
        txt_jg_red_gamesplayed_champion.close()
        txt_jg_red_gamesplayed_champion_r = open(
            "jg_red_gamesplayed_champion.txt", "r")
        txt_jg_red_gamesplayed_champion_r_text = txt_jg_red_gamesplayed_champion_r.read()
        print("Número de jogos com campeão:",
              txt_jg_red_gamesplayed_champion_r_text)
    except:
        pass

    # MID leaguegraphs:
    leaguegraph_main_profile_stats = "https://www.leagueofgraphs.com/pt/summoner/champions/"
    print("Coletando informações de", txt_mid_red_nick_store_text_r)
    mid_lane = "/middle"  # aqui estão identificadas as lanes
    mid_red_leaguegraph_profile = leaguegraph_main_profile_stats + \
                                   mid_red_champion.lower() + "/" + "br/" + txt_mid_red_nick_store_text_r + mid_lane
    driver.get(mid_red_leaguegraph_profile)
    time.sleep(10)

    try:
        player_gamesjogados_month = driver.find_element_by_xpath(
            '//*[@id="graphDD54"]')
        txt_mid_red_gamesjogados_month = open(
            "mid_red_gamesjogados_month.txt", "w")
        txt_mid_red_gamesjogados_month.write(player_gamesjogados_month.text)
        txt_mid_red_gamesjogados_month.close()
        txt_mid_red_gamesjogados_month_r = open(
            "mid_red_gamesjogados_month.txt", "r")
        txt_mid_red_gamesjogados_month_text_r = txt_mid_red_gamesjogados_month_r.read()
        print("Jogos com", txt_mid_red_champion_store_text_r,
              "nos últimos 30 dias:", txt_mid_red_gamesjogados_month_text_r)

        # coleta porcentagem de vitoria no mês com campeão
        player_wr_champion_month = driver.find_element_by_xpath(
            '//*[@id="graphDD55"]')
        txt_mid_red_wr_champion_month = open(
            "txt_mid_red_wr_champion_month.txt", "w")
        txt_mid_red_wr_champion_month.write(player_wr_champion_month.text)
        txt_mid_red_wr_champion_month.close()
        txt_mid_red_wr_champion_month_r = open(
            "txt_mid_red_wr_champion_month.txt", "r")
        txt_mid_red_wr_champion_month_text_r = txt_mid_red_wr_champion_month_r.read()
        print("Taxa de vitória:", txt_mid_red_wr_champion_month_text_r)

        # taxa de vitórias em lutas em equipe mes:

        player_tfwr_champion_month = driver.find_element_by_xpath(
            '//*[@id="graphDD23"]')
        txt_mid_red_tfwr_champion_month = open(
            "txt_mid_red_tfwr_champion_month.txt", "w")
        txt_mid_red_tfwr_champion_month.write(player_tfwr_champion_month.text)
        txt_mid_red_tfwr_champion_month.close()
        txt_mid_red_tfwr_champion_month_r = open(
            "txt_mid_red_tfwr_champion_month.txt", "r")
        txt_mid_red_tfwr_champion_month_text_r = txt_mid_red_tfwr_champion_month_r.read()
        print("Taxa de Vitória de Team Fights",
              txt_mid_red_tfwr_champion_month_text_r)

        # taxa de vitoria em 1v1:

        player_1v1wr_champion_month = driver.find_element_by_xpath(
            '//*[@id="graphDD24"]')
        txt_mid_red_1v1wr_champion_month = open(
            "txt_mid_red_1v1wr_champion_month.txt", "w")
        txt_mid_red_1v1wr_champion_month.write(player_1v1wr_champion_month.text)
        txt_mid_red_1v1wr_champion_month.close()
        txt_mid_red_1v1wr_champion_month_r = open(
            "txt_mid_red_1v1wr_champion_month.txt", "r")
        txt_mid_red_1v1wr_champion_month_r_text = txt_mid_red_1v1wr_champion_month_r.read()
        print("Taxa de vitória de 1v1", txt_mid_red_1v1wr_champion_month_r_text)
        # taxa de participação nas lutas:

        player_tfp_champion_month = driver.find_element_by_xpath(
            '//*[@id="graphDD26"]')
        txt_mid_red_tfp_champion_month = open(
            "txt_mid_red_tfp_champion_month.txt", "w")
        txt_mid_red_tfp_champion_month.write(player_tfp_champion_month.text)
        txt_mid_red_tfp_champion_month.close()
        txt_mid_red_tfp_champion_month_r = open(
            "txt_mid_red_tfp_champion_month.txt", "r")
        txt_mid_red_tfp_champion_month_r_text = txt_mid_red_tfp_champion_month_r.read()
        print("Taxa de participação em TFs", txt_mid_red_tfp_champion_month_r_text)

    except:
        pass

    # league graphs mid na rota
    mid_lane = "/middle"  # aqui estão identificadas as lanes
    mid_red_leaguegraph_profile = leaguegraph_main_profile_stats + \
                                   "/" + "br/" + txt_mid_red_nick_store_text_r + mid_lane
    driver.get(mid_red_leaguegraph_profile)
    time.sleep(5)
    try:
        player_gamesjogados_month = driver.find_element_by_xpath(
            '//*[@id="graphDD54"]')
        txt_mid_red_rota_gamesjogados_month = open(
            "mid_red_rota_gamesjogados_month.txt", "w")
        txt_mid_red_rota_gamesjogados_month.write(player_gamesjogados_month.text)
        txt_mid_red_rota_gamesjogados_month.close()
        txt_mid_red_rota_gamesjogados_month_r = open(
            "mid_red_rota_gamesjogados_month.txt", "r")
        txt_mid_red_rota_gamesjogados_month_text_r = txt_mid_red_rota_gamesjogados_month_r.read()
        print("Jogos na rota", mid_lane,
              "nos últimos 30 dias:", txt_mid_red_rota_gamesjogados_month_text_r)

        # coleta porcentagem de vitoria no mês com campeão
        player_wr_champion_month = driver.find_element_by_xpath(
            '//*[@id="graphDD55"]')
        txt_mid_red_rota_champion_month = open(
            "txt_mid_red_rota_champion_month.txt", "w")
        txt_mid_red_rota_champion_month.write(player_wr_champion_month.text)
        txt_mid_red_rota_champion_month.close()
        txt_mid_red_rota_champion_month_r = open(
            "txt_mid_red_rota_champion_month.txt", "r")
        txt_mid_red_rota_champion_month_text_r = txt_mid_red_rota_champion_month_r.read()
        print("Taxa de vitória:", txt_mid_red_rota_champion_month_text_r)

        # taxa de vitórias em lutas em equipe mes:

        player_tfwr_champion_month = driver.find_element_by_xpath(
            '//*[@id="graphDD23"]')
        txt_mid_red_rota_tfwr_champion_month = open(
            "txt_mid_red_rota_tfwr_champion_month.txt", "w")
        txt_mid_red_rota_tfwr_champion_month.write(
            player_tfwr_champion_month.text)
        txt_mid_red_rota_tfwr_champion_month.close()
        txt_mid_red_rota_tfwr_champion_month_r = open(
            "txt_mid_rota_red_tfwr_champion_month.txt", "r")
        txt_mid_red_rota_tfwr_champion_month_text_r = txt_mid_red_rota_tfwr_champion_month_r.read()
        print("Taxa de Vitória de Team Fights",
              txt_mid_red_rota_tfwr_champion_month_text_r)

        # taxa de vitoria em 1v1:

        player_1v1wr_champion_month = driver.find_element_by_xpath(
            '//*[@id="graphDD24"]')
        txt_mid_red_rota_1v1wr_champion_month = open(
            "txt_top_red_rota_1v1wr_champion_month.txt", "w")
        txt_mid_red_rota_1v1wr_champion_month.write(
            player_1v1wr_champion_month.text)
        txt_mid_red_rota_1v1wr_champion_month.close()
        txt_mid_red_rota_1v1wr_champion_month_r = open(
            "txt_mid_red_rota_1v1wr_champion_month.txt", "r")
        txt_mid_red_rota_1v1wr_champion_month_r_text = txt_top_red_rota_1v1wr_champion_month_r.read()
        print("Taxa de vitória de 1v1", txt_top_red_rota_1v1wr_champion_month_r_text)
        # taxa de participação nas lutas:

        player_tfp_champion_month = driver.find_element_by_xpath(
            '//*[@id="graphDD26"]')
        txt_top_red_rota_tfp_champion_month = open(
            "txt_top_red_rota_tfp_champion_month.txt", "w")
        txt_top_red_rota_tfp_champion_month.write(player_tfp_champion_month.text)
        txt_top_red_rota_tfp_champion_month.close()
        txt_top_red_rota_tfp_champion_month_r = open(
            "txt_top_red_rota_tfp_champion_month.txt", "r")
        txt_top_red_rota_tfp_champion_month_r_text = txt_top_red_rota_tfp_champion_month_r.read()
        print("Taxa de participação em TFs",
              txt_top_red_rota_tfp_champion_month_r_text)

    except:
        pass

    # MOBALYTICS MID

    # MID red - Mobalytics
    mobalytics_main_profile_stats = "https://app.mobalytics.gg/lol/profile/br/"
    mid_red_mobalytics_profile = mobalytics_main_profile_stats + \
                                  txt_mid_red_nick_store_text_r + "/" + "champions?champion=" + mid_red_champion
    driver.get(mid_red_mobalytics_profile)
    time.sleep(5)
    try:
        # winrate season mid red
        mid_red_champion_alltime_wr = driver.find_element_by_xpath(
            '//*[@id="app-content"]/div[1]/div[4]/div[2]/div/div[3]/div/div[2]/div[2]/div[4]/div/div[3]')
        txt_mid_red_champion_alltime_wr = open(
            "mid_red_champion_alltime_wr.txt", "w")
        txt_mid_red_champion_alltime_wr.write(mid_red_champion_alltime_wr.text)
        txt_mid_red_champion_alltime_wr.close()
        txt_mid_red_champion_alltime_wr_r = open(
            "mid_red_champion_alltime_wr.txt", "r")
        txt_mid_red_champion_alltime_wr_r_text = txt_mid_red_champion_alltime_wr_r.read()
        print("Winrate Mid red season", txt_mid_red_champion_alltime_wr_r_text)

        # mid red kda season
        mid_red_champion_kda = driver.find_element_by_xpath(
            '//*[@id="app-content"]/div[1]/div[4]/div[2]/div/div[3]/div/div[2]/div[2]/div[5]')
        txt_mid_red_champion_kda = open("mid_red_champion_kda.txt", "w")
        txt_mid_red_champion_kda.write(mid_red_champion_kda.text)
        txt_mid_red_champion_kda.close()
        txt_mid_red_champion_kda_r = open("mid_red_champion_kda.txt", "r")
        txt_mid_red_champion_kda_r_text = txt_mid_red_champion_kda_r.read()
        print("KDA da season", txt_mid_red_champion_kda_r_text)

        # vision score
        mid_red_champion_ward = driver.find_element_by_xpath(
            '//*[@id="app-content"]/div[1]/div[4]/div[2]/div/div[3]/div/div[2]/div[2]/div[7]')
        txt_mid_red_champion_ward = open("txt_mid_red_champion_ward", "w")
        txt_mid_red_champion_ward.write(mid_red_champion_ward.text)
        txt_mid_red_champion_ward.close()
        txt_mid_red_champion_ward_r = open("txt_mid_red_champion_ward", "r")
        txt_mid_red_champion_ward_r_text = txt_mid_red_champion_ward_r.read()
        print("Placar de visão season:", txt_mid_red_champion_ward_r_text)

        # numero de jogos com o campeao
        mid_red_gamesplayed_champion = driver.find_element_by_xpath(
            '//*[@id="app-content"]/div[1]/div[4]/div[2]/div/div[3]/div/div[2]/div[2]/div[3]')
        txt_mid_red_gamesplayed_champion = open(
            "mid_red_gamesplayed_champion.txt", "w")
        txt_mid_red_gamesplayed_champion.write(
            mid_red_gamesplayed_champion.text)
        txt_mid_red_gamesplayed_champion.close()
        txt_mid_red_gamesplayed_champion_r = open(
            "mid_red_gamesplayed_champion.txt", "r")
        txt_mid_red_gamesplayed_champion_r_text = txt_mid_red_gamesplayed_champion_r.read()
        print(txt_mid_red_gamesplayed_champion_r_text)

    except:
        pass

    # ADC leaguegraphs:

    leaguegraph_main_profile_stats = "https://www.leagueofgraphs.com/pt/summoner/champions/"
    print("Coletando informações de", txt_adc_red_nick_store_text_r)
    adc_lane = "/adc"  # aqui estão identificadas as lanes
    adc_red_leaguegraph_profile = leaguegraph_main_profile_stats + \
                                   adc_red_champion.lower() + "/" + "br/" + txt_adc_red_nick_store_text_r + adc_lane
    driver.get(adc_red_leaguegraph_profile)
    time.sleep(10)
    try:
        player_gamesjogados_month = driver.find_element_by_xpath(
            '//*[@id="graphDD54"]')
        txt_adc_red_gamesjogados_month = open(
            "adc_red_gamesjogados_month.txt", "w")
        txt_adc_red_gamesjogados_month.write(player_gamesjogados_month.text)
        txt_adc_red_gamesjogados_month.close()
        txt_adc_red_gamesjogados_month_r = open(
            "adc_red_gamesjogados_month.txt", "r")
        txt_adc_red_gamesjogados_month_text_r = txt_adc_red_gamesjogados_month_r.read()
        print("Jogos com", txt_adc_red_champion_store_text_r,
              "nos últimos 30 dias:", txt_adc_red_gamesjogados_month_text_r)

        # coleta porcentagem de vitoria no mês com campeão
        player_wr_champion_month = driver.find_element_by_xpath(
            '//*[@id="graphDD55"]')
        txt_adc_red_wr_champion_month = open(
            "txt_adc_red_wr_champion_month.txt", "w")
        txt_adc_red_wr_champion_month.write(player_wr_champion_month.text)
        txt_adc_red_wr_champion_month.close()
        txt_adc_red_wr_champion_month_r = open(
            "txt_adc_red_wr_champion_month.txt", "r")
        txt_adc_red_wr_champion_month_text_r = txt_adc_red_wr_champion_month_r.read()
        print("Taxa de vitória:", txt_adc_red_wr_champion_month_text_r)

        # taxa de vitórias em lutas em equipe mes:

        player_tfwr_champion_month = driver.find_element_by_xpath(
            '//*[@id="graphDD23"]')
        txt_adc_red_tfwr_champion_month = open(
            "txt_adc_red_tfwr_champion_month.txt", "w")
        txt_adc_red_tfwr_champion_month.write(player_tfwr_champion_month.text)
        txt_adc_red_tfwr_champion_month.close()
        txt_adc_red_tfwr_champion_month_r = open(
            "txt_adc_red_tfwr_champion_month.txt", "r")
        txt_adc_red_tfwr_champion_month_text_r = txt_adc_red_tfwr_champion_month_r.read()
        print("Taxa de Vitória de Team Fights",
              txt_adc_red_tfwr_champion_month_text_r)

        # taxa de vitoria em 1v1:

        player_1v1wr_champion_month = driver.find_element_by_xpath(
            '//*[@id="graphDD24"]')
        txt_adc_red_1v1wr_champion_month = open(
            "txt_adc_red_1v1wr_champion_month.txt", "w")
        txt_adc_red_1v1wr_champion_month.write(player_1v1wr_champion_month.text)
        txt_adc_red_1v1wr_champion_month.close()
        txt_adc_red_1v1wr_champion_month_r = open(
            "txt_adc_red_1v1wr_champion_month.txt", "r")
        txt_adc_red_1v1wr_champion_month_r_text = txt_adc_red_1v1wr_champion_month_r.read()
        print("Taxa de vitória de 1v1", txt_adc_red_1v1wr_champion_month_r_text)
        # taxa de participação nas lutas:

        player_tfp_champion_month = driver.find_element_by_xpath(
            '//*[@id="graphDD26"]')
        txt_adc_red_tfp_champion_month = open(
            "txt_mid_red_tfp_champion_month.txt", "w")
        txt_adc_red_tfp_champion_month.write(player_tfp_champion_month.text)
        txt_adc_red_tfp_champion_month.close()
        txt_adc_red_tfp_champion_month_r = open(
            "txt_adc_red_tfp_champion_month.txt", "r")
        txt_adc_red_tfp_champion_month_r_text = txt_adc_red_tfp_champion_month_r.read()
        print("Taxa de participação em TFs", txt_adc_red_tfp_champion_month_r_text)
    except:
        pass

    # league graphs adc na rota
    adc_lane = "/adc"  # aqui estão identificadas as lanes
    adc_red_leaguegraph_profile = leaguegraph_main_profile_stats + \
                                   "/" + "br/" + txt_adc_red_nick_store_text_r + adc_lane
    driver.get(adc_red_leaguegraph_profile)
    time.sleep(5)
    try:
        player_gamesjogados_month = driver.find_element_by_xpath(
            '//*[@id="graphDD54"]')
        txt_adc_red_rota_gamesjogados_month = open(
            "adc_red_rota_gamesjogados_month.txt", "w")
        txt_adc_red_rota_gamesjogados_month.write(player_gamesjogados_month.text)
        txt_adc_red_rota_gamesjogados_month.close()
        txt_adc_red_rota_gamesjogados_month_r = open(
            "adc_red_rota_gamesjogados_month.txt", "r")
        txt_adc_red_rota_gamesjogados_month_text_r = txt_adc_red_rota_gamesjogados_month_r.read()
        print("Jogos na rota", adc_lane,
              "nos últimos 30 dias:", txt_adc_red_rota_gamesjogados_month_text_r)

        # coleta porcentagem de vitoria no mês com campeão
        player_wr_champion_month = driver.find_element_by_xpath(
            '//*[@id="graphDD55"]')
        txt_adc_red_rota_champion_month = open(
            "txt_adc_red_rota_champion_month.txt", "w")
        txt_adc_red_rota_champion_month.write(player_wr_champion_month.text)
        txt_adc_red_rota_champion_month.close()
        txt_adc_red_rota_champion_month_r = open(
            "txt_adc_red_rota_champion_month.txt", "r")
        txt_adc_red_rota_champion_month_text_r = txt_adc_red_rota_champion_month_r.read()
        print("Taxa de vitória:", txt_adc_red_rota_champion_month_text_r)

        # taxa de vitórias em lutas em equipe mes:

        player_tfwr_champion_month = driver.find_element_by_xpath(
            '//*[@id="graphDD23"]')
        txt_adc_red_rota_tfwr_champion_month = open(
            "txt_adc_red_rota_tfwr_champion_month.txt", "w")
        txt_adc_red_rota_tfwr_champion_month.write(
            player_tfwr_champion_month.text)
        txt_adc_red_rota_tfwr_champion_month.close()
        txt_adc_red_rota_tfwr_champion_month_r = open(
            "txt_adc_red_rota_tfwr_champion_month.txt", "r")
        txt_adc_red_rota_tfwr_champion_month_text_r = txt_adc_red_rota_tfwr_champion_month_r.read()
        print("Taxa de Vitória de Team Fights",
              txt_adc_red_rota_tfwr_champion_month_text_r)

        # taxa de vitoria em 1v1:

        player_1v1wr_champion_month = driver.find_element_by_xpath(
            '//*[@id="graphDD24"]')
        txt_adc_red_rota_1v1wr_champion_month = open(
            "txt_top_red_rota_1v1wr_champion_month.txt", "w")
        txt_adc_red_rota_1v1wr_champion_month.write(
            player_1v1wr_champion_month.text)
        txt_adc_red_rota_1v1wr_champion_month.close()
        txt_adc_red_rota_1v1wr_champion_month_r = open(
            "txt_adc_red_rota_1v1wr_champion_month.txt", "r")
        txt_adc_red_rota_1v1wr_champion_month_r_text = txt_top_red_rota_1v1wr_champion_month_r.read()
        print("Taxa de vitória de 1v1", txt_top_red_rota_1v1wr_champion_month_r_text)
        # taxa de participação nas lutas:

        player_tfp_champion_month = driver.find_element_by_xpath(
            '//*[@id="graphDD26"]')
        txt_adc_red_rota_tfp_champion_month = open(
            "txt_top_red_rota_tfp_champion_month.txt", "w")
        txt_adc_red_rota_tfp_champion_month.write(player_tfp_champion_month.text)
        txt_adc_red_rota_tfp_champion_month.close()
        txt_adc_red_rota_tfp_champion_month_r = open(
            "txt_top_red_rota_tfp_champion_month.txt", "r")
        txt_adc_red_rota_tfp_champion_month_r_text = txt_adc_red_rota_tfp_champion_month_r.read()
        print("Taxa de participação em TFs",
              txt_adc_red_rota_tfp_champion_month_r_text)

    except:
        pass

        # ADC red - Mobalytics
    mobalytics_main_profile_stats = "https://app.mobalytics.gg/lol/profile/br/"
    adc_red_mobalytics_profile = mobalytics_main_profile_stats + \
                                  txt_adc_red_nick_store_text_r + "/" + "champions?champion=" + adc_red_champion
    driver.get(adc_red_mobalytics_profile)
    time.sleep(5)
    try:
        # winrate season adc red
        adc_red_champion_alltime_wr = driver.find_element_by_xpath(
            '//*[@id="app-content"]/div[1]/div[4]/div[2]/div/div[3]/div/div[2]/div[2]/div[4]/div/div[3]')
        txt_adc_red_champion_alltime_wr = open(
            "adc_red_champion_alltime_wr.txt", "w")
        txt_adc_red_champion_alltime_wr.write(adc_red_champion_alltime_wr.text)
        txt_adc_red_champion_alltime_wr.close()
        txt_adc_red_champion_alltime_wr_r = open(
            "adc_red_champion_alltime_wr.txt", "r")
        txt_adc_red_champion_alltime_wr_r_text = txt_adc_red_champion_alltime_wr_r.read()
        print("Winrate season:", txt_adc_red_champion_alltime_wr_r_text)

        # adc red kda season
        adc_red_champion_kda = driver.find_element_by_xpath(
            '//*[@id="app-content"]/div[1]/div[4]/div[2]/div/div[3]/div/div[2]/div[2]/div[5]')
        txt_adc_red_champion_kda = open("adc_red_champion_kda.txt", "w")
        txt_adc_red_champion_kda.write(adc_red_champion_kda.text)
        txt_adc_red_champion_kda.close()
        txt_adc_red_champion_kda_r = open("adc_red_champion_kda.txt", "r")
        txt_adc_red_champion_kda_r_text = txt_adc_red_champion_kda_r.read()
        print("KDA da season", txt_adc_red_champion_kda_r_text)
        # vision score - ADc
        adc_red_champion_ward = driver.find_element_by_xpath(
            '//*[@id="app-content"]/div[1]/div[4]/div[2]/div/div[3]/div/div[2]/div[2]/div[7]')
        txt_adc_red_champion_ward = open("txt_adc_red_champion_ward", "w")
        txt_adc_red_champion_ward.write(adc_red_champion_ward.text)
        txt_adc_red_champion_ward.close()
        txt_adc_red_champion_ward_r = open("txt_adc_red_champion_ward", "r")
        txt_adc_red_champion_ward_r_text = txt_adc_red_champion_ward_r.read()
        print("Placar de visão:", txt_adc_red_champion_ward_r_text)

        # numero de jogos com o campeao  adc
        adc_red_gamesplayed_champion = driver.find_element_by_xpath(
            '//*[@id="app-content"]/div[1]/div[4]/div[2]/div/div[3]/div/div[2]/div[2]/div[3]')
        txt_adc_red_gamesplayed_champion = open(
            "adc_red_gamesplayed_champion.txt", "w")
        txt_adc_red_gamesplayed_champion.write(adc_red_gamesplayed_champion.text)
        txt_adc_red_gamesplayed_champion.close()
        txt_adc_red_gamesplayed_champion_r = open(
            "adc_red_gamesplayed_champion.txt", "r")
        txt_adc_red_gamesplayed_champion_r_text = txt_adc_red_gamesplayed_champion_r.read()
        print("Nome de jogos com o campeão:",
              txt_adc_red_gamesplayed_champion_r_text)

        # SUP leaguegraphs:

        leaguegraph_main_profile_stats = "https://www.leagueofgraphs.com/pt/summoner/champions/"
        print("Coletando informações de", txt_sup_red_nick_store_text_r)
        sup_lane = "/support"  # aqui estão identificadas as lanes
        sup_red_leaguegraph_profile = leaguegraph_main_profile_stats + \
                                       sup_red_champion.lower() + "/" + "br/" + txt_sup_red_nick_store_text_r + sup_lane
        driver.get(sup_red_leaguegraph_profile)
        time.sleep(10)

    except:
        pass
    try:
        player_gamesjogados_month = driver.find_element_by_xpath(
            '//*[@id="graphDD54"]')
        txt_sup_red_gamesjogados_month = open(
            "sup_red_gamesjogados_month.txt", "w")
        txt_sup_red_gamesjogados_month.write(player_gamesjogados_month.text)
        txt_sup_red_gamesjogados_month.close()
        txt_sup_red_gamesjogados_month_r = open(
            "sup_red_gamesjogados_month.txt", "r")
        txt_sup_red_gamesjogados_month_text_r = txt_sup_red_gamesjogados_month_r.read()
        print("Jogos com", txt_sup_red_champion_store_text_r,
              "nos últimos 30 dias:", txt_sup_red_gamesjogados_month_text_r)

        # coleta porcentagem de vitoria no mês com campeão
        player_wr_champion_month = driver.find_element_by_xpath(
            '//*[@id="graphDD55"]')
        txt_sup_red_wr_champion_month = open(
            "txt_sup_red_wr_champion_month.txt", "w")
        txt_sup_red_wr_champion_month.write(player_wr_champion_month.text)
        txt_sup_red_wr_champion_month.close()
        txt_sup_red_wr_champion_month_r = open(
            "txt_sup_red_wr_champion_month.txt", "r")
        txt_sup_red_wr_champion_month_text_r = txt_sup_red_wr_champion_month_r.read()
        print("Taxa de vitória:", txt_sup_red_wr_champion_month_text_r)

        # taxa de vitórias em lutas em equipe mes:

        player_tfwr_champion_month = driver.find_element_by_xpath(
            '//*[@id="graphDD23"]')
        txt_sup_red_tfwr_champion_month = open(
            "txt_sup_red_tfwr_champion_month.txt", "w")
        txt_sup_red_tfwr_champion_month.write(player_tfwr_champion_month.text)
        txt_sup_red_tfwr_champion_month.close()
        txt_sup_red_tfwr_champion_month_r = open(
            "txt_sup_red_tfwr_champion_month.txt", "r")
        txt_sup_red_tfwr_champion_month_text_r = txt_sup_red_tfwr_champion_month_r.read()
        print("Taxa de Vitória de Team Fights",
              txt_sup_red_tfwr_champion_month_text_r)

        # taxa de vitoria em 1v1:

        player_1v1wr_champion_month = driver.find_element_by_xpath(
            '//*[@id="graphDD24"]')
        txt_sup_red_1v1wr_champion_month = open(
            "txt_sup_red_1v1wr_champion_month.txt", "w")
        txt_sup_red_1v1wr_champion_month.write(player_1v1wr_champion_month.text)
        txt_sup_red_1v1wr_champion_month.close()
        txt_sup_red_1v1wr_champion_month_r = open(
            "txt_sup_red_1v1wr_champion_month.txt", "r")
        txt_sup_red_1v1wr_champion_month_r_text = txt_sup_red_1v1wr_champion_month_r.read()
        print("Taxa de vitória de 1v1", txt_sup_red_1v1wr_champion_month_r_text)
        # taxa de participação nas lutas:

        player_tfp_champion_month = driver.find_element_by_xpath(
            '//*[@id="graphDD26"]')
        txt_sup_red_tfp_champion_month = open(
            "txt_mid_red_tfp_champion_month.txt", "w")
        txt_sup_red_tfp_champion_month.write(player_tfp_champion_month.text)
        txt_sup_red_tfp_champion_month.close()
        txt_sup_red_tfp_champion_month_r = open(
            "txt_sup_red_tfp_champion_month.txt", "r")
        txt_sup_red_tfp_champion_month_r_text = txt_sup_red_tfp_champion_month_r.read()
        print("Taxa de participação em TFs", txt_sup_red_tfp_champion_month_r_text)
    except:
        pass

    # ENTRA NA PAGINA DO SUP NA LANE

    leaguegraph_main_profile_stats = "https://www.leagueofgraphs.com/pt/summoner/champions/"

    sup_lane = "/support"  # aqui estão identificadas as lanes
    sup_red_leaguegraph_profile = leaguegraph_main_profile_stats + \
                                   "/" + "br/" + txt_sup_red_nick_store_text_r + sup_lane
    driver.get(sup_red_leaguegraph_profile)
    time.sleep(5)
    try:
        player_gamesjogados_month = driver.find_element_by_xpath(
            '//*[@id="graphDD54"]')
        txt_sup_red_rota_gamesjogados_month = open(
            "sup_red_rota_gamesjogados_month.txt", "w")
        txt_sup_red_rota_gamesjogados_month.write(player_gamesjogados_month.text)
        txt_sup_red_rota_gamesjogados_month.close()
        txt_sup_red_rota_gamesjogados_month_r = open(
            "sup_red_rota_gamesjogados_month.txt", "r")
        txt_sup_red_rota_gamesjogados_month_text_r = txt_sup_red_rota_gamesjogados_month_r.read()
        print("Jogos na rota", sup_lane,
              "nos últimos 30 dias:", txt_sup_red_rota_gamesjogados_month_text_r)

        # coleta porcentagem de vitoria no mês com campeão
        player_wr_champion_month = driver.find_element_by_xpath(
            '//*[@id="graphDD55"]')
        txt_sup_red_rota_champion_month = open(
            "txt_sup_red_rota_champion_month.txt", "w")
        txt_sup_red_rota_champion_month.write(player_wr_champion_month.text)
        txt_sup_red_rota_champion_month.close()
        txt_sup_red_rota_champion_month_r = open(
            "txt_sup_red_rota_champion_month.txt", "r")
        txt_sup_red_rota_champion_month_text_r = txt_sup_red_rota_champion_month_r.read()
        print("Taxa de vitória:", txt_sup_red_rota_champion_month_text_r)

        # taxa de vitórias em lutas em equipe mes:

        player_tfwr_champion_month = driver.find_element_by_xpath(
            '//*[@id="graphDD23"]')
        txt_sup_red_rota_tfwr_champion_month = open(
            "txt_sup_red_rota_tfwr_champion_month.txt", "w")
        txt_sup_red_rota_tfwr_champion_month.write(
            player_tfwr_champion_month.text)
        txt_sup_red_rota_tfwr_champion_month.close()
        txt_sup_red_rota_tfwr_champion_month_r = open(
            "txt_sup_rota_red_tfwr_champion_month.txt", "r")
        txt_sup_red_rota_tfwr_champion_month_text_r = txt_sup_red_rota_tfwr_champion_month_r.read()
        print("Taxa de Vitória de Team Fights",
              txt_sup_red_rota_tfwr_champion_month_text_r)

        # taxa de vitoria em 1v1:

        player_1v1wr_champion_month = driver.find_element_by_xpath(
            '//*[@id="graphDD24"]')
        txt_sup_red_rota_1v1wr_champion_month = open(
            "txt_sup_red_rota_1v1wr_champion_month.txt", "w")
        txt_sup_red_rota_1v1wr_champion_month.write(
            player_1v1wr_champion_month.text)
        txt_sup_red_rota_1v1wr_champion_month.close()
        txt_sup_red_rota_1v1wr_champion_month_r = open(
            "txt_sup_red_rota_1v1wr_champion_month.txt", "r")
        txt_sup_red_rota_1v1wr_champion_month_r_text = txt_sup_red_rota_1v1wr_champion_month_r.read()
        print("Taxa de vitória de 1v1", txt_sup_red_rota_1v1wr_champion_month_r_text)
        # taxa de participação nas lutas:

        player_tfp_champion_month = driver.find_element_by_xpath(
            '//*[@id="graphDD26"]')
        txt_sup_red_rota_tfp_champion_month = open(
            "txt_sup_red_rota_tfp_champion_month.txt", "w")
        txt_sup_red_rota_tfp_champion_month.write(player_tfp_champion_month.text)
        txt_sup_red_rota_tfp_champion_month.close()
        txt_sup_red_rota_tfp_champion_month_r = open(
            "txt_sup_red_rota_tfp_champion_month.txt", "r")
        txt_sup_red_rota_tfp_champion_month_r_text = txt_sup_red_rota_tfp_champion_month_r.read()
        print("Taxa de participação em TFs",
              txt_sup_red_rota_tfp_champion_month_r_text)


    except:
        pass

        # SUP red - Mobalytics
    mobalytics_main_profile_stats = "https://app.mobalytics.gg/lol/profile/br/"
    sup_red_mobalytics_profile = mobalytics_main_profile_stats + \
                                  txt_sup_red_nick_store_text_r + "/" + "champions?champion=" + sup_red_champion
    driver.get(sup_red_mobalytics_profile)
    time.sleep(5)

    # winrate season sup red
    try:
    
      sup_red_champion_alltime_wr = driver.find_element_by_xpath(
          '//*[@id="app-content"]/div[1]/div[4]/div[2]/div/div[3]/div/div[2]/div[2]/div[4]/div/div[3]')
      txt_sup_red_champion_alltime_wr = open(
          "sup_red_champion_alltime_wr.txt", "w")
      txt_sup_red_champion_alltime_wr.write(sup_red_champion_alltime_wr.text)
      txt_sup_red_champion_alltime_wr.close()
      txt_sup_red_champion_alltime_wr_r = open(
          "sup_red_champion_alltime_wr.txt", "r")
      txt_sup_red_champion_alltime_wr_r_text = txt_sup_red_champion_alltime_wr_r.read()
      print("winrate:", txt_sup_red_champion_alltime_wr_r_text)
  
      # sup red kda season
      sup_red_champion_kda = driver.find_element_by_xpath(
          '//*[@id="app-content"]/div[1]/div[4]/div[2]/div/div[3]/div/div[2]/div[2]/div[5]')
      txt_sup_red_champion_kda = open("sup_red_champion_kda.txt", "w")
      txt_sup_red_champion_kda.write(sup_red_champion_kda.text)
      txt_sup_red_champion_kda.close()
      txt_sup_red_champion_kda_r = open("sup_red_champion_kda.txt", "r")
      txt_sup_red_champion_kda_r_text = txt_sup_red_champion_kda_r.read()
      print("Kda da season:", txt_sup_red_champion_kda_r_text)
  
      # vision score - sup
      sup_red_champion_ward = driver.find_element_by_xpath(
          '//*[@id="app-content"]/div[1]/div[4]/div[2]/div/div[3]/div/div[2]/div[2]/div[7]')
      txt_sup_red_champion_ward = open("txt_sup_red_champion_ward", "w")
      txt_sup_red_champion_ward.write(sup_red_champion_ward.text)
      txt_sup_red_champion_ward.close()
      txt_sup_red_champion_ward_r = open("txt_sup_red_champion_ward", "r")
      txt_sup_red_champion_ward_r_text = txt_sup_red_champion_ward_r.read()
      print("Placar de visão:", txt_sup_red_champion_ward_r_text)
  
      # numero de jogos com o campeao  sup
      sup_red_gamesplayed_champion = driver.find_element_by_xpath(
          '//*[@id="app-content"]/div[1]/div[4]/div[2]/div/div[3]/div/div[2]/div[2]/div[3]')
      txt_sup_red_gamesplayed_champion = open(
          "sup_red_gamesplayed_champion.txt", "w")
      txt_sup_red_gamesplayed_champion.write(sup_red_gamesplayed_champion.text)
      txt_sup_red_gamesplayed_champion.close()
      txt_sup_red_gamesplayed_champion_r = open(
          "sup_red_gamesplayed_champion.txt", "r")
      txt_sup_red_gamesplayed_champion_r_text = txt_sup_red_gamesplayed_champion_r.read()
      print("Jogos com o campeão:", txt_sup_red_gamesplayed_champion_r_text)

    except:
       pass
    
      # identificação de jogador para coleta de infomações dos ultimos 30 dias com o campeao:
  
      # ir para a pagina do perfil do TOPred

# ENTRA NO PERFIL DO TOP COM O CAMPEAO
    leaguegraph_main_profile_stats = "https://www.leagueofgraphs.com/pt/summoner/champions/"

    top_lane = "/top"  # aqui estão identificadas as lanes
    top_blue_leaguegraph_profile = leaguegraph_main_profile_stats + \
                                  top_blue_champion.lower() + "/" + "br/" + txt_top_blue_nick_store_text_r + top_lane
    driver.get(top_blue_leaguegraph_profile)
    time.sleep(5)

    print("Coletando informações de", txt_top_blue_nick_store_text_r)
    # script de coleta de informações jogador, indentificação de elemento + store:
    # coleta games jogados no mês com o campeao:
    try:
        player_gamesjogados_month = driver.find_element_by_xpath(
            '//*[@id="graphDD54"]')
        txt_top_blue_gamesjogados_month = open(
            "top_blue_gamesjogados_month.txt", "w")
        txt_top_blue_gamesjogados_month.write(player_gamesjogados_month.text)
        txt_top_blue_gamesjogados_month.close()
        txt_top_blue_gamesjogados_month_r = open(
            "top_blue_gamesjogados_month.txt", "r")
        txt_top_blue_gamesjogados_month_text_r = txt_top_blue_gamesjogados_month_r.read()
        print("Jogos com", txt_top_blue_champion_store_text_r,
              "nos últimos 30 dias:", txt_top_blue_gamesjogados_month_text_r)

        # coleta porcentagem de vitoria no mês com campeão
        player_wr_champion_month = driver.find_element_by_xpath(
            '//*[@id="graphDD55"]')
        txt_top_blue_wr_champion_month = open(
            "txt_top_blue_wr_champion_month.txt", "w")
        txt_top_blue_wr_champion_month.write(player_wr_champion_month.text)
        txt_top_blue_wr_champion_month.close()
        txt_top_blue_wr_champion_month_r = open(
            "txt_top_blue_wr_champion_month.txt", "r")
        txt_top_blue_wr_champion_month_text_r = txt_top_blue_wr_champion_month_r.read()
        print("Taxa de vitória:", txt_top_blue_wr_champion_month_text_r)

        # taxa de vitórias em lutas em equipe mes:

        player_tfwr_champion_month = driver.find_element_by_xpath(
            '//*[@id="graphDD23"]')
        txt_top_blue_tfwr_champion_month = open(
            "txt_top_blue_tfwr_champion_month.txt", "w")
        txt_top_blue_tfwr_champion_month.write(player_tfwr_champion_month.text)
        txt_top_blue_tfwr_champion_month.close()
        txt_top_blue_tfwr_champion_month_r = open(
            "txt_top_blue_tfwr_champion_month.txt", "r")
        txt_top_blue_tfwr_champion_month_text_r = txt_top_blue_tfwr_champion_month_r.read()
        print("Taxa de Vitória de Team Fights",
              txt_top_blue_tfwr_champion_month_text_r)

        # taxa de vitoria em 1v1:

        player_1v1wr_champion_month = driver.find_element_by_xpath(
            '//*[@id="graphDD24"]')
        txt_top_blue_1v1wr_champion_month = open(
            "txt_top_blue_1v1wr_champion_month.txt", "w")
        txt_top_blue_1v1wr_champion_month.write(player_1v1wr_champion_month.text)
        txt_top_blue_1v1wr_champion_month.close()
        txt_top_blue_1v1wr_champion_month_r = open(
            "txt_top_blue_1v1wr_champion_month.txt", "r")
        txt_top_blue_1v1wr_champion_month_r_text = txt_top_blue_1v1wr_champion_month_r.read()
        print("Taxa de vitória de 1v1", txt_top_blue_1v1wr_champion_month_r_text)
        # taxa de participação nas lutas:

        player_tfp_champion_month = driver.find_element_by_xpath(
            '//*[@id="graphDD26"]')
        txt_top_blue_tfp_champion_month = open(
            "txt_top_blue_tfp_champion_month.txt", "w")
        txt_top_blue_tfp_champion_month.write(player_tfp_champion_month.text)
        txt_top_blue_tfp_champion_month.close()
        txt_top_blue_tfp_champion_month_r = open(
            "txt_top_blue_tfp_champion_month.txt", "r")
        txt_top_blue_tfp_champion_month_r_text = txt_top_blue_tfp_champion_month_r.read()
        print("Taxa de participação em TFs", txt_top_blue_tfp_champion_month_r_text)

    except:
        pass
        # ENTRA NO PERFIL DO TOP NA ROTA
    leaguegraph_main_profile_stats = "https://www.leagueofgraphs.com/pt/summoner/champions/"

    top_lane = "/top"  # aqui estão identificadas as lanes
    top_blue_leaguegraph_profile = leaguegraph_main_profile_stats + \
                                  "/" + "br/" + txt_top_blue_nick_store_text_r + top_lane
    driver.get(top_blue_leaguegraph_profile)
    time.sleep(5)
    try:
        player_gamesjogados_month = driver.find_element_by_xpath(
            '//*[@id="graphDD54"]')
        txt_top_blue_rota_gamesjogados_month = open(
            "top_blue_rota_gamesjogados_month.txt", "w")
        txt_top_blue_rota_gamesjogados_month.write(player_gamesjogados_month.text)
        txt_top_blue_rota_gamesjogados_month.close()
        txt_top_blue_rota_gamesjogados_month_r = open(
            "top_blue_rota_gamesjogados_month.txt", "r")
        txt_top_blue_rota_gamesjogados_month_text_r = txt_top_blue_rota_gamesjogados_month_r.read()
        print("Jogos na rota", top_lane,
              "nos últimos 30 dias:", txt_top_blue_rota_gamesjogados_month_text_r)

        # coleta porcentagem de vitoria no mês com campeão
        player_wr_champion_month = driver.find_element_by_xpath(
            '//*[@id="graphDD55"]')
        txt_top_blue_rota_champion_month = open(
            "txt_top_blue_rota_champion_month.txt", "w")
        txt_top_blue_rota_champion_month.write(player_wr_champion_month.text)
        txt_top_blue_rota_champion_month.close()
        txt_top_blue_rota_champion_month_r = open(
            "txt_top_blue_rota_champion_month.txt", "r")
        txt_top_blue_rota_champion_month_text_r = txt_top_blue_rota_champion_month_r.read()
        print("Taxa de vitória:", txt_top_blue_rota_champion_month_text_r)

        # taxa de vitórias em lutas em equipe mes:

        player_tfwr_champion_month = driver.find_element_by_xpath(
            '//*[@id="graphDD23"]')
        txt_top_blue_rota_tfwr_champion_month = open(
            "txt_top_blue_rota_tfwr_champion_month.txt", "w")
        txt_top_blue_rota_tfwr_champion_month.write(
            player_tfwr_champion_month.text)
        txt_top_blue_rota_tfwr_champion_month.close()
        txt_top_blue_rota_tfwr_champion_month_r = open(
            "txt_top_blue_rota_tfwr_champion_month.txt", "r")
        txt_top_blue_rota_tfwr_champion_month_text_r = txt_top_blue_rota_tfwr_champion_month_r.read()
        print("Taxa de Vitória de Team Fights",
              txt_top_blue_rota_tfwr_champion_month_text_r)

        # taxa de vitoria em 1v1:

        player_1v1wr_champion_month = driver.find_element_by_xpath(
            '//*[@id="graphDD24"]')
        txt_top_blue_rota_1v1wr_champion_month = open(
            "txt_top_blue_rota_1v1wr_champion_month.txt", "w")
        txt_top_blue_rota_1v1wr_champion_month.write(
            player_1v1wr_champion_month.text)
        txt_top_blue_rota_1v1wr_champion_month.close()
        txt_top_blue_rota_1v1wr_champion_month_r = open(
            "txt_top_blue_rota_1v1wr_champion_month.txt", "r")
        txt_top_blue_rota_1v1wr_champion_month_r_text = txt_top_blue_rota_1v1wr_champion_month_r.read()
        print("Taxa de vitória de 1v1", txt_top_blue_rota_1v1wr_champion_month_r_text)
        # taxa de participação nas lutas:

        player_tfp_champion_month = driver.find_element_by_xpath(
            '//*[@id="graphDD26"]')
        txt_top_blue_rota_tfp_champion_month = open(
            "txt_top_blue_rota_tfp_champion_month.txt", "w")
        txt_top_blue_rota_tfp_champion_month.write(player_tfp_champion_month.text)
        txt_top_blue_rota_tfp_champion_month.close()
        txt_top_blue_rota_tfp_champion_month_r = open(
            "txt_top_blue_rota_tfp_champion_month.txt", "r")
        txt_top_blue_rota_tfp_champion_month_r_text = txt_top_blue_rota_tfp_champion_month_r.read()
        print("Taxa de participação em TFs",
              txt_top_blue_rota_tfp_champion_month_r_text)

    except:
        pass

    # TOP blue - Mobalytics
    mobalytics_main_profile_stats = "https://app.mobalytics.gg/lol/profile/br/"
    top_blue_mobalytics_profile = mobalytics_main_profile_stats + \
                                 txt_top_blue_nick_store_text_r + "/" + "champions?champion=" + top_blue_champion
    driver.get(top_blue_mobalytics_profile)
    time.sleep(5)

    try:
        top_blue_champion_alltime_wr = driver.find_element_by_xpath(
            '//*[@id="app-content"]/div[1]/div[4]/div[2]/div/div[3]/div/div[2]/div[2]/div[4]/div/div[3]')
        txt_top_blue_champion_alltime_wr = open(
            "top_blue_champion_alltime_wr.txt", "w")
        txt_top_blue_champion_alltime_wr.write(top_blue_champion_alltime_wr.text)
        txt_top_blue_champion_alltime_wr.close()
        txt_top_blue_champion_alltime_wr_r = open(
            "top_blue_champion_alltime_wr.txt", "r")
        txt_top_blue_champion_alltime_wr_r_text = txt_top_blue_champion_alltime_wr_r.read()
        print("Winrate na season:", txt_top_blue_champion_alltime_wr_r_text)

        # top blue kda season
        top_blue_champion_kda = driver.find_element_by_xpath(
            '//*[@id="app-content"]/div[1]/div[4]/div[2]/div/div[3]/div/div[2]/div[2]/div[5]')
        txt_top_blue_champion_kda = open("top_blue_champion_kda.txt", "w")
        txt_top_blue_champion_kda.write(top_blue_champion_kda.text)
        txt_top_blue_champion_kda.close()
        txt_top_blue_champion_kda_r = open("top_blue_champion_kda.txt", "r")
        txt_top_blue_champion_kda_r_text = txt_top_blue_champion_kda_r.read()
        print("KDA com o champion:", txt_top_blue_champion_kda_r_text)

        # vision score
        top_blue_champion_ward = driver.find_element_by_xpath(
            '//*[@id="app-content"]/div[1]/div[4]/div[2]/div/div[3]/div/div[2]/div[2]/div[7]')
        txt_top_blue_champion_ward = open("txt_top_blue_champion_ward", "w")
        txt_top_blue_champion_ward.write(top_blue_champion_ward.text)
        txt_top_blue_champion_ward.close()
        txt_top_blue_champion_ward_r = open("txt_top_blue_champion_ward", "r")
        txt_top_blue_champion_ward_r_text = txt_top_blue_champion_ward_r.read()
        print("Placar de visão:", txt_top_blue_champion_ward_r_text)

        # numero de jogos com o campeao
        top_blue_gamesplayed_champion = driver.find_element_by_xpath(
            '//*[@id="app-content"]/div[1]/div[4]/div[2]/div/div[3]/div/div[2]/div[2]/div[3]')
        txt_top_blue_gamesplayed_champion = open(
            "top_blue_gamesplayed_champion.txt", "w")
        txt_top_blue_gamesplayed_champion.write(top_blue_gamesplayed_champion.text)
        txt_top_blue_gamesplayed_champion.close()
        txt_top_blue_gamesplayed_champion_r = open(
            top_blue_gamesplayed_champion.txt, "r")
        txt_top_blue_gamesplayed_champion_r_text = txt_top_blue_gamesplayed_champion_r.read()
        print("Total de jogos:", txt_top_blue_gamesplayed_champion_r_text)
    except:
        pass

    # ir para a pagina do leaguegraphs do JG blue

    leaguegraph_main_profile_stats = "https://www.leagueofgraphs.com/pt/summoner/champions/"
    print("Coletando informações de", txt_jg_blue_nick_store_text_r)
    jg_lane = "/jungle"  # aqui estão identificadas as lanes

    wukongtesttop()

    jg_blue_leaguegraph_profile = leaguegraph_main_profile_stats + \
                                 jg_blue_champion.lower() + "/" + "br/" + txt_jg_blue_nick_store_text_r + jg_lane
    driver.get(jg_blue_leaguegraph_profile)
    time.sleep(5)
    # script de coleta de informações jogador, indentificação de elemento + store:
    # coleta games jogados no mês com o campeao:

    # coleta games jogados no mês com o campeao: JG
    try:
        player_gamesjogados_month = driver.find_element_by_xpath(
            '//*[@id="graphDD54"]')
        txt_jg_blue_gamesjogados_month = open(
            "jg_blue_gamesjogados_month.txt", "w")
        txt_jg_blue_gamesjogados_month.write(player_gamesjogados_month.text)
        txt_jg_blue_gamesjogados_month.close()
        txt_jg_blue_gamesjogados_month_r = open(
            "jg_blue_gamesjogados_month.txt", "r")
        txt_jg_blue_gamesjogados_month_text_r = txt_jg_blue_gamesjogados_month_r.read()
        print("Jogos com", txt_jg_blue_champion_store_text_r,
              "nos últimos 30 dias:", txt_jg_blue_gamesjogados_month_text_r)

        # coleta porcentagem de vitoria no mês com campeão
        player_wr_champion_month = driver.find_element_by_xpath(
            '//*[@id="graphDD55"]')
        txt_jg_blue_wr_champion_month = open(
            "txt_jg_blue_wr_champion_month.txt", "w")
        txt_jg_blue_wr_champion_month.write(player_wr_champion_month.text)
        txt_jg_blue_wr_champion_month.close()
        txt_jg_blue_wr_champion_month_r = open(
            "txt_jg_blue_wr_champion_month.txt", "r")
        txt_jg_blue_wr_champion_month_text_r = txt_jg_blue_wr_champion_month_r.read()
        print("Taxa de vitória:", txt_jg_blue_wr_champion_month_text_r)
        # taxa de vitórias em lutas em equipe mes:

        player_tfwr_champion_month = driver.find_element_by_xpath(
            '//*[@id="graphDD23"]')
        txt_jg_blue_tfwr_champion_month = open(
            "txt_jg_blue_tfwr_champion_month.txt", "w")
        txt_jg_blue_tfwr_champion_month.write(player_tfwr_champion_month.text)
        txt_jg_blue_tfwr_champion_month.close()
        txt_jg_blue_tfwr_champion_month_r = open(
            "txt_jg_blue_tfwr_champion_month.txt", "r")
        txt_jg_blue_tfwr_champion_month_text_r = txt_jg_blue_tfwr_champion_month_r.read()
        print("Taxa de Vitória de Team Fights",
              txt_jg_blue_tfwr_champion_month_text_r)

        # taxa de vitoria em 1v1:

        player_1v1wr_champion_month = driver.find_element_by_xpath(
            '//*[@id="graphDD24"]')
        txt_jg_blue_1v1wr_champion_month = open(
            "txt_jg_blue_1v1wr_champion_month.txt", "w")
        txt_jg_blue_1v1wr_champion_month.write(player_1v1wr_champion_month.text)
        txt_jg_blue_1v1wr_champion_month.close()
        txt_jg_blue_1v1wr_champion_month_r = open(
            "txt_jg_blue_1v1wr_champion_month.txt", "r")
        txt_jg_blue_1v1wr_champion_month_r_text = txt_jg_blue_1v1wr_champion_month_r.read()
        print("Taxa de vitória de 1v1", txt_jg_blue_1v1wr_champion_month_r_text)

        # taxa de participação nas lutas:

        player_tfp_champion_month = driver.find_element_by_xpath(
            '//*[@id="graphDD26"]')
        txt_jg_blue_tfp_champion_month = open(
            "txt_jg_blue_tfp_champion_month.txt", "w")
        txt_jg_blue_tfp_champion_month.write(player_tfp_champion_month.text)
        txt_jg_blue_tfp_champion_month.close()
        txt_jg_blue_tfp_champion_month_r = open(
            "txt_jg_blue_tfp_champion_month.txt", "r")
        txt_jg_blue_tfp_champion_month_r_text = txt_jg_blue_tfp_champion_month_r.read()
        print("Taxa de participação em TFs", txt_jg_blue_tfp_champion_month_r_text)
    except:
        pass

    # ENTRA NA PAGINA DO JG NA LANE

    leaguegraph_main_profile_stats = "https://www.leagueofgraphs.com/pt/summoner/champions/"

    jg_lane = "/jungle"  # aqui estão identificadas as lanes
    jg_blue_leaguegraph_profile = leaguegraph_main_profile_stats + \
                                 "/" + "br/" + txt_jg_blue_nick_store_text_r + jg_lane
    driver.get(jg_blue_leaguegraph_profile)
    time.sleep(5)
    try:
        player_gamesjogados_month = driver.find_element_by_xpath(
            '//*[@id="graphDD54"]')
        txt_jg_blue_rota_gamesjogados_month = open(
            "jg_blue_rota_gamesjogados_month.txt", "w")
        txt_jg_blue_rota_gamesjogados_month.write(player_gamesjogados_month.text)
        txt_jg_blue_rota_gamesjogados_month.close()
        txt_jg_blue_rota_gamesjogados_month_r = open(
            "jg_blue_rota_gamesjogados_month.txt", "r")
        txt_jg_blue_rota_gamesjogados_month_text_r = txt_jg_blue_rota_gamesjogados_month_r.read()
        print("Jogos na rota", jg_lane,
              "nos últimos 30 dias:", txt_jg_blue_rota_gamesjogados_month_text_r)

        # coleta porcentagem de vitoria no mês com campeão
        player_wr_champion_month = driver.find_element_by_xpath(
            '//*[@id="graphDD55"]')
        txt_jg_blue_rota_champion_month = open(
            "txt_jg_blue_rota_champion_month.txt", "w")
        txt_jg_blue_rota_champion_month.write(player_wr_champion_month.text)
        txt_jg_blue_rota_champion_month.close()
        txt_jg_blue_rota_champion_month_r = open(
            "txt_jg_blue_rota_champion_month.txt", "r")
        txt_jg_blue_rota_champion_month_text_r = txt_jg_blue_rota_champion_month_r.read()
        print("Taxa de vitória:", txt_jg_blue_rota_champion_month_text_r)

        # taxa de vitórias em lutas em equipe mes:

        player_tfwr_champion_month = driver.find_element_by_xpath(
            '//*[@id="graphDD23"]')
        txt_jg_blue_rota_tfwr_champion_month = open(
            "txt_jg_blue_rota_tfwr_champion_month.txt", "w")
        txt_jg_blue_rota_tfwr_champion_month.write(
            player_tfwr_champion_month.text)
        txt_jg_blue_rota_tfwr_champion_month.close()
        txt_jg_blue_rota_tfwr_champion_month_r = open(
            "txt_jg_rota_blue_tfwr_champion_month.txt", "r")
        txt_jg_blue_rota_tfwr_champion_month_text_r = txt_jg_blue_rota_tfwr_champion_month_r.read()
        print("Taxa de Vitória de Team Fights",
              txt_jg_blue_rota_tfwr_champion_month_text_r)

        # taxa de vitoria em 1v1:

        player_1v1wr_champion_month = driver.find_element_by_xpath(
            '//*[@id="graphDD24"]')
        txt_jg_blue_rota_1v1wr_champion_month = open(
            "txt_jg_blue_rota_1v1wr_champion_month.txt", "w")
        txt_jg_blue_rota_1v1wr_champion_month.write(
            player_1v1wr_champion_month.text)
        txt_jg_blue_rota_1v1wr_champion_month.close()
        txt_jg_blue_rota_1v1wr_champion_month_r = open(
            "txt_jg_blue_rota_1v1wr_champion_month.txt", "r")
        txt_jg_blue_rota_1v1wr_champion_month_r_text = txt_jg_blue_rota_1v1wr_champion_month_r.read()
        print("Taxa de vitória de 1v1", txt_jg_blue_rota_1v1wr_champion_month_r_text)
        # taxa de participação nas lutas:

        player_tfp_champion_month = driver.find_element_by_xpath(
            '//*[@id="graphDD26"]')
        txt_jg_blue_rota_tfp_champion_month = open(
            "txt_jg_blue_rota_tfp_champion_month.txt", "w")
        txt_jg_blue_rota_tfp_champion_month.write(player_tfp_champion_month.text)
        txt_jg_blue_rota_tfp_champion_month.close()
        txt_jg_blue_rota_tfp_champion_month_r = open(
            "txt_jg_blue_rota_tfp_champion_month.txt", "r")
        txt_jg_blue_rota_tfp_champion_month_r_text = txt_jg_blue_rota_tfp_champion_month_r.read()
        print("Taxa de participação em TFs",
              txt_jg_blue_rota_tfp_champion_month_r_text)

    except:
        pass

    # JG blue - Mobalytics

    mobalytics_main_profile_stats = "https://app.mobalytics.gg/lol/profile/br/"
    jg_blue_mobalytics_profile = mobalytics_main_profile_stats + \
                                txt_jg_blue_nick_store_text_r + "/" + "champions?champion=" + jg_blue_champion
    driver.get(jg_blue_mobalytics_profile)
    time.sleep(5)
    try:
        # winrate season jg blue
        jg_blue_champion_alltime_wr = driver.find_element_by_xpath(
            '//*[@id="app-content"]/div[1]/div[4]/div[2]/div/div[3]/div/div[2]/div[2]/div[4]/div/div[3]')
        txt_jg_blue_champion_alltime_wr = open(
            "jg_blue_champion_alltime_wr.txt", "w")
        txt_jg_blue_champion_alltime_wr.write(jg_blue_champion_alltime_wr.text)
        txt_jg_blue_champion_alltime_wr.close()
        txt_jg_blue_champion_alltime_wr_r = open(
            "jg_blue_champion_alltime_wr.txt", "r")
        txt_jg_blue_champion_alltime_wr_r_text = txt_jg_blue_champion_alltime_wr_r.read()
        print("Winrate da season:", txt_jg_blue_champion_alltime_wr_r_text)

        # jg blue kda season
        jg_blue_champion_kda = driver.find_element_by_xpath(
            '//*[@id="app-content"]/div[1]/div[4]/div[2]/div/div[3]/div/div[2]/div[2]/div[5]')
        txt_jg_blue_champion_kda = open("jg_blue_champion_kda.txt", "w")
        txt_jg_blue_champion_kda.write(jg_blue_champion_kda.text)
        txt_jg_blue_champion_kda.close()
        txt_jg_blue_champion_kda_r = open("jg_blue_champion_kda.txt", "r")
        txt_jg_blue_champion_kda_r_text = txt_jg_blue_champion_kda_r.read()
        print("KDA na season", txt_jg_blue_champion_kda_r_text)

        # vision score -JG
        jg_blue_champion_ward = driver.find_element_by_xpath(
            '//*[@id="app-content"]/div[1]/div[4]/div[2]/div/div[3]/div/div[2]/div[2]/div[7]')
        txt_jg_blue_champion_ward = open("txt_jg_blue_champion_ward", "w")
        txt_jg_blue_champion_ward.write(jg_blue_champion_ward.text)
        txt_jg_blue_champion_ward.close()
        txt_jg_blue_champion_ward_r = open("txt_jg_blue_champion_ward", "r")
        txt_jg_blue_champion_ward_r_text = txt_jg_blue_champion_ward_r.read()
        print("Placar de visão:", txt_jg_blue_champion_ward_r_text)

        # numero de jogos com o campeao  JG
        jg_blue_gamesplayed_champion = driver.find_element_by_xpath(
            '//*[@id="app-content"]/div[1]/div[4]/div[2]/div/div[3]/div/div[2]/div[2]/div[3]')
        txt_jg_blue_gamesplayed_champion = open(
            "jg_blue_gamesplayed_champion.txt", "w")
        txt_jg_blue_gamesplayed_champion.write(jg_blue_gamesplayed_champion.text)
        txt_jg_blue_gamesplayed_champion.close()
        txt_jg_blue_gamesplayed_champion_r = open(
            "jg_blue_gamesplayed_champion.txt", "r")
        txt_jg_blue_gamesplayed_champion_r_text = txt_jg_blue_gamesplayed_champion_r.read()
        print("Número de jogos com campeão:",
              txt_jg_blue_gamesplayed_champion_r_text)
    except:
        pass

    # MID leaguegraphs:
    leaguegraph_main_profile_stats = "https://www.leagueofgraphs.com/pt/summoner/champions/"
    print("Coletando informações de", txt_mid_blue_nick_store_text_r)
    mid_lane = "/middle"  # aqui estão identificadas as lanes
    mid_blue_leaguegraph_profile = leaguegraph_main_profile_stats + \
                                  mid_blue_champion.lower() + "/" + "br/" + txt_mid_blue_nick_store_text_r + mid_lane
    driver.get(mid_blue_leaguegraph_profile)
    time.sleep(10)

    try:
        player_gamesjogados_month = driver.find_element_by_xpath(
            '//*[@id="graphDD54"]')
        txt_mid_blue_gamesjogados_month = open(
            "mid_blue_gamesjogados_month.txt", "w")
        txt_mid_blue_gamesjogados_month.write(player_gamesjogados_month.text)
        txt_mid_blue_gamesjogados_month.close()
        txt_mid_blue_gamesjogados_month_r = open(
            "mid_blue_gamesjogados_month.txt", "r")
        txt_mid_blue_gamesjogados_month_text_r = txt_mid_blue_gamesjogados_month_r.read()
        print("Jogos com", txt_mid_blue_champion_store_text_r,
              "nos últimos 30 dias:", txt_mid_blue_gamesjogados_month_text_r)

        # coleta porcentagem de vitoria no mês com campeão
        player_wr_champion_month = driver.find_element_by_xpath(
            '//*[@id="graphDD55"]')
        txt_mid_blue_wr_champion_month = open(
            "txt_mid_blue_wr_champion_month.txt", "w")
        txt_mid_blue_wr_champion_month.write(player_wr_champion_month.text)
        txt_mid_blue_wr_champion_month.close()
        txt_mid_blue_wr_champion_month_r = open(
            "txt_mid_blue_wr_champion_month.txt", "r")
        txt_mid_blue_wr_champion_month_text_r = txt_mid_blue_wr_champion_month_r.read()
        print("Taxa de vitória:", txt_mid_blue_wr_champion_month_text_r)

        # taxa de vitórias em lutas em equipe mes:

        player_tfwr_champion_month = driver.find_element_by_xpath(
            '//*[@id="graphDD23"]')
        txt_mid_blue_tfwr_champion_month = open(
            "txt_mid_blue_tfwr_champion_month.txt", "w")
        txt_mid_blue_tfwr_champion_month.write(player_tfwr_champion_month.text)
        txt_mid_blue_tfwr_champion_month.close()
        txt_mid_blue_tfwr_champion_month_r = open(
            "txt_mid_blue_tfwr_champion_month.txt", "r")
        txt_mid_blue_tfwr_champion_month_text_r = txt_mid_blue_tfwr_champion_month_r.read()
        print("Taxa de Vitória de Team Fights",
              txt_mid_blue_tfwr_champion_month_text_r)

        # taxa de vitoria em 1v1:

        player_1v1wr_champion_month = driver.find_element_by_xpath(
            '//*[@id="graphDD24"]')
        txt_mid_blue_1v1wr_champion_month = open(
            "txt_mid_blue_1v1wr_champion_month.txt", "w")
        txt_mid_blue_1v1wr_champion_month.write(player_1v1wr_champion_month.text)
        txt_mid_blue_1v1wr_champion_month.close()
        txt_mid_blue_1v1wr_champion_month_r = open(
            "txt_mid_blue_1v1wr_champion_month.txt", "r")
        txt_mid_blue_1v1wr_champion_month_r_text = txt_mid_blue_1v1wr_champion_month_r.read()
        print("Taxa de vitória de 1v1", txt_mid_blue_1v1wr_champion_month_r_text)
        # taxa de participação nas lutas:

        player_tfp_champion_month = driver.find_element_by_xpath(
            '//*[@id="graphDD26"]')
        txt_mid_blue_tfp_champion_month = open(
            "txt_mid_blue_tfp_champion_month.txt", "w")
        txt_mid_blue_tfp_champion_month.write(player_tfp_champion_month.text)
        txt_mid_blue_tfp_champion_month.close()
        txt_mid_blue_tfp_champion_month_r = open(
            "txt_mid_blue_tfp_champion_month.txt", "r")
        txt_mid_blue_tfp_champion_month_r_text = txt_mid_blue_tfp_champion_month_r.read()
        print("Taxa de participação em TFs", txt_mid_blue_tfp_champion_month_r_text)

    except:
        pass

    # league graphs mid na rota
    mid_lane = "/middle"  # aqui estão identificadas as lanes
    mid_blue_leaguegraph_profile = leaguegraph_main_profile_stats + \
                                  "/" + "br/" + txt_mid_blue_nick_store_text_r + mid_lane
    driver.get(mid_blue_leaguegraph_profile)
    time.sleep(5)
    try:
        player_gamesjogados_month = driver.find_element_by_xpath(
            '//*[@id="graphDD54"]')
        txt_mid_blue_rota_gamesjogados_month = open(
            "mid_blue_rota_gamesjogados_month.txt", "w")
        txt_mid_blue_rota_gamesjogados_month.write(player_gamesjogados_month.text)
        txt_mid_blue_rota_gamesjogados_month.close()
        txt_mid_blue_rota_gamesjogados_month_r = open(
            "mid_blue_rota_gamesjogados_month.txt", "r")
        txt_mid_blue_rota_gamesjogados_month_text_r = txt_mid_blue_rota_gamesjogados_month_r.read()
        print("Jogos na rota", mid_lane,
              "nos últimos 30 dias:", txt_mid_blue_rota_gamesjogados_month_text_r)

        # coleta porcentagem de vitoria no mês com campeão
        player_wr_champion_month = driver.find_element_by_xpath(
            '//*[@id="graphDD55"]')
        txt_mid_blue_rota_champion_month = open(
            "txt_mid_blue_rota_champion_month.txt", "w")
        txt_mid_blue_rota_champion_month.write(player_wr_champion_month.text)
        txt_mid_blue_rota_champion_month.close()
        txt_mid_blue_rota_champion_month_r = open(
            "txt_mid_blue_rota_champion_month.txt", "r")
        txt_mid_blue_rota_champion_month_text_r = txt_mid_blue_rota_champion_month_r.read()
        print("Taxa de vitória:", txt_mid_blue_rota_champion_month_text_r)

        # taxa de vitórias em lutas em equipe mes:

        player_tfwr_champion_month = driver.find_element_by_xpath(
            '//*[@id="graphDD23"]')
        txt_mid_blue_rota_tfwr_champion_month = open(
            "txt_mid_blue_rota_tfwr_champion_month.txt", "w")
        txt_mid_blue_rota_tfwr_champion_month.write(
            player_tfwr_champion_month.text)
        txt_mid_blue_rota_tfwr_champion_month.close()
        txt_mid_blue_rota_tfwr_champion_month_r = open(
            "txt_mid_rota_blue_tfwr_champion_month.txt", "r")
        txt_mid_blue_rota_tfwr_champion_month_text_r = txt_mid_blue_rota_tfwr_champion_month_r.read()
        print("Taxa de Vitória de Team Fights",
              txt_mid_blue_rota_tfwr_champion_month_text_r)

        # taxa de vitoria em 1v1:

        player_1v1wr_champion_month = driver.find_element_by_xpath(
            '//*[@id="graphDD24"]')
        txt_mid_blue_rota_1v1wr_champion_month = open(
            "txt_top_blue_rota_1v1wr_champion_month.txt", "w")
        txt_mid_blue_rota_1v1wr_champion_month.write(
            player_1v1wr_champion_month.text)
        txt_mid_blue_rota_1v1wr_champion_month.close()
        txt_mid_blue_rota_1v1wr_champion_month_r = open(
            "txt_mid_blue_rota_1v1wr_champion_month.txt", "r")
        txt_mid_blue_rota_1v1wr_champion_month_r_text = txt_top_blue_rota_1v1wr_champion_month_r.read()
        print("Taxa de vitória de 1v1", txt_top_blue_rota_1v1wr_champion_month_r_text)
        # taxa de participação nas lutas:

        player_tfp_champion_month = driver.find_element_by_xpath(
            '//*[@id="graphDD26"]')
        txt_top_blue_rota_tfp_champion_month = open(
            "txt_top_blue_rota_tfp_champion_month.txt", "w")
        txt_top_blue_rota_tfp_champion_month.write(player_tfp_champion_month.text)
        txt_top_blue_rota_tfp_champion_month.close()
        txt_top_blue_rota_tfp_champion_month_r = open(
            "txt_top_blue_rota_tfp_champion_month.txt", "r")
        txt_top_blue_rota_tfp_champion_month_r_text = txt_top_blue_rota_tfp_champion_month_r.read()
        print("Taxa de participação em TFs",
              txt_top_blue_rota_tfp_champion_month_r_text)

    except:
        pass

    # MOBALYTICS MID

    try:
         # MID blue - Mobalytics
        mobalytics_main_profile_stats = "https://app.mobalytics.gg/lol/profile/br/"
        mid_blue_mobalytics_profile = mobalytics_main_profile_stats + \
                                     txt_mid_blue_nick_store_text_r + "/" + "champions?champion=" + mid_blue_champion
        driver.get(mid_blue_mobalytics_profile)
        time.sleep(5)
    
        # winrate season mid blue
        mid_blue_champion_alltime_wr = driver.find_element_by_xpath(
            '//*[@id="app-content"]/div[1]/div[4]/div[2]/div/div[3]/div/div[2]/div[2]/div[4]/div/div[3]')
        txt_mid_blue_champion_alltime_wr = open(
            "mid_blue_champion_alltime_wr.txt", "w")
        txt_mid_blue_champion_alltime_wr.write(mid_blue_champion_alltime_wr.text)
        txt_mid_blue_champion_alltime_wr.close()
        txt_mid_blue_champion_alltime_wr_r = open(
            "mid_blue_champion_alltime_wr.txt", "r")
        txt_mid_blue_champion_alltime_wr_r_text = txt_mid_blue_champion_alltime_wr_r.read()
        print("Winrate Mid blue season", txt_mid_blue_champion_alltime_wr_r_text)
    
        # mid blue kda season
        mid_blue_champion_kda = driver.find_element_by_xpath(
            '//*[@id="app-content"]/div[1]/div[4]/div[2]/div/div[3]/div/div[2]/div[2]/div[5]')
        txt_mid_blue_champion_kda = open("mid_blue_champion_kda.txt", "w")
        txt_mid_blue_champion_kda.write(mid_blue_champion_kda.text)
        txt_mid_blue_champion_kda.close()
        txt_mid_blue_champion_kda_r = open("mid_blue_champion_kda.txt", "r")
        txt_mid_blue_champion_kda_r_text = txt_mid_blue_champion_kda_r.read()
        print("KDA da season", txt_mid_blue_champion_kda_r_text)
    
        # vision score
        mid_blue_champion_ward = driver.find_element_by_xpath(
            '//*[@id="app-content"]/div[1]/div[4]/div[2]/div/div[3]/div/div[2]/div[2]/div[7]')
        txt_mid_blue_champion_ward = open("txt_mid_blue_champion_ward", "w")
        txt_mid_blue_champion_ward.write(mid_blue_champion_ward.text)
        txt_mid_blue_champion_ward.close()
        txt_mid_blue_champion_ward_r = open("txt_mid_blue_champion_ward", "r")
        txt_mid_blue_champion_ward_r_text = txt_mid_blue_champion_ward_r.read()
        print("Placar de visão season:", txt_mid_blue_champion_ward_r_text)
    
        # numero de jogos com o campeao
        mid_blue_gamesplayed_champion = driver.find_element_by_xpath(
            '//*[@id="app-content"]/div[1]/div[4]/div[2]/div/div[3]/div/div[2]/div[2]/div[3]')
        txt_mid_blue_gamesplayed_champion = open(
            "mid_blue_gamesplayed_champion.txt", "w")
        txt_mid_blue_gamesplayed_champion.write(
            mid_blue_gamesplayed_champion.text)
        txt_mid_blue_gamesplayed_champion.close()
        txt_mid_blue_gamesplayed_champion_r = open(
            "mid_blue_gamesplayed_champion.txt", "r")
        txt_mid_blue_gamesplayed_champion_r_text = txt_mid_blue_gamesplayed_champion_r.read()
        print(txt_mid_blue_gamesplayed_champion_r_text)
    
    except:
        pass
        
   
    # ADC leaguegraphs:

    leaguegraph_main_profile_stats = "https://www.leagueofgraphs.com/pt/summoner/champions/"
    print("Coletando informações de", txt_adc_blue_nick_store_text_r)
    adc_lane = "/adc"  # aqui estão identificadas as lanes
    adc_blue_leaguegraph_profile = leaguegraph_main_profile_stats + \
                                  adc_blue_champion.lower() + "/" + "br/" + txt_adc_blue_nick_store_text_r + adc_lane
    driver.get(adc_blue_leaguegraph_profile)
    time.sleep(10)
    try:
        player_gamesjogados_month = driver.find_element_by_xpath(
            '//*[@id="graphDD54"]')
        txt_adc_blue_gamesjogados_month = open(
            "adc_blue_gamesjogados_month.txt", "w")
        txt_adc_blue_gamesjogados_month.write(player_gamesjogados_month.text)
        txt_adc_blue_gamesjogados_month.close()
        txt_adc_blue_gamesjogados_month_r = open(
            "adc_blue_gamesjogados_month.txt", "r")
        txt_adc_blue_gamesjogados_month_text_r = txt_adc_blue_gamesjogados_month_r.read()
        print("Jogos com", txt_adc_blue_champion_store_text_r,
              "nos últimos 30 dias:", txt_adc_blue_gamesjogados_month_text_r)

        # coleta porcentagem de vitoria no mês com campeão
        player_wr_champion_month = driver.find_element_by_xpath(
            '//*[@id="graphDD55"]')
        txt_adc_blue_wr_champion_month = open(
            "txt_adc_blue_wr_champion_month.txt", "w")
        txt_adc_blue_wr_champion_month.write(player_wr_champion_month.text)
        txt_adc_blue_wr_champion_month.close()
        txt_adc_blue_wr_champion_month_r = open(
            "txt_adc_blue_wr_champion_month.txt", "r")
        txt_adc_blue_wr_champion_month_text_r = txt_adc_blue_wr_champion_month_r.read()
        print("Taxa de vitória:", txt_adc_blue_wr_champion_month_text_r)

        # taxa de vitórias em lutas em equipe mes:

        player_tfwr_champion_month = driver.find_element_by_xpath(
            '//*[@id="graphDD23"]')
        txt_adc_blue_tfwr_champion_month = open(
            "txt_adc_blue_tfwr_champion_month.txt", "w")
        txt_adc_blue_tfwr_champion_month.write(player_tfwr_champion_month.text)
        txt_adc_blue_tfwr_champion_month.close()
        txt_adc_blue_tfwr_champion_month_r = open(
            "txt_adc_blue_tfwr_champion_month.txt", "r")
        txt_adc_blue_tfwr_champion_month_text_r = txt_adc_blue_tfwr_champion_month_r.read()
        print("Taxa de Vitória de Team Fights",
              txt_adc_blue_tfwr_champion_month_text_r)

        # taxa de vitoria em 1v1:

        player_1v1wr_champion_month = driver.find_element_by_xpath(
            '//*[@id="graphDD24"]')
        txt_adc_blue_1v1wr_champion_month = open(
            "txt_adc_blue_1v1wr_champion_month.txt", "w")
        txt_adc_blue_1v1wr_champion_month.write(player_1v1wr_champion_month.text)
        txt_adc_blue_1v1wr_champion_month.close()
        txt_adc_blue_1v1wr_champion_month_r = open(
            "txt_adc_blue_1v1wr_champion_month.txt", "r")
        txt_adc_blue_1v1wr_champion_month_r_text = txt_adc_blue_1v1wr_champion_month_r.read()
        print("Taxa de vitória de 1v1", txt_adc_blue_1v1wr_champion_month_r_text)
        # taxa de participação nas lutas:

        player_tfp_champion_month = driver.find_element_by_xpath(
            '//*[@id="graphDD26"]')
        txt_adc_blue_tfp_champion_month = open(
            "txt_mid_blue_tfp_champion_month.txt", "w")
        txt_adc_blue_tfp_champion_month.write(player_tfp_champion_month.text)
        txt_adc_blue_tfp_champion_month.close()
        txt_adc_blue_tfp_champion_month_r = open(
            "txt_adc_blue_tfp_champion_month.txt", "r")
        txt_adc_blue_tfp_champion_month_r_text = txt_adc_blue_tfp_champion_month_r.read()
        print("Taxa de participação em TFs", txt_adc_blue_tfp_champion_month_r_text)
    except:
        pass

    # league graphs adc na rota
    adc_lane = "/adc"  # aqui estão identificadas as lanes
    adc_blue_leaguegraph_profile = leaguegraph_main_profile_stats + \
                                  "/" + "br/" + txt_adc_blue_nick_store_text_r + adc_lane
    driver.get(adc_blue_leaguegraph_profile)
    time.sleep(5)
    try:
        player_gamesjogados_month = driver.find_element_by_xpath(
            '//*[@id="graphDD54"]')
        txt_adc_blue_rota_gamesjogados_month = open(
            "adc_blue_rota_gamesjogados_month.txt", "w")
        txt_adc_blue_rota_gamesjogados_month.write(player_gamesjogados_month.text)
        txt_adc_blue_rota_gamesjogados_month.close()
        txt_adc_blue_rota_gamesjogados_month_r = open(
            "adc_blue_rota_gamesjogados_month.txt", "r")
        txt_adc_blue_rota_gamesjogados_month_text_r = txt_adc_blue_rota_gamesjogados_month_r.read()
        print("Jogos na rota", adc_lane,
              "nos últimos 30 dias:", txt_adc_blue_rota_gamesjogados_month_text_r)

        # coleta porcentagem de vitoria no mês com campeão
        player_wr_champion_month = driver.find_element_by_xpath(
            '//*[@id="graphDD55"]')
        txt_adc_blue_rota_champion_month = open(
            "txt_adc_blue_rota_champion_month.txt", "w")
        txt_adc_blue_rota_champion_month.write(player_wr_champion_month.text)
        txt_adc_blue_rota_champion_month.close()
        txt_adc_blue_rota_champion_month_r = open(
            "txt_adc_blue_rota_champion_month.txt", "r")
        txt_adc_blue_rota_champion_month_text_r = txt_adc_blue_rota_champion_month_r.read()
        print("Taxa de vitória:", txt_adc_blue_rota_champion_month_text_r)

        # taxa de vitórias em lutas em equipe mes:

        player_tfwr_champion_month = driver.find_element_by_xpath(
            '//*[@id="graphDD23"]')
        txt_adc_blue_rota_tfwr_champion_month = open(
            "txt_adc_blue_rota_tfwr_champion_month.txt", "w")
        txt_adc_blue_rota_tfwr_champion_month.write(
            player_tfwr_champion_month.text)
        txt_adc_blue_rota_tfwr_champion_month.close()
        txt_adc_blue_rota_tfwr_champion_month_r = open(
            "txt_adc_blue_rota_tfwr_champion_month.txt", "r")
        txt_adc_blue_rota_tfwr_champion_month_text_r = txt_adc_blue_rota_tfwr_champion_month_r.read()
        print("Taxa de Vitória de Team Fights",
              txt_adc_blue_rota_tfwr_champion_month_text_r)

        # taxa de vitoria em 1v1:

        player_1v1wr_champion_month = driver.find_element_by_xpath(
            '//*[@id="graphDD24"]')
        txt_adc_blue_rota_1v1wr_champion_month = open(
            "txt_top_blue_rota_1v1wr_champion_month.txt", "w")
        txt_adc_blue_rota_1v1wr_champion_month.write(
            player_1v1wr_champion_month.text)
        txt_adc_blue_rota_1v1wr_champion_month.close()
        txt_adc_blue_rota_1v1wr_champion_month_r = open(
            "txt_adc_blue_rota_1v1wr_champion_month.txt", "r")
        txt_adc_blue_rota_1v1wr_champion_month_r_text = txt_top_blue_rota_1v1wr_champion_month_r.read()
        print("Taxa de vitória de 1v1", txt_top_blue_rota_1v1wr_champion_month_r_text)
        # taxa de participação nas lutas:

        player_tfp_champion_month = driver.find_element_by_xpath(
            '//*[@id="graphDD26"]')
        txt_adc_blue_rota_tfp_champion_month = open(
            "txt_top_blue_rota_tfp_champion_month.txt", "w")
        txt_adc_blue_rota_tfp_champion_month.write(player_tfp_champion_month.text)
        txt_adc_blue_rota_tfp_champion_month.close()
        txt_adc_blue_rota_tfp_champion_month_r = open(
            "txt_top_blue_rota_tfp_champion_month.txt", "r")
        txt_adc_blue_rota_tfp_champion_month_r_text = txt_adc_blue_rota_tfp_champion_month_r.read()
        print("Taxa de participação em TFs",
              txt_adc_blue_rota_tfp_champion_month_r_text)

    except:
        pass

     
    try: 
        # ADC blue - Mobalytics
        mobalytics_main_profile_stats = "https://app.mobalytics.gg/lol/profile/br/"
        adc_blue_mobalytics_profile = mobalytics_main_profile_stats + \
                                     txt_adc_blue_nick_store_text_r + "/" + "champions?champion=" + adc_blue_champion
        driver.get(adc_blue_mobalytics_profile)
        time.sleep(5)
    
        # winrate season adc blue
        adc_blue_champion_alltime_wr = driver.find_element_by_xpath(
            '//*[@id="app-content"]/div[1]/div[4]/div[2]/div/div[3]/div/div[2]/div[2]/div[4]/div/div[3]')
        txt_adc_blue_champion_alltime_wr = open(
            "adc_blue_champion_alltime_wr.txt", "w")
        txt_adc_blue_champion_alltime_wr.write(adc_blue_champion_alltime_wr.text)
        txt_adc_blue_champion_alltime_wr.close()
        txt_adc_blue_champion_alltime_wr_r = open(
            "adc_blue_champion_alltime_wr.txt", "r")
        txt_adc_blue_champion_alltime_wr_r_text = txt_adc_blue_champion_alltime_wr_r.read()
        print("Winrate season:", txt_adc_blue_champion_alltime_wr_r_text)
    
        # adc blue kda season
        adc_blue_champion_kda = driver.find_element_by_xpath(
            '//*[@id="app-content"]/div[1]/div[4]/div[2]/div/div[3]/div/div[2]/div[2]/div[5]')
        txt_adc_blue_champion_kda = open("adc_blue_champion_kda.txt", "w")
        txt_adc_blue_champion_kda.write(adc_blue_champion_kda.text)
        txt_adc_blue_champion_kda.close()
        txt_adc_blue_champion_kda_r = open("adc_blue_champion_kda.txt", "r")
        txt_adc_blue_champion_kda_r_text = txt_adc_blue_champion_kda_r.read()
        print("KDA da season", txt_adc_blue_champion_kda_r_text)
        # vision score - ADc
        adc_blue_champion_ward = driver.find_element_by_xpath(
            '//*[@id="app-content"]/div[1]/div[4]/div[2]/div/div[3]/div/div[2]/div[2]/div[7]')
        txt_adc_blue_champion_ward = open("txt_adc_blue_champion_ward", "w")
        txt_adc_blue_champion_ward.write(adc_blue_champion_ward.text)
        txt_adc_blue_champion_ward.close()
        txt_adc_blue_champion_ward_r = open("txt_adc_blue_champion_ward", "r")
        txt_adc_blue_champion_ward_r_text = txt_adc_blue_champion_ward_r.read()
        print("Placar de visão:", txt_adc_blue_champion_ward_r_text)
    
        # numero de jogos com o campeao  adc
        adc_blue_gamesplayed_champion = driver.find_element_by_xpath(
            '//*[@id="app-content"]/div[1]/div[4]/div[2]/div/div[3]/div/div[2]/div[2]/div[3]')
        txt_adc_blue_gamesplayed_champion = open(
            "adc_blue_gamesplayed_champion.txt", "w")
        txt_adc_blue_gamesplayed_champion.write(adc_blue_gamesplayed_champion.text)
        txt_adc_blue_gamesplayed_champion.close()
        txt_adc_blue_gamesplayed_champion_r = open(
            "adc_blue_gamesplayed_champion.txt", "r")
        txt_adc_blue_gamesplayed_champion_r_text = txt_adc_blue_gamesplayed_champion_r.read()
        print("Nome de jogos com o campeão:", txt_adc_blue_gamesplayed_champion_r_text)
    except:
        pass
    # SUP leaguegraphs:
    
    leaguegraph_main_profile_stats = "https://www.leagueofgraphs.com/pt/summoner/champions/"
    print("Coletando informações de", txt_sup_blue_nick_store_text_r)
    sup_lane = "/support"  # aqui estão identificadas as lanes
    sup_blue_leaguegraph_profile = leaguegraph_main_profile_stats + \
                                  sup_blue_champion.lower() + "/" + "br/" + txt_sup_blue_nick_store_text_r + sup_lane
    driver.get(sup_blue_leaguegraph_profile)
    time.sleep(10)
    try:
        player_gamesjogados_month = driver.find_element_by_xpath(
            '//*[@id="graphDD54"]')
        txt_sup_blue_gamesjogados_month = open(
            "sup_blue_gamesjogados_month.txt", "w")
        txt_sup_blue_gamesjogados_month.write(player_gamesjogados_month.text)
        txt_sup_blue_gamesjogados_month.close()
        txt_sup_blue_gamesjogados_month_r = open(
            "sup_blue_gamesjogados_month.txt", "r")
        txt_sup_blue_gamesjogados_month_text_r = txt_sup_blue_gamesjogados_month_r.read()
        print("Jogos com", txt_sup_blue_champion_store_text_r,
              "nos últimos 30 dias:", txt_sup_blue_gamesjogados_month_text_r)

        # coleta porcentagem de vitoria no mês com campeão
        player_wr_champion_month = driver.find_element_by_xpath(
            '//*[@id="graphDD55"]')
        txt_sup_blue_wr_champion_month = open(
            "txt_sup_blue_wr_champion_month.txt", "w")
        txt_sup_blue_wr_champion_month.write(player_wr_champion_month.text)
        txt_sup_blue_wr_champion_month.close()
        txt_sup_blue_wr_champion_month_r = open(
            "txt_sup_blue_wr_champion_month.txt", "r")
        txt_sup_blue_wr_champion_month_text_r = txt_sup_blue_wr_champion_month_r.read()
        print("Taxa de vitória:", txt_sup_blue_wr_champion_month_text_r)

        # taxa de vitórias em lutas em equipe mes:

        player_tfwr_champion_month = driver.find_element_by_xpath(
            '//*[@id="graphDD23"]')
        txt_sup_blue_tfwr_champion_month = open(
            "txt_sup_blue_tfwr_champion_month.txt", "w")
        txt_sup_blue_tfwr_champion_month.write(player_tfwr_champion_month.text)
        txt_sup_blue_tfwr_champion_month.close()
        txt_sup_blue_tfwr_champion_month_r = open(
            "txt_sup_blue_tfwr_champion_month.txt", "r")
        txt_sup_blue_tfwr_champion_month_text_r = txt_sup_blue_tfwr_champion_month_r.read()
        print("Taxa de Vitória de Team Fights",
              txt_sup_blue_tfwr_champion_month_text_r)

        # taxa de vitoria em 1v1:

        player_1v1wr_champion_month = driver.find_element_by_xpath(
            '//*[@id="graphDD24"]')
        txt_sup_blue_1v1wr_champion_month = open(
            "txt_sup_blue_1v1wr_champion_month.txt", "w")
        txt_sup_blue_1v1wr_champion_month.write(player_1v1wr_champion_month.text)
        txt_sup_blue_1v1wr_champion_month.close()
        txt_sup_blue_1v1wr_champion_month_r = open(
            "txt_sup_blue_1v1wr_champion_month.txt", "r")
        txt_sup_blue_1v1wr_champion_month_r_text = txt_sup_blue_1v1wr_champion_month_r.read()
        print("Taxa de vitória de 1v1", txt_sup_blue_1v1wr_champion_month_r_text)
        # taxa de participação nas lutas:

        player_tfp_champion_month = driver.find_element_by_xpath(
            '//*[@id="graphDD26"]')
        txt_sup_blue_tfp_champion_month = open(
            "txt_mid_blue_tfp_champion_month.txt", "w")
        txt_sup_blue_tfp_champion_month.write(player_tfp_champion_month.text)
        txt_sup_blue_tfp_champion_month.close()
        txt_sup_blue_tfp_champion_month_r = open(
            "txt_sup_blue_tfp_champion_month.txt", "r")
        txt_sup_blue_tfp_champion_month_r_text = txt_sup_blue_tfp_champion_month_r.read()
        print("Taxa de participação em TFs", txt_sup_blue_tfp_champion_month_r_text)
    except:
        pass

    # ENTRA NA PAGINA DO SUP NA LANE

    leaguegraph_main_profile_stats = "https://www.leagueofgraphs.com/pt/summoner/champions/"

    sup_lane = "/support"  # aqui estão identificadas as lanes
    sup_blue_leaguegraph_profile = leaguegraph_main_profile_stats + \
                                  "/" + "br/" + txt_sup_blue_nick_store_text_r + sup_lane
    driver.get(sup_blue_leaguegraph_profile)
    time.sleep(5)
    try:
        player_gamesjogados_month = driver.find_element_by_xpath(
            '//*[@id="graphDD54"]')
        txt_sup_blue_rota_gamesjogados_month = open(
            "sup_blue_rota_gamesjogados_month.txt", "w")
        txt_sup_blue_rota_gamesjogados_month.write(player_gamesjogados_month.text)
        txt_sup_blue_rota_gamesjogados_month.close()
        txt_sup_blue_rota_gamesjogados_month_r = open(
            "sup_blue_rota_gamesjogados_month.txt", "r")
        txt_sup_blue_rota_gamesjogados_month_text_r = txt_sup_blue_rota_gamesjogados_month_r.read()
        print("Jogos na rota", sup_lane,
              "nos últimos 30 dias:", txt_sup_blue_rota_gamesjogados_month_text_r)

        # coleta porcentagem de vitoria no mês com campeão
        player_wr_champion_month = driver.find_element_by_xpath(
            '//*[@id="graphDD55"]')
        txt_sup_blue_rota_champion_month = open(
            "txt_sup_blue_rota_champion_month.txt", "w")
        txt_sup_blue_rota_champion_month.write(player_wr_champion_month.text)
        txt_sup_blue_rota_champion_month.close()
        txt_sup_blue_rota_champion_month_r = open(
            "txt_sup_blue_rota_champion_month.txt", "r")
        txt_sup_blue_rota_champion_month_text_r = txt_sup_blue_rota_champion_month_r.read()
        print("Taxa de vitória:", txt_sup_blue_rota_champion_month_text_r)

        # taxa de vitórias em lutas em equipe mes:

        player_tfwr_champion_month = driver.find_element_by_xpath(
            '//*[@id="graphDD23"]')
        txt_sup_blue_rota_tfwr_champion_month = open(
            "txt_sup_blue_rota_tfwr_champion_month.txt", "w")
        txt_sup_blue_rota_tfwr_champion_month.write(
            player_tfwr_champion_month.text)
        txt_sup_blue_rota_tfwr_champion_month.close()
        txt_sup_blue_rota_tfwr_champion_month_r = open(
            "txt_sup_rota_blue_tfwr_champion_month.txt", "r")
        txt_sup_blue_rota_tfwr_champion_month_text_r = txt_sup_blue_rota_tfwr_champion_month_r.read()
        print("Taxa de Vitória de Team Fights",
              txt_sup_blue_rota_tfwr_champion_month_text_r)

        # taxa de vitoria em 1v1:

        player_1v1wr_champion_month = driver.find_element_by_xpath(
            '//*[@id="graphDD24"]')
        txt_sup_blue_rota_1v1wr_champion_month = open(
            "txt_sup_blue_rota_1v1wr_champion_month.txt", "w")
        txt_sup_blue_rota_1v1wr_champion_month.write(
            player_1v1wr_champion_month.text)
        txt_sup_blue_rota_1v1wr_champion_month.close()
        txt_sup_blue_rota_1v1wr_champion_month_r = open(
            "txt_sup_blue_rota_1v1wr_champion_month.txt", "r")
        txt_sup_blue_rota_1v1wr_champion_month_r_text = txt_sup_blue_rota_1v1wr_champion_month_r.read()
        print("Taxa de vitória de 1v1", txt_sup_blue_rota_1v1wr_champion_month_r_text)
        # taxa de participação nas lutas:

        player_tfp_champion_month = driver.find_element_by_xpath(
            '//*[@id="graphDD26"]')
        txt_sup_blue_rota_tfp_champion_month = open(
            "txt_sup_blue_rota_tfp_champion_month.txt", "w")
        txt_sup_blue_rota_tfp_champion_month.write(player_tfp_champion_month.text)
        txt_sup_blue_rota_tfp_champion_month.close()
        txt_sup_blue_rota_tfp_champion_month_r = open(
            "txt_sup_blue_rota_tfp_champion_month.txt", "r")
        txt_sup_blue_rota_tfp_champion_month_r_text = txt_sup_blue_rota_tfp_champion_month_r.read()
        print("Taxa de participação em TFs",
              txt_sup_blue_rota_tfp_champion_month_r_text)


    except:
        pass

    try:
            # SUP blue - Mobalytics
        mobalytics_main_profile_stats = "https://app.mobalytics.gg/lol/profile/br/"
        sup_blue_mobalytics_profile = mobalytics_main_profile_stats + \
                                     txt_sup_blue_nick_store_text_r + "/" + "champions?champion=" + sup_blue_champion
        driver.get(sup_blue_mobalytics_profile)
        time.sleep(5)
    
        # winrate season sup blue
        sup_blue_champion_alltime_wr = driver.find_element_by_xpath(
            '//*[@id="app-content"]/div[1]/div[4]/div[2]/div/div[3]/div/div[2]/div[2]/div[4]/div/div[3]')
        txt_sup_blue_champion_alltime_wr = open(
            "sup_blue_champion_alltime_wr.txt", "w")
        txt_sup_blue_champion_alltime_wr.write(sup_blue_champion_alltime_wr.text)
        txt_sup_blue_champion_alltime_wr.close()
        txt_sup_blue_champion_alltime_wr_r = open(
            "sup_blue_champion_alltime_wr.txt", "r")
        txt_sup_blue_champion_alltime_wr_r_text = txt_sup_blue_champion_alltime_wr_r.read()
        print("winrate:", txt_sup_blue_champion_alltime_wr_r_text)
    
        # sup blue kda season
        sup_blue_champion_kda = driver.find_element_by_xpath(
            '//*[@id="app-content"]/div[1]/div[4]/div[2]/div/div[3]/div/div[2]/div[2]/div[5]')
        txt_sup_blue_champion_kda = open("sup_blue_champion_kda.txt", "w")
        txt_sup_blue_champion_kda.write(sup_blue_champion_kda.text)
        txt_sup_blue_champion_kda.close()
        txt_sup_blue_champion_kda_r = open("sup_blue_champion_kda.txt", "r")
        txt_sup_blue_champion_kda_r_text = txt_sup_blue_champion_kda_r.read()
        print("Kda da season:", txt_sup_blue_champion_kda_r_text)
    
        # vision score - sup
        sup_blue_champion_ward = driver.find_element_by_xpath(
            '//*[@id="app-content"]/div[1]/div[4]/div[2]/div/div[3]/div/div[2]/div[2]/div[7]')
        txt_sup_blue_champion_ward = open("txt_sup_blue_champion_ward", "w")
        txt_sup_blue_champion_ward.write(sup_blue_champion_ward.text)
        txt_sup_blue_champion_ward.close()
        txt_sup_blue_champion_ward_r = open("txt_sup_blue_champion_ward", "r")
        txt_sup_blue_champion_ward_r_text = txt_sup_blue_champion_ward_r.read()
        print("Placar de visão:", txt_sup_blue_champion_ward_r_text)
    
        # numero de jogos com o campeao  sup
        sup_blue_gamesplayed_champion = driver.find_element_by_xpath(
            '//*[@id="app-content"]/div[1]/div[4]/div[2]/div/div[3]/div/div[2]/div[2]/div[3]')
        txt_sup_blue_gamesplayed_champion = open(
            "sup_blue_gamesplayed_champion.txt", "w")
        txt_sup_blue_gamesplayed_champion.write(sup_blue_gamesplayed_champion.text)
        txt_sup_blue_gamesplayed_champion.close()
        txt_sup_blue_gamesplayed_champion_r = open(
            "sup_blue_gamesplayed_champion.txt", "r")
        txt_sup_blue_gamesplayed_champion_r_text = txt_sup_blue_gamesplayed_champion_r.read()
        print("Jogos com o campeão:", txt_sup_blue_gamesplayed_champion_r_text)












    except:
        pass


       #variables for use
def data():       
        p = -1

        top_red1v1 = 0
        top_blue1v1 = 0
        
        
        
        #champion name top
        txt_top_red_champion_store_r = open("top_red_champion.txt", "r")
        txt_top_red_champion_store_text_r = txt_top_red_champion_store_r.read()


        txt_top_blue_champion_store_r = open("top_blue_champion.txt", "r")
        txt_top_blue_champion_store_text_r = txt_top_blue_champion_store_r.read()


        print(txt_top_red_champion_store_text_r, "vs", txt_top_blue_champion_store_text_r)


      #Opens month champion winrate
        txt_top_red_wr_champion_month_r = open("C:/xampp/htdocs/PogDotGG/bin/txt_top_red_wr_champion_month.txt", "r")
        txt_top_red_wr_champion_month_text_r = txt_top_red_wr_champion_month_r.read()
        trwrchampion_month = txt_top_red_wr_champion_month_text_r.strip('%')
        trwrchampion_month_float = float(trwrchampion_month)
        
        print("Taxa de vitória RED:", trwrchampion_month)
        time.sleep(0)

        txt_top_blue_wr_champion_month_r = open(
            "txt_top_blue_wr_champion_month.txt", "r")
        txt_top_blue_wr_champion_month_text_r = txt_top_blue_wr_champion_month_r.read()
        tbwrchampion_month = txt_top_blue_wr_champion_month_text_r.strip('%')
        tbwrchampion_month_float = float(tbwrchampion_month)
        print("Taxa de vitória BLUE:", tbwrchampion_month)
        time.sleep(0)

         #calculates the difference
        if tbwrchampion_month_float < trwrchampion_month_float:                                                         
            print("Red wins")
            time.sleep(0)
            
            twrchampion_month_result = (tbwrchampion_month_float-trwrchampion_month_float) * p
            winner1top = "red"
            top_red1v1 = top_red1v1 + twrchampion_month_result
            print("Até então Blue points:", top_blue1v1)
            time.sleep(0)
            print("Até então Red points:", top_red1v1)
            time.sleep(0)



        else:
            print("blue Wins")
            time.sleep(0)
            twbchampion_month_result = (tbwrchampion_month_float-trwrchampion_month_float) *p
            print(twbchampion_month_result)
            time.sleep(0)
            winner1top = "blue"
            top_blue1v1 = top_blue1v1 + twbchampion_month_result
            print("Até então Blue points:", top_blue1v1)
            print("Até então Red points:", top_red1v1)
            time.sleep(0)


      
      
      
      

            
        




       #difference in lane winrate

        

         #Opens month champion winrate rota top blue
        txt_top_red_rota_champion_month_r = open("C:/xampp/htdocs/PogDotGG/txt_top_red_rota_champion_month.txt", "r")
        txt_top_red_rota_champion_month_text_r = txt_top_red_rota_champion_month_r.read()
        trwrrota_month = txt_top_red_rota_champion_month_text_r.strip('%')
        trwrrota_month_float = float(trwrrota_month)
        txt_top_red_rota_champion_month_r.close()
        print("Taxa de vitória RED:", trwrrota_month_float)
        time.sleep(0)





        txt_top_blue_rota_champion_month_r = open("txt_top_blue_rota_wr_champion_month.txt", "r")
        txt_top_blue_rota_champion_month_text_r = txt_top_blue_rota_champion_month_r.read()
        tbwrrota_month = txt_top_blue_rota_champion_month_text_r.strip('%')
        tbwrrota_month_float = float(tbwrrota_month)
        print("Taxa de vitória BLUE:", tbwrrota_month_float)
        txt_top_blue_rota_champion_month_r.close()
        #calculates difference:
        if trwrrota_month_float > tbwrrota_month_float:                                 
          
          print("Red wins")
          time.sleep(0)
          
          twrrota_month_result = (tbwrrota_month_float-trwrrota_month_float) * p
    
          winner1top = "red"
          print(top_red1v1)
          time.sleep(0)

          
          top_blue1v1 = float(top_blue1v1 + twrrota_month_result)
          print(top_red1v1)
          time.sleep(0)

          print("Até então Blue points:", top_blue1v1)
          time.sleep(0)
          print("Até então Red points:", top_red1v1)
          time.sleep(0)

        else:
             
         print("Blue wins")
         time.sleep(0)

         twrbrota_month_result = (tbwrrota_month_float-trwrrota_month_float) * p
         print(twrbrota_month_result)
         time.sleep(0)
         winner1top = "blue"
        
         top_blue1v1 = top_blue1v1 + twrbrota_month_result
         print(top_blue1v1)
         time.sleep(0)   
 
           #evaluates the quality of the player top champion red
  
        if (trwrchampion_month_float + trwrrota_month_float) / 2 > 50:
            top_red_quality =  1     

        else: 
            top_red_quality = 0


        if top_red_quality == 1:
            print("Jogador bom no TOP Vermelho")
            time.sleep(0)
        else:
            print("Jogador ruim no TOP Azul")  
            time.sleep(0)



            #evaluates the quality of the player top champion blue

        overall_red_top = (trwrchampion_month_float + trwrrota_month_float) / 2
        overall_blue_top = (tbwrchampion_month_float + tbwrrota_month_float) / 2
    
        print("Over all top RED", overall_red_top)
        time.sleep(0)
        print("Over all top blue", overall_blue_top)
        time.sleep(0)
        
        if overall_red_top > 50:
            top_blue_quality =  1     
        else: 
            top_blue_quality = 0   
 
        if overall_blue_top > 50:

           print("Jogador bom no top Azul")
        else:
           print("Jogador ruim no top Azul") 

        print("Resultado final:")
        print("Over all do top RED")
        print(overall_red_top)
        print("Over all do top Azul")
        print(overall_blue_top)

    #variables for use
       
        p = -1
        jg_red1v1 = 0
        jg_blue1v1 = 0
        
    
    
        #champion name jg
        txt_jg_red_champion_store_r = open("jg_red_champion.txt", "r")
        txt_jg_red_champion_store_text_r = txt_jg_red_champion_store_r.read()
        txt_jg_blue_champion_store_r = open("jg_blue_champion.txt", "r")
        txt_jg_blue_champion_store_text_r = txt_jg_blue_champion_store_r.read()
        print(txt_jg_red_champion_store_text_r, "vs", txt_jg_blue_champion_store_text_r)
        #Opens month champion winrate
        txt_jg_red_wr_champion_month_r = open("C:/xampp/htdocs/PogDotGG/bin/txt_jg_red_wr_champion_month.txt", "r")
        txt_jg_red_wr_champion_month_text_r = txt_jg_red_wr_champion_month_r.read()
        trwrchampion_month = txt_jg_red_wr_champion_month_text_r.strip('%')
        trwrchampion_month_float = float(trwrchampion_month)
        
        print("Taxa de vitória RED:", trwrchampion_month)
        time.sleep(0)
        txt_jg_blue_wr_champion_month_r = open(
            "txt_jg_blue_wr_champion_month.txt", "r")
        txt_jg_blue_wr_champion_month_text_r = txt_jg_blue_wr_champion_month_r.read()
        tbwrchampion_month = txt_jg_blue_wr_champion_month_text_r.strip('%')
        tbwrchampion_month_float = float(tbwrchampion_month)
        print("Taxa de vitória BLUE:", tbwrchampion_month)
        time.sleep(0)
         #calculates the difference
        if tbwrchampion_month_float < trwrchampion_month_float:                                                     
            print("Red wins")
            time.sleep(0)
            
            twrchampion_month_result = (tbwrchampion_month_float-trwrchampion_month_float) * p
            winner1jg = "red"
            jg_red1v1 = jg_red1v1 + twrchampion_month_result
            print("Até então Blue points:", jg_blue1v1)
            time.sleep(0)
            print("Até então Red points:", jg_red1v1)
            time.sleep(0)
        else:
            print("blue Wins")
            time.sleep(0)
            twbchampion_month_result = (tbwrchampion_month_float-trwrchampion_month_float) *p
            print(twbchampion_month_result)
            time.sleep(0)
            winner1jg = "blue"
            jg_blue1v1 = jg_blue1v1 + twbchampion_month_result
            print("Até então Blue points:", jg_blue1v1)
            print("Até então Red points:", jg_red1v1)
            time.sleep(0)
            
        
        #difference in lane winrate
        
         #Opens month champion winrate rota jg blue
        txt_jg_red_rota_champion_month_r = open("C:/xampp/htdocs/PogDotGG/txt_jg_red_rota_champion_month.txt", "r")
        txt_jg_red_rota_champion_month_text_r = txt_jg_red_rota_champion_month_r.read()
        trwrrota_month = txt_jg_red_rota_champion_month_text_r.strip('%')
        trwrrota_month_float = float(trwrrota_month)
        txt_jg_red_rota_champion_month_r.close()
        print("Taxa de vitória RED:", trwrrota_month_float)
        time.sleep(0)
        txt_jg_blue_rota_champion_month_r = open("txt_jg_blue_rota_wr_champion_month.txt", "r")
        txt_jg_blue_rota_champion_month_text_r = txt_jg_blue_rota_champion_month_r.read()
        tbwrrota_month = txt_jg_blue_rota_champion_month_text_r.strip('%')
        tbwrrota_month_float = float(tbwrrota_month)
        print("Taxa de vitória BLUE:", tbwrrota_month_float)
        txt_jg_blue_rota_champion_month_r.close()
        #calculates difference:
        if trwrrota_month_float > tbwrrota_month_float:                                 
          
          print("Red wins")
          time.sleep(0)
          
          twrrota_month_result = (tbwrrota_month_float-trwrrota_month_float) * p
          winner1jg = "red"
          print(jg_red1v1)
          time.sleep(0)
          
          jg_blue1v1 = float(jg_blue1v1 + twrrota_month_result)
          print(jg_red1v1)
          time.sleep(0)
          print("Até então Blue points:", jg_blue1v1)
          time.sleep(0)
          print("Até então Red points:", jg_red1v1)
          time.sleep(0)
        else:
             
         print("Blue wins")
         time.sleep(0)
         twrbrota_month_result = (tbwrrota_month_float-trwrrota_month_float) * p
         print(twrbrota_month_result)
         time.sleep(0)
         winner1jg = "blue"
        
         jg_blue1v1 = jg_blue1v1 + twrbrota_month_result
         print(jg_blue1v1)
         time.sleep(0)   
           #evaluates the quality of the player jg champion red
        if (trwrchampion_month_float + trwrrota_month_float) / 2 > 50:
            jg_red_quality =  1     
        else: 
            jg_red_quality = 0
        if jg_red_quality == 1:
            print("Jogador bom no TOP Vermelho")
            time.sleep(0)
        else:
            print("Jogador ruim no TOP Azul")  
            time.sleep(0)
            #evaluates the quality of the player jg champion blue
        overall_red_jg = (trwrchampion_month_float + trwrrota_month_float) / 2
        overall_blue_jg = (tbwrchampion_month_float + tbwrrota_month_float) / 2
        print("Over all jg RED", overall_red_jg)
        time.sleep(0)
        print("Over all jg blue", overall_blue_jg)
        time.sleep(0)
        
        if overall_red_jg > 50:
            jg_blue_quality =  1     
        else: 
            jg_blue_quality = 0   
        if overall_blue_jg > 50:
           print("Jogador bom no jg Azul")
        else:
           print("Jogador ruim no jg Azul") 
        print("Resultado final:")
        print("Over all do jg RED")
        print(overall_red_jg)
        print("Over all do jg Azul")
        print(overall_blue_jg)        
        #variables for use
          
        p = -1
        mid_red1v1 = 0
        mid_blue1v1 = 0
        
        
        
        #champion name mid
        txt_mid_red_champion_store_r = open("mid_red_champion.txt", "r")
        txt_mid_red_champion_store_text_r = txt_mid_red_champion_store_r.read()
        txt_mid_blue_champion_store_r = open("mid_blue_champion.txt", "r")
        txt_mid_blue_champion_store_text_r = txt_mid_blue_champion_store_r.read()
        print(txt_mid_red_champion_store_text_r, "vs", txt_mid_blue_champion_store_text_r)
        #Opens month champion winrate
        txt_mid_red_wr_champion_month_r = open("C:/xampp/htdocs/PogDotGG/bin/txt_mid_red_wr_champion_month.txt", "r")
        txt_mid_red_wr_champion_month_text_r = txt_mid_red_wr_champion_month_r.read()
        trwrchampion_month = txt_mid_red_wr_champion_month_text_r.strip('%')
        trwrchampion_month_float = float(trwrchampion_month)
        
        print("Taxa de vitória RED:", trwrchampion_month)
        time.sleep(0)
        txt_mid_blue_wr_champion_month_r = open(
            "txt_mid_blue_wr_champion_month.txt", "r")
        txt_mid_blue_wr_champion_month_text_r = txt_mid_blue_wr_champion_month_r.read()
        tbwrchampion_month = txt_mid_blue_wr_champion_month_text_r.strip('%')
        tbwrchampion_month_float = float(tbwrchampion_month)
        print("Taxa de vitória BLUE:", tbwrchampion_month)
        time.sleep(0)
         #calculates the difference
        if tbwrchampion_month_float < trwrchampion_month_float:                                                     
            print("Red wins")
            time.sleep(0)
            
            twrchampion_month_result = (tbwrchampion_month_float-trwrchampion_month_float) * p
            winner1mid = "red"
            mid_red1v1 = mid_red1v1 + twrchampion_month_result
            print("Até então Blue points:", mid_blue1v1)
            time.sleep(0)
            print("Até então Red points:", mid_red1v1)
            time.sleep(0)
        else:
            print("blue Wins")
            time.sleep(0)
            twbchampion_month_result = (tbwrchampion_month_float-trwrchampion_month_float) *p
            print(twbchampion_month_result)
            time.sleep(0)
            winner1mid = "blue"
            mid_blue1v1 = mid_blue1v1 + twbchampion_month_result
            print("Até então Blue points:", mid_blue1v1)
            print("Até então Red points:", mid_red1v1)
            time.sleep(0)
            
        
        #difference in lane winrate
        
         #Opens month champion winrate rota mid blue
        txt_mid_red_rota_champion_month_r = open("C:/xampp/htdocs/PogDotGG/txt_mid_red_rota_champion_month.txt", "r")
        txt_mid_red_rota_champion_month_text_r = txt_mid_red_rota_champion_month_r.read()
        trwrrota_month = txt_mid_red_rota_champion_month_text_r.strip('%')
        trwrrota_month_float = float(trwrrota_month)
        txt_mid_red_rota_champion_month_r.close()
        print("Taxa de vitória RED:", trwrrota_month_float)
        time.sleep(0)
        txt_mid_blue_rota_champion_month_r = open("txt_mid_blue_rota_wr_champion_month.txt", "r")
        txt_mid_blue_rota_champion_month_text_r = txt_mid_blue_rota_champion_month_r.read()
        tbwrrota_month = txt_mid_blue_rota_champion_month_text_r.strip('%')
        tbwrrota_month_float = float(tbwrrota_month)
        print("Taxa de vitória BLUE:", tbwrrota_month_float)
        txt_mid_blue_rota_champion_month_r.close()
        #calculates difference:
        if trwrrota_month_float > tbwrrota_month_float:                                 
          
          print("Red wins")
          time.sleep(0)
          
          twrrota_month_result = (tbwrrota_month_float-trwrrota_month_float) * p
          winner1mid = "red"
          print(mid_red1v1)
          time.sleep(0)
          
          mid_blue1v1 = float(mid_blue1v1 + twrrota_month_result)
          print(mid_red1v1)
          time.sleep(0)
          print("Até então Blue points:", mid_blue1v1)
          time.sleep(0)
          print("Até então Red points:", mid_red1v1)
          time.sleep(0)
        else:
             
         print("Blue wins")
         time.sleep(0)
         twrbrota_month_result = (tbwrrota_month_float-trwrrota_month_float)
         print(twrbrota_month_result)
         time.sleep(0)
         winner1mid = "blue"
        
         mid_blue1v1 = mid_blue1v1 + twrbrota_month_result
         print(mid_blue1v1)
         time.sleep(0)   
           #evaluates the quality of the player mid champion red
        if (trwrchampion_month_float + trwrrota_month_float) / 2 > 50:
            mid_red_quality =  1     
        else: 
            mid_red_quality = 0
        if mid_red_quality == 1:
            print("Jogador bom no TOP Vermelho")
            time.sleep(0)
        else:
            print("Jogador ruim no TOP Azul")  
            time.sleep(0)
            #evaluates the quality of the player mid champion blue
        overall_red_mid = (trwrchampion_month_float + trwrrota_month_float) / 2
        overall_blue_mid = (tbwrchampion_month_float + tbwrrota_month_float) / 2
        print("Over all mid RED", overall_red_mid)
        time.sleep(0)
        print("Over all mid blue", overall_blue_mid)
        time.sleep(0)
        
        if overall_red_mid > 50:
            mid_blue_quality =  1     
        else: 
            mid_blue_quality = 0   
        if overall_blue_mid > 50:
           print("Jogador bom no mid Azul")
        else:
           print("Jogador ruim no mid Azul") 
        print("Resultado final:")
        print("Over all do mid RED")
        print(overall_red_mid)
        print("Over all do mid Azul")
        print(overall_blue_mid)
        p = -1
        adc_red1v1 = 0
        adc_blue1v1 = 0
        
        
        
        #champion name adc
        txt_adc_red_champion_store_r = open("adc_red_champion.txt", "r")
        txt_adc_red_champion_store_text_r = txt_adc_red_champion_store_r.read()
        txt_adc_blue_champion_store_r = open("adc_blue_champion.txt", "r")
        txt_adc_blue_champion_store_text_r = txt_adc_blue_champion_store_r.read()
        print(txt_adc_red_champion_store_text_r, "vs", txt_adc_blue_champion_store_text_r)
        #Opens month champion winrate
        txt_adc_red_wr_champion_month_r = open("C:/xampp/htdocs/PogDotGG/bin/txt_adc_red_wr_champion_month.txt", "r")
        txt_adc_red_wr_champion_month_text_r = txt_adc_red_wr_champion_month_r.read()
        trwrchampion_month = txt_adc_red_wr_champion_month_text_r.strip('%')
        trwrchampion_month_float = float(trwrchampion_month)
        
        print("Taxa de vitória RED:", trwrchampion_month)
        time.sleep(0)
        txt_adc_blue_wr_champion_month_r = open(
            "txt_adc_blue_wr_champion_month.txt", "r")
        txt_adc_blue_wr_champion_month_text_r = txt_adc_blue_wr_champion_month_r.read()
        tbwrchampion_month = txt_adc_blue_wr_champion_month_text_r.strip('%')
        tbwrchampion_month_float = float(tbwrchampion_month)
        print("Taxa de vitória BLUE:", tbwrchampion_month)
        time.sleep(0)
         #calculates the difference
        if tbwrchampion_month_float < trwrchampion_month_float:                                                     
            print("Red wins")
            time.sleep(0)
            
            twrchampion_month_result = (tbwrchampion_month_float-trwrchampion_month_float) * p
            winner1adc = "red"
            adc_red1v1 = adc_red1v1 + twrchampion_month_result
            print("Até então Blue points:", adc_blue1v1)
            time.sleep(0)
            print("Até então Red points:", adc_red1v1)
            time.sleep(0)
        else:
            print("blue Wins")
            time.sleep(0)
            twbchampion_month_result = (tbwrchampion_month_float-trwrchampion_month_float) *p
            print(twbchampion_month_result)
            time.sleep(0)
            winner1adc = "blue"
            adc_blue1v1 = adc_blue1v1 + twbchampion_month_result
            print("Até então Blue points:", adc_blue1v1)
            print("Até então Red points:", adc_red1v1)
            time.sleep(0)
            
        
   #     difference in lane winrate
        
         #Opens month champion winrate rota adc blue
        txt_adc_red_rota_champion_month_r = open("C:/xampp/htdocs/PogDotGG/txt_adc_red_rota_champion_month.txt", "r")
        txt_adc_red_rota_champion_month_text_r = txt_adc_red_rota_champion_month_r.read()
        trwrrota_month = txt_adc_red_rota_champion_month_text_r.strip('%')
        trwrrota_month_float = float(trwrrota_month)
        txt_adc_red_rota_champion_month_r.close()
        print("Taxa de vitória RED:", trwrrota_month_float)
        time.sleep(0)
        txt_adc_blue_rota_champion_month_r = open("txt_adc_blue_rota_wr_champion_month.txt", "r")
        txt_adc_blue_rota_champion_month_text_r = txt_adc_blue_rota_champion_month_r.read()
        tbwrrota_month = txt_adc_blue_rota_champion_month_text_r.strip('%')
        tbwrrota_month_float = float(tbwrrota_month)
        print("Taxa de vitória BLUE:", tbwrrota_month_float)
        txt_adc_blue_rota_champion_month_r.close()
        #calculates difference:
        if trwrrota_month_float > tbwrrota_month_float:                                 
          
          print("Red wins")
          time.sleep(0)
          
          twrrota_month_result = (tbwrrota_month_float-trwrrota_month_float) * p
          winner1adc = "red"
          print(adc_red1v1)
          time.sleep(0)
          
          adc_blue1v1 = float(adc_blue1v1 + twrrota_month_result)
          print(adc_red1v1)
          time.sleep(0)
          print("Até então Blue points:", adc_blue1v1)
          time.sleep(0)
          print("Até então Red points:", adc_red1v1)
          time.sleep(0)
        else:
             
         print("Blue wins")
         time.sleep(0)
         twrbrota_month_result = (tbwrrota_month_float-trwrrota_month_float) * p
         print(twrbrota_month_result)
         time.sleep(0)
         winner1adc = "blue"
        
         adc_blue1v1 = adc_blue1v1 + twrbrota_month_result
         print(adc_blue1v1)
         time.sleep(0)   
           #evaluates the quality of the player adc champion red
        if (trwrchampion_month_float + trwrrota_month_float) / 2 > 50:
            adc_red_quality =  1     
        else: 
            adc_red_quality = 0
        if adc_red_quality == 1:
            print("Jogador bom no TOP Vermelho")
            time.sleep(0)
        else:
            print("Jogador ruim no TOP Azul")  
            time.sleep(0)
            #evaluates the quality of the player adc champion blue
        overall_red_adc = (trwrchampion_month_float + trwrrota_month_float) / 2
        overall_blue_adc = (tbwrchampion_month_float + tbwrrota_month_float) / 2
        print("Over all adc RED", overall_red_adc)
        time.sleep(0)
        print("Over all adc blue", overall_blue_adc)
        time.sleep(0)
        
        if overall_red_adc > 50:
            adc_blue_quality =  1     
        else: 
            adc_blue_quality = 0   
        if overall_blue_adc > 50:
           print("Jogador bom no adc Azul")
        else:
           print("Jogador ruim no adc Azul") 
        print("Resultado final:")
        print("Over all do adc RED")
        print(overall_red_adc)
        print("Over all do adc Azul")
        print(overall_blue_adc)
        p = -1
        sup_red1v1 = 0
        sup_blue1v1 = 0
        
        
        
        #champion name sup
        txt_sup_red_champion_store_r = open("sup_red_champion.txt", "r")
        txt_sup_red_champion_store_text_r = txt_sup_red_champion_store_r.read()
        txt_sup_blue_champion_store_r = open("sup_blue_champion.txt", "r")
        txt_sup_blue_champion_store_text_r = txt_sup_blue_champion_store_r.read()
        print(txt_sup_red_champion_store_text_r, "vs", txt_sup_blue_champion_store_text_r)
        #Opens month champion winrate
        txt_sup_red_wr_champion_month_r = open("C:/xampp/htdocs/PogDotGG/bin/txt_sup_red_wr_champion_month.txt", "r")
        txt_sup_red_wr_champion_month_text_r = txt_sup_red_wr_champion_month_r.read()
        trwrchampion_month = txt_sup_red_wr_champion_month_text_r.strip('%')
        trwrchampion_month_float = float(trwrchampion_month)
        
        print("Taxa de vitória RED:", trwrchampion_month)
        time.sleep(0)
        txt_sup_blue_wr_champion_month_r = open(
            "txt_sup_blue_wr_champion_month.txt", "r")
        txt_sup_blue_wr_champion_month_text_r = txt_sup_blue_wr_champion_month_r.read()
        tbwrchampion_month = txt_sup_blue_wr_champion_month_text_r.strip('%')
        tbwrchampion_month_float = float(tbwrchampion_month)
        print("Taxa de vitória BLUE:", tbwrchampion_month)
        time.sleep(0)
         #calculates the difference
        if tbwrchampion_month_float < trwrchampion_month_float:                                                     
            print("Red wins")
            time.sleep(0)
            
            twrchampion_month_result = (tbwrchampion_month_float-trwrchampion_month_float) * p
            winner1sup = "red"
            sup_red1v1 = sup_red1v1 + twrchampion_month_result
            print("Até então Blue points:", sup_blue1v1)
            time.sleep(0)
            print("Até então Red points:", sup_red1v1)
            time.sleep(0)
        else:
            print("blue Wins")
            time.sleep(0)
            twbchampion_month_result = (tbwrchampion_month_float-trwrchampion_month_float) *p
            print(twbchampion_month_result)
            time.sleep(0)
            winner1sup = "blue"
            sup_blue1v1 = sup_blue1v1 + twbchampion_month_result
            print("Até então Blue points:", sup_blue1v1)
            print("Até então Red points:", sup_red1v1)
            time.sleep(0)
            
        
        #difference in lane winrate
        
         #Opens month champion winrate rota sup blue
        txt_sup_red_rota_champion_month_r = open("C:/xampp/htdocs/PogDotGG/txt_sup_red_rota_champion_month.txt", "r")
        txt_sup_red_rota_champion_month_text_r = txt_sup_red_rota_champion_month_r.read()
        trwrrota_month = txt_sup_red_rota_champion_month_text_r.strip('%')
        trwrrota_month_float = float(trwrrota_month)
        txt_sup_red_rota_champion_month_r.close()
        print("Taxa de vitória RED:", trwrrota_month_float)
        time.sleep(0)
        txt_sup_blue_rota_champion_month_r = open("txt_sup_blue_rota_wr_champion_month.txt", "r")
        txt_sup_blue_rota_champion_month_text_r = txt_sup_blue_rota_champion_month_r.read()
        tbwrrota_month = txt_sup_blue_rota_champion_month_text_r.strip('%')
        tbwrrota_month_float = float(tbwrrota_month)
        print("Taxa de vitória BLUE:", tbwrrota_month_float)
        txt_sup_blue_rota_champion_month_r.close()
        #calculates difference:
        if trwrrota_month_float > tbwrrota_month_float:                                 
          
          print("Red wins")
          time.sleep(0)
          
          twrrota_month_result = (tbwrrota_month_float-trwrrota_month_float) * p
          winner1sup = "red"
          print(sup_red1v1)
          time.sleep(0)
          
          sup_blue1v1 = float(sup_blue1v1 + twrrota_month_result)
          print(sup_red1v1)
          time.sleep(0)
          print("Até então Blue points:", sup_blue1v1)
          time.sleep(0)
          print("Até então Red points:", sup_red1v1)
          time.sleep(0)
        else:
             
         print("Blue wins")
         time.sleep(0)
         twrbrota_month_result = (tbwrrota_month_float-trwrrota_month_float) * p
         print(twrbrota_month_result)
         time.sleep(0)
         winner1sup = "blue"
        
         sup_blue1v1 = sup_blue1v1 + twrbrota_month_result
         print(sup_blue1v1)
         time.sleep(0)   
           #evaluates the quality of the player sup champion red
        if (trwrchampion_month_float + trwrrota_month_float) / 2 > 50:
            sup_red_quality =  1     
        else: 
            sup_red_quality = 0
        if sup_red_quality == 1:
            print("Jogador bom no TOP Vermelho")
            time.sleep(0)
        else:
            print("Jogador ruim no TOP Azul")  
            time.sleep(0)
            #evaluates the quality of the player sup champion blue
        overall_red_sup = (trwrchampion_month_float + trwrrota_month_float) / 2
        overall_blue_sup = (tbwrchampion_month_float + tbwrrota_month_float) / 2
        print("Over all sup RED", overall_red_sup)
        time.sleep(0)
        print("Over all sup blue", overall_blue_sup)
        time.sleep(0)
        
        if overall_red_sup > 50:
            sup_blue_quality =  1     
        else: 
            sup_blue_quality = 0   
        if overall_blue_sup > 50:
           print("Jogador bom no sup Azul")
        else:
           print("Jogador ruim no sup Azul") 
        print("Resultado final:")
        print("Over all do sup RED")
        print(overall_red_sup)
        print("Over all do sup Azul")
        print(overall_blue_sup)
    
    
        team_blue_overall = (overall_blue_top + overall_blue_jg + overall_blue_mid + overall_blue_adc + overall_blue_sup) / 5
        team_red_overall = (overall_red_top + overall_red_jg + overall_red_mid + overall_red_adc + overall_red_sup) / 5
    
        print("Over all time azul:", team_blue_overall)
        print("Over all time vermelho", team_red_overall)
        time.sleep(2)
        if overall_blue_top < overall_red_top:
            print("Provavel vencedor: Top Vermelho:",  txt_top_red_champion_store_text_r)
        else:
            print("Provavel vencedor do Top Azul:",  txt_top_blue_champion_store_text_r)
        time.sleep(2)
        
        
        if overall_blue_jg < overall_red_jg:
            print("Provavel vencedor:Jg Vermelho",  txt_jg_red_champion_store_text_r)
        else:
            print("Provavel vencedor: Jg Azul",  txt_jg_blue_champion_store_text_r)

        time.sleep(2)
        if overall_blue_mid < overall_red_mid:
            print("Provavel vencedor: Mid Vermelho",  txt_mid_red_champion_store_text_r)
        else:
            print("Provavel vencedor:Mid Azul",  txt_mid_blue_champion_store_text_r)        

        time.sleep(2)
        if (overall_blue_adc + overall_blue_sup) /2 < (overall_red_adc + overall_red_sup):
            print("Provavel vencedor na botlane: time vermelho:",  txt_adc_red_champion_store_text_r," e", txt_sup_red_champion_store_text_r)
            
        else:
            print("Provavel vencedor na botlane: time azul:",  txt_adc_blue_champion_store_text_r," e", txt_sup_blue_champion_store_text_r)
        
        
        
        time.sleep(2)
        if overall_blue_sup < overall_red_sup:
            print("Provavel vencedor do sup:",  txt_sup_red_champion_store_text_r)
        else:
            print("Provavel vencedor do sup:",  txt_sup_blue_champion_store_text_r)
        
            
            
        

        
colectdata()
data()
            
                     
    
    
    
    
    

            
            
                  
    

               
               
               
               
               
               
               
               
               
               
                
    

                

            
 
 
      
    
    
#loads the dat

#makes the c
