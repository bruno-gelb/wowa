### wowa

World of Warcraft console addon manager

### features

* install, uninstall, upgrade [Twitch (CurseForge) addons](https://www.curseforge.com/wow/addons) in bulk from command line or from file
* lightweight and fast. Index and downloads are cached
* well thought-out interface
* requires no authorization wheresoever
* *(soon to be supported)* WoW installation path and version autodetect
* *(soon to be supported)* no installation required, just run the `.exe` file
* *(soon to be supported)* colorful output
* *(soon to be supported)* multiple addon providers ([wowinterface.com](https://wowinterface.com), [wowmatrix.com](https://wowmatrix.com))

### usage

Install addon:
```
wowa.py install recount
```
Install addons in bulk:
```
wowa.py install recount tomtom auctioneer
```
**TBI** Install specific version of addon:
```
wowa.py install recount==8.2.0a
```
**TBI** Install addons from file:
```
wowa.py install -y addons.yaml
```
Uninstall addon:
```
wowa.py uninstall recount
```
Uninstall all addons:
```
wowa.py uninstall
```
List installed addons:
```
wowa.py list
```
**TBI** Search for available to install addon versions:
```
wowa.py search recount
```
**TBI** Show addon info (description, total downloads, ..):
```
wowa.py info recount
```
**TBI** Upgrade all addons:
```
wowa.py upgrade
```
**TBI** Upgrade specific addon:
```
wowa.py upgrade recount
```
Show all available commands of the addon manager:
```
wowa.py --help
```
Show addon manager version:
```
wowa.py --version
```