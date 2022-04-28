# A collection of useful tools
- net6-upgrade/upgrade_net6.py - A tool that takes given .csproj file and updates it to .NET 6, it updates all dependencies that are available on https://nuget.org to the latest stable release. It's version control friendly as it only performs string operations so resulting file will be exactly the same as the source file.

## upgrade_net6.py usage
Script is going to go through the .csproj file and extract packages, it is going to use NuGet.org RSS feed to extract the newest, stable release of the given package.   

Overwriting source file:  
`python upgrade_net6.py --input absolut/path/to/the/file/Project.csproj --overwrite`  

Creating new output file - the output file must not exist - this is to prevent accidental overwritting:  
`python upgrade_net6.py --input absolut/path/to/the/file/Project.csproj --output absolut/path/to/the/file/Project2.csproj`  


