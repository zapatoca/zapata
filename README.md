![Python application](https://github.com/zapatoca/zapata/workflows/Python%20application/badge.svg)

# zapata

## Spin DEV environment

* Run: `vagrant up dev`<br>
* Zapata - http://localhost:5000
* Vault  - http://localhost:8200

Or

* Run: `terraform apply -auto-approve`


## Teardown DEV environment

* Run: `vagrant destroy -f dev`

Or

* Run: `terraform destroy -auto-approve`


## Spin STAGE environment

* Run: `vagrant up stage`<br>
* Zapata - http://\<public ip\>:5000
* Vault  - http://\<public ip\>:8200


## Teardown STAGE environment

* Run: `vagrant destroy -f stage`
