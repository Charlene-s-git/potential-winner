"""
Crypto Transfer Tool - Configuration Manager

This module handles application configuration.
"""

import json
import os
from typing import Dict, Optional


class ConfigManager:
    """Manages application configuration."""
    
    DEFAULT_NETWORKS = {
        "ethereum_mainnet": {
            "name": "Ethereum Mainnet",
            "rpc_url": "https://eth.llamarpc.com",
            "chain_id": 1,
            "symbol": "ETH",
            "explorer": "https://etherscan.io"
        },
        "ethereum_sepolia": {
            "name": "Ethereum Sepolia Testnet",
            "rpc_url": "https://rpc.sepolia.org",
            "chain_id": 11155111,
            "symbol": "ETH",
            "explorer": "https://sepolia.etherscan.io"
        },
        "polygon_mainnet": {
            "name": "Polygon Mainnet",
            "rpc_url": "https://polygon-rpc.com",
            "chain_id": 137,
            "symbol": "MATIC",
            "explorer": "https://polygonscan.com"
        },
        "bsc_mainnet": {
            "name": "Binance Smart Chain Mainnet",
            "rpc_url": "https://bsc-dataseed.binance.org",
            "chain_id": 56,
            "symbol": "BNB",
            "explorer": "https://bscscan.com"
        }
    }
    
    def __init__(self, config_file: str = "config/networks.json"):
        """
        Initialize configuration manager.
        
        Args:
            config_file: Path to configuration file
        """
        self.config_file = config_file
        self.networks = self._load_config()
    
    def _load_config(self) -> Dict:
        """
        Load configuration from file or use defaults.
        
        Returns:
            dict: Network configurations
        """
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, 'r') as f:
                    return json.load(f)
            except Exception:
                return self.DEFAULT_NETWORKS
        return self.DEFAULT_NETWORKS
    
    def save_config(self):
        """Save current configuration to file."""
        os.makedirs(os.path.dirname(self.config_file), exist_ok=True)
        with open(self.config_file, 'w') as f:
            json.dump(self.networks, f, indent=2)
    
    def get_network(self, network_key: str) -> Optional[Dict]:
        """
        Get network configuration by key.
        
        Args:
            network_key: Network identifier
            
        Returns:
            dict: Network configuration or None
        """
        return self.networks.get(network_key)
    
    def list_networks(self) -> Dict:
        """
        Get all available networks.
        
        Returns:
            dict: All network configurations
        """
        return self.networks
    
    def add_network(self, key: str, config: Dict):
        """
        Add a custom network configuration.
        
        Args:
            key: Network identifier
            config: Network configuration
        """
        self.networks[key] = config
        self.save_config()
