#!/usr/bin/bash

echo ''
echo '#################'
echo 'Installing Satellite'
echo '#################'

/usr/bin/dnf install satellite -y

echo ''
echo '#################'
echo 'Running Satellite installer'
echo '#################'

echo "$(hostname -I | awk '{print $1}') $(hostname -f)" > /etc/hosts

/usr/sbin/satellite-installer --scenario satellite \
        --foreman-initial-admin-username admin \
        --foreman-initial-admin-password admin
