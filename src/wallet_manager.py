"""
Crypto Transfer Tool - Wallet Manager

This module handles wallet operations including:
- Creating new wallets
- Loading existing wallets
- Managing private keys securely
"""

from eth_account import Account
from eth_account.signers.local import LocalAccount
import json
import os
from typing import Optional


class WalletManager:
    """Manages cryptocurrency wallet operations."""
    
    def __init__(self, wallet_dir: str = "wallets"):
        """
        Initialize the wallet manager.
        
        Args:
            wallet_dir: Directory to store wallet files
        """
        self.wallet_dir = wallet_dir
        if not os.path.exists(wallet_dir):
            os.makedirs(wallet_dir)
    
    def create_wallet(self) -> LocalAccount:
        """
        Create a new wallet with a random private key.
        
        Returns:
            LocalAccount: New wallet account
        """
        Account.enable_unaudited_hdwallet_features()
        account = Account.create()
        return account
    
    def load_wallet_from_private_key(self, private_key: str) -> LocalAccount:
        """
        Load wallet from a private key.
        
        Args:
            private_key: Private key as hex string
            
        Returns:
            LocalAccount: Wallet account
        """
        account = Account.from_key(private_key)
        return account
    
    def get_wallet_info(self, account: LocalAccount) -> dict:
        """
        Get wallet information.
        
        Args:
            account: Wallet account
            
        Returns:
            dict: Wallet information including address
        """
        return {
            "address": account.address,
            "public_key": account.address
        }
    
    def export_wallet(self, account: LocalAccount, password: str, filename: Optional[str] = None) -> str:
        """
        Export wallet to encrypted JSON file.
        
        Args:
            account: Wallet account to export
            password: Password to encrypt the wallet
            filename: Optional filename (defaults to address.json)
            
        Returns:
            str: Path to the exported wallet file
        """
        if filename is None:
            filename = f"{account.address}.json"
        
        filepath = os.path.join(self.wallet_dir, filename)
        encrypted = Account.encrypt(account.key, password)
        
        with open(filepath, 'w') as f:
            json.dump(encrypted, f, indent=2)
        
        return filepath
    
    def import_wallet(self, filepath: str, password: str) -> LocalAccount:
        """
        Import wallet from encrypted JSON file.
        
        Args:
            filepath: Path to encrypted wallet file
            password: Password to decrypt the wallet
            
        Returns:
            LocalAccount: Imported wallet account
        """
        with open(filepath, 'r') as f:
            encrypted = json.load(f)
        
        private_key = Account.decrypt(encrypted, password)
        account = Account.from_key(private_key)
        
        return account
