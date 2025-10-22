# Quick Start Guide - Crypto Transfer Tool

This guide will help you get started with the Crypto Transfer Tool in just a few minutes.

## Step 1: Installation

```bash
# Clone the repository
git clone https://github.com/Charlene-s-git/potential-winner.git
cd potential-winner

# Install dependencies
pip install -r requirements.txt
```

## Step 2: Create Your First Wallet

```bash
python crypto_transfer.py create-wallet
```

This will:
- Generate a new wallet address and private key
- Give you the option to encrypt and save it with a password

**🔐 IMPORTANT**: Save your private key securely! It's the only way to access your funds.

## Step 3: Get Test Funds (for Testing)

1. Copy your new wallet address
2. Visit a testnet faucet (e.g., https://sepoliafaucet.com/)
3. Request free test ETH for your address

## Step 4: Check Your Balance

```bash
python crypto_transfer.py balance YOUR_ADDRESS --network ethereum_sepolia
```

Replace `YOUR_ADDRESS` with your wallet address from Step 2.

## Step 5: Make Your First Transfer

```bash
python crypto_transfer.py transfer RECIPIENT_ADDRESS 0.001 --network ethereum_sepolia
```

You'll be prompted to:
1. Enter your private key
2. Review the transaction details
3. Confirm the transfer

## Available Commands

### List Networks
See all supported blockchain networks:
```bash
python crypto_transfer.py list-networks
```

### Check Balance
Check balance of any address:
```bash
python crypto_transfer.py balance <ADDRESS> --network <NETWORK>
```

### Transfer Crypto
Send cryptocurrency:
```bash
python crypto_transfer.py transfer <TO_ADDRESS> <AMOUNT> --network <NETWORK>
```

### Import Wallet
Import an encrypted wallet:
```bash
python crypto_transfer.py import-wallet <WALLET_FILE>
```

## Supported Networks

- `ethereum_sepolia` - Ethereum testnet (recommended for testing)
- `ethereum_mainnet` - Ethereum mainnet (use real funds carefully!)
- `polygon_mainnet` - Polygon network
- `bsc_mainnet` - Binance Smart Chain

## Best Practices

✅ **DO:**
- Test with testnets first
- Keep your private keys secure
- Double-check addresses before transferring
- Keep transaction hashes for records

❌ **DON'T:**
- Share your private key with anyone
- Commit private keys to version control
- Use mainnet without testing first
- Transfer large amounts without testing

## Example Workflow

1. **Create wallet** → Get address and private key
2. **Fund wallet** → Get test tokens from faucet
3. **Check balance** → Verify funds received
4. **Transfer** → Send to another address
5. **Verify** → Check transaction on block explorer

## Troubleshooting

**Can't connect to network?**
- Check your internet connection
- Try a different RPC endpoint in `config/networks.json`

**Transaction fails?**
- Ensure sufficient balance for amount + gas fees
- Check if recipient address is valid
- Verify you're on the correct network

**Wallet import fails?**
- Verify the password is correct
- Check the wallet file is not corrupted

## Need Help?

- Check the main [README.md](README.md) for detailed documentation
- Review [examples/basic_usage.py](examples/basic_usage.py) for code examples
- Visit the GitHub repository for issues and support

## Security Reminder

⚠️ **This tool handles cryptocurrency and private keys. Always:**
- Keep your private keys secure
- Use strong passwords for encrypted wallets
- Test with small amounts first
- Verify all transaction details before confirming
- Never share your private keys with anyone

Happy transferring! 🚀
