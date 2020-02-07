# The following fixes a bug
# https://github.com/mitchellh/vagrant-aws/issues/566
class Hash
  def slice(*keep_keys)
    h = {}
    keep_keys.each { |key| h[key] = fetch(key) if has_key?(key) }
    h
  end unless Hash.method_defined?(:slice)
  def except(*less_keys)
    slice(*keys - less_keys)
  end unless Hash.method_defined?(:except)
end
# End of bug fix

Vagrant.configure("2") do |config|

  config.vm.provision "shell", 
    path:"bootstrap-db.sh", 
    env: {"GUEST_HOME" => "/vagrant"}
  config.vm.provision "shell", 
    path:"bootstrap-app.sh",
    env: {"GUEST_HOME" => "/vagrant"}

  config.vm.define "dev" do |dev|
    dev.vm.box = "hashicorp/bionic64"
    dev.vm.network "forwarded_port", guest: 5000, host: 5000 
    dev.vm.network "forwarded_port", guest: 3306, host: 3306 
  end

  config.vm.define "stage" do |stage|
    stage.vm.box = "dummy"
    stage.vm.box_url = "https://github.com/mitchellh/vagrant-aws/raw/master/dummy.box"
    stage.vm.synced_folder '.', '/vagrant', disabled: false, type: 'rsync'
    stage.vm.provider :aws do |aws|
      aws.keypair_name = "osx_rsa"
      aws.ami = "ami-06358f49b5839867c"
      aws.instance_type = "t2.micro"
      aws.subnet_id = "subnet-2c67fe64"
      aws.security_groups = "sg-7b78fe07"
      aws.associate_public_ip = true
      aws.aws_profile = "stage"
    end
    stage.ssh.username = "ubuntu"
    stage.ssh.private_key_path = "~/.ssh/osx_rsa.pem"
  end

  config.vm.define "prod" do |prod|
    prod.vm.box = "dummy"
    prod.vm.box_url = "https://github.com/mitchellh/vagrant-aws/raw/master/dummy.box"
    prod.vm.synced_folder '.', '/vagrant', disabled: false, type: 'rsync'
    prod.vm.provider :aws do |aws|
      aws.keypair_name = "osx_rsa"
      aws.ami = "ami-06358f49b5839867c"
      aws.instance_type = "t2.micro"
      aws.subnet_id = "subnet-2c67fe64"
      aws.security_groups = "sg-7b78fe07"
      aws.associate_public_ip = true
      aws.aws_profile = "prod"
    end
    prod.ssh.username = "ubuntu"
    prod.ssh.private_key_path = "~/.ssh/osx_rsa.pem"
  end

end
