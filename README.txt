# Removing tabs from file (OSX)
sed 's/\	/,/g' pidlog2.txt
# Removing trailing character from file
sed 's/.$//' roll1new.txt >> roll1new2.txt
