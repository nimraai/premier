import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

def main():
   
    driver = webdriver.Chrome()

    
    uuid = 1  

    base_url = 'https://www.istockphoto.com/photos/bedroom='

    with open("istock_image_links2.csv", "w", newline="") as csvfile:
        fieldnames = ["UUID", "Page_URL", "Image_URL", "Title"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for page in range(7001, 9000):  
            url = f'{base_url}{page}'  # Update the URL with the page number

            driver.get(url)

            image_elements = driver.find_elements(By.CLASS_NAME, 'Q1yS6PaawlCD2gctKc2c')
            for i_e in image_elements:
                images = i_e.find_elements(By.TAG_NAME, 'img')
                for img in images:
                    image_url = img.get_attribute('src')
                    image_title = img.get_attribute('alt')  # Extract the image title
                    writer.writerow({"UUID": uuid, "Page_URL": url, "Image_URL": image_url, "Title": image_title})
                    uuid += 1

   
    driver.quit()

if __name__ == "__main__":
    main()
