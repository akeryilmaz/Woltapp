Woltapp Task

Run these commands before use:
mkdir -p ~/bin
cp median_times.py ~/bin
cp Helsinki.csv ~/bin
cp pickup_times.csv ~/bin
export PATH=$PATH":$HOME/bin"

Then, use as:
median_times.py Location yyyy-mm-dd hh-hh Path

eg:
median_times.py Helsinki 2019-01-07 19-20 median_times.csv

After Use you can run commands:
rm -rf ~/bin

P.S: For different locations, script can be used, provided that LocationName.csv file is in ~/bin directory.
