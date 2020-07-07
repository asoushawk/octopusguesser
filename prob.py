from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

options = Options()
options.headless = False  # aqui dá pra por se o navegador é para aparecer ou não
driver = webdriver.Chrome(
    options=options, executable_path=r'C:\Program Files (x86)\chromedriver.exe')
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

time.sleep(15)
try:
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

except:
    print("O jogador não está em partida!")
    time.sleep(3)
    quit()

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

# SUP_BLUE
txt_sup_blue_champion_store = open("sup_blue_champion.txt", "w")
txt_sup_blue_champion_store.write(sup_blue_champion)
txt_sup_blue_champion_store.close()
txt_sup_blue_champion_store_r = open("sup_blue_champion.txt", "r")
txt_sup_blue_champion_store_text_r = txt_sup_blue_champion_store_r.read()


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


# Comando STORE para gravar o Texto
# TOP_RED:
txt_top_red_champion_store = open("top_red_champion.txt", "w")
txt_top_red_champion_store.write(top_red_champion)
txt_top_red_champion_store.close()
txt_top_red_champion_store_r = open("top_red_champion.txt", "r")
txt_top_red_champion_store_text_r = txt_top_red_champion_store_r.read()

# JG_RED
txt_jg_red_champion_store = open("jg_red_champion.txt", "w")
txt_jg_red_champion_store.write(jg_red_champion)
txt_jg_red_champion_store.close()
txt_jg_red_champion_store_r = open("jg_red_champion.txt", "r")
txt_jg_red_champion_store_text_r = txt_jg_red_champion_store_r.read()
# MID_RED
txt_mid_red_champion_store = open("mid_red_champion.txt", "w")
txt_mid_red_champion_store.write(mid_red_champion)
txt_mid_red_champion_store.close()
txt_mid_red_champion_store_r = open("mid_red_champion.txt", "r")
txt_mid_red_champion_store_text_r = txt_mid_red_champion_store_r.read()
# ADC_RED
txt_adc_red_champion_store = open("adc_red_champion.txt", "w")
txt_adc_red_champion_store.write(adc_red_champion)
txt_adc_red_champion_store.close()
txt_adc_red_champion_store_r = open("adc_red_champion.txt", "r")
txt_adc_red_champion_store_text_r = txt_adc_red_champion_store_r.read()

# SUP_RED
txt_sup_red_champion_store = open("sup_red_champion.txt", "w")
txt_sup_red_champion_store.write(sup_red_champion)
txt_sup_red_champion_store.close()
txt_sup_red_champion_store_r = open("sup_red_champion.txt", "r")
txt_sup_red_champion_store_text_r = txt_sup_red_champion_store_r.read()


# time vermelho nicks:
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

# STORE PARA OS NICKS RED:
# TOP_RED:
txt_top_red_nick_store = open("top_red_nick.txt", "w")
txt_top_red_nick_store.write(top_red_nick.text)
txt_top_red_nick_store.close()
txt_top_red_nick_store_r = open("top_red_nick.txt", "r")
txt_top_red_nick_store_text_r = txt_top_red_nick_store_r.read()

# JG RED:
txt_jg_red_nick_store = open("jg_red_nick.txt", "w")
txt_jg_red_nick_store.write(jg_red_nick.text)
txt_jg_red_nick_store.close()
txt_jg_red_nick_store_r = open("jg_red_nick.txt", "r")
txt_jg_red_nick_store_text_r = txt_jg_red_nick_store_r.read()

# MID RED:
txt_mid_red_nick_store = open("mid_red_nick.txt", "w")
txt_mid_red_nick_store.write(mid_red_nick.text)
txt_mid_red_nick_store.close()
txt_mid_red_nick_store_r = open("mid_red_nick.txt", "r")
txt_mid_red_nick_store_text_r = txt_mid_red_nick_store_r.read()

