Vagrant.configure("2") do |config|
  config.vm.box = "hashicorp/bionic64"
  config.vm.provision "shell", path:"bootstrap-db.sh"
  config.vm.provision "shell", path:"bootstrap-app.sh"
  config.vm.network "forwarded_port", guest: 5000, host: 5000 
end
