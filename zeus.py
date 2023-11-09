import requests
from bs4 import BeautifulSoup
from argparse import ArgumentParser
import os
import json
import shutil

PKG_DIR = "athena_pkgs/"
CURRENT_DIR = os.getcwd()
BANNER = '''
╔═════════════════════════════════════════════════════════════════════════╗
║ Zeus Package Manager for AthenaEnv (PlayStation® 2) JavaScript packages ║
╟────────────────────> Made by github.com/terremoth <─────────────────────╢
╚═════════════════════════════════════════════════════════════════════════╝'''

print(BANNER)

argparser = ArgumentParser()

argparser.add_argument('--install',    '-i', type=str, help='Install a package')
argparser.add_argument('--remove',     '-r', type=str, help='Remove a package')
argparser.add_argument('--update',     '-u', type=str, help='Update a package')
argparser.add_argument('--update-all', '-a', help='Update all packages', action='store_true')
argparser.add_argument('--search',     '-s', type=str, help='Search for a package')
argparser.add_argument('--list',       '-l', help='List all available packages', action='store_true')

args = argparser.parse_args()
# print(args)
# exit()

if not (args.install or args.remove or args.search or args.update):
    argparser.error('No command supplied for Zeus')

if args.remove:

    if not(os.path.isdir(PKG_DIR)):
        print("Error: no athena_libs directory found into the current path.")
        exit(1)

    full_lib_path = PKG_DIR+"/"+args.remove

    if not(os.path.isdir(full_lib_path)):
        print(f"Error: no package \"{args.remove}\" installed")
        exit(1)

    try:
        shutil.rmtree(full_lib_path)
        print(f"Done removing package: {args.remove}")
        exit(0)

    except:
        print("You need to have privileges to delete this directory. Please execute this script as admin or give the right permissions.")
        exit(1)


MAIN_REPO = "https://github.com/terremoth/athenaenv-libs"
RAW_REPO  = "https://raw.githubusercontent.com/terremoth/athenaenv-libs/main/"
PACKAGE_URL = MAIN_REPO+'/tree/main/'

HEADERS = ({'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.2403.157 Safari/537.36', 
        'Accept-Language': 'pt-BR, en;q=0.5'})
    
page = requests.get(MAIN_REPO, headers=HEADERS)

if page.status_code != 200:
    print("Error: AthenaEnv lib repository could not be fetched. Check your internet connection.")
    exit(1)


soup = BeautifulSoup(page.text, 'html.parser')
resp = soup.select('.js-navigation-open.Link--primary')

repos = []

for element in resp:
    if '/tree/' in element['href']:
        repos.append(element.get_text())

# --------------------------------------------------------------

def create_athena_dir_if_not_exist():
    os.makedirs(PKG_DIR, exist_ok=True)
        

def create_pkg_dir_if_not_exist(pkgname):
    
    create_athena_dir_if_not_exist()
    os.makedirs(PKG_DIR+pkgname, exist_ok=True)


package = args.install or args.update or args.update_all

if not(package in repos):
    print(f"Error: There is no package called \"{package}\"")
    exit(1)
    

def download_in_dir(url):
    
    page = requests.get(url, headers=HEADERS)
    
    if page.status_code != 200:
        print("Error: This repository url does not exist. This error is supposed to never happens!")
        exit(1)


    soup = BeautifulSoup(page.text, 'html.parser')

    json_object = json.loads(soup.text)

    items_in_dir = json_object['payload']['tree']['items']
    
    for item in items_in_dir:

        if item['contentType'] == 'directory':
            os.makedirs(PKG_DIR+item['path'], exist_ok=True)
            download_in_dir(PACKAGE_URL+item['path'])
        else:
            if item['name'] != 'description.txt':
                # print("to download: "+RAW_REPO+item['path'])
                with open(PKG_DIR+item['path'], "wb+") as output_file:
                    output_file.write(page.content)

    
create_pkg_dir_if_not_exist(package)

download_in_dir(PACKAGE_URL+package)