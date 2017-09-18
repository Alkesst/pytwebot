# Quijote
###### A Trhead in Twitter.
## Introduction
With this stuff the bot posts every 15 minutes a 140 character fragment from the novel "El ingenioso hidalgo Don Quijote de la Mancha" by Miguel de Cervantes, a Spanish reference writer.

## Basic Behavior
The bot uses 3 files, one file has got the entire novel in .txt, another file saves the last position read in the .txt novel, and the last one contains the last published tweet id. Every 15 mins, the bot replies itself with a new 140 character fragment.
The bot wont publish unfinished words, it cheks if the next character in a word is a " "
```python
    pos = line.rfind(" ")
    position_file.write(str(int(seekline) + pos) + "\n")
    line = line[0:pos]
```
