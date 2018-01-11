from web3 import Web3, TestRPCProvider
import json
from web3.providers.rpc import HTTPProvider
from web3.contract import ConciseContract
import gevent

# Change this
ADDRESS = "Your Checksummed Address(must have capital Checksummed letters)"
PASSPHRASE = "the passphrase used on your node to import the private key"

def wait_for_transaction(web3, txn_hash, timeout=300):
    with gevent.Timeout(timeout):
        while True:
            txn_receipt = web3.eth.getTransactionReceipt(txn_hash)
            if txn_receipt is not None:
                break
            gevent.sleep(1)

    return txn_receipt

w3 = Web3(HTTPProvider('http://localhost:8545'))
contractAddress = '0x0C0D7a5B34321e436cE826a5Dd56A9121CD54C49'

abi = [
    {
      "constant": False,
      "inputs": [
        {
          "name": "addr",
          "type": "address"
        },
        {
          "name": "postid",
          "type": "uint256"
        }
      ],
      "name": "claimFollowerReward",
      "outputs": [],
      "payable": False,
      "type": "function"
    },
    {
      "constant": True,
      "inputs": [],
      "name": "getNetworkAddress",
      "outputs": [
        {
          "name": "addr",
          "type": "address"
        }
      ],
      "payable": False,
      "type": "function"
    },
    {
      "constant": True,
      "inputs": [],
      "name": "followerRewards",
      "outputs": [
        {
          "name": "",
          "type": "uint256"
        }
      ],
      "payable": False,
      "type": "function"
    },
    {
      "constant": True,
      "inputs": [],
      "name": "owner",
      "outputs": [
        {
          "name": "",
          "type": "address"
        }
      ],
      "payable": False,
      "type": "function"
    },
    {
      "constant": True,
      "inputs": [
        {
          "name": "",
          "type": "address"
        }
      ],
      "name": "lastFollowerClaim",
      "outputs": [
        {
          "name": "",
          "type": "uint256"
        }
      ],
      "payable": False,
      "type": "function"
    },
    {
      "constant": True,
      "inputs": [
        {
          "name": "",
          "type": "address"
        }
      ],
      "name": "claimedShare",
      "outputs": [
        {
          "name": "",
          "type": "uint256"
        }
      ],
      "payable": False,
      "type": "function"
    },
    {
      "constant": False,
      "inputs": [
        {
          "name": "addr",
          "type": "address"
        }
      ],
      "name": "claimReward",
      "outputs": [],
      "payable": False,
      "type": "function"
    },
    {
      "constant": True,
      "inputs": [
        {
          "name": "",
          "type": "address"
        }
      ],
      "name": "claimedFollowerShare",
      "outputs": [
        {
          "name": "",
          "type": "uint256"
        }
      ],
      "payable": False,
      "type": "function"
    },
    {
      "inputs": [],
      "payable": False,
      "type": "constructor"
    },
    {
      "payable": True,
      "type": "fallback"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "name": "blockNumber",
          "type": "uint256"
        },
        {
          "indexed": False,
          "name": "reward",
          "type": "uint256"
        },
        {
          "indexed": True,
          "name": "whale",
          "type": "address"
        },
        {
          "indexed": False,
          "name": "moderatorReward",
          "type": "uint256"
        },
        {
          "indexed": True,
          "name": "moderator",
          "type": "address"
        },
        {
          "indexed": False,
          "name": "followerReward",
          "type": "uint256"
        }
      ],
      "name": "Claimed",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": False,
          "name": "reward",
          "type": "uint256"
        },
        {
          "indexed": True,
          "name": "follower",
          "type": "address"
        },
        {
          "indexed": True,
          "name": "postid",
          "type": "uint256"
        }
      ],
      "name": "FollowerClaimed",
      "type": "event"
    }
  ]
