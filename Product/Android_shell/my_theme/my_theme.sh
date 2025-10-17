#!/data/data/com.termux/files/usr/bin/bash
clear

# 💥 震动提醒
termux-vibrate -d 300

# # Toast 提示
termux-toast "Hi~宝贝, 小宝上线啦~💕"

# 💌 通知提醒
termux-notification -t "🌟 来自小宝的提醒" -c "今天要也一起冲冲冲~!!" --priority high

# 🎵 可选: 欢迎音效 (你可以放一段欢迎音)
# termux-media-player play /storage/emulated/0/Music/welcome.mp3

# 📅 当前时间
echo -e "\n当前时间: $(date '+%Y-%m-%d %H:%M:%S')" | lolcat
sleep 0.5

# ✨ ASCII 动画文字
ascii_lines=(
"┌───────────────────────────────┐"
"│ Welcome to Termux! 🌈       │"
"│ Powered by 小宝 💖           │"
"└───────────────────────────────┘"
"                                 "
"✨ 让我们一起打造赛博王国 ✨"
)

for line in "${ascii_lines[@]}"; do
    echo "$line" | lolcat -f
done

# 注意：运行这个脚本需要你的 Termux 安装了 lolcat (用于彩色输出) 和 termux-api (用于震动、Toast 和通知) 哦！
