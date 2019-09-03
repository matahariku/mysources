
Let's show how to install python-mode on Vim 8 on a Debian 9 host

<pre>
kalou@vps:~$ dpkg -l | grep vim | head -1
ii  vim                               2:8.0.0197-4+deb9u3                amd64        Vi IMproved - enhanced vi editor

</pre>

python-mode needs python support for vim vim-python, which brings python support for vim, is provided by the virtual package vim-nox

<pre>

kalou@vps:~$ sudo apt install vim-nox
Reading package lists... Done
Building dependency tree
Reading state information... Done
The following additional packages will be installed:
  libpython3.5 libruby2.3 libtcl8.6 rake ruby ruby-did-you-mean ruby-minitest ruby-net-telnet ruby-power-assert ruby-test-unit ruby2.3
  rubygems-integration
Suggested packages:
  tcl8.6 ri ruby-dev bundler cscope vim-doc
Recommended packages:
  zip fonts-lato
The following NEW packages will be installed:
  libpython3.5 libruby2.3 libtcl8.6 rake ruby ruby-did-you-mean ruby-minitest ruby-net-telnet ruby-power-assert ruby-test-unit ruby2.3
  rubygems-integration vim-nox
0 upgraded, 13 newly installed, 0 to remove and 0 not upgraded.
Need to get 7,017 kB of archives.
After this operation, 26.7 MB of additional disk space will be used.
Do you want to continue? [Y/n]

</pre>


Make the appropriate directory structure to install a plugin with Vim 8.x and up

<pre>

kalou@vps:~$ mkdir -p ~/.vim/pack/python-mode/start
kalou@vps:~$ cd ~/.vim/pack/python-mode/start
kalou@vps:~$ git clone --recurse-submodules --depth=1 https://github.com/python-mode/python-mode.git

</pre>

Start Vim, you're done !
