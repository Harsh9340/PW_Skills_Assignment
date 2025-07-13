import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen as uReq
import os
save_dir = "image/"
if not os.path.exists(save_dir):
    os.makedirs(save_dir)
query = "sudhanshu kumar ineuron"
response = requests.get(f"https://www.google.com/search?q={query}&sca_esv=8db25267be52ac73&rlz=1C1CHBF_enIN1098IN1098&sxsrf=AE3TifMPSeFOl8GKmxwoT3_Ebh7LrKGU_g:1752385942687&udm=2&fbs=AIIjpHxU7SXXniUZfeShr2fp4giZ1Y6MJ25_tmWITc7uy4KIeqDdErwP5rACeJAty2zADJjYuUnSkczEhozYdaq1wZrEWeBTRRMkGx8PE2F9zI9kP0W9slwfD0e_E2SCYpxxEsASI-LxkVBvfu-XibWr_YDicyb17E6vKrWBOlLdgfdjFpLOhNCkwKiTYaFviHAaGJoUkT5_nrzWq6VkkQdeHpPTQCkROQ&q=sudhanshu+kumar+ineuron&sa=X&ved=2ahUKEwjp7P2skrmOAxUq1TgGHYb6HO8QtKgLegQIExAB&biw=681&bih=632&dpr=1")
soup = BeautifulSoup(response.content,'html.parser')
images_tages = soup.find_all("img")
del images_tages[0]
for i in images_tages:
    images_url = i['src']
    image_data =  requests.get(images_url).content
    with open(os.path.join(save_dir,f"{query}_{images_tages.index(i)}.jpg"),"wb")as f:
        f.write(image_data)
requests.get(images_tages[1]['src']).content
