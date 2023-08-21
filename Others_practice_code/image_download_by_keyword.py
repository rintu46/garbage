from bing_image_downloader import downloader

query_string_list = [ "Pantene Shampoo","Clinic Plus Shampoo"]      #give the keyword for what your looking for


for query in query_string_list:
    downloader.download(query, limit=50, output_dir='/home/parvej/Sikder Md Saiful Islam/June/unknown data/',
                         adult_filter_off=True, force_replace=False, timeout=60, verbose=True)     


#change the output dir based on your location