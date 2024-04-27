<p align="center">
   <h1 align="center">✨ AI Wallpaper</h1>
</p>
<p align="center">
   <a href="https://github.com/khoj-ai/khoj"><img src="https://badgen.net/badge/powered by/%E2%9C%A8khoj%20ai/27c2d8/" /></a>
   <a href="LICENSE"><img src="https://badgen.net/github/license/debanjum/ai-wallpaper" /></a>
</p>

<p align="center">
   Get fresh, personal AI painted wallpapers daily
</p>

Features
--------
- Get fresh, personal wallpapers painted for you by [khoj ai](https://github.com/khoj-ai/khoj)
- Automatically weaves your current city, moon phase, weather and (even recent experiences!) into the painting
- Updates your Android or Mac wallpaper automatically
- Schedule it to run every day and night
- Customize the wallpapers by telling khoj what styles and information to use

![](./assets/sample_khoj_wallpaper_2.png)


Prequisites
------------

- Generate a (free) [Khoj API Key](https://app.khoj.dev/config#clients) or [setup a self-hosted Khoj](https://docs.khoj.dev/get-started/setup/)
- Install [Termux](https://f-droid.org/en/packages/com.termux/) to use on Android
- Requires a Mac or Android Operating System. *Windows, Linux support if enough demand*

Install
------------

1. Clone this Repository

2. Run any of the following commands to paint and update your wallpaper
   ```python
   # Minimal
   KHOJ_API_KEY=<YOUR_KHOJ_API_KEY> python Wallpaper.py

   # With Custom Prompt
   KHOJ_API_KEY=<YOUR_KHOJ_API_KEY> python Wallpaper.py "Generate a wallpaper based on the latest news here"

   # With Custom Wallpaper File Path
   KHOJ_API_KEY=<YOUR_KHOJ_API_KEY> WALLPAPER_PATH="~/Pictures/wallpaper.png" python Wallpaper.py

   # With Self-hosted Khoj
   KHOJ_HOST="http://localhost:42100" python Wallpaper.py
   ```

Extensions
------------
### Automatically get a fresh and personal wallpaper painted for you every day and night
  - Create a simple shell script to call the AI wallpaper creation command
    ```shell
     cd /path/to/ai/wallpaper/folder/
     echo "#!/bin/sh\nKHOJ_API_KEY=<YOUR_KHOJ_API_KEY> python $PWD/Wallpaper.py" > wallpaper.sh
     chmod +x wallpaper.sh
    ```
  - On Android: Use [termux-job-scheduler](https://wiki.termux.com/wiki/Termux:API#:~:text=termux-job-scheduler) on Termux to get yourself a fresh and personal wallpaper painted every 12 hours
    ```shell
     # Install termux-job-scheduler to trigger script at a regular interval
     pkg install termux-job-scheduler
     # Make Khoj paint you a new wallpaper every 12 hours
     termux-job-scheduler -s /path/to/ai/wallpaper/folder/wallpaper.sh --period-ms 43200000 --persisted true
     # Optional, check that the script is active
     # termux-job-scheduler -p
    ```
    Note: *You can use [Tasker](https://play.google.com/store/apps/details?id=net.dinglisch.android.taskerm&hl=en&gl=US) + [Termux:Tasker](https://wiki.termux.com/wiki/Termux:Tasker) or other automations apps to trigger the Wallpaper script as well*
  - On Mac: Use Cron to get yourself a fresh and personal wallpaper painted every 12 hours
    ```shell
     # Open crontab in edit mode
     crontab -e

     # Add below snippet to your crontab
     # 0 */12 * * /path/to/ai/wallpaper/folder/wallpaper.sh

     # Optional, check that the script is active
     # crontab -l
    ```

### Weave experiences from your notes into the Wallpapers
The AI wallpaper script can automatically incorporate any recent experiences from your notes into it's paintings. To use this you will need to sync your notes with Khoj.


LICENSE
------------
This program is free software; it is distributed under the GNU General Public License v3.

[GPLv3](LICENSE) © debanjum
