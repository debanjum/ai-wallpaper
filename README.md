WEATHER WALLPAPER
====================
> Update Wallpaper Based on Weather Conditions, City & Time


DEPENDENCIES
------------
+ `BASH`
+ `notify-send`: For Wallpaper Updating Notification [you can replace/modify the notification command to whatever suits]
+ `gsettings`: For Updating Wallpaper [you can replace/modify the wallpaper updating command to whatever suits]


INSTALLATION
------------
1. Clone Repository and Move into it
```$ git clone https://github.com/debanjum/Weatherwall.git && cd WeatherWall```
2. Get API Key for [Wunderground](http://www.wunderground.com/weather/api/) and APP ID for [Wolfram 
Alpha]((https://developer.wolframalpha.com/portal/apisignup.html))
3. Run the following commands
```sh
	#Make Scripts Suitable for execution. Customise for Your Build
	$ find ./ -type f -exec sed -i 's/\/path\/to/***/g' {} \; #Replace *** with repo folder location
	$ find ./ -type f -exec sed -i 's/YOUR_WOLFRAM_ALPHA_APPID/***/g' {} \;	#Replace *** with APP ID 
	$ find ./ -type f -exec sed -i 's/YOUR_WUNDERGROUND_APIKEY/***/g' {} \; #Replace *** with API KEY
	$ find ./ -type f -exec sed -i 's/City_1/***/g' {} \;   #Replace *** with City Name
	$ find ./ -type f -exec sed -i 's/Wunderground_City_1/***/g' {} \;   #Replace *** with wunderground's name for the above city_1
	#Optional
	$ find ./ -type f -exec sed -i 's/City_2/***/g' {} \;   #Replace *** with 2nd City Name
	$ find ./ -type f -exec sed -i 's/Wunderground_City_2/***/g' {} \;   #Replace *** with wunderground's name for the above city_2

	#Make Scripts executable
	$ sudo chmod +x Weather Wallpaper Wallpaper2 Location/Locate 
	# Run Scripts  
	$ ./Location/Locate	# Updates your Current Location
	$ ./Wallpaper2  	# Updates Wallpaper Based on Current Location Weather
	$ ./Wallpaper [Current/Forecast] [City]	#Enter Wunderground's Name for your City Name 
```

*For further details see: INSTALL*
 
DEBUGGING
------------
#### [WALLPAPER2](Wallpaper2) SCRIPT NOT RUNNING
1. If ```Location/location``` doesn't contain Your City Name you entered in ```INSTALLATION/4.```, replace
```cat ./Location/L.txt | grep "Chennai" ==> cat ./Location/L.txt | grep "keyword_in_Location/location```
2. If script still doesn't run, find your locations wunderground understandable name from the net, replace 
``` Wallpaper Current "Chennai" ==> Wallpaper Current "Wunderground_Understandable_City_Name" ```

#### WALLPAPER NOT UPDATING
1. Refresh your Desktop. On Gnome: ```Alt+F2``` & ```r```. Check whether you system uses *gsettings* if not replace with command line 
function of choice for changing desktop background on your OS
3. In case you're using your own wallpapers, Edit wallpaper script and point `$wallpaperdir` to desired wallpapers folder. Make sure 
they follow naming convention specified.



SCRIPTS:
------------
+ [Weather](Weather)	: To get updated weather report of specified city  
+ [Wallpaper](Wallpaper)  : To update wallpaper based on the weather report [current/forecast] & time in specified city  
+ [Wallpaper2](Wallpaper2): To update wallpaper based on the weather report [current/forecast] & time in auto-detected city  
+ [Locate_DDG](Locate_DDG) : To obtain current location based on ip using DuckDuckGo  
+ [Locate_WA](Locate_WA) : To obtain current location based on ip using Wolfram Alpha. Requires 
[App_ID](https://developer.wolframalpha.com/portal/apisignup.html)

FOLDERS:
------------
+ [.wallpapers](.wallpapers): Folder containing the wallpapers. See #*WALLPAPER NAMING CONVENTION*
+ [Icons](Icons) : Contains the Notification Icon.s
+ [Reports](Reports) : Contains the Weather Reports.
+ [Location](Location) : Script For Obtaining Current Location. See [README](LOCATION/README)


WALLPAPER NAMING CONVENTION: 
------------
```
  (timeofday)(weathercondition) (randomnumber).jpg
  where
    (timeofday)         = sr/m/ss/n     = Sunrise/Morning/Sunset/Night
    (weathercondition)  = cr/cd/f/r/    = Clear/Cloudy/Fog/Rain
    (randomnumber)      = 1,2,3...      = For selecting a random wallpaper
  example
    sscd (9).jpg        = SunsetCloudy9 = Chosen at cloudy sunset in specified city
```


ICONS
------------
+ The icons are licensed under the [CC0](https://creativecommons.org/publicdomain/zero/1.0/)
+ These icons are derivatives of icons from [THE NOUN PROJECT](http://thenounproject.com/) which are licensed under 
[CC-BY-SA](https://creativecommons.org/licenses/by-sa/3.0/)
+ See [Attributions](Icons/ATTRIBUTION).


REPORTS
------------

| Raw Report 	  |	Naming Convention		  |	Contains		 |
|:---------------:|:-------------------------------------:|:----------------------------:|
| Structure	  |	     `City`			  |    Raw XML from Wundergroud  |
| Example 	  |           `London`			  |    1 Day London Weather XML	 |
| **Final Report**|					  |	 			 |
| Structure	  | `City_Current` OR `City_Forecast` 	  |   Essential Weather Detail	 |
| Example 	  |       `London_Forecast`		  | 1 Day London Weather Forecast|


KNOWN ISSUES
------------
+ If using cron to run the wallpaper script and are running into problems. 
  Please verify that your crontab has the required environment variables to 
  update the wallpaper correctly : `dbus session bus address` + `PATH`
  If you don't know what to do just paste the results of running `env` in bash 
  into the top of crontab after every login
  OR 
+ Set up a script to run at login to do it for you
  OR
+ Ask me nicely and i might give you my script.


NOTE
------------
This program stores your location in plain text in your working directory. 
The only web queries made are to ```DuckDuckGo``` or ```Wolfram Alpha``` [for location querying] and ```Wunderground``` [for weather 
retrieval]
No data is communicated to any parties not mentioned above by the scripts themselves. Having said that it is considered the users 
prerogative to keep there data secure in whichever way they deem fit. The script(s) in this repository are, of course, open to scrutiny so edit as you deem appropriate.


BUGS
------------
Please file bugs at:  repo-url/issues
  
  
LICENSE
------------
This program is free software; it is distributed under the GNU General Public License v3.

[GPLv3](LICENSE) © [debanjum](debanjum@gmail.com)