# ADC: RED:
txt_adc_red_nick_store = open("adc_red_nick.txt", "w")
txt_adc_red_nick_store.write(adc_red_nick.text)
txt_adc_red_nick_store.close()
txt_adc_red_nick_store_r = open("adc_red_nick.txt", "r")
txt_adc_red_nick_store_text_r = txt_adc_red_nick_store_r.read()

# SUP RED:
txt_sup_red_nick_store = open("sup_red_nick.txt", "w")
txt_sup_red_nick_store.write(sup_red_nick.text)
txt_sup_red_nick_store.close()
txt_sup_red_nick_store_r = open("sup_red_nick.txt", "r")
txt_sup_red_nick_store_text_r = txt_sup_red_nick_store_r.read()

# NICKS BLUE:

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


# STORE PARA OS NICKS BLUE:
# TOP_BLUE:
txt_top_blue_nick_store = open("top_blue_nick.txt", "w")
txt_top_blue_nick_store.write(top_blue_nick.text)
txt_top_blue_nick_store.close()
txt_top_blue_nick_store_r = open("top_blue_nick.txt", "r")
txt_top_blue_nick_store_text_r = txt_top_blue_nick_store_r.read()

# JG BLUE:
txt_jg_blue_nick_store = open("jg_blue_nick.txt", "w")
txt_jg_blue_nick_store.write(jg_blue_nick.text)
txt_jg_blue_nick_store.close()
txt_jg_blue_nick_store_r = open("jg_blue_nick.txt", "r")
txt_jg_blue_nick_store_text_r = txt_jg_blue_nick_store_r.read()

# MID BLUE:
txt_mid_blue_nick_store = open("mid_blue_nick.txt", "w")
txt_mid_blue_nick_store.write(mid_blue_nick.text)
txt_mid_blue_nick_store.close()
txt_mid_blue_nick_store_r = open("mid_blue_nick.txt", "r")
txt_mid_blue_nick_store_text_r = txt_mid_blue_nick_store_r.read()

# ADC: BLUE:
txt_adc_blue_nick_store = open("adc_blue_nick.txt", "w")
txt_adc_blue_nick_store.write(adc_blue_nick.text)
txt_adc_blue_nick_store.close()
txt_adc_blue_nick_store_r = open("adc_blue_nick.txt", "r")
txt_adc_blue_nick_store_text_r = txt_adc_blue_nick_store_r.read()

# SUP BLUE:
txt_sup_blue_nick_store = open("sup_blue_nick.txt", "w")
txt_sup_blue_nick_store.write(sup_blue_nick.text)
txt_sup_blue_nick_store.close()
txt_sup_blue_nick_store_r = open("sup_blue_nick.txt", "r")
txt_sup_blue_nick_store_text_r = txt_sup_blue_nick_store_r.read()


# taxa de vitoria time azul com o campeão:
top_blue_win_champion = driver.find_element_by_xpath(
    '//*[@id="liveContent"]/div[1]/ul[1]/li[1]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]')
jg_blue_win_champion = driver.find_element_by_xpath(
    '//*[@id="liveContent"]/div[1]/ul[1]/li[2]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]')
mid_blue_win_champion = driver.find_element_by_xpath(
    '//*[@id="liveContent"]/div[1]/ul[1]/li[3]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]')
adc_blue_win_champion = driver.find_element_by_xpath(
    '//*[@id="liveContent"]/div[1]/ul[1]/li[4]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]')
sup_blue_win_champion = driver.find_element_by_xpath(
    '//*[@id="liveContent"]/div[1]/ul[1]/li[5]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]')
# store:

# TOP BLUE
txt_top_blue_win_champion = open("txt_top_blue_win_champion.txt", "w")
txt_top_blue_win_champion.write(top_blue_win_champion.text)
txt_top_blue_win_champion.close()
txt_top_blue_win_champion_r = open("txt_top_blue_win_champion.txt", "r")
txt_top_blue_win_champion_r_text = txt_top_blue_win_champion_r.read()

