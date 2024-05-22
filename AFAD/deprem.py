import requests
from bs4 import BeautifulSoup

url ="https://deprem.afad.gov.tr/last-earthquakes.html"
response = requests.get(url)

# İnternet bağlantısının başarılı olduğundan emin olalım
if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")

    table = soup.find("table")
    rows = table.find_all("tr")

    for i, row in enumerate(rows[:10]):
        cells = row.find_all("td")

        if cells:
            location = cells[6].text.strip()
            magnitude = float(cells[5].text.strip())  # Büyüklüğü bir sayıya dönüştürelim
            longitude = cells[3].text.strip()
            date = cells[0].text.strip()
            id = cells[7].text.strip()

            # Büyüklüğü 2'den fazla olan depremleri kontrol edelim
            if magnitude > 2:
                print("Yer: " + location)
                print("Büyüklük: " + str(magnitude))
                print("Derinlik: " + longitude)
                print("Tarih: " + date)
                print("\n")
else:
    print("İnternet bağlantısında bir sorun oluştu. İşlem gerçekleştirilemiyor.")
