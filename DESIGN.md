PyDominion Design
=================

This documents the design of the PyDominion game and gives a general guideline as to how to code it/design it. You do not have to follow this exact specification if you don't like it, but I hope it gives a good starting point.

The design of this game is supposed to be instructional, and therefore creating the game should be **evolutionary** rather than a singular effort to create a completed, graphical, multi-player, networked game from scratch.

Elements of the Game
====================

The basic elements of the game are:

* Players
* Cards (and card sets)
* The rule/play engine

Player
------

A **Player** is any entity that participates in the game. They have a state associated with them (like player name). I think that is really the only state that would need to be associated with a player, but you are free to do whatever you want.

A very basic player class could be:

    class Player:
        def __init__(self, player_number, player_name):
            self.player_name = player_name

Card
----

A **Card** is the basic unit of the game and represents the cards used in the *Dominion* board game. The game has various types of cards, like **Treasure**, **Victory**, **Curse**, and **Kingdom**. You can model it a couple ways that I can think of off the top of my head, but the one that I might go with would be the following:

As a single card class that has some information like the *name* of the card, and the *type* it represents:

    class Card:
        def __init__(self, name, type):
            self.name = name
            self.type = type # like "Victory", "Treasure", "Kingdom", etc.


Why this design? A few reasons:

 * The cards themselves are really just used as identification markers (and later, to apply a graphical representation of them).
 * Building logic directly into the cards will restrict any functionality you want to add like "Custom Rules", as you would then have to either override the behavior of the cards or do something else equally ugly. You would instead use a separate object that managed the cards and knew the rules (and separate the concerns of what a card is and what the game thinks a particular card is).


## Game and Playing Engine

This is the real core of the game, and what will drive the actual playing. You could imagine this subsystem of the game code to have the following responsibilities:

* Drive the main game loop
* Take input from players 
* Drive each player's turn phases (**Action**, **Buy**, **Cleanup**, **Draw**)
* Keep track of the players and whose turn it is.
* Keep track of the cards every player has
* Keep track of the central card decks
* Execute the effects of cards used in the game
* Keep track of the game state and end the game when the end game conditions are met

# Requirements for a Basic Implementation (version 0.1)

So with the core elements out, the game itself does need the following functionality for a basic implementation:

## Support Only Treasure and Victory Cards

You can play Dominion only buying Treasure cards and Victory cards every turn, so I would only support those two cards for the first version to see if your implementation makes sense.

## Basic Human vs Computer Mode

This will allow you to test that your game engine functions with at least two players. The computer AI serves to automate your playing, and the AI can simply buy treasure/victory cards every single turn.

## Text-Mode

I chose Dominion as the initial game to implement because it doesn't require graphics to work. The first implementation of the game should be a playable text-only game, playable from a single command window where players take turns at the keyboard choosing what to do each phase.

------

And that's it for what is essentially version 0.1 of the game - create the core game components and implement a playable, very basic text-based version of the game.

# Requirements for a Slightly-More Advanced Implementation (version 0.2)

These are requirements for version 2.0 of the game, which builds on top of the core components. Ideally, your game core won't need much modification, if any, to add the functionality in this version.

This version will still only run on a single computer and players will take turns playing.

## Two-Player Mode

The game should implement at least two-player mode first. However, as the playing engine keeps track of players, it should be simple enough to have the engine keep a list of players and loop through them every turn.

## Support all the Standard Card Types

Implement the additional card types, but only implement a handful of actual cards for the game (pick a couple of your favorite or whatever).

## Build Logic to Support the Card Actions

This follows from the previous bullet point - implement actual behaviors for various Kingdom cards into your game.

--------

And that's version 0.2 - you will have a game that supports multiple human users, and can execute the logic to use cards.

# Requirements for a Full-Featured (Yet Still Basic) Game (version 0.3)

## Basic Graphical Mode

Make the game graphical. Create a window for the application once you run it, and use simple graphics to represent the 'board'. Draw rectangles to represent cards, and put basic text on the cards (like the name of the card, and type).

For the player whose turn it currently is, draw the cards that they have in their hand. Do not worry about representing all players' cards.

# Even More Advanced Game Stuff

This is stuff beyond the previous versions, and are improvements.

* Add nicer graphics
* Add audio
* Add networked/multi-window play - multiple players can interact with a single game instance
* Allow for custom rules