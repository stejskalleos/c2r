#!/usr/bin/bash

echo '#################'
echo 'Enabling Satellite repositories'
echo '#################'

/usr/bin/subscription-manager repos --enable=rhel-8-for-x86_64-baseos-rpms \
  --enable=rhel-8-for-x86_64-appstream-rpms \
  --enable=satellite-6.13-for-rhel-8-x86_64-rpms \
  --enable=satellite-maintenance-6.13-for-rhel-8-x86_64-rpms


echo '#################'
echo 'Updating system'
echo '#################'

/usr/bin/dnf module enable satellite -y
/usr/bin/dnf update -y

echo ''
