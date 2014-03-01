INSTALLATION
===============

BASIC
---------------
1. Clone folder to desired local directory
	git clone repo-url.git
2. Edit wallpaper script and point to desired wallpapers folder in gsettings commands.
3. Edit Wunderground API Key to your Key 
  + To obtain wunderground API key
  + Go to wunderground developers site
  + Create account [If you don't have one already]
  + Obtain API Key
  + Replace in Script
    * Note: Google's your friend. If you're convinced its not, try DuckDuckGo.
4. Make Weather, Wallpaper Scripts executable 
	sudo chmod +c Weather
	sudo chmod +c Wallpaper
5. Run Scripts
  - If Auto Locating
		./Wallpaper Current
		./Wallpaper Forecast
  - If India
		./Wallpaper Current/Forecast City
		./Weather Current/Forecast City
  - Else
		./Wallpaper Current/Forecast City Country
		./Weather Current/Forecast City Country


INTERMEDIATE
---------------
  + Add Wallpaper & Weather scripts to /bin or user bin folder
  + Add cronjob to update every sunrise, morning, noon, sunset, night
  + Run script from Startup Applications to run @ login
  + Sync with Tasker on Phone, so that you have the same wallpapers on both screens!
    + Add Wallpaper No to Dropbox
    + Create Tasker Profile to Obtain Weather Conditions + Time
    + Add Wallpapers Folder to Phone/Dropbox
    + Update Wallpaper to "(timeofday)(weather) (DropboxNo).jpg"
    OR
    See Note: BASIC > 3 > *
    OR
    Ask me for my tasker profile 
    * Note: You'll need to do extract the (DropboxNo) yourself, thats trivial though


TROUBLESHOOTING
---------------
+ To avoid having to update dbus_session_address manually every login
  - In Startup Application add script to set environment variables in crontab
+ Edit wallpaper script and point to desired wallpapers folder in gsettings commands correctly
  - The wallpapersdir variable doesn't do anything as of now 
    + Can't get it to work with the find, shuf command in script :(