# JG BLUE

txt_jg_blue_win_champion = open("txt_jg_blue_win_champion.txt", "w")
txt_jg_blue_win_champion.write(jg_blue_win_champion.text)
txt_jg_blue_win_champion.close()
txt_jg_blue_win_champion_r = open("txt_jg_blue_win_champion.txt", "r")
txt_jg_blue_win_champion_r_text = txt_jg_blue_win_champion_r.read()

# MID BLUE

txt_mid_blue_win_champion = open("txt_mid_blue_win_champion.txt", "w")
txt_mid_blue_win_champion.write(mid_blue_win_champion.text)
txt_mid_blue_win_champion.close()
txt_mid_blue_win_champion_r = open("txt_mid_blue_win_champion.txt", "r")
txt_mid_blue_win_champion_r_text = txt_mid_blue_win_champion_r.read()

# ADC BLUE
txt_adc_blue_win_champion = open("txt_adc_blue_win_champion.txt", "w")
txt_adc_blue_win_champion.write(adc_blue_win_champion.text)
txt_adc_blue_win_champion.close()
txt_adc_blue_win_champion_r = open("txt_adc_blue_win_champion.txt", "r")
txt_adc_blue_win_champion_r_text = txt_adc_blue_win_champion_r.read()

# SUP BLUE

txt_sup_blue_win_champion = open("txt_sup_blue_win_champion.txt", "w")
txt_sup_blue_win_champion.write(sup_blue_win_champion.text)
txt_sup_blue_win_champion.close()
txt_sup_blue_win_champion_r = open("txt_top_blue_win_champion.txt", "r")
txt_sup_blue_win_champion_r_text = txt_top_blue_win_champion_r.read()


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

# SUP BLUE

txt_sup_red_win_champion = open("txt_sup_red_win_champion.txt", "w")
txt_sup_red_win_champion.write(sup_red_win_champion.text)
txt_sup_red_win_champion.close()
txt_sup_red_win_champion_r = open("txt_top_red_win_champion.txt", "r")
txt_sup_red_win_champion_r_text = txt_top_red_win_champion_r.read()


# Kda do cara com o campeão - Time Azul:
top_blue_champion_kda = driver.find_element_by_xpath(
    '//*[@id="liveContent"]/div[1]/ul[1]/li[1]/div/div[2]/div[1]/div/div[1]/div[2]/div[2]/div[1]')
jg_blue_champion_kda = driver.find_element_by_xpath(
    '//*[@id="liveContent"]/div[1]/ul[1]/li[2]/div/div[2]/div[1]/div/div[1]/div[2]/div[2]/div[1]')
mid_blue_champion_kda = driver.find_element_by_xpath(
    '//*[@id="liveContent"]/div[1]/ul[1]/li[3]/div/div[2]/div[1]/div/div[1]/div[2]/div[2]/div[1]')
adc_blue_champion_kda = driver.find_element_by_xpath(
    '//*[@id="liveContent"]/div[1]/ul[1]/li[4]/div/div[2]/div[1]/div/div[1]/div[2]/div[2]/div[1]')
sup_blue_champion_kda = driver.find_element_by_xpath(
    '//*[@id="liveContent"]/div[1]/ul[1]/li[5]/div/div[2]/div[1]/div/div[1]/div[2]/div[2]/div[1]')

# STORE KDA

# TOPBLUE
txt_top_blue_champion_kda = open("top_blue_champion_kda.txt", "w")
txt_top_blue_champion_kda.write(top_blue_champion_kda.text)
txt_top_blue_champion_kda.close()
txt_top_blue_champion_kda_r = open("top_blue_champion_kda.txt", "r")
txt_top_blue_champion_kda_r_text = txt_top_blue_champion_kda_r.read()

