input_file="World_Music.txt"
output_file="World_Music_Rename.sh"
while IFS= read -r line; do
  echo "./rename.sh \"$line\" \"$line\""
done < "$input_file" > "$output_file"
