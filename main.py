import sys
import json
import subprocess
import base64
import os
import shutil
import re

def run_command(pubfileid, save_location):
    print(f"----------Downloading {pubfileid}--------\n")
    dir_option = f"-dir \"{save_location}\""  # Ensure the directory path is correctly formatted for Windows
    command = fr"C:\Users\Ericc\Downloads\dwd\Release\net8.0\DepotDownloaderMod.exe -app 431960 -pubfile {pubfileid} -verify-all -username {username} -password {password
    } {dir_option}"
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True,creationflags=subprocess.CREATE_NO_WINDOW)
    for line in process.stdout:
        print(line)
    process.stdout.close()
    process.wait()
    print(f"-------------Download finished-----------\n")

# Accounts and passwords
accounts = {'ruiiixx': 'S67GBTB83D3Y',
    'premexilmenledgconis': 'M3BYYkhaSmxEYg==',
    'vAbuDy': 'Qm9vbHE4dmlw',
    'adgjl1182': 'UUVUVU85OTk5OQ==',
    'gobjj16182': 'enVvYmlhbzgyMjI=',
    '787109690': 'SHVjVXhZTVFpZzE1'
    }
# passwords = {account: base64.b64decode(accounts[account]).decode('utf-8') for account in accounts}
#screw this wierd tkinter sh*t
#also like how is this real its just free steam accounts with games lol
username = 'ruiiixx'
password = 'S67GBTB83D3Y'

def wallpaper_location():
    try:
        with open('lastsavelocation.cfg', 'r') as file:
            target_directory = file.read().strip()
            if os.path.isdir(target_directory):
                global save_location
                save_location = target_directory
            else:
                raise FileNotFoundError
    except FileNotFoundError:
        with open('lastsavelocation.cfg', 'w') as file:
            file.write("Put Lively location here")
        print("Location")

def wallpaper_exe_location():
    try:
        with open('wallpaperexe.json', 'r') as file:
            json_data = json.loads(file.read())
            global wallpaper_exe
            global wallpaper_ui
            wallpaper_exe = json_data.get("Lively_exe")
            wallpaper_ui = json_data.get("Lively_ui")
    except FileNotFoundError:
        with open('wallpaperexe.json', 'w') as file:
            file.write(f"""
            {{
                "Lively_exe": "C:/Users/{os.getlogin()}/AppData/Local/Programs/Lively Wallpaper/Lively.exe",
                "Lively_ui": "C:/Users/{os.getlogin()}/AppData/Local/Programs/Lively Wallpaper/Plugins/UI/Lively.UI.WinUI.exe"
            }}
            """)
        print("Auto-generated config")
        sys.exit(1)

def convert_format(input_data):
    if isinstance(input_data, str):
        input_data = json.loads(input_data)
    # Extract values from the input JSON
    title = input_data.get("title", "Untitled")
    preview = input_data.get("preview", "preview.jpg")
    file_name = input_data.get("file", "video.mp4")
    desc = input_data.get("description", "No description provided")
    
    # Create the output JSON structure
    output_data = {
        "AppVersion": "0.3.1.0",
        "Title": title,
        "Thumbnail": preview, 
        "Preview": preview,
        "Desc": desc,
        "License": "Legal stuff bla bla bla",
        "Type": 7, #didn't read documentation, its proabaly fine
        "FileName": file_name
    }
    
    return output_data, file_name, preview, title


if input("local ") == "yes":
    wallpaper_location()
    wallpaper_exe_location()
    path = input("file path: ")
    with open(f'{path}/project.json', 'r', encoding="utf8") as file:
        jsonf = file.read()
    converted_json, filename, preview, title = convert_format(jsonf)
    print(json.dumps(converted_json, indent=2))
    if os.path.exists(f'{save_location}/{title}'):
        if input("Clear folder? y/n: ") == "y":
            shutil.rmtree(f'{save_location}/{title}')
            os.mkdir(f'{save_location}/{title}')
        else:
            sys.exit(1)
    else:
        os.mkdir(f'{save_location}/{title}')
    with open(f'{save_location}/{title}/LivelyInfo.json', 'w') as file:
        file.write(json.dumps(converted_json, indent=2))
    shutil.copy(f'{path}/{filename}', f'{save_location}/{title}/{filename}')
    shutil.copy(f'{path}/{preview}', f'{save_location}/{title}/{preview}')
    #should probably use api but whatever
    try:
        subprocess.run("taskkill -f -im Lively.UI.WinUI.exe")
    except:
        pass
    try:
        subprocess.run("taskkill -f -im Lively.exe")
    except:
        pass
    os.popen(wallpaper_exe)
    print(wallpaper_ui)
    subprocess.run(wallpaper_ui)


else:
    wallpaper_location()
    wallpaper_exe_location()
    if os.path.exists("./tmp"):
        shutil.rmtree("./tmp")
    os.mkdir("./tmp")
    path = input("url path: ")
    path = re.search(r'\b\d{8,10}\b', path.strip())
    run_command(path.group(0), "./tmp")
    with open(f'./tmp/project.json', 'r', encoding="utf8") as file:
        jsonf = file.read()
    converted_json, filename, preview, title = convert_format(jsonf)
    print(json.dumps(converted_json, indent=2))
    if os.path.exists(f'{save_location}/{title}'):
        if input("Clear folder? y/n: ") == "y":
            shutil.rmtree(f'{save_location}/{title}')
            os.mkdir(f'{save_location}/{title}')
        else:
            sys.exit(1)
    else:
        os.mkdir(f'{save_location}/{title}')
    with open(f'{save_location}/{title}/LivelyInfo.json', 'w') as file:
        file.write(json.dumps(converted_json, indent=2))
    shutil.copy(f'./tmp/{filename}', f'{save_location}/{title}/{filename}')
    print(f'./tmp/{filename}' + f'{save_location}/{title}/{filename}')
    shutil.copy(f'./tmp/{preview}', f'{save_location}/{title}/{preview}')
    try:
        subprocess.run(f"{wallpaper_exe} --shutdown true")
    except:
        pass
    os.popen(wallpaper_exe)
    subprocess.run(f"{wallpaper_exe} --showApp true")
    shutil.rmtree("./tmp/")
    subprocess.run("taskkill -f -im pythonw.exe")
    subprocess.run("taskkill -f -im py.exe")
    subprocess.run("taskkill -f -im python.exe")
    sys.exit(0)