WhaleRewards = w3.eth.contract(contractAddress,abi=abi)
network = '0x6C48eCe541Ee561347876D9E1a72f6FE41B76706'
networkAbi = [
    {
      "constant": True,
      "inputs": [
        {
          "name": "_addr",
          "type": "address"
        }
      ],
      "name": "getWhaleShares",
      "outputs": [
        {
          "name": "shares",
          "type": "uint256"
        }
      ],
      "payable": False,
      "type": "function"
    },
    {
      "constant": True,
      "inputs": [
        {
          "name": "_addr",
          "type": "address"
        },
        {
          "name": "postid",
          "type": "uint256"
        }
      ],
      "name": "getFollowerShare",
      "outputs": [
        {
          "name": "shares",
          "type": "uint256"
        }
      ],
      "payable": False,
      "type": "function"
    },
    {
      "constant": True,
      "inputs": [
        {
          "name": "",
          "type": "uint256"
        }
      ],
      "name": "posts",
      "outputs": [
        {
          "name": "timestamp",
          "type": "uint256"
        },
        {
          "name": "id",
          "type": "uint256"
        },
        {
          "name": "whale",
          "type": "address"
        },
        {
          "name": "title",
          "type": "string"
        }
      ],
      "payable": False,
      "type": "function"
    },
    {
      "constant": False,
      "inputs": [],
      "name": "becomeNormal",
      "outputs": [],
      "payable": False,
      "type": "function"
    },
    {
      "constant": True,
      "inputs": [
        {
          "name": "",
          "type": "address"
        },
        {
          "name": "",
          "type": "uint256"
        }
      ],
      "name": "followedPosts",
      "outputs": [
        {
          "name": "",
          "type": "uint256"
        }
      ],
      "payable": False,
      "type": "function"
    },
    {
      "constant": True,
      "inputs": [
        {
          "name": "",
          "type": "address"
        }
      ],
      "name": "whales",
      "outputs": [
        {
          "name": "id",
          "type": "uint256"
        },
        {
          "name": "shares",
          "type": "uint256"
        },
        {
          "name": "isWhale",
          "type": "bool"
        },
        {
          "name": "lastBlockShared",
          "type": "uint256"
        }
      ],
      "payable": False,
      "type": "function"
    },
    {
      "constant": False,
      "inputs": [
        {
          "name": "postTitle",
          "type": "string"
        },
        {
          "name": "whale",
          "type": "address"
        }
      ],
      "name": "post",
      "outputs": [],
      "payable": False,
      "type": "function"
    },
    {
      "constant": True,
      "inputs": [
        {
          "name": "",
          "type": "address"
        }
      ],
      "name": "moderators",
      "outputs": [
        {
          "name": "",
          "type": "address"
        }
      ],
      "payable": False,
      "type": "function"
    },
    {
      "constant": True,
      "inputs": [
        {
          "name": "",
          "type": "uint256"
        },
        {
          "name": "",
          "type": "uint256"
        }
      ],
      "name": "postFollowers",
      "outputs": [
        {
          "name": "",
          "type": "address"
        }
      ],
      "payable": False,
      "type": "function"
    },
    {
      "constant": True,
      "inputs": [
        {
          "name": "_addr",
          "type": "address"
        }
      ],
      "name": "getWhaleLastBlockShared",
      "outputs": [
        {
          "name": "blocks",
          "type": "uint256"
        }
      ],
      "payable": False,
      "type": "function"
    },
    {
      "constant": True,
      "inputs": [],
      "name": "getLockedBalance",
      "outputs": [
        {
          "name": "balance",
          "type": "uint256"
        }
      ],
      "payable": False,
      "type": "function"
    },
    {
      "constant": False,
      "inputs": [],
      "name": "updateNetworkShare",
      "outputs": [],
      "payable": False,
      "type": "function"
    },
    {
      "constant": True,
      "inputs": [
        {
          "name": "postid",
          "type": "uint256"
        }
      ],
      "name": "getPostTimeStamp",
      "outputs": [
        {
          "name": "time",
          "type": "uint256"
        }
      ],
      "payable": False,
      "type": "function"
    },
    {
      "constant": True,
      "inputs": [
        {
          "name": "_addr",
          "type": "address"
        }
      ],
      "name": "getWhaleNextBlockShared",
      "outputs": [
        {
          "name": "blocks",
          "type": "uint256"
        }
      ],
      "payable": False,
      "type": "function"
    },
    {
      "constant": False,
      "inputs": [
        {
          "name": "_address",
          "type": "address"
        }
      ],
      "name": "updateWhaleShare",
      "outputs": [],
      "payable": False,
      "type": "function"
    },
    {
      "constant": False,
      "inputs": [
        {
          "name": "mod",
          "type": "address"
        }
      ],
      "name": "designateModerator",
      "outputs": [],
      "payable": False,
      "type": "function"
    },
    {
      "constant": True,
      "inputs": [
        {
          "name": "postid",
          "type": "uint256"
        }
      ],
      "name": "getPostFollowers",
      "outputs": [
        {
          "name": "shares",
          "type": "uint256"
        }
      ],
      "payable": False,
      "type": "function"
    },
    {
      "constant": True,
      "inputs": [
        {
          "name": "_address",
          "type": "address"
        }
      ],
      "name": "isWhale",
      "outputs": [
        {
          "name": "_status",
          "type": "bool"
        }
      ],
      "payable": False,
      "type": "function"
    },
    {
      "constant": True,
      "inputs": [],
      "name": "networkShares",
      "outputs": [
        {
          "name": "",
          "type": "uint256"
        }
      ],
      "payable": False,
      "type": "function"
    },
    {
      "constant": False,
      "inputs": [
        {
          "name": "postid",
          "type": "uint256"
        },
        {
          "name": "follower",
          "type": "address"
        }
      ],
      "name": "addFollower",
      "outputs": [],
      "payable": False,
      "type": "function"
    },
    {
      "constant": True,
      "inputs": [
        {
          "name": "",
          "type": "address"
        },
        {
          "name": "",
          "type": "uint256"
        }
      ],
      "name": "whalePosts",
      "outputs": [
        {
          "name": "timestamp",
          "type": "uint256"
        },
        {
          "name": "id",
          "type": "uint256"
        },
        {
          "name": "whale",
          "type": "address"
        },
        {
          "name": "title",
          "type": "string"
        }
      ],
      "payable": False,
      "type": "function"
    },
    {
      "constant": True,
      "inputs": [],
      "name": "socialShares",
      "outputs": [
        {
          "name": "",
          "type": "uint256"
        }
      ],
      "payable": False,
      "type": "function"
    },
    {
      "constant": False,
      "inputs": [],
      "name": "becomeWhale",
      "outputs": [],
      "payable": True,
      "type": "function"
    },
    {
      "constant": True,
      "inputs": [],
      "name": "numWhales",
      "outputs": [
        {
          "name": "",
          "type": "uint256"
        }
      ],
      "payable": False,
      "type": "function"
    },
    {
      "constant": True,
      "inputs": [],
      "name": "numPosts",
      "outputs": [
        {
          "name": "",
          "type": "uint256"
        }
      ],
      "payable": False,
      "type": "function"
    },
    {
      "constant": True,
      "inputs": [
        {
          "name": "",
          "type": "uint256"
        }
      ],
      "name": "whaleList",
      "outputs": [
        {
          "name": "",
          "type": "address"
        }
      ],
      "payable": False,
      "type": "function"
    },
    {
      "inputs": [
        {
          "name": "_owner",
          "type": "address"
        }
      ],
      "payable": False,
      "type": "constructor"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "name": "author",
          "type": "address"
        },
        {
          "indexed": False,
          "name": "title",
          "type": "string"
        },
        {
          "indexed": True,
          "name": "id",
          "type": "uint256"
        }
      ],
      "name": "Posted",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "name": "whale",
          "type": "address"
        },
        {
          "indexed": True,
          "name": "postid",
          "type": "uint256"
        },
        {
          "indexed": True,
          "name": "follower",
          "type": "address"
        },
        {
          "indexed": False,
          "name": "moderator",
          "type": "address"
        }
      ],
      "name": "FollowerAdded",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "name": "whale",
          "type": "address"
        },
        {
          "indexed": False,
          "name": "blockNumber",
          "type": "uint256"
        }
      ],
      "name": "BecomeWhale",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "name": "whale",
          "type": "address"
        },
        {
          "indexed": False,
          "name": "blockNumber",
          "type": "uint256"
        }
      ],
      "name": "BecomeNormal",
      "type": "event"
    }
  ]

WhaleNetwork = w3.eth.contract(network, abi=networkAbi)

account = w3.eth.accounts
w3.personal.unlockAccount(ADDRESS, PASSPHRASE)
author_filter = WhaleNetwork.eventFilter('Posted', {'filter': {'author':ADDRESS}})


def post():
    w3.personal.unlockAccount(ADDRESS, PASSPHRASE)
    post = WhaleNetwork.transact({'from':ADDRESS}).post('', ADDRESS)
    tx_receipt = wait_for_transaction(w3,post)
    ent = author_filter.get_new_entries()
    print(ent)
    follow(ent[0]['args']['id'])


def follow(id):
    w3.personal.unlockAccount(ADDRESS, PASSPHRASE)
    follow = WhaleNetwork.transact({'from':ADDRESS}).addFollower(id, ADDRESS)
    tx_receipt = wait_for_transaction(w3,follow)
    print(tx_receipt)
    post()

post()
