import requests

SAVED_SITE_FILE_PATH = './site.txt'
SITE_URL = 'https://www.sullivancounty-pa.us/covid19'

def get_site(site_url):
  return requests.get(site_url)

def get_saved_site_response(file_path):
  try:
    with open(file_path, 'r') as save_file:
      return save_file.read()
  except FileNotFoundError as e:
    print("no saved site found")
    return None

def save_new_site_response(file_path, site_response):
  with open(file_path, 'w') as save_file:
    save_file.write(site_response)

if __name__ == '__main__':
  last_site_content = get_saved_site_response(SAVED_SITE_FILE_PATH)
  new_site_content = get_site(SITE_URL).content
  if str(last_site_content) != str(new_site_content):
    print("the site has changed")
  save_new_site_response(SAVED_SITE_FILE_PATH, str(new_site_content))
  
  
