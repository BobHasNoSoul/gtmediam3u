import requests
import json

# Define the base URLs
channel_info_url = "http://192.168.1.178:181/getallservices?id=4400&count=700&page=-1"
#epg_info_base_url = "http://192.168.1.178:181/proginfo?id="

# Send a GET request to retrieve channel information
channel_info_response = requests.get(channel_info_url)
channel_info_data = channel_info_response.json()

# Create an empty list to store M3U entries
m3u_entries = []

# Iterate through the channels and create M3U entries
for channel in channel_info_data["services"]:
    channel_name = channel["servicename"]
    channel_id = channel["id"]
    video_stream_url = channel["url"]

    # Send a GET request to retrieve EPG information for the channel
    epg_info_url = f"{epg_info_base_url}{channel_id}"
    epg_info_response = requests.get(epg_info_url)
    epg_info_data = epg_info_response.json()

    # Create M3U entry with EPG information and add it to the list
    m3u_entry = f"#EXTINF:-1 tvg-id=\"{channel_id}\" tvg-name=\"{channel_name}\",{channel_name}\n{video_stream_url}"
    m3u_entries.append(m3u_entry)

# Create the final M3U playlist by joining all the entries
m3u_playlist = "\n".join(m3u_entries)

# Write the M3U playlist to a file
with open("channels.m3u", "w") as m3u_file:
    m3u_file.write(m3u_playlist)

print("M3U playlist containing all channels and EPG data has been created.")
