Param(
    [string]$filename
)

if (-not $filename) {
    Write-Host "Iltimos, fayl nomini kiriting, masalan: .\push_day.ps1 -filename day2_12_12_25.py"
    exit
}

# Git qo‘shish
git add $filename

# Commit qilish
git commit -m "Add $filename"

# GitHub’ga push qilish
git push

Write-Host "$filename muvaffaqiyatli GitHub’ga yuklandi!"
