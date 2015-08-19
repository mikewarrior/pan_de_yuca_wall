Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/trusty64"

  config.vm.synced_folder "salt/roots/", "/srv/salt/"

  config.vm.provision :salt do |salt|
    salt.bootstrap_options = "-P"
    salt.minion_config = "salt/minion"
    salt.run_highstate = true
  end
end
