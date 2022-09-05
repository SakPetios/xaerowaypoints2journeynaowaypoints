## Transfer the waypoints from Xaeros minimap mod to journeymini map with this script

### How to use:

With python run the file main.py followed with the xaeros minimap file and the parameter -f before the file then you also type the directory's path using the -fd parameter you want the waypoints to be saved.

eg.
> python main.py -f [file] -fd [folder]
## NOTE!
xaeros minimap mod save it's waypoints in 1 file but journeymap saves them to multiple files (1 file for each waypoint) as a result expect more that one file to appear
in your provided directory

# Troubleshooting:


# I get an Error (ERROR) File is a folder
- This happens when you file you provided the program is a folder check if the file is actually a folder.
- This can also occur when you provided the program with the wrong parameters. Check if you have typed the parameters correctly
Eg. python main.py -fd [file] -fd [folder].

Error-----------------^^^In this case I have typed "d" were I should not have

# I get an Error (Error) File/Folder Does not exist
- This happens when the file/folder you give to the main does not exist

# I get an Error (ERROR) Path must be folder
- Same case with the first error but with folder
- This happens when the path you provided leads to a file

