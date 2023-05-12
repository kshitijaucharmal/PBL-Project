# StockFish Commands
## Start New Game
```bash
stockfish ucinewgame
```
## Get Ready
```bash
stockfish isready # returns readyok
```

## Position Types
+ ```stockfish position startpos```
+ ```stockfish position fen rnbqkbnr/pppppppp/8/8/6P1/8/PPPPPP1P/RNBQKBNR b KQkq - 0 1```
+ ```stockfish position fen rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1 moves g2g4 d7d5 f1g2 c8g4 c2c4```

## Get Best Move
```bash
stockfish go depth 1 # Returns best move
```
