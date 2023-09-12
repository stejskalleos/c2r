# Convert2RHEL Satellite Appliance repository
```
http://c2r.stejskalleos.cz/
```

# How to install
Add repo `/etc/yum.repos.d/c2r-satellite.repo`
```
# /etc/yum.repos.d/c2r-satellite.repo

[c2r-satellite]
name=Convert2RHEL Satellite Appliance
baseurl=http://c2r.stejskalleos.cz/rhel/8/x86_64
enabled=1
```

Install rpm
```
dnf install convert2rhel-init
```

# How to develop
For inspiration see:
```
https://gist.github.com/fernandoaleman/1377211
```

# How to sync from local to repo
```
rsync -avzhe ssh /path/to/c2r/repo/* account@stejskalleos.cz:/var/www/c2
```