# JGBLUE
txt_jg_blue_champion_kda = open("jg_blue_champion_kda.txt", "w")
txt_jg_blue_champion_kda.write(jg_blue_champion_kda.text)
txt_jg_blue_champion_kda.close()
txt_jg_blue_champion_kda_r = open("jg_blue_champion_kda.txt", "r")
txt_jg_blue_champion_kda_r_text = txt_jg_blue_champion_kda_r.read()

# MIDBLUE
txt_mid_blue_champion_kda = open("mid_blue_champion_kda.txt", "w")
txt_mid_blue_champion_kda.write(mid_blue_champion_kda.text)
txt_mid_blue_champion_kda.close()
txt_mid_blue_champion_kda_r = open("mid_blue_champion_kda.txt", "r")
txt_mid_blue_champion_kda_r_text = txt_mid_blue_champion_kda_r.read()

# ADCBLUE

txt_adc_blue_champion_kda = open("adc_blue_champion_kda.txt", "w")
txt_adc_blue_champion_kda.write(adc_blue_champion_kda.text)
txt_adc_blue_champion_kda.close()
txt_adc_blue_champion_kda_r = open("adc_blue_champion_kda.txt", "r")
txt_adc_blue_champion_kda_r_text = txt_adc_blue_champion_kda_r.read()


# supBLUE
txt_sup_blue_champion_kda = open("sup_blue_champion_kda.txt", "w")
txt_sup_blue_champion_kda.write(sup_blue_champion_kda.text)
txt_sup_blue_champion_kda.close()
txt_sup_blue_champion_kda_r = open("sup_blue_champion_kda.txt", "r")
txt_sup_blue_champion_kda_r_text = txt_sup_blue_champion_kda_r.read()


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
top_blue_mainrole = driver.find_element_by_xpath(
    '//*[@id="liveContent"]/div[1]/ul[1]/li[1]/div/div[2]/div[3]/div[1]/div[2]/div[2]/span')
jg_blue_mainrole = driver.find_element_by_xpath(
    '//*[@id="liveContent"]/div[1]/ul[1]/li[2]/div/div[2]/div[3]/div[1]/div[2]/div[2]/span')
mid_blue_mainrole = driver.find_element_by_xpath(
    '//*[@id="liveContent"]/div[1]/ul[1]/li[3]/div/div[2]/div[3]/div[1]/div[2]/div[2]/span')
adc_blue_mainrole = driver.find_element_by_xpath(
    '//*[@id="liveContent"]/div[1]/ul[1]/li[4]/div/div[2]/div[3]/div[1]/div[2]/div[2]/span')
sup_blue_mainrole = driver.find_element_by_xpath(
    '//*[@id="liveContent"]/div[1]/ul[1]/li[5]/div/div[2]/div[3]/div[1]/div[2]/div[2]/span')


# identificação de jogador para coleta de infomações dos ultimos 30 dias com o campeao:

# ir para a pagina do perfil do TOPBLUE
def wukongtesttop():
    maybewukong = txt_top_blue_champion_store_text_r
    if maybewukong == "Wukong":
        top_blue_champion = "monkeyking"
        leaguegraph_main_profile_stats = "https://www.leagueofgraphs.com/pt/summoner/champions/"

        top_lane = "/top"  # aqui estão identificadas as lanes
        top_blue_leaguegraph_profile = leaguegraph_main_profile_stats + \
            top_blue_champion.lower() + "/" + "br/" + txt_jg_blue_nick_store_text_r + top_lane
        driver.get(top_blue_leaguegraph_profile)
        time.sleep(5)


wukongtesttop()
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

mobalytics_main_profile_stats = "https://app.mobalytics.gg/lol/profile/br/"
top_blue_mobalytics_profile = mobalytics_main_profile_stats + \
    txt_top_blue_nick_store_text_r + "/" + "champions?champion=" + top_blue_champion
driver.get(top_blue_mobalytics_profile)
time.sleep(30)
top_blue_champion_alltime_wr = driver.find_element_by_xpath(
    '//*[@id="app-content"]/div[1]/div[4]/div[2]/div/div[3]/div/div[2]/div[2]/div[4]/div/div[3]')
