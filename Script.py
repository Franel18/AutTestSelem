from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_login_and_checkout():
    driver = webdriver.Chrome()  # Asegúrate de que chromedriver.exe esté en la carpeta
    driver.maximize_window()
    
    try:
        # 1. Ir a SauceDemo
        driver.get("https://www.saucedemo.com/")
        
        # 2. Hacer login
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        time.sleep(2)
        
        # 3. Añadir producto al carrito
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        time.sleep(1)
        
        # 4. Ir al carrito y hacer checkout
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        driver.find_element(By.ID, "checkout").click()
        time.sleep(1)
        
        # 5. Rellenar datos de envío
        driver.find_element(By.ID, "first-name").send_keys("John")
        driver.find_element(By.ID, "last-name").send_keys("Doe")
        driver.find_element(By.ID, "postal-code").send_keys("12345")
        driver.find_element(By.ID, "continue").click()
        time.sleep(1)
        
        # 6. Finalizar compra
        driver.find_element(By.ID, "finish").click()
        assert "Thank you for your order" in driver.page_source
        
        # Captura de pantalla
        driver.save_screenshot("screenshots/checkout_exitoso.png")
        print("✅ Prueba exitosa!")
        
    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    test_login_and_checkout()