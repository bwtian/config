
### This file is automaticlly created by linuxInstall.org, do not change!!!
#!/bin/bash
cp ~/.bashrc ~/.bashrc.backup.`date +%Y-%m-%d-%H:%M`
cp ~/.bash_aliases ~/.bash_aliases.backup.`date +%Y-%m-%d-%H:%M`
rm -f ~/.bash_aliases
rm -f ~/.bashrc
ln -sfv ~/SparkleShare/config/shells/bash/bashrc ~/.bashrc
ln -sfv ~/SparkleShare/config/shells/bash/bash_aliases ~/.bash_aliases
