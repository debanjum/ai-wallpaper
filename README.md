✨ AI Wallpaper
====================
> Get Khoj AI to paint custom wallpapers based on your location, weather (and even notes)


![](./assets/sample_khoj_wallpaper_2.png)


Prequisites
------------

- Generate a (free) [Khoj API Key](https://app.khoj.dev/config#clients)
- Install [Termux](https://f-droid.org/en/packages/com.termux/) to use on Android
- Mac or Android Operating System. *Windows, Linux support coming soon!*

Install
------------

1. Clone this Repository

2. Run any of the following commands to generate and set your Android, Mac wallpaper
   ```python
   # Minimal
   KHOJ_API_KEY=<YOUR_KHOJ_API_KEY> python Wallpaper.py

   # With Custom Prompt
   KHOJ_API_KEY=<YOUR_KHOJ_API_KEY> python Wallpaper.py "Generate a wallpaper based on the latest news here"

   # With Custom Wallpaper File Path
   KHOJ_API_KEY=<YOUR_KHOJ_API_KEY> WALLPAPER_PATH="~/Pictures/wallpaper.py" python Wallpaper.py

   # With Self-hosted Khoj
   KHOJ_HOST="http://localhost:42100" python Wallpaper.py

   ```

Extensions
------------
- Use Tasker on Android and Cron on Mac to automatically have Khoj paint a fresh Wallpaper for you daily
- Share your notes with Khoj to have the script incorporate elements from your recent notes into the wallpaper


LICENSE
------------
This program is free software; it is distributed under the GNU General Public License v3.

[GPLv3](LICENSE) © debanjum
