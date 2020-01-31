Vagrant.configure("2") do |config|
  config.vm.box = "hashicorp/bionic64"
  config.vm.provision "shell", 
    path:"bootstrap-db.sh",
    env: {"GUEST_HOME" => "/vagrant"}
  config.vm.provision "shell", 
    path:"bootstrap-app.sh",
    env: {"GUEST_HOME" => "/vagrant"}
  config.vm.network "forwarded_port", guest: 5000, host: 5000 
end
