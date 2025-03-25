# Simple Blockchain Simulation

## Overview
This project is a basic blockchain simulation built using Python. It demonstrates the core principles of a blockchain, including block creation, hashing, proof-of-work, and chain validation.

## Features
- Implements a blockchain with blocks containing:
  - Index
  - Timestamp
  - Transactions
  - Previous block hash
  - Current block hash (computed using SHA-256)
  - Nonce for Proof-of-Work
- Simple Proof-of-Work mechanism (adjustable difficulty)
- Blockchain validation to detect tampering
- Demonstrates blockchain immutability by modifying a block and checking integrity

## Prerequisites
- Python 3.x installed

## Installation & Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/princeoftm/Interview_1.git
   cd blockchain-simulation
   ```
2. Run the script:
   ```bash
   python x.py
   ```
3. The program will:
   - Create a genesis block
   - Add a few blocks with sample transactions
   - Display the blockchain
   - Demonstrate tampering and show how validation detects it

## Expected Output
1. The blockchain before tampering.
2. The validation status (should be `True`).
3. The blockchain after modifying a block.
4. The validation status after tampering (should be `False`).

## Example Output
```
Blockchain before tampering:
{
    "index": 0,
    "timestamp": 1673423445.673,
    "transactions": "Genesis Block",
    "previous_hash": "0",
    "hash": "0000abcdef..."
}
...
Is blockchain valid? True

Blockchain after tampering:
...
Is blockchain valid? False
```

## Docker Setup (Optional)
To run the project using Docker:
1. Build the Docker image:
   ```bash
   docker build -t blockchain-simulation .
   ```
2. Run the container:
   ```bash
   docker run --rm blockchain-simulation
   ```
## License
MIT License.
