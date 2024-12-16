#!/usr/bin/env python3
import json
from web3 import Web3
from solcx import compile_source, install_solc

class Web3Handler:
    def __init__(self, factoryAddress, private_key):
        self.ganache_url = "http://127.0.0.1:8545"

        install_solc("0.8.0")

        with open("./Vault1Factory.sol", "r") as file:
            contract_source_code = file.read()

        compiled_sol = compile_source(
            contract_source_code,
            output_values=["abi", "bin"],
            solc_version="0.8.0",
        )
        vault_contract_id, vault_contract_interface = compiled_sol.popitem()
        contract_id, contract_interface = compiled_sol.popitem()

        self.web3 = Web3(Web3.HTTPProvider(self.ganache_url))
        if self.web3.is_connected():
            print("Connected to local blockchain")
        else:
            print("Failed to connect")
            exit(0)
        self.private_key = private_key
        self.account = self.web3.eth.account.from_key(private_key)
        self.factory = self.web3.eth.contract(address=factoryAddress, abi=contract_interface["abi"])
        self.allowedaddrs = open('allowed.txt', 'r').readlines()

    def createInstance(self):
        nonce = self.web3.eth.get_transaction_count(self.account.address)
        tx = self.factory.functions.createInstance().build_transaction({
            'chainId': 31337,
            'gas': 1000000,
            'gasPrice': self.web3.to_wei('500', 'gwei'),
            'nonce': nonce,
            'value': self.web3.to_wei(0.1, 'ether')
        })

        signed_tx = self.web3.eth.account.sign_transaction(tx, self.private_key)

        tx_hash = self.web3.eth.send_raw_transaction(signed_tx.raw_transaction)
        tx_receipt = self.web3.eth.wait_for_transaction_receipt(tx_hash)
        
        
        logs = []
        while not len(logs):
            print("****Waiting for deployment receipt****")
            logs = self.factory.events.InstanceCreated().process_receipt(tx_receipt)
        open('allowed.txt', 'a').writelines(logs[0]['args']['instanceAddress'] + '\n')
        return logs[0]['args']['instanceAddress']
    
    def createAccount(self):
        account = self.web3.eth.account.create()

        return account._private_key, account.address
    def transferFunds(self, addr):

        transaction = {
            'to': addr,
            'value': self.web3.to_wei(2, 'ether'),
            'gas': 1000000,
            'gasPrice': self.web3.to_wei('1', 'gwei'),
            'nonce': self.web3.eth.get_transaction_count(self.account.address),
        }

        signed_txn = self.web3.eth.account.sign_transaction(transaction, self.private_key)
        tx_hash = self.web3.eth.send_raw_transaction(signed_txn.raw_transaction)
        txn_receipt = self.web3.eth.wait_for_transaction_receipt(tx_hash)
    def validateInstance(self, contractAddress, playerAddress):
        return_value = None
        if contractAddress + '\n' not in self.allowedaddrs:
            print("I have not created that contract.") #sanity check so you cant deploy your own Vault contracts and set yourself as owner
            exit(0)
        try:
            return_value = self.factory.functions.validateInstance(contractAddress, playerAddress).call({'gas': 100000, 'gasPrice': self.web3.to_wei('1', 'gwei')})
        except:
            print("Got an error, check the format of addresses or wait for contract deployment block to be mined")
            exit()
        if return_value:
            file = open('allowed.txt', 'r') #Make sure each flag can only be claimed once
            r = file.readlines()
            r.remove(contractAddress + '\n')
            file.close()
            file = open('allowed.txt', 'w')
            file.writelines(r)
            file.close()
        return return_value
    def privateFromAccount(self, pk):
        return self.web3.eth.account.from_key(pk).address

w3h = Web3Handler("FACTORYADDRESS", "0xdf3d2184679232ecf3c8dfc86719a1087a9d04b9e5af4a5953641b7572770f23") 
#w3h = Web3Handler("0xCf7Ed3AccA5a467e9e704C703E8D87F634fB0Fc9", "0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80")
# For testing purposes
print('[0] Get instance')
print('[1] Verify ownership of contract')
inp = input("Choice: ")
if len(inp) != 1 and (not inp == 1 or not inp == 0):
    exit(0)
if inp == '0':
    pk, addr = w3h.createAccount()
    inst = w3h.createInstance()
    print("\nHttpProvider: http://challs.crate.nu:50005")
    print("ChainId: 31337")
    print('Account address:', addr)
    print('Private Key:', pk.hex())
    print('Vault 1 contract instance:', inst)
    w3h.transferFunds(addr)
    print("Balance:", w3h.web3.from_wei(w3h.web3.eth.get_balance(addr), 'ether'), 'ether')
    print("Done")
if inp == '1':
    pk = input("Player private key (0x...): ")
    ca = input("Vault contract address (0x...): ")
    
    if not ca.startswith("0x") or not ca.startswith("0x"):
        print("Enter in hex format as 0x")
        exit(0)
    pa = w3h.privateFromAccount(pk) 
    if pa == "FACTORYADDRESS":
    #if pa == "0xE86F04FD7d6a16e1F4FB77A6e6fbc7661a673dAd":
        print("Invalid account")
        exit(0)
    if w3h.validateInstance(ca, pa):
        print("cratectf{DontStoreSecretsOnBlockchain!}")
    else:
        print("You dont have ownership of target contract")
