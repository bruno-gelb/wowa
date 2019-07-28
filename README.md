### wowa

World of Warcraft console addon manager

### usage

Install addon:
```
wowa.py install recount
```
Install specific version of addon:
```
wowa.py install recount==8.2
```
Install addons in bulk:
```
wowa.py install -f addons.yaml
```
Uninstall addon:
```
wowa.py uninstall recount
```
Upgrade all addons:
```
wowa.py upgrade
```
Upgrade specific addon:
```
wowa.py upgrade recount
```
List installed addons:
```
wowa.py installed
```
Show info about specific installed addon:
```
wowa.py installed recount
```
Search for available to install addon versions:
```
wowa.py search recount (вывести доступные в индексе версии аддона)
```
Show addon info (description, total downloads, ..):
```
wowa.py info recount
```
Show all available commands of the addon manager:
```
wowa --help (вывести помощь)
```
Show addon manager version:
```
wowa -v (вывести версию)
```