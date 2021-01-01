terraform {
}

resource "docker_network" "zapata_network" {
  name = "zapata_network"
}

resource "docker_volume" "zapata_volume" {
  name = "zapata_volume"
}

resource "docker_container" "vault-server" {
  image   = "vault:1.3.2"
  name    = "vault-server"
  command = ["server"]
  restart = "always"
  ports {
    internal = "8200"
    external = "8200"
  }
  volumes {
    host_path      = "${path.cwd}/zapata/vault"
    container_path = "/vault"
  }
  env = ["VAULT_ADDR=http://localhost:8200"]
  capabilities {
    add = ["IPC_LOCK"]
  }
  networks_advanced {
    name = "zapata_network"
  }
}

resource "docker_container" "vault-client" {
  image   = "vault:1.3.2"
  name    = "vault-client"
  command = ["/usr/local/bin/vault-init.sh"]
  volumes {
    host_path      = "${path.cwd}/zapata/vault/vault-init.sh"
    container_path = "/usr/local/bin/vault-init.sh"
  }
  volumes {
    host_path      = "${path.cwd}/zapata/vault/vault-init.py"
    container_path = "/usr/local/bin/vault-init.py"
  }
  volumes {
    host_path      = "${path.cwd}/zapata/vault"
    container_path = "/vault"
  }
  volumes {
    host_path      = "${path.cwd}/zapata/vault/.env"
    container_path = "/.env"
  }
  volumes {
    host_path      = "${path.cwd}/zapata/vault/requirements.txt"
    container_path = "/requirements.txt"
  }
  volumes {
    host_path      = "${path.cwd}/modules"
    container_path = "/modules"
  }
  env = ["VAULT_ADDR=http://vault-servert:8200"]
  depends_on = [
    docker_container.vault-server
  ]
  user = "0"
  networks_advanced {
    name = "zapata_network"
  }
}
