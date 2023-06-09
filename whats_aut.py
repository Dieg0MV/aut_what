import xlrd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time


class Logica:
    def __init__(self):

        self.servic = Service('/home/mrhead/Desktop/whats_app/chromedriver')
        self.driver = webdriver.Chrome(service=self.servic)
        self.start_url = 'https://web.whatsapp.com'

        self.driver.get(self.start_url)

        time.sleep(50)

        # De aquí sacamos los números
        self.excelFile = xlrd.open_workbook("name.xls")
        self.sheet1 = self.excelFile.sheet_by_index(0)

        for i in range(1, self.sheet1.nrows):

            # Elementos del campo de búsqueda
                numeros = self.sheet1.cell_value(rowx=i, colx=0)
                file_s = self.driver.find_element(By.CLASS_NAME, 'selectable-text.copyable-text')


                file_s.send_keys(numeros)
                time.sleep(1)
                file_s.send_keys(Keys.ENTER)

            # Esperar unos segundos para asegurarse de que se haya abierto la conversación
                time.sleep(2)

                # Enviar el mensaje utilizando pywhatkit
                chat_box = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')

                # Esperar unos segundos para que el mensaje se envíe antes de pasar al siguiente número
                time.sleep(1)
                chat_box.send_keys("Mensaje")
                chat_box.send_keys(Keys.ENTER)
                time.sleep(5)

            # Cerrar el navegador
        self.driver.quit()


if __name__ == '__main__':
    Logica()
