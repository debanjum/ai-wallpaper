LOCATE
====================
+ Update Current Location based on your IP


DEPENDENCIES
-----------------
+ Bash: 
   - notify-send: For Wallpaper Updating Notification [not necessary, you can replace/modify the notification command to whatever suits]
   - gsettings: For Updating Wallpaper [you can replace/modify the wallpaper updating command to whatever suits]


SCRIPTS:
-----------------
+ Locate_DDG: To get Current/LastKnown Location by querying DuckDuckGo. Currently Less Accurate
+ Locate_WA: To get Current/LastKnown Location by querying Wolfram Alpha. Requires Wolfram Alpha AppID in Script. More Accurate


FOLDERS:
-----------------
+ Icons	: Contains the Notification Icons.  [ see ICONS ]


ICONS
-----------------
+ The icons are licensed under the CC0: See https://creativecommons.org/publicdomain/zero/1.0/ for further details.
+ These icons are derivatives of icons from THE NOUN PROJECT which are licensed under CC-BY-SA. 
  See http://thenounproject.com/ and https://creativecommons.org/licenses/by-sa/3.0/ for further details.
+ See ./Icons/ATTRIBUTION for Attributions.


INSTALLATION
-----------------
1. Clone folder to desired local directory	`git clone repo-url.git`
2. If querying Wolfram Alpha, 
   1. Get [App_ID](https://developer.wolframalpha.com/portal/apisignup.html). 
   2. Create Application. 
   3. Obtain APP_ID. 
   4. Edit Wolfram Alpha script and add your APP_ID.
3. Copy Script to be used [Locate_DDG or Locate_WA] to ../Locate & make it executable
	$ cp Location/Locate_WA ../Locate
	$ sudo chmod +x ./Locate
  4. Run Scripts
	$ ./Locate


BUGS
-----------------
Please file bugs at:  repo-url/issues

LICENSE
-----------------
This program is free software; it is distributed under the GNU General Public License v3.

[GPLv3](LICENSE) © [debanjum](debanjum@gmail.com)
