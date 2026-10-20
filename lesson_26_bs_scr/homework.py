from bs4 import BeautifulSoup
import requests
from pathlib import Path

# Клас Product для даних про товар


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = float(price)

    @property
    def price_with_tax(self):
        """Обчислює ціну з податком (20%)"""
        return round(self.price * 1.2, 2)


def scrape_local_html(filepath):
    """Скрапер локального HTML файлу"""
    # Отримуємо повний шлях відносно розташування скрипта
    script_dir = Path(__file__).parent
    full_path = script_dir / filepath
    
    with open(full_path, "r", encoding="utf-8") as file:
        html = file.read()

    soup = BeautifulSoup(html, "html.parser")

    # Отримання заголовка
    title = soup.find("h1")
    print(f"\nЗаголовок: {title.text if title else 'Не знайдено'}")

    # Отримання всіх параграфів
    paragraphs = soup.find_all("p")
    print(f"\nКількість параграфів: {len(paragraphs)}")

    # Отримання ціни
    price = soup.find(class_="price")
    print(f"\nКонтейнер price (не ціна товару): {price.text if price else 'Не знайдено'}")

    # Отримання всіх посилань
    links = soup.find_all("a")
    print(f"\nКількість посилань: {len(links)}")
    for link in links:
        print(f"  - {link['href']}: {link.text}")

    # Отримання товарів через CSS селектори
    titles = soup.select(".product > .title")
    prices = soup.select(".product > .price")

    products = []
    for title, price in zip(titles, prices):
        product = Product(title.text.strip(), price.text.strip())
        products.append(product)

    return products


def main():
    """Головна функція"""
    print("=== Веб-скрапер локального HTML ===")

    products = scrape_local_html("index.html")

    print("\n=== Товари ===")
    for product in products:
        print(f"Назва: {product.name}")
        print(f"Ціна: {product.price} грн.")
        print(f"Ціна з податком: {product.price_with_tax} грн.")
        print()


if __name__ == "__main__":
    main()
