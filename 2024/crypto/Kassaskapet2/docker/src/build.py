import json
from web3 import Web3
from solcx import compile_source, install_solc

install_solc("0.8.0")

with open("./Vault2Factory.sol", "r") as file:
    contract_source_code = file.read()

compiled_sol = compile_source(
    contract_source_code,
    output_values=["abi", "bin"],
    solc_version="0.8.0",
)

vault_contract_id, vault_contract_interface = compiled_sol.popitem()
contract_id, contract_interface = compiled_sol.popitem()

abi = contract_interface["abi"]
bytecode = contract_interface["bin"]

ganache_url = "http://127.0.0.1:8545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

private_key = "0xdf3d2184679232ecf3c8dfc86719a1087a9d04b9e5af4a5953641b7572770f23"
#private_key="0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80"
account = web3.eth.account.from_key(private_key)

if web3.is_connected():
    print("Connected to Ethereum node")
else:
    print("Failed to connect")

def deploy_contract():
    nonce = web3.eth.get_transaction_count(account.address)

    contract = web3.eth.contract(abi=abi, bytecode=bytecode)
    tx = contract.constructor().build_transaction({
        'chainId': 31337,
        'gas': 7000000,
        'gasPrice': web3.to_wei('1', 'gwei'),
        'nonce': nonce,
    })


    signed_tx = web3.eth.account.sign_transaction(tx, private_key)
    
    tx_hash = web3.eth.send_raw_transaction(signed_tx.raw_transaction)
    tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
    print(f"Contract deployed at address: {tx_receipt.contractAddress}")
    return tx_receipt.contractAddress

if __name__ == "__main__":
    contract_address = deploy_contract()
    contract = web3.eth.contract(address=contract_address, abi=abi)
    
