"""
Proxy
Účel: poskytnutí objektu, který funguje jako náhrada za skutečný objekt používaný klientem.

Vlastnosti:

proxy v názvu třídy představující proxy
společné rozhraní sdílené proxy a cílovým objektem
transparentní použití pro koncového uživatele
skryté detaily implementace
Proxy - typy
remote - reprezentace objektu v jiném prostoru (např. vzdálený počítač)
virtual - lze použít jako mezipaměť pro odkaz na objekt
security - přidání bezpečnostní vrstvy k objektu

Virtual proxy priklad
"""


class Image:
    def show(self):
        pass


class RealImage(Image):
    def __init__(self, filename):
        self.filename = filename
        self._load_image()

    def _load_image(self):
        print(f"Loading image from {self.filename}")

    def show(self):
        print(f"Displaying {self.filename}")


class ImageProxy(Image):
    def __init__(self, filename):
        self.filename = filename
        self._real_image = None

    def show(self):
        if self._real_image is None:
            self._real_image = RealImage(self.filename)
        self._real_image.show()


def main_proxy():
    proxy_image = ImageProxy("photo.jpg")
    proxy_image.show()  # Loads and displays the image
    proxy_image.show()  # Displays the image without loading again


if __name__ == "__main__":
    main_proxy()