print("Taxa de vitórias com", txt_top_blue_champion_store_text_r,
      "total", top_blue_champion_alltime_wr.text)


# ir para a pagina do perfil do JG Blue

leaguegraph_main_profile_stats = "https://www.leagueofgraphs.com/pt/summoner/champions/"
print("Coletando informações de", txt_jg_blue_nick_store_text_r)
jg_lane = "/jungle"  # aqui estão identificadas as lanes


def wukongtestjg():
    maybewukong = txt_jg_blue_champion_store_text_r
    if maybewukong == "Wukong":
        jg_blue_champion = "monkeyking"


wukongtesttop()

jg_blue_leaguegraph_profile = leaguegraph_main_profile_stats + \
    jg_blue_champion.lower() + "/" + "br/" + txt_jg_blue_nick_store_text_r + jg_lane
driver.get(jg_blue_leaguegraph_profile)
time.sleep(5)
# script de coleta de informações jogador, indentificação de elemento + store:
# coleta games jogados no mês com o campeao:
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

    # pegar dados jg mobalitcs
    mobalytics_main_profile_stats = "https://app.mobalytics.gg/lol/profile/br/"
    jg_blue_mobalytics_profile = mobalytics_main_profile_stats + \
        txt_jg_blue_nick_store_text_r + "/" + "champions?champion=" + jg_blue_champion
    driver.get(jg_blue_mobalytics_profile)
    time.sleep(30)
    jg_blue_champion_alltime_wr = driver.find_element_by_xpath(
        '//*[@id="app-content"]/div[1]/div[4]/div[2]/div/div[3]/div/div[2]/div[2]/div[4]/div/div[3]')
    print("Taxa de vitórias com", txt_jg_blue_champion_store_text_r,
          "total", jg_blue_champion_alltime_wr.text)
except:
    pass


# MID leaguegraphs:

leaguegraph_main_profile_stats = "https://www.leagueofgraphs.com/pt/summoner/champions/"
print("Coletando informações de", txt_mid_blue_nick_store_text_r)
mid_lane = "/middle"  # aqui estão identificadas as lanes
mid_blue_leaguegraph_profile = leaguegraph_main_profile_stats + \
    mid_blue_champion.lower() + "/" + "br/" + txt_mid_blue_nick_store_text_r + mid_lane
driver.get(mid_blue_leaguegraph_profile)
time.sleep(5)
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

# ADC leaguegraphs:

leaguegraph_main_profile_stats = "https://www.leagueofgraphs.com/pt/summoner/champions/"
print("Coletando informações de", txt_adc_blue_nick_store_text_r)
adc_lane = "/adc"  # aqui estão identificadas as lanes
adc_blue_leaguegraph_profile = leaguegraph_main_profile_stats + \
    adc_blue_champion.lower() + "/" + "br/" + txt_adc_blue_nick_store_text_r + adc_lane
driver.get(adc_blue_leaguegraph_profile)
time.sleep(5)
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

# SUP leaguegraphs:

leaguegraph_main_profile_stats = "https://www.leagueofgraphs.com/pt/summoner/champions/"
print("Coletando informações de", txt_sup_blue_nick_store_text_r)
sup_lane = "/adc"  # aqui estão identificadas as lanes
sup_blue_leaguegraph_profile = leaguegraph_main_profile_stats + \
    sup_blue_champion.lower() + "/" + "br/" + txt_sup_blue_nick_store_text_r + sup_lane
driver.get(sup_blue_leaguegraph_profile)
time.sleep(5)
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


def showinfo():  # mostrar jogadores e campeoes
    print("Jogadores Time Azul:")
    print(txt_top_blue_nick_store_text_r, "-",
          txt_top_blue_champion_store_text_r, )
    print(txt_jg_blue_nick_store_text_r, "-",
          txt_jg_blue_champion_store_text_r, )
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
