Hello judges! We are so excited to have you here to try our program! There are a few important dependancies that you will need to install first though, but please READ THE ENITRE README BEFORE DOWNLOADING ANYTHING, To ensure proper installation of this demo.

1. This project relies on two tools used for pen testing in Cybersecurity, nmap and Metasploit. UNDER NO CURCIMSTANCE WILL YOU ATTEMPT TO INSTALL this in order to cause harm to anyone else or violate there personal data and security in any way shape or form.

Although we do not utilize it for this, Metasploit is a very cybercecurity software, and is very popular for applications in CTFs. Because of this, it contains some files that will alert your 
antivirus. 

2. THIS PROJECT WILL ONLY RUN ON LINUX. If you wish to install it, please use an Ubuntu or other similar linux Virtual Machine, such as kali-linux or parrot-os as it will not work otherwise.

3. BE CAUTIOUS WHEN USING THIS PROGRAM. DO NOT USE THIS ON ANY IP OTHER THAN YOUR OWN. You must be aware that a large number of requests will be made by this program to the network of choice, and less stable networks have a rather high chance of failing. REMEBER PLEASE ONLY USE ON IP'S THAT YOU OWN AND NOT RANDOM IP'S.

ONCE THE FOLLOWING IS INSTALLED, RUN uimain.py TO ACCESS THE PROGRAM.

INSTALLATION:

1. Metasploit. Copy and paste the lines one at a time in your Ubuntu terminal, and you could be good to go. If you have trouble, refer to https://www.darkoperator.com/installing-metasploit-in-ubunt.

  sudo add-apt-repository -y ppa:webupd8team/java
  sudo apt-get update
  sudo apt-get -y install oracle-java8-installer
  
  sudo apt-get update
  sudo apt-get upgrade
  
  sudo apt-get nmap
  
  sudo apt-get install build-essential libreadline-dev libssl-dev libpq5 libpq-dev libreadline5 libsqlite3-dev libpcap-dev git-core autoconf postgresql pgadmin3 curl zlib1g-dev libxml2-dev libxslt1-dev libyaml-dev curl zlib1g-dev gawk bison libffi-dev libgdbm-dev libncurses5-dev libtool sqlite3 libgmp-dev gnupg2 dirmngr
      If this line doesn't work, you may need to intall certain dependancies individually as they arrise.
      
  gpg2 --keyserver hkp://pool.sks-keyservers.net --recv-keys 409B6B1796C275462A1703113804BB82D39DC0E3 7D2BAF1CF37B13E2069D6956105BD0E739499BDB
  curl -L https://get.rvm.io | bash -s stable
  source ~/.rvm/scripts/rvm
  echo "source ~/.rvm/scripts/rvm" >> ~/.bashrc
  source ~/.bashrc
  RUBYVERSION=$(wget https://raw.githubusercontent.com/rapid7/metasploit-framework/master/.ruby-version -q -O - )
  rvm install $RUBYVERSION
  rvm use $RUBYVERSION --default
  ruby -v
  
        If this doesn't work its usually okay
        
cd ~
git clone git://github.com/sstephenson/rbenv.git .rbenv
echo 'export PATH="$HOME/.rbenv/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(rbenv init -)"' >> ~/.bashrc
exec $SHELL

git clone git://github.com/sstephenson/ruby-build.git ~/.rbenv/plugins/ruby-build
echo 'export PATH="$HOME/.rbenv/plugins/ruby-build/bin:$PATH"' >> ~/.bashrc

# sudo plugin so we can run Metasploit as root with "rbenv sudo msfconsole" 
git clone git://github.com/dcarley/rbenv-sudo.git ~/.rbenv/plugins/rbenv-sudo

exec $SHELL

RUBYVERSION=$(wget https://raw.githubusercontent.com/rapid7/metasploit-framework/master/.ruby-version -q -O - )
rbenv install $RUBYVERSION
rbenv global $RUBYVERSION
ruby -v

mkdir ~/Development
cd ~/Development
git clone https://github.com/nmap/nmap.git
cd nmap 
./configure
make
sudo make install
make clean

cd /opt
sudo git clone https://github.com/rapid7/metasploit-framework.git
sudo chown -R `whoami` /opt/metasploit-framework
cd metasploit-framework

cd metasploit-framework

gem install bundler
bundle install

cd metasploit-framework
sudo bash -c 'for MSF in $(ls msf*); do ln -s /opt/metasploit-framework/$MSF /usr/local/bin/$MSF;done'

echo "export PATH=$PATH:/usr/lib/postgresql/10/bin" >> ~/.bashrc
. ~/.bashrc 

sudo usermod -a -G postgres `whoami`
sudo su - `whoami

cd /opt/metasploit-framework/
./msfdb init

msfconsole
