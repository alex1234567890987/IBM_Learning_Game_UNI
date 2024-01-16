import pygame 
import os 
print("Your Current Directory in Main before adjustment is = ",os.getcwd())


from blockchain_house.ibm_blockchain.blockChainHouse import BlockchainHouse 
from blockchain_house.ibm_blockchain.blockChainHouse import *

os.chdir("./")
print("Your Current Directory in Main after adjustment is = ",os.getcwd())

BlockchainHouse(1024, 800, 60, HomeNode())

