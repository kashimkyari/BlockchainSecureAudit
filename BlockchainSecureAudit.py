from web3 import Web3
import random
import string

class VulnerabilityScanner:
    def __init__(self, contract_code):
        self.contract_code = contract_code

    def scan(self):
        vulnerabilities = []
        if "call.value" in self.contract_code:
            vulnerabilities.append("Reentrancy vulnerability detected")
        return vulnerabilities

class SmartContractDeployer:
    def __init__(self, blockchain_network):
        self.blockchain_network = blockchain_network

    def deploy_contract(self, contract_code):
        contract_address = self.blockchain_network.deploy_contract(contract_code)
        return contract_address

class BlockchainNetwork:
    def __init__(self, provider_url):
        self.provider_url = provider_url
        self.w3 = Web3(Web3.HTTPProvider(provider_url))

    def deploy_contract(self, contract_code):
        # Compile and deploy the contract
        compiled_contract = self.w3.eth.contract(abi=contract_code['abi'], bytecode=contract_code['bytecode'])
        tx_hash = compiled_contract.constructor().transact()
        tx_receipt = self.w3.eth.waitForTransactionReceipt(tx_hash)
        contract_address = tx_receipt.contractAddress
        return contract_address

if __name__ == "__main__":
    # Connect to the local Ganache instance
    provider_url = "http://127.0.0.1:7545"
    blockchain_network = BlockchainNetwork(provider_url)

    # Sample smart contract code
    contract_code = {
        "abi": [
            {
                "constant": False,
                "inputs": [],
                "name": "withdraw",
                "outputs": [],
                "payable": True,
                "stateMutability": "payable",
                "type": "function"
            }
        ],
        "bytecode": "0x608060405234801561001057600080fd5b5060df8061001f6000396000f3006080604052600436106049576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff168063f8a8fd6d14604e578063f8b2cb4f146073575b600080fd5b348015605957600080fd5b5060786004803603810190808035906020019092919050505060a0565b60405180821515815260200191505060405180910390f35b60005481565b806000819055505b5056fea165627a7a723058204c5c9477b6c5de3d36a71e2d8e0d15775ed5560bb55a02b24c3485aa058efaf10029",
    }

    # Deploy the contract
    ethereum_network = BlockchainNetwork(provider_url)
    ethereum_deployer = SmartContractDeployer(ethereum_network)
    contract_address = ethereum_deployer.deploy_contract(contract_code)

    # Scan the deployed contract for vulnerabilities
    scanner = VulnerabilityScanner(contract_code)
    vulnerabilities = scanner.scan()
    if vulnerabilities:
        print("Vulnerabilities found:")
        for vulnerability in vulnerabilities:
            print(vulnerability)
    else:
        print("No vulnerabilities found.")
