import os
import json
import commentjson
import traceback
from datetime import datetime
from aiohttp import ClientSession
from PIL import Image
from io import BytesIO
import re
import concurrent.futures
from datetime import datetime
from zoneinfo import ZoneInfo
import numpy as np
import cv2
import math
import matplotlib.pyplot as plt
import math



class LearnTools:

    def monitor(self,data):
        """_summary_
        :: Function to monitor data in console
        Args:
            data (_type_): prints the given python dict
        """
        print('~'*100)
        print(json.dumps(data))
        print('#'*100)

    def clean_string(self,item):
        """_summary_
        :: Function to clean special characters in a given string
        Args:
            item (_type_): string
        Returns:
            _type_: string
        """
        return re.sub(r"[^a-zA-Z0-9\s\-_]", "", item)

    def load_data(self, data_dir):
        """_summary_
        :: Function to load all the json file in a given path
        Args:
            data_dir (_type_): _description_. path to the folder where all the json files are stored
        Returns:
            _type_: _description_. creates a new python dictionary where the key is the fileName and value is the json contents
        """
        json_data = {}
        def load_file(file): # helper function to read and load all json files in the target dir
            file_name = os.path.splitext(file)[0]
            file_path = os.path.join(data_dir, file)
            with open(file_path, "r", encoding="utf-8") as data:
                # return file_name, json.load(data)
                return file_name, commentjson.load(data)

        with concurrent.futures.ThreadPoolExecutor() as executor:
            json_data.update(dict(executor.map(load_file, [f for f in os.listdir(data_dir) if f.endswith(".json")])))
        return json_data


    def removeIntegers(self,input_string):
        """_summary_
        :: Function to remove any integer from a given string
        Args:
            input_string (_type_): _description_. String from which integers need to be removed
        Returns:
            _type_: _description_. string without integers
        """
        return re.sub(r'\s*\d', '', input_string)


    async def get_image(self, img_url, padding=100):
        """_summary_
        :: Function to fetch image from a given url and add padding around it if required
        Args:
            img_url (_type_): the url of the image
            padding (int, optional): _description_. Defaults to 100.
        Returns:
            _type_: _description_. PIL image object
        """
        try:
            async with ClientSession() as session:
                async with session.get(img_url) as response:
                    response.raise_for_status()
                    image = Image.open(BytesIO(await response.read())).convert("RGB")

                    scale = 1 / math.sqrt(10)  # 10 times smaller image
                    new_size = (
                        max(1, int(image.width * scale)),
                        max(1, int(image.height * scale)),
                    )

                    image = image.resize(new_size, Image.Resampling.LANCZOS)
                    return image

        except Exception as e:
            traceback.print_exc()
            raise ValueError(f"Invalid URL ==>>{img_url}<<== : {str(e)}")


    def pil_to_cv2(self, pil_image):
        """Convert PIL image to OpenCV image (BGR format)"""
        cv_image = np.array(pil_image)            # Convert PIL to NumPy array (RGB)
        if pil_image.mode == "RGBA":
            cv_image = cv2.cvtColor(cv_image, cv2.COLOR_RGBA2BGR)
        else:
            cv_image = cv2.cvtColor(cv_image, cv2.COLOR_RGB2BGR)
        return cv_image




    def formatTime(self, record, datefmt=None):
        """_summary_
        :: Function to format time in Daka timezone
        Args:
            record (_type_): _description_
            datefmt (_type_, optional): _description_. Defaults to None.

        Returns:
            _type_: _description_. Dahaka Timezone formatted time string
        """
        dt = datetime.fromtimestamp(record.created, ZoneInfo("Asia/Dhaka"))
        if datefmt:
            s = dt.strftime(datefmt)
        else:
            s = dt.strftime("%Y-%m-%d %I:%M:%S %p")
        return s


    def show_two_images(self, title1, img1, title2, img2):
        fig, axs = plt.subplots(1, 2, figsize=(24, 12))

        img1_rgb = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
        axs[0].imshow(img1_rgb)
        axs[0].set_title(title1)
        axs[0].axis('off')

        img2_rgb = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
        axs[1].imshow(img2_rgb)
        axs[1].set_title(title2)
        axs[1].axis('off')

        plt.show()
