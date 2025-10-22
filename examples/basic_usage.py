#!/usr/bin/env python3
"""
Example: Basic usage of the Crypto Transfer Tool

This example demonstrates how to:
1. Create a new wallet
2. Check balance
3. Transfer cryptocurrency (simulation)
"""

import sys
import os

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from wallet_manager import WalletManager
from blockchain_client import BlockchainClient
from config_manager import ConfigManager


def example_create_wallet():
    """Example: Create a new wallet."""
    print("\n" + "="*60)
    print("EXAMPLE 1: Creating a New Wallet")
    print("="*60)
    
    wallet_manager = WalletManager()
    account = wallet_manager.create_wallet()
    
    print(f"✅ New wallet created!")
    print(f"   Address: {account.address}")
    print(f"   Private Key: {account.key.hex()[:10]}...{account.key.hex()[-10:]}")
    print(f"\n⚠️  IMPORTANT: In production, never display the full private key!")
    

def example_get_wallet_info():
    """Example: Get wallet information."""
    print("\n" + "="*60)
    print("EXAMPLE 2: Getting Wallet Information")
    print("="*60)
    
    wallet_manager = WalletManager()
    account = wallet_manager.create_wallet()
    
    info = wallet_manager.get_wallet_info(account)
    print(f"✅ Wallet information:")
    print(f"   Address: {info['address']}")
    print(f"   Public Key: {info['public_key']}")


def example_list_networks():
    """Example: List available networks."""
    print("\n" + "="*60)
    print("EXAMPLE 3: Listing Available Networks")
    print("="*60)
    
    config_manager = ConfigManager()
    networks = config_manager.list_networks()
    
    print(f"✅ Available networks ({len(networks)}):")
    for key, config in networks.items():
        print(f"   - {key}: {config['name']} ({config['symbol']})")


def example_check_balance():
    """Example: Check balance (requires network connection)."""
    print("\n" + "="*60)
    print("EXAMPLE 4: Checking Balance (Demo)")
    print("="*60)
    
    config_manager = ConfigManager()
    network_config = config_manager.get_network('ethereum_sepolia')
    
    print(f"Network: {network_config['name']}")
    print(f"Symbol: {network_config['symbol']}")
    print(f"RPC URL: {network_config['rpc_url']}")
    
    # Note: To actually check a balance, you need:
    # client = BlockchainClient(network_config['rpc_url'])
    # balance = client.get_balance("0xYourAddress")
    print(f"\nℹ️  To check an actual balance, use:")
    print(f"   python crypto_transfer.py balance <ADDRESS> --network ethereum_sepolia")


def example_wallet_encryption():
    """Example: Encrypt and save a wallet."""
    print("\n" + "="*60)
    print("EXAMPLE 5: Wallet Encryption (Demo)")
    print("="*60)
    
    wallet_manager = WalletManager(wallet_dir="/tmp/example_wallets")
    account = wallet_manager.create_wallet()
    
    print(f"✅ Created wallet: {account.address}")
    
    # In production, use a secure password from user input
    password = "example_password_DO_NOT_USE"
    
    try:
        filepath = wallet_manager.export_wallet(account, password, "example_wallet.json")
        print(f"✅ Wallet encrypted and saved to: {filepath}")
        
        # Demonstrate importing the wallet back
        imported_account = wallet_manager.import_wallet(filepath, password)
        print(f"✅ Wallet imported successfully!")
        print(f"   Imported address: {imported_account.address}")
        print(f"   Original address: {account.address}")
        print(f"   Match: {imported_account.address == account.address}")
        
        # Clean up example file
        os.remove(filepath)
        print(f"✅ Cleaned up example wallet file")
        
    except Exception as e:
        print(f"❌ Error: {e}")


def main():
    """Run all examples."""
    print("\n" + "="*60)
    print("CRYPTO TRANSFER TOOL - USAGE EXAMPLES")
    print("="*60)
    print("\nThis script demonstrates various features of the tool.")
    print("For actual transfers, use the CLI: python crypto_transfer.py")
    
    # Run examples
    example_create_wallet()
    example_get_wallet_info()
    example_list_networks()
    example_check_balance()
    example_wallet_encryption()
    
    print("\n" + "="*60)
    print("EXAMPLES COMPLETED")
    print("="*60)
    print("\nTo use the CLI tool, try:")
    print("  python crypto_transfer.py --help")
    print("  python crypto_transfer.py create-wallet")
    print("  python crypto_transfer.py list-networks")
    print("  python crypto_transfer.py balance <ADDRESS> --network ethereum_sepolia")
    print("\n")


if __name__ == '__main__':
    main()
