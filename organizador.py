import os
from tkinter.filedialog import askdirectory

path = askdirectory(title='Select a folder')

files_list = os.listdir(path)

places = {
    "images": [".png", ".jpg", ".jpeg"],
    "spreadsheets": [".xlsx", ".xls", ".xlsm", ],
    "pdf": [".pdf"],
    "csv": [".csv"],
    "power bi": [".pbix"],
    "word": [".doc", ".docm", ".docx"]
}

for file in files_list:
    name, extension = os.path.splitext(f"{path}/{file}")
    for folder in places:
        if extension in places[folder]:
            if not os.path.exists(f"{path}/{folder}"):
                os.mkdir(f"{path}/{folder}")
            os.rename(f"{path}/{file}",(f"{path}/{folder}/{file}"))

