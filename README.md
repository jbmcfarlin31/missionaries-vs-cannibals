# missionaries-vs-cannibals
A Python program of the Missionaries vs Cannibals game

# Prequisites
Python 3+ or higher

You will need PrettyTable installed for this to work
```bash
pip install PTable

# note if using Python 3 you might have to run it like so:
pip3 install PTable
```

You also need to make sure that the `GameLogic.py` class file is in the same location as the `main.py` file.

# How to Play
The task is simple - move all of the missionaries and cannibals from one side of the bank to the other. Easy, right?

The boat can only have two people on board, and there has to be one person to drive the boat back to the other side.

To run the program, clone the repo and then when inside run it like any other Python program:
```bash
python main.py

# note if using Python 3 you might have to run it like so:
python3 main.py
```

# Pit falls
If at any point on either side of the bank the cannibals out number the missionaries, they will eat the missionaries, and you will lose.
