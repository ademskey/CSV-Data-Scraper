
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import requests
import pandas as pd
import time
import io
import os

# Define the URL of the CSV file to download
# url = 'https://data.wa.gov/api/views/f6w7-q2d2/rows.csv?accessType=DOWNLOAD'
url = 'https://gist.githubusercontent.com/armgilles/194bcff35001e7eb53a2a8b441e8b2c6/raw/92200bc0a673d5ce2110aaad4544ed6c4010f687/pokemon.csv'

# Define the path of the output CSV file
output_csv_path = r'C:\Users\adamc\Desktop\Data Scraper Test\test.csv'

# make sure to import io, os, pandas, requests, and beautiful soup if parsing html info
# success variable, will stop loop in event get from url fails
success = 0
print('Running Script ...')
while success == 0:
    response = requests.get(url)
    # check if url response is valid
    if response.ok:
        # read responses content (what it grabbed from URL)
        # decode content because request library returns stream of bytes of content which must be decoded
        data = response.content.decode('utf-8')

        # read data from url into data frame
        # io.BytesIO makes it a file-like object that allows pandas to store the data
        # dataframe can then be manipulated and put into a file
        df = pd.read_csv(io.BytesIO(response.content))

        # print(df.head()) <-- this can be used to test for if correct data pulled in (prints first 5)
        if not os.path.exists(output_csv_path):  # if directory doesn't exist make a new one
            print('New directory made')
            os.makedirs(output_csv_path)  # construct a path with the provided path if not exist

        df.to_csv(output_csv_path, index=False)  # write dataframe data to CSV file (will overwrite)
        print(f"Data saved to file: {output_csv_path}")  # print location data saved to

    else:
        print('Error:', response.status_code)  # if response failed print failure code
        success = 1
    # Sleep for 5 seconds before downloading the next version of the CSV file
    time.sleep(5)
