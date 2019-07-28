### wowa

wowa = World of Warcraft console Addon manager

![wowa](https://raw.githubusercontent.com/nazarov-tech/wowa/master/static/wowa_demo.gif)

### features
* install, uninstall, upgrade [Twitch (CurseForge) addons](https://www.curseforge.com/wow/addons) in bulk from command line or from file
* lightweight and fast. Index and downloads are cached
* well thought-out colorful interface
* requires no authorization wheresoever
* *(soon to be supported)* WoW installation path and version autodetect
* *(soon to be supported)* Windows installation binary ( `*.exe` / `*.msi` )
* *(soon to be supported)* multiple addon providers ([wowinterface.com](https://wowinterface.com), [wowmatrix.com](https://wowmatrix.com))
* *(later to be supported)* OS X / Linux installation binaries
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

### comparison to other WoW CLI addon tools

first of all, all these developers did fantastic job!
And please use these tools if you are willing to.

I'm not arranging this sheet to attack them.
It is merely a shy attempt to defend my own solution. :)

If you know some tool that should be added in this sheet, please contact me via issue / pull request!

|project|language|github stars|commits|last commit|forks|how exactly wowa is better|
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| [kuhnertdm/wow-addon-updater](https://github.com/kuhnertdm/wow-addon-updater) | Python | 116 | 123 | 11 months ago | 38 | No ready-to-use binary provided for the end users. The tool can serve only as an updater (no other addon managment), and the user has to manually search for http links and form the file (usability issues).  |
| [zekesonxx/wow-cli](https://github.com/zekesonxx/wow-cli) | JavaScript | 12 | 26 | 4 years ago | 4 | Even the latest fork was dropped 2 years ago. Interface is lacking consistency and features. No ready-to-use binary provided for the end users. |
| [wttw/wowaddon](https://github.com/wttw/wowaddon) | Go | 5 | 39 | 2 years ago | 2 | No ready-to-use binary provided for the end users. Was not tested with real WoW installation. |
| [acdtrx/wowam](https://github.com/acdtrx/wowam) | JavaScript | 1 | 21 | 3 years ago | None | No ready-to-use binary provided for the end users. Unsupported. Only couple of command implemented, no documentation or usability effot made. |
| [qwezarty/wow-addon-manager](https://github.com/qwezarty/wow-addon-manager) | Python | 0 | 38 | 5 months ago | None| Dropped at the early stage of development (according to readme). No ready-to-use binary provided for the end users. |