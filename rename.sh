# Rename an mp3 and all references to it
# Usage: rename.sh <old> <new>
# Example: rename.sh Oh_Lord_Won\'t_You_Buy_me_A_Mercedes_Benz_\(02\).mp3 Oh_Lord_Won\'t_You_Buy_me_A_Mercedes_Benz_\(03\).mp3

old=$1
new=$2

git mv mp3/$old mp3/$new
sed -i "s/$old/$new/g" songs.csv
sed -i "s/$old/$new/g" *.html
sed -i "s/$old/$new/g" *.txt
git commit -m "rename $old to $new" -a
echo "Do lyrics manually if needed"

