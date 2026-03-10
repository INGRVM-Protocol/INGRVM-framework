import requests
import json
import time
import hashlib
from typing import Dict, List, Any, Optional

class INGRVMSDK:
    """
    Phase 7: The INGRVM Python SDK.
    Allows developers to interact with the neuromorphic mesh programmatically.
    """
    def __init__(self, hub_url: str = "http://192.168.68.51:8000", peer_id: str = "SDK_CLIENT"):
        self.hub_url = hub_url
        self.peer_id = peer_id

    # --- Mesh Discovery ---
    def ping(self) -> Dict[str, Any]:
        """ Checks connectivity to the Hub. """
        try:
            return requests.get(f"{self.hub_url}/api/mesh/ping").json()
        except Exception as e:
            return {"status": "ERROR", "message": str(e)}

    # --- Neural Inference ---
    def send_spike(self, text: str, ingrvm_id: str = "sentiment_alpha") -> Dict[str, Any]:
        """ Fires a neural pulse (inference request) into the mesh. """
        # Auto-generate PoI for the developer
        poi_hash = hashlib.sha256(text.encode('utf-8')).hexdigest()
        
        payload = {
            "text": text,
            "ingrvm_id": ingrvm_id,
            "peer_id": self.peer_id,
            "poi_hash": poi_hash
        }
        try:
            return requests.post(f"{self.hub_url}/api/infer", json=payload).json()
        except Exception as e:
            return {"status": "ERROR", "message": str(e)}

    # --- Marketplace ---
    def list_marketplace(self) -> List[Dict[str, Any]]:
        """ Returns all available neuromorphic ingrvms. """
        try:
            return requests.get(f"{self.hub_url}/api/marketplace/catalog").json()
        except:
            return []

    def search(self, query: str) -> List[Dict[str, Any]]:
        """ Searches the marketplace. """
        try:
            return requests.get(f"{self.hub_url}/api/marketplace/search?q={query}").json()
        except:
            return []

    # --- Economy ---
    def get_balance(self) -> float:
        """ Returns the $DOPA balance for the current identity. """
        try:
            res = requests.get(f"{self.hub_url}/api/rewards/{self.peer_id}").json()
            return res.get("total", 0.0)
        except:
            return 0.0

    def get_ledger(self) -> List[Dict[str, Any]]:
        """ Returns recent transaction history. """
        try:
            return requests.get(f"{self.hub_url}/api/ledger/{self.peer_id}").json()
        except:
            return []

    # --- Governance ---
    def vote(self, proposal_id: str, vote_value: bool) -> Dict[str, Any]:
        """ Casts a DAO vote. """
        payload = {
            "proposal_id": proposal_id,
            "peer_id": self.peer_id,
            "vote": vote_value
        }
        try:
            return requests.post(f"{self.hub_url}/api/dao/vote", json=payload).json()
        except Exception as e:
            return {"status": "ERROR", "message": str(e)}

# --- Usage Example ---
if __name__ == "__main__":
    client = INGRVMSDK(peer_id="SDK_TESTER_01")
    
    print("--- INGRVM SDK Test ---")
    print(f"Ping: {client.ping()}")
    
    print("\nFiring Spike...")
    res = client.send_spike("The future is neuromorphic.")
    print(f"Result: {res}")
    
    print(f"\nCurrent Balance: {client.get_balance()} $DOPA")


