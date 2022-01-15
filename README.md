# Connect 4

Connect 4 is a strategy game where the idea is to get 4 of your own discs in a line in any direction, horizontally, vertically or diagonally ( -- ¦ / \ ), hence you connect 4 together. You must also block your opponent from connecting 4 and can be quite satisfying when you plan and predict a few moves in advance.

This game is useful for people who spend a lot of time in terminals and allows them to let off steam. They can have a quick game lasting less than a minute, or continue playing until they've beaten the computer, so it's good for somebody to play whether they only have a free moment or lots of time to spare.

A deployed version may be found here: [Connect 4](http://my-connect-4.herokuapp.com/)

![Connect 4](https://github.com/MadStu/connect-4/raw/main/assets/images/web-page.png)

## Planning 

I planned to make a python game that could run in any python3 terminal window and be challenging enough for the player to want to return to the game again and again.

Connect 4 was a game I thought could meet the criteria I was looking for and could easily be represented within a text based GUI.

Before writing any code I first built a flow chart to map out where it needed to start, where it needed to go and how it would end.

This helped massively at the beginning of the project and I used that to build the initial basic functioning game loop which everything since has been based upon.

![Flow Chart](https://github.com/MadStu/connect-4/raw/main/assets/images/flow-chart.png)

### Existing Features

- __Text Based GUI__

  - The game's GUI is entirely text based and can be run directly in any python3 terminal.

![Text Based GUI](https://github.com/MadStu/connect-4/raw/main/assets/images/text-based-gui.png)

- __New Gameplay Concept__

  - The regular version of the game is 6 columns tall and 7 columns wide. This game starts you on level 1 which is 12 columns wide. This makes it easier as you have more space to win.
  - Every time you win a game, you move up a level and the column width is shortened.

![New Gameplay Comcept](https://github.com/MadStu/connect-4/raw/main/assets/images/new-game-concept.png)

- __Hard Mode__

  - The game features a hard mode allowing the player to play against a harder opponent.
  - This gives the player a real sense of achievement when they win. 

![Hard Mode](https://github.com/MadStu/connect-4/raw/main/assets/images/hard-mode.png)

- __Animated Disc Drop__

  - Basic animation is included which shows the player discs falling as they're dropped into the column which is visually appealing.

![Animated Disc Drop](https://github.com/MadStu/connect-4/raw/main/assets/images/animated-disc-drop.png)

- __Status Bar__

  - A status bar keeps the player informed with the level they're on, what game difficulty they're playing and who's turn it is.

![Status Bar](https://github.com/MadStu/connect-4/raw/main/assets/images/status-bar.png)

- __Input Validation__

  - Any input from the user is validated, asking if they want to play hard mode, play again or from the column number they enter.

![Input Validation](https://github.com/MadStu/connect-4/raw/main/assets/images/input-validation.png)

- __Coloured Winning Discs__

  - When either the user or computer player wins, the winning discs are highlighted red to show the line of connect 4.

![Coloured Winning Discs](https://github.com/MadStu/connect-4/raw/main/assets/images/coloured-winning-discs.png)

- __Cheat Code__

  - The game includes a cheat code (88) which may give a hint to the player of the next column to try.
  - If the computer hasn't seen a potentially winning pattern the player is instead shown a message that cheaters never prosper.

![Cheat Message](https://github.com/MadStu/connect-4/raw/main/assets/images/cheat-message.png)

- __Score Board__

  - A score board shows the player the top ten scores.
  - The player scores are kept in a local .csv file.

![Score Board](https://github.com/MadStu/connect-4/raw/main/assets/images/score-board.png)

### Features Left to Implement

- ~~Implement a points system based on number of turns.~~
- ~~Add a high score board.~~
- Add AI that learns and predicts the players next move based on their previous pattern of moves.
- Make the Easy mode opponent easier to beat.

## Testing

I've tested the code continuously as I've developed it, making sure all functionality works as it should and fix any typos or coding errors as and when they happen.

I also asked friends and family to play with and try to produce errors or unintended behaviours.

Some feedback I had was that the computer was too hard to beat on Easy mode so I plan to make that mode a little easier.

### Validator Testing 

- PEP8
  - No errors or warnings were returned when passing through [PEP8online.com](http://pep8online.com/).

### Bugs

- ~~herokuapp.com not displaying underscores on the logo.~~
  - Solved by making the logo art text have a lighter weight.
- ~~Game would say there's a winner if it was a tie.~~
  - Solved by adding a disc counter.
- ~~Computer finds the next move to beat the player, but if the player goes there, the computer would still place disc in the same column.~~
  - Solved by checking all discs after a move and not just the previous players.
- ~~Computer would ignore it's own potential win, prioritising blocking the player.~~
  - Solved by: 
    - Having the computer check it's own discs after the players.
    - Prioritising discs with 3 in a row over discs with 2 in a row.
- ~~Computer would try to block players by placing discs in the next column, but the square under where the winning disc would go is empty so the disc just falls past.~~
  - Solved by checking to see if the square underneath is empty.
- ~~Checking the square underneath could produce an IndexError as it wouldn't exist.~~
  - Solved by using a Try/Except block to handle it.
- ~~Recursion Error when the program is checking winners and checking for next computer move.~~
  - Solved by increasing the recursion limit.
- ~~IndexError when resetting game after player has reached top level.~~
  - Solved by adding if else in the reset_game function. It now checks to see if the level was at the top level or not.
- ~~Game difficulty not changing mode when the player selects a different setting after winning at top level.~~
  - Solved, I'd missed adding the setting in the choose_mode function as the default mode was "easy" and only changed when player set mode to "hard".
- ~~Score increments highly when you input invalid data when choosing difficulty mode before game starts.~~
  - Solved by removing the call to reset_game which is no longer required there.
- ~~Scoreboard updates twice when player completes the game and doesn't continue the playing.~~
  - Solved by checking the game level within the play_again function.

## Deployment

I've deployed it on herokuapp.com and used the following method.

- The connect4 game can be deployed to herokuapp.com using a web interface terminal template. The steps to deploy are as follows: 
    - Sign up or log in to herokuapp.com.
    - Click "New" then "Create new app".
    - Enter an app name, choose your region and then click "Create app".
    - On the next page, go to the Settings Tab.
    - Click on "Reveal Config Vars". Add "port" in the KEY text field and "8000" in the VALUE text field, then click the "Add" button.
    - Click on "Add buildpack" and add the python build pack first, then save changes.
    - Click on "Add buildpack" again and add the nodejs build pack for the web interface to work. Be sure these 2 are in that order, Python first.
    - Click on the Deploy tab at the top, select GitHub and connect to your GitHub account.
    - Search for the repository name (connect-4) and click the "Connect" button.
    - Scroll down to the Automatic deploys section and choose the main branch to deploy from.
    - Click the "Enable Automatic Deploys" button which syncs the herokuapp.com files with your repository every so often.

You can also deploy to your own systems.

- If you wish to deploy within your own Python3 environment:
    - Download or copy the contents of run.py and scores.csv to your own system.
    - make sure the scores.csv has writeable permissions.
    - Run the game by typing: ***__python3 run.py__***

## Credits 

- I used the Code Institute web template and terminal window to deploy the program.
- I initially used the check_winner function from https://github.com/justinvallely/Python-Connect-4/blob/master/connect4.py (Line 69).
- I learned how to clear the terminal screen from this tutorial: https://www.geeksforgeeks.org/clear-screen-python/
- I learned how to work with .csv files from this website: https://www.pythontutorial.net/python-basics/python-read-csv-file/
- I got the Connect 4 logo text from this website: https://patorjk.com/software/taag/#p=display&f=Doom&t=Connect%204
- I made the flowchart by using this website:  https://online.visual-paradigm.com/
- I used a royalty free image of an old computer from: https://www.pikpng.com/
- I included quotes from 2001: A Space Odyssey by Arthur C. Clarke
- I included a quote from The Hitchhiker's Guide to the Galaxy by Douglas Adams
