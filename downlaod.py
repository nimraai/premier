import csv
import requests
import os

def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def download_images_from_csv(csv_filename, output_directory): #,start,end):
    with open(csv_filename, mode='r') as csvfile:
    
        reader = csv.DictReader(csvfile)
        rows = list(reader)
        """ start = max(0,start)
        end =min(end, len(rows))"""
        for i in range(len(rows)):
            row = rows[i]
            image_url = row['Image_URL']
            image_uuid = row['UUID']

            
            create_directory(output_directory)

           
            image_filename = os.path.join(output_directory, f"{image_uuid}.jpg")
            with open(image_filename, 'wb') as image_file:
                response = requests.get(image_url)
                if response.status_code == 200:
                    image_file.write(response.content)
                    print(f"Downloaded: {image_filename}")
                else:
                    print(f"Failed to download: {image_url}")

if __name__ == "__main__":
    csv_filename = "zeroduplicates.csv"  
    output_directory = "istock_i" 
    """ start_index = 26823
    end_index = 50000 """
    download_images_from_csv(csv_filename, output_directory) #start_index ,end_index)
