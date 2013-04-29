"""
Parses and validates inputs and instantiates a random game of War.
"""

from war import War

def main():
    w = War()
    w.play(verbose=True)

if __name__ == '__main__':
    main()
