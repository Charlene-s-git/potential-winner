#!/usr/bin/env python3
"""
Crypto Transfer Tool - Command Line Interface

A tool to transfer cryptocurrency from blockchain to personal wallet.
"""

import argparse
import sys
import os
from getpass import getpass
from typing import Optional

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from wallet_manager import WalletManager
from blockchain_client import BlockchainClient
from config_manager import ConfigManager


class CryptoTransferCLI:
    """Command-line interface for crypto transfer tool."""
    
    def __init__(self):
        self.wallet_manager = WalletManager()
        self.config_manager = ConfigManager()
    
    def create_wallet(self, args):
        """Create a new wallet."""
        print("Creating new wallet...")
        account = self.wallet_manager.create_wallet()
        
        print("\n" + "="*60)
        print("NEW WALLET CREATED")
        print("="*60)
        print(f"Address: {account.address}")
        print(f"Private Key: {account.key.hex()}")
        print("="*60)
        print("\n⚠️  IMPORTANT: Save your private key securely!")
        print("   Never share it with anyone.")
        print("   You will need it to access your funds.")
        
        # Ask if user wants to encrypt and save
        save = input("\nDo you want to encrypt and save this wallet? (y/n): ").lower()
        if save == 'y':
            password = getpass("Enter password to encrypt wallet: ")
            confirm_password = getpass("Confirm password: ")
            
            if password != confirm_password:
                print("❌ Passwords don't match!")
                return
            
            filepath = self.wallet_manager.export_wallet(account, password)
            print(f"✅ Wallet saved to: {filepath}")
    
    def import_wallet(self, args):
        """Import wallet from file."""
        filepath = args.file
        password = getpass("Enter wallet password: ")
        
        try:
            account = self.wallet_manager.import_wallet(filepath, password)
            print("\n" + "="*60)
            print("WALLET IMPORTED")
            print("="*60)
            print(f"Address: {account.address}")
            print("="*60)
        except Exception as e:
            print(f"❌ Failed to import wallet: {e}")
    
    def check_balance(self, args):
        """Check balance of an address."""
        network_config = self.config_manager.get_network(args.network)
        if not network_config:
            print(f"❌ Unknown network: {args.network}")
            return
        
        print(f"Connecting to {network_config['name']}...")
        client = BlockchainClient(network_config['rpc_url'])
        
        if not client.is_connected():
            print("❌ Failed to connect to network")
            return
        
        print(f"✅ Connected to {network_config['name']}")
        
        try:
            balance = client.get_balance(args.address)
            print("\n" + "="*60)
            print("BALANCE")
            print("="*60)
            print(f"Address: {args.address}")
            print(f"Balance: {balance} {network_config['symbol']}")
            print("="*60)
        except Exception as e:
            print(f"❌ Failed to get balance: {e}")
    
    def transfer(self, args):
        """Transfer cryptocurrency."""
        network_config = self.config_manager.get_network(args.network)
        if not network_config:
            print(f"❌ Unknown network: {args.network}")
            return
        
        # Load wallet
        private_key = getpass("Enter your private key: ")
        try:
            account = self.wallet_manager.load_wallet_from_private_key(private_key)
        except Exception as e:
            print(f"❌ Invalid private key: {e}")
            return
        
        print(f"\nConnecting to {network_config['name']}...")
        client = BlockchainClient(network_config['rpc_url'])
        
        if not client.is_connected():
            print("❌ Failed to connect to network")
            return
        
        print(f"✅ Connected to {network_config['name']}")
        
        # Check balance
        balance = client.get_balance(account.address)
        print(f"\nYour balance: {balance} {network_config['symbol']}")
        
        if balance < args.amount:
            print(f"❌ Insufficient balance")
            return
        
        # Get gas price
        gas_price = client.get_gas_price()
        gas_limit = 21000  # Standard transfer
        gas_cost_eth = client.web3.from_wei(gas_price * gas_limit, 'ether')
        
        print("\n" + "="*60)
        print("TRANSFER DETAILS")
        print("="*60)
        print(f"From: {account.address}")
        print(f"To: {args.to}")
        print(f"Amount: {args.amount} {network_config['symbol']}")
        print(f"Gas Cost (estimate): {gas_cost_eth} {network_config['symbol']}")
        print(f"Total Cost: {float(args.amount) + float(gas_cost_eth)} {network_config['symbol']}")
        print("="*60)
        
        confirm = input("\nConfirm transfer? (yes/no): ").lower()
        if confirm != 'yes':
            print("❌ Transfer cancelled")
            return
        
        print("\nSending transaction...")
        try:
            result = client.transfer(account, args.to, args.amount)
            print("\n" + "="*60)
            print("TRANSFER SUCCESSFUL")
            print("="*60)
            print(f"Transaction Hash: {result['transaction_hash']}")
            print(f"Status: {result['status']}")
            print(f"Block Number: {result['block_number']}")
            print(f"Gas Used: {result['gas_used']}")
            print(f"Explorer: {network_config['explorer']}/tx/{result['transaction_hash']}")
            print("="*60)
        except Exception as e:
            print(f"❌ Transfer failed: {e}")
    
    def list_networks(self, args):
        """List available networks."""
        networks = self.config_manager.list_networks()
        print("\n" + "="*60)
        print("AVAILABLE NETWORKS")
        print("="*60)
        for key, config in networks.items():
            print(f"\n{key}:")
            print(f"  Name: {config['name']}")
            print(f"  Chain ID: {config['chain_id']}")
            print(f"  Symbol: {config['symbol']}")
            print(f"  RPC: {config['rpc_url']}")
        print("="*60)
    
    def run(self):
        """Run the CLI application."""
        parser = argparse.ArgumentParser(
            description='Crypto Transfer Tool - Move crypto from blockchain to personal wallet',
            formatter_class=argparse.RawDescriptionHelpFormatter
        )
        
        subparsers = parser.add_subparsers(dest='command', help='Available commands')
        
        # Create wallet command
        subparsers.add_parser('create-wallet', help='Create a new wallet')
        
        # Import wallet command
        import_parser = subparsers.add_parser('import-wallet', help='Import wallet from file')
        import_parser.add_argument('file', help='Path to encrypted wallet file')
        
        # Check balance command
        balance_parser = subparsers.add_parser('balance', help='Check balance of an address')
        balance_parser.add_argument('address', help='Wallet address')
        balance_parser.add_argument('--network', default='ethereum_sepolia', help='Network to use (default: ethereum_sepolia)')
        
        # Transfer command
        transfer_parser = subparsers.add_parser('transfer', help='Transfer cryptocurrency')
        transfer_parser.add_argument('to', help='Recipient address')
        transfer_parser.add_argument('amount', type=float, help='Amount to transfer')
        transfer_parser.add_argument('--network', default='ethereum_sepolia', help='Network to use (default: ethereum_sepolia)')
        
        # List networks command
        subparsers.add_parser('list-networks', help='List available networks')
        
        args = parser.parse_args()
        
        if not args.command:
            parser.print_help()
            return
        
        # Route to appropriate handler
        if args.command == 'create-wallet':
            self.create_wallet(args)
        elif args.command == 'import-wallet':
            self.import_wallet(args)
        elif args.command == 'balance':
            self.check_balance(args)
        elif args.command == 'transfer':
            self.transfer(args)
        elif args.command == 'list-networks':
            self.list_networks(args)


if __name__ == '__main__':
    cli = CryptoTransferCLI()
    cli.run()
