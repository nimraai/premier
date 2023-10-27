import pandas as pd
#file_path = '/home/umair/Desktop/nimra/istock/istock_image_links.csv'
df = pd.read_csv('istock_image_links2.csv')
    
df.drop_duplicates(subset='Image_URL', keep='first', inplace=True)
df.to_csv('newfile12.csv', index=False)