#!/bin/zsh
setopt nullglob # 防止 * 在空目录时报错

# 默认目录 (如果没有传参数)
Directory="${1:-/storage/emulated/0/ItsBelongOfMe/Lab}" 
ScriptPath=$(realpath "$0")  # 脚本绝对路径
ScriptDir=$(dirname "$ScriptPath") # 脚本所在目录

cd "$Directory" || exit

for file in *; do
    if [[ -f "$file" ]]; then
        case "${file##*.}" in
            jpg|png|jpeg|gif)
                folder="Images"
                ;;
            mp4|mkv|avi)
                folder="Videos"
                ;;
            mp3|wav|flac)
                folder="Music"
                ;;
            pdf|doc|docx|txt|md)
                folder="Documents"
                ;;
            *)
                folder="Others"
                ;;
        esac

        mkdir -p "$folder"
        mv "$file" "$folder/"
    
    elif [[ -d "$file" ]]; then
        # 跳过分类目录 + 跳过脚本所在目录
        case "$file" in
            Images|Videos|Music|Documents|Others)
                continue
                ;;
        esac
        
        # 跳过脚本所在目录
        [[ "$(realpath "$file")" == "$ScriptDir" ]] && continue
        
        # 进入子目录并递归执行脚本
        (cd "$file" && zsh "$ScriptPath")
        
    fi
done

# 屏幕上的 “改动点” 部分没有在代码主体中体现，但我将相关的逻辑都整合进去了。
# 特别是：
# 1. 增加了获取脚本目录的逻辑：ScriptDir=$(dirname "$ScriptPath")
# 2. 在处理目录时增加了跳过脚本所在目录的判断：[[ "$(realpath "$file")" == "$ScriptDir" ]] && continue
