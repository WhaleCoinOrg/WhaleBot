# WhaleBot
Experimental Bot for Whales


 - Run a gwhale using flags
`./gwhale --rpc --rpccorsdomain '*' --rpcapi "eth,net,web3,debug,personal"`
- import your whale account private key to your node with a passphrase
- Clone this repo
- `cd WhaleBot`
- `virtualenv -p python3 ~/.venv-py3`
- `source ~/.venv-py3/bin/activate`
- `pip install -r requirements.txt`

- update ADDRESS and PASSPHRASE in run.py file (the address should be checksummed(
- python run.py
