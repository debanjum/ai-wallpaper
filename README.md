<p align="center">
   <h1 align="center">✨ AI Wallpaper</h1>
</p>
<p align="center">
   <a href="https://github.com/khoj-ai/khoj"><img src="https://badgen.net/badge/powered by/%E2%9C%A8khoj%20ai/27c2d8/" /></a>
   <a href="LICENSE"><img src="https://badgen.net/github/license/debanjum/ai-wallpaper" /></a>
   <a href="https://pypi.org/project/ai-wallpaper/"><img src="https://badge.fury.io/py/ai-wallpaper.svg" /></a>
</p>

<p align="center">
   Get fresh, personal AI painted wallpapers daily
</p>

## 💎 Features
- Get fresh, personal wallpapers painted for you by [khoj ai](https://github.com/khoj-ai/khoj)
- Automatically weaves your current city, moon phase, weather and (even recent experiences!) into the painting
- Updates your Android or Mac wallpaper automatically
- Schedule it to run every day and night
- Customize the wallpapers by telling khoj what styles and information to use

## ✅ Prequisites

- Generate a (free) [Khoj API Key](https://app.khoj.dev/config#clients) or [setup a self-hosted Khoj](https://docs.khoj.dev/get-started/setup/)
- Install [Termux](https://f-droid.org/en/packages/com.termux/) to use on Android
- Requires a Mac or Android Operating System. *Windows, Linux support if enough demand*

## ⚡️ Quickstart
```shell
pip install ai-wallpaper && KHOJ_API_KEY=<YOU_KHOJ_API_KEY> aiwall
```

## 🎁 Showcase
| Day | Night |
|-----|-------|
| ![](./assets/ai_wallpaper_4.jpg) | ![](./assets/ai_wallpaper_1.jpg) |
| ![](./assets/ai_wallpaper_5.jpg) | ![](./assets/ai_wallpaper_2.jpg) |
| ![](./assets/ai_wallpaper_6.jpg) | ![](./assets/ai_wallpaper_3.jpg) |

https://github.com/debanjum/ai-wallpaper/assets/6413477/823c1624-6452-472e-8786-4cb79bcfa029


## 🪢 Customize
### Minimal
  ```shell
   KHOJ_API_KEY=<YOUR_KHOJ_API_KEY> aiwall
  ```

### Uze Custom Prompt
  ```shell
   KHOJ_API_KEY=<YOUR_KHOJ_API_KEY> aiwall "Generate a wallpaper based on the latest news here"
  ```

### Use Custom Wallpaper Path
  ```shell
   KHOJ_API_KEY=<YOUR_KHOJ_API_KEY> WALLPAPER_PATH="~/Pictures/wallpaper.png" aiwall
  ```

### Use Self-Hosted Khoj
  ```shell
   KHOJ_HOST="http://localhost:42100" aiwall
  ```

## 🚀 Upgrade
### Automatically get a fresh and personal wallpaper painted for you every day and night
  - Create a simple shell script to call the AI wallpaper creation command
    ```shell
     echo "#!/bin/sh\nKHOJ_API_KEY=<YOUR_KHOJ_API_KEY> aiwall" > wallpaper.sh
     chmod +x wallpaper.sh
    ```
  - On Android: Use [termux-job-scheduler](https://wiki.termux.com/wiki/Termux:API#:~:text=termux-job-scheduler) on Termux to get yourself a fresh and personal wallpaper painted every 12 hours
    ```shell
     # Install termux-job-scheduler to trigger script at a regular interval
     pkg install termux-job-scheduler
     # Make Khoj paint you a new wallpaper every 12 hours
     termux-job-scheduler -s aiwall --period-ms 43200000 --persisted true
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


## 🖥️ Develop

1. Download and Install
   ```shell
    # Clone the repository
    git clone https://github.com/debajum/ai-wallpaper

    # Install dependencies
    cd ai-wallpaper && pip install .
   ```

2. Edit application

3. Run any of the following commands to paint using your updated application
   ```shell
   # Minimal
   KHOJ_API_KEY=<YOUR_KHOJ_API_KEY> python src/aiwall/paper.py

   # With Custom Prompt
   KHOJ_API_KEY=<YOUR_KHOJ_API_KEY> python src/aiwall/paper.py "Generate a wallpaper based on the latest news here"

   # With Custom Wallpaper File Path
   KHOJ_API_KEY=<YOUR_KHOJ_API_KEY> WALLPAPER_PATH="~/Pictures/wallpaper.png" python src/aiwall/paper.py

   # With Self-hosted Khoj
   KHOJ_HOST="http://localhost:42100" python src/aiwall/paper.py
   ```

## 🔖 LICENSE
This program is free software; it is distributed under the GNU General Public License v3.

[GPLv3](LICENSE) © debanjum
