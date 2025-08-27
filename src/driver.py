from pg_engine import Engine
from sys import argv

if __name__ == '__main__':
    game_engine = Engine()

    if len(argv) > 1:
        print(argv)

        if argv[1] == '0':
            # Do 1 loop.
            game_engine.run(debugCode=1)
        
    game_engine.run()