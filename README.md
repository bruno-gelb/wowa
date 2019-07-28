### wowa

wowa = World of Warcraft console Addon manager

![wowa](https://raw.githubusercontent.com/nazarov-tech/wowa/master/static/wowa_demo.gif)

### features
* install, uninstall, upgrade [Twitch (CurseForge) addons](https://www.curseforge.com/wow/addons) in bulk from command line or from file
* lightweight and fast. Index and downloads are cached
* well thought-out colorful interface
* requires no authorization wheresoever
* *(soon to be implemented)* WoW installation path and version autodetect
* *(soon to be implemented)* Windows ready-to-use installation binary ( `*.exe` / `*.msi` )
* *(soon to be implemented)* multiple addon providers ([wowinterface.com](https://wowinterface.com), [wowmatrix.com](https://wowmatrix.com))
* *(later to be implemented)* OS X / Linux ready-to-use installation binaries
### usage

```
wowa.py install recount  # install addon
wowa.py install recount tomtom auctioneer  # install addons in bulk
wowa.py install recount==8.2.0a  # install specific version of addon <to be implemented>
wowa.py install -y addons.yaml  # install addons from file <to be implemented>
wowa.py uninstall recount  # uninstall addon
wowa.py uninstall  # uninstall all addons
wowa.py list  # list installed addons
wowa.py search recount  # search for available to install addon versions <to be implemented>
wowa.py info recount  #  show addon info (description, total downloads, ..) <to be implemented>
wowa.py upgrade  # upgrade all addons <to be implemented>
wowa.py upgrade recount  # upgrade specific addon <to be implemented>
wowa.py --help  # show all available commands of the addon manager
wowa.py --version  # show addon manager version
```

### why not use Twitch client / WowMatrix / WoWInterface / Tukui?

1. Twitch client is most popular, however, it's also slow and bloated with streams, games, chats, .. (sorry). This tool solves one and only one problem: to manage WoW addons. And does it well.
1. Each popular GUI client (Twitch, WowMatrix, WoWInterface, Tukui) support only their own addons repository. This tool is intended to support all of them.
1. CLI is quicker and more powerful of GUI by it's nature.

### why not use other WoW CLI addon tools?

|project|language|github stars|commits|last commit|forks|how exactly wowa is better|
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| [kuhnertdm/wow-addon-updater](https://github.com/kuhnertdm/wow-addon-updater) | Python | 116 | 123 | 11 months ago | 38 | No ready-to-use binary provided for the end users. The tool can serve only as an updater (no other addon management), and the user has to manually search for http links and form the file (usability issues).  |
| [zekesonxx/wow-cli](https://github.com/zekesonxx/wow-cli) | JavaScript | 12 | 26 | 4 years ago | 4 | Even the latest fork was dropped 2 years ago. Interface is lacking consistency and features. No ready-to-use binary provided for the end users. |
| [wttw/wowaddon](https://github.com/wttw/wowaddon) | Go | 5 | 39 | 2 years ago | 2 | No ready-to-use binary provided for the end users. Was not tested with real WoW installation. |
| [acdtrx/wowam](https://github.com/acdtrx/wowam) | JavaScript | 1 | 21 | 3 years ago | None | No ready-to-use binary provided for the end users. Unsupported. Only couple of commands implemented, no documentation or usability effort made. |
| [qwezarty/wow-addon-manager](https://github.com/qwezarty/wow-addon-manager) | Python | 0 | 38 | 5 months ago | None| Dropped at the early stage of development (according to readme). No ready-to-use binary provided for the end users. |

### contributing

You are welcome to contribute: [contributing guide](CONTRIBUTING.md).