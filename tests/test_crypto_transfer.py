"""
Tests for Crypto Transfer Tool

Basic tests to validate core functionality.
"""

import unittest
import sys
import os

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from wallet_manager import WalletManager
from config_manager import ConfigManager


class TestWalletManager(unittest.TestCase):
    """Test wallet management functionality."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.wallet_manager = WalletManager(wallet_dir="/tmp/test_wallets")
    
    def test_create_wallet(self):
        """Test wallet creation."""
        account = self.wallet_manager.create_wallet()
        self.assertIsNotNone(account)
        self.assertIsNotNone(account.address)
        self.assertTrue(account.address.startswith('0x'))
        self.assertEqual(len(account.address), 42)
    
    def test_load_wallet_from_private_key(self):
        """Test loading wallet from private key."""
        # Create a wallet first
        account1 = self.wallet_manager.create_wallet()
        private_key = account1.key.hex()
        
        # Load it back
        account2 = self.wallet_manager.load_wallet_from_private_key(private_key)
        
        # Should be the same address
        self.assertEqual(account1.address, account2.address)
    
    def test_get_wallet_info(self):
        """Test getting wallet information."""
        account = self.wallet_manager.create_wallet()
        info = self.wallet_manager.get_wallet_info(account)
        
        self.assertIn('address', info)
        self.assertIn('public_key', info)
        self.assertEqual(info['address'], account.address)


class TestConfigManager(unittest.TestCase):
    """Test configuration management."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.config_manager = ConfigManager(config_file="/tmp/test_networks.json")
    
    def test_default_networks(self):
        """Test that default networks are loaded."""
        networks = self.config_manager.list_networks()
        self.assertGreater(len(networks), 0)
        self.assertIn('ethereum_mainnet', networks)
        self.assertIn('ethereum_sepolia', networks)
    
    def test_get_network(self):
        """Test getting specific network configuration."""
        network = self.config_manager.get_network('ethereum_sepolia')
        self.assertIsNotNone(network)
        self.assertIn('name', network)
        self.assertIn('rpc_url', network)
        self.assertIn('chain_id', network)
        self.assertIn('symbol', network)
    
    def test_network_properties(self):
        """Test network configuration properties."""
        network = self.config_manager.get_network('ethereum_mainnet')
        self.assertEqual(network['chain_id'], 1)
        self.assertEqual(network['symbol'], 'ETH')
    
    def test_add_network(self):
        """Test adding a custom network."""
        custom_network = {
            "name": "Test Network",
            "rpc_url": "https://test.example.com",
            "chain_id": 999,
            "symbol": "TEST",
            "explorer": "https://explorer.example.com"
        }
        
        self.config_manager.add_network('test_network', custom_network)
        retrieved = self.config_manager.get_network('test_network')
        
        self.assertIsNotNone(retrieved)
        self.assertEqual(retrieved['chain_id'], 999)
        self.assertEqual(retrieved['symbol'], 'TEST')


if __name__ == '__main__':
    unittest.main()
