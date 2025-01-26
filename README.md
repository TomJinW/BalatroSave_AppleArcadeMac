# BalatroSave_AppleArcadeMac
Import &amp; Export Save Files to/from Balatro+ for Apple Arcade on macOS, meta.jkr and profile.jkr only, save.jkr is not handled.

# How to use

-  Export Save:
    ```
    python3 export_balatro/exportSave.py
    ```
    This will generate {profile_number}_meta.jkr and {profile_number}_profile.jkr .

-  Import Save:
    ```
    python3 import_balatro/importSave.py
    ```
    This will find existing {profile_number}_meta.jkr and {profile_number}_profile.jkr , and then use its data to inject into .plist file of the Apple Arcade game. Launch the game and create profiles in the game first in order to inject the data.
