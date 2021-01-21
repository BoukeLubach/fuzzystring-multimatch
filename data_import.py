import pandas as pd 
import os

script_dir = os.path.dirname(__file__)
os.environ.setdefault('DJANGO_SETTINGS_MODULE','fwTagfilter.settings')

import django
django.setup()

from tsData.models import MeasurementTag

 #<-- absolute dir the script is in
rel_file_path = "data/tagNames.csv"
rel_path = os.path.join(script_dir, rel_file_path)


def populate():
    df = pd.read_csv(rel_path, sep=';', encoding = "ISO-8859-1")

    for i in range(df.shape[0]):
        print(df.iloc[i])
        tag_instance = MeasurementTag(
                                tagName = df['tagname'].iloc[i],
                                description = df['description'].iloc[i],
                                uom = df['uom'].iloc[i],   
                                site = df['site'].iloc[i], 
                                company = df['company'].iloc[i],

        )
        
        tag_instance.save()



if __name__ == "__main__":
    populate()


