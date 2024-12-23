import plistlib
import base64
import getpass

# Get the current username
username = getpass.getuser()

# Specify the path to your binary plist file
file_path = f"/Users/{username}/Library/Containers/com.playstack.balatroarcade/Data/Library/Preferences/com.playstack.balatroarcade.plist"

# Open and read the binary plist file
with open(file_path, "rb") as file:
    plist_data = plistlib.load(file)

# Print the contents of the plist file

for i in range(1,4):
	if (f'{i}__profile.jkr.data' not in plist_data):
		continue
	meta_data = plist_data[f'{i}__meta.jkr.data']
	profile_data = plist_data[f'{i}__profile.jkr.data']
	
	with open(f'{i}-meta.jkr', "wb") as file:
		print(f'Writing meta data {i}_meta.jkr')
		file.write(meta_data)
		file.close()

	with open(f'{i}-profile.jkr', "wb") as file:
		print(f'Writing profile data {i}_profile.jkr')
		file.write(profile_data)
		file.close()
