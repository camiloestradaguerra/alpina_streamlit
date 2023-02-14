import os, time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from datetime import datetime
import pandas as pd
import scraper_ciudad as _scraper1


def _todas_las_ciudades():
        
    frames = [] 
    for i in range(0, 4):
        time.sleep(2)
        datos = _scraper1._ciudad_individual(i)
        frames.append(datos)
    df = pd.concat(frames)
    df.to_csv('df_TODAS_LAS_CIUDADES.csv', encoding='utf-8-sig', index=False)
        
    return df


