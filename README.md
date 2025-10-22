# Crypto Transfer Tool

A secure and user-friendly command-line tool to transfer cryptocurrency from blockchain networks to personal wallets. This tool supports multiple blockchain networks including Ethereum, Polygon, and Binance Smart Chain.

## Features

- 🔐 **Secure Wallet Management**: Create new wallets or import existing ones
- 💰 **Balance Checking**: Check balances across multiple networks
- 🚀 **Easy Transfers**: Transfer crypto with simple commands
- 🌐 **Multi-Network Support**: Works with Ethereum, Polygon, BSC, and more
- 🔒 **Private Key Security**: Encrypted wallet storage with password protection
- ⛽ **Gas Estimation**: Automatic gas price and limit estimation

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/Charlene-s-git/potential-winner.git
cd potential-winner
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. (Optional) Copy example configuration:
```bash
cp config/networks.json.example config/networks.json
```

## Usage

### Create a New Wallet

Create a new cryptocurrency wallet:

```bash
python crypto_transfer.py create-wallet
```

This will:
- Generate a new private key
- Display your wallet address
- Optionally encrypt and save the wallet with a password

**⚠️ IMPORTANT**: Save your private key securely! Never share it with anyone.

### Check Balance

Check the balance of any wallet address:

```bash
python crypto_transfer.py balance <ADDRESS> --network ethereum_sepolia
```

Example:
```bash
python crypto_transfer.py balance 0x742d35Cc6634C0532925a3b844Bc454e4438f44e --network ethereum_sepolia
```

### Transfer Cryptocurrency

Transfer crypto from your wallet to another address:

```bash
python crypto_transfer.py transfer <TO_ADDRESS> <AMOUNT> --network ethereum_sepolia
```

Example (transfer 0.01 ETH):
```bash
python crypto_transfer.py transfer 0x742d35Cc6634C0532925a3b844Bc454e4438f44e 0.01 --network ethereum_sepolia
```

You'll be prompted to:
1. Enter your private key
2. Review transaction details
3. Confirm the transfer

### List Available Networks

See all supported blockchain networks:

```bash
python crypto_transfer.py list-networks
```

Default networks include:
- `ethereum_mainnet` - Ethereum Mainnet
- `ethereum_sepolia` - Ethereum Sepolia Testnet (recommended for testing)
- `polygon_mainnet` - Polygon Mainnet
- `bsc_mainnet` - Binance Smart Chain Mainnet

### Import Encrypted Wallet

Import a previously encrypted wallet:

```bash
python crypto_transfer.py import-wallet <PATH_TO_WALLET_FILE>
```

## Supported Networks

| Network | Key | Chain ID | Symbol |
|---------|-----|----------|--------|
| Ethereum Mainnet | ethereum_mainnet | 1 | ETH |
| Ethereum Sepolia Testnet | ethereum_sepolia | 11155111 | ETH |
| Polygon Mainnet | polygon_mainnet | 137 | MATIC |
| BSC Mainnet | bsc_mainnet | 56 | BNB |

## Security Best Practices

### 🔐 Private Key Security

1. **Never share your private key** with anyone
2. **Never commit private keys** to version control
3. **Use encrypted wallet files** for storage
4. **Use strong passwords** for wallet encryption
5. **Keep backups** of your encrypted wallets in secure locations

### 🧪 Testing

- Always test with **testnets** first (like Sepolia)
- Use small amounts when testing on mainnet
- Double-check addresses before transferring

### 🔍 Verification

- Always verify transaction details before confirming
- Check the transaction on blockchain explorers
- Keep transaction hashes for your records

## Project Structure

```
potential-winner/
├── crypto_transfer.py          # Main CLI application
├── src/
│   ├── wallet_manager.py       # Wallet creation and management
│   ├── blockchain_client.py    # Blockchain interactions
│   └── config_manager.py       # Network configuration
├── config/
│   └── networks.json.example   # Example network configuration
├── wallets/                    # Encrypted wallet storage (git-ignored)
├── requirements.txt            # Python dependencies
└── README.md                   # This file
```

## Common Use Cases

### 1. Test with Sepolia Testnet

Get free Sepolia ETH from a faucet (e.g., https://sepoliafaucet.com/), then:

```bash
# Create wallet
python crypto_transfer.py create-wallet

# Check balance
python crypto_transfer.py balance YOUR_ADDRESS --network ethereum_sepolia

# Transfer
python crypto_transfer.py transfer RECIPIENT_ADDRESS 0.01 --network ethereum_sepolia
```

### 2. Transfer from Exchange to Personal Wallet

1. Create a personal wallet with this tool
2. Withdraw from your exchange to your wallet address
3. Use this tool to check your balance
4. Transfer to other addresses as needed

### 3. Manage Multiple Wallets

Create and encrypt multiple wallets for different purposes:

```bash
python crypto_transfer.py create-wallet
# Save as wallet1.json

python crypto_transfer.py create-wallet
# Save as wallet2.json
```

## Troubleshooting

### Connection Issues

If you can't connect to a network:
- Check your internet connection
- Try a different RPC endpoint
- Verify the network is not experiencing downtime

### Transaction Failures

If a transaction fails:
- Ensure you have sufficient balance (including gas fees)
- Check if the network is congested
- Verify the recipient address is correct
- Try increasing gas price during high network activity

### Import/Export Issues

If wallet import/export fails:
- Verify the password is correct
- Check file permissions
- Ensure the wallet file is not corrupted

## Advanced Configuration

### Custom RPC Endpoints

Edit `config/networks.json` to add custom RPC endpoints:

```json
{
  "my_custom_network": {
    "name": "My Custom Network",
    "rpc_url": "https://my-custom-rpc-url.com",
    "chain_id": 12345,
    "symbol": "CUSTOM",
    "explorer": "https://explorer.example.com"
  }
}
```

## Dependencies

- `web3==6.11.3` - Ethereum blockchain interaction
- `eth-account==0.10.0` - Ethereum account management
- `python-dotenv==1.0.0` - Environment variable management

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available for educational and personal use.

## Disclaimer

⚠️ **IMPORTANT DISCLAIMER**:
- This tool is provided as-is for educational purposes
- Always test with testnet before using mainnet
- The authors are not responsible for any loss of funds
- Use at your own risk
- Never share your private keys
- Always verify transaction details before confirming

## Support

For issues, questions, or contributions, please visit:
https://github.com/Charlene-s-git/potential-winner

---

**Remember**: Always keep your private keys secure and never share them with anyone!