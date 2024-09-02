from web3 import Web3

# Connect to the Arbitrum Sepolia node
w3 = Web3(Web3.HTTPProvider('YOUR_ARBITRUM_SEPOLIA_URL'))

# Check if connected
if not w3.isConnected():
    raise Exception("Failed to connect to the Arbitrum Sepolia node")

# Set up the account
private_key = 'YOUR_PRIVATE_KEY'
account = w3.eth.account.privateKeyToAccount(private_key)

# Define the contract address and input data
contract_address = '0x8D86c3573928CE125f9b2df59918c383aa2B514D'
input_data = '0x56591d59627373700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000004CBB1421DF1CF362DC618d887056802d8adB7BC000000000000000000000000000000000000000000000000000005ae1a09d680e0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000005af3107a4000'

# Define transaction parameters
gas_limit = 2000000
gas_price = w3.toWei('10', 'gwei')
chain_id = 421614  # Chain ID for Arbitrum Sepolia

# Function to send a transaction to the contract
def send_transaction(amount):
    nonce = w3.eth.getTransactionCount(account.address)
    transaction = {
        'to': contract_address,
        'data': input_data,
        'value': w3.toWei(amount, 'ether'),
        'gas': gas_limit,
        'gasPrice': gas_price,
        'nonce': nonce,
        'chainId': chain_id
    }

    signed_txn = w3.eth.account.signTransaction(transaction, private_key)
    txn_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction)
    return txn_hash

# Send transactions repeatedly
num_transactions = 10  # Change this to the number of transactions you want to send
amount_per_transaction = 0.0001  # Amount in ETH

for _ in range(num_transactions):
    txn_hash = send_transaction(amount_per_transaction)
    print(f'Transaction hash: {txn_hash.hex()}')
  
