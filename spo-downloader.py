from bs4 import BeautifulSoup
import requests




def extract_music_songs(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        print(soup)
        # Find all meta tags within the head section with name='music:song'
        meta_tags = soup.head.find_all('meta', attrs={'name': 'music:song'})
        # Extract content of the meta tags
        songs = []
        for tag in meta_tags:
            songs.append(tag['content'])

        return songs
    else:
        print("Failed to retrieve page:", response.status_code)
        return []


def extract_artist_and_songs(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all meta tags within the head section with name='music:song'
        title = soup.head.find_all('meta', attrs={'property': 'og:title'})
        artist = soup.head.find_all('meta', attrs={'property': 'og:description'})
        
        # Extract content of the meta tags
        songs = []
        songs.append({
           'track_name': title[0].get('content') ,'artist_name':  artist[0].get('content')
        })
        return songs
    else:
        print("Failed to retrieve page:", response.status_code)
        return []

def generate_bash_script(json_data):
    # Start the Bash script content
    script_content = '''#!/bin/bash\n\n'''

    # Loop through each JSON object
    for item in json_data:
        # Extract track name and artist name from JSON
        track_name = item['track_name']
        artist_name = item['artist_name']

        # Add commands to the Bash script content
        script_content += f'yt-dlp --extract-audio --audio-format mp3 "ytsearch:'+track_name+'"\n'
        # Add more commands as needed...

    # Print the generated Bash script content
    with open("output.sh", "w") as file:
    # Write the data to the file
        file.write(script_content)



# Example usage
url = 'https://open.spotify.com/playlist/6lfdNsMe55niLUywavtOSI'
songs = extract_music_songs(url)


tracks = []
# Print the extracted songs
if songs:
    print("Songs:")
    for song in songs:
        tracks.append(extract_artist_and_songs(song)[0])
    generate_bash_script(tracks)
    print('playlist scraping successfull')
    print('starting song downloads')
else:
    print("No songs found.")


import subprocess

bash_script_path = 'output.sh'

# Execute the bash script and capture the output
result = subprocess.run(['bash', bash_script_path], capture_output=True, text=True)

# Check if the bash script executed successfully
if result.returncode == 0:
    print("Bash script executed successfully.")
    print("Output:")
    print(result.stdout)
else:
    print("Error executing bash script:")
    print(result.stderr)



 