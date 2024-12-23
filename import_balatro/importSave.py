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

	# Open and read the file in binary mode
	with open(f'{i}-meta.jkr', "rb") as file:
		meta_data = file.read()

	with open(f'{i}-profile.jkr', "rb") as file:
		profile_data = file.read()


	plist_data[f'{i}__meta.jkr.data'] = meta_data
	plist_data[f'{i}__profile.jkr.data'] = profile_data
	

with open(file_path, "wb") as file:
    plistlib.dump(plist_data, file)