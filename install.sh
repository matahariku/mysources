#/bin/bash

#
# GOAL
# 
# - once downloaded (git/http/scp)
#   curl http://github.com/matahariku/mysources/install.sh
#   to local user home directory,

usage () {
cat << EOT
./install.sh # will install below <HOME>/mysources
EOT
} 

[ -f $HOME/install.sh ] || {
 usage
}
