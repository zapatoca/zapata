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

  config.vm.provision :docker
  config.vm.provision :docker_compose,
    compose_version: "1.28.2",
    yml: "/vagrant/docker-compose.yml",
    run: "always",
    env: {
      "HOME"                  => "/vagrant",
      "AWS_ACCESS_KEY_ID"     => ENV['AWS_ACCESS_KEY_ID'],
      "AWS_SECRET_ACCESS_KEY" => ENV['AWS_SECRET_ACCESS_KEY'],
      "AWS_DEFAULT_REGION"    => ENV['AWS_DEFAULT_REGION']
    }

  config.vm.define "dev" do |dev|
    dev.vm.box = "hashicorp/bionic64"
    dev.vm.network "forwarded_port", guest: 5000, host: 5000
    dev.vm.network "forwarded_port", guest: 5432, host: 5432

    dev.trigger.before :destroy do |trigger|
      trigger.info = "Dumping the database before destroying the VM..."
      trigger.on_error = :continue
      trigger.run_remote = {inline: "docker exec -t db pg_dump -U zapata zapata -f /tmp/dump.sql"}
    end

    dev.trigger.after :up do |trigger|
      trigger.info = "Restoring the database after spinning the VM..."
      trigger.on_error = :continue
      trigger.run_remote = {inline: "sleep 30;docker exec -t db psql -U zapata -d zapata -f /tmp/dump.sql"}
    end
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
