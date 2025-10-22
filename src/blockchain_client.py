"""
Crypto Transfer Tool - Blockchain Client

This module handles blockchain interactions including:
- Connecting to blockchain networks
- Checking balances
- Transferring cryptocurrency
"""

from web3 import Web3
from eth_account.signers.local import LocalAccount
from typing import Optional, Dict
import time


class BlockchainClient:
    """Handles blockchain network connections and transactions."""
    
    def __init__(self, rpc_url: str):
        """
        Initialize blockchain client.
        
        Args:
            rpc_url: RPC endpoint URL for blockchain network
        """
        self.web3 = Web3(Web3.HTTPProvider(rpc_url))
        self.rpc_url = rpc_url
    
    def is_connected(self) -> bool:
        """
        Check if connected to blockchain network.
        
        Returns:
            bool: True if connected, False otherwise
        """
        try:
            return self.web3.is_connected()
        except Exception:
            return False
    
    def get_balance(self, address: str) -> float:
        """
        Get balance of an address in ETH.
        
        Args:
            address: Ethereum address
            
        Returns:
            float: Balance in ETH
        """
        checksum_address = Web3.to_checksum_address(address)
        balance_wei = self.web3.eth.get_balance(checksum_address)
        balance_eth = self.web3.from_wei(balance_wei, 'ether')
        return float(balance_eth)
    
    def get_gas_price(self) -> int:
        """
        Get current gas price.
        
        Returns:
            int: Gas price in Wei
        """
        return self.web3.eth.gas_price
    
    def estimate_gas(self, from_address: str, to_address: str, value_wei: int) -> int:
        """
        Estimate gas for a transaction.
        
        Args:
            from_address: Sender address
            to_address: Recipient address
            value_wei: Amount to send in Wei
            
        Returns:
            int: Estimated gas limit
        """
        try:
            gas_estimate = self.web3.eth.estimate_gas({
                'from': Web3.to_checksum_address(from_address),
                'to': Web3.to_checksum_address(to_address),
                'value': value_wei
            })
            return gas_estimate
        except Exception as e:
            # Return default gas limit if estimation fails
            return 21000
    
    def transfer(
        self,
        from_account: LocalAccount,
        to_address: str,
        amount_eth: float,
        gas_price: Optional[int] = None,
        gas_limit: Optional[int] = None
    ) -> Dict[str, str]:
        """
        Transfer cryptocurrency from one address to another.
        
        Args:
            from_account: Sender account with private key
            to_address: Recipient address
            amount_eth: Amount to send in ETH
            gas_price: Optional gas price in Wei (uses network price if None)
            gas_limit: Optional gas limit (estimates if None)
            
        Returns:
            dict: Transaction details including hash
        """
        # Convert addresses to checksum format
        from_address = Web3.to_checksum_address(from_account.address)
        to_address = Web3.to_checksum_address(to_address)
        
        # Convert amount to Wei
        value_wei = self.web3.to_wei(amount_eth, 'ether')
        
        # Get gas price if not provided
        if gas_price is None:
            gas_price = self.get_gas_price()
        
        # Estimate gas if not provided
        if gas_limit is None:
            gas_limit = self.estimate_gas(from_address, to_address, value_wei)
        
        # Get nonce
        nonce = self.web3.eth.get_transaction_count(from_address)
        
        # Build transaction
        transaction = {
            'nonce': nonce,
            'to': to_address,
            'value': value_wei,
            'gas': gas_limit,
            'gasPrice': gas_price,
            'chainId': self.web3.eth.chain_id
        }
        
        # Sign transaction
        signed_txn = self.web3.eth.account.sign_transaction(transaction, from_account.key)
        
        # Send transaction
        tx_hash = self.web3.eth.send_raw_transaction(signed_txn.rawTransaction)
        
        # Wait for transaction receipt
        tx_receipt = self.web3.eth.wait_for_transaction_receipt(tx_hash)
        
        return {
            'transaction_hash': tx_hash.hex(),
            'status': 'success' if tx_receipt['status'] == 1 else 'failed',
            'block_number': tx_receipt['blockNumber'],
            'gas_used': tx_receipt['gasUsed']
        }
    
    def get_transaction_status(self, tx_hash: str) -> Dict:
        """
        Get status of a transaction.
        
        Args:
            tx_hash: Transaction hash
            
        Returns:
            dict: Transaction status details
        """
        try:
            tx_receipt = self.web3.eth.get_transaction_receipt(tx_hash)
            return {
                'status': 'success' if tx_receipt['status'] == 1 else 'failed',
                'block_number': tx_receipt['blockNumber'],
                'gas_used': tx_receipt['gasUsed']
            }
        except Exception as e:
            return {
                'status': 'pending',
                'error': str(e)
            }
