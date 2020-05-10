
## TEST : One config.spec to different platform binary.

### Concept **1** : Expands the resource files to a temporary file instead of storing them to the distribution file.

+ `extra_datas()` function in config.spec: Extract files under directory separately.

+ Specify all resource files in config.spec.

+ In main script (mikochiku_alarm.py), paths of all resource files are redirected to Temp dir by `resource_path()` function.

### Pros : 
+ The extracted directory of user is clean (only one .exe file).

### Cons :
+ Code maintenance becomes cumbersome: 
+ + We have to maintain config.spec every time we add a resource file.
+ + and, when specifying the path of a resource file in the main script, it should be enclosed in the resource_path() function.