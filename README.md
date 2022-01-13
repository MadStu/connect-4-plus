# Connect 4

Connect 4 is a strategy game where the idea is to get 4 of your own discs in a line in any direction, horizontally, vertically or diagonally ( -- ¦ / \ ), hence you connect 4 together. You must also block your opponent from connecting 4 and can be quite satisfying when you plan and predict a few moves in advance.

This game is useful for people who spend a lot of time in terminals and allows them to let off steam. They can have a quick game lasting less than a minute, or continue playing until they've beaten the computer, so it's good for somebody to play whether they only have a free moment or lots of time to spare.

A deployed version may be found here: [Connect 4](http://my-connect-4.herokuapp.com/)

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

### Features Left to Implement

- Implement a points system based on number of turns
- Add a high score board
- Add AI that learns and predicts the players next move based on their previous pattern of moves

## Testing

I've tested the code continuously as I've developed it, making sure all functionality works as it should and fix any typos or coding errors as and when they happen.

I also asked friends and family to play with and try to produce errors or unintended behaviours 

### Validator Testing 

- PEP8
  - No errors or warnings were returned when passing through [PEP8online.com](http://pep8online.com/)

### Bugs

You will need to mention unfixed bugs and why they were not fixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a big variable to consider, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed. 

## Deployment

The deployed program can be found here - http://my-connect-4.herokuapp.com/

- The connect4 game was deployed to herokuapp.com using a web interface terminal template. The steps to deploy are as follows: 
    - Sign up or log in to herokuapp.com.
    - Click "New" then "Create new app".
    - Enter an app name, choose your region and then click "Create app".
    - On the next page, go to the Settings Tab.
    - Click on "Reveal Config Vars". Add "port" in the KEY text field and "8000" in the VALUE text field, then click the "Add" button.
    - Click on "Add buildpack" and add the python build pack first, then save changes.
    - Click on "Add buildpack" again and add the nodejs build pack for the web interface to work.
    - Click on the Deploy tab at the top, select GitHub and connect to your GitHub account.
    - Search for the repository name (connect-4) and click the "Connect" button.
    - Scroll down to the Automatic deploys section and choose the main branch to deploy from.
    - Click the "Enable Automatic Deploys" button which syncs the herokuapp.com files with your repository every so often.

## Credits 

In this section you need to reference where you got your content, media and extra help from. It is common practice to use code from other repositories and tutorials, however, it is important to be very specific about these sources to avoid plagiarism. 

You can break the credits section up into Content and Media, depending on what you have included in your project. 

### Content 

- The text for the Home page was taken from Wikipedia Article A
- Instructions on how to implement form validation on the Sign Up page was taken from [Specific YouTube Tutorial](https://www.youtube.com/)
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)

### Media

- The photos used on the home and sign up page are from This Open Source site
- The images used for the gallery page were taken from this other open source site


Congratulations on completing your Readme, you have made another big stride in the direction of being a developer! 

## Other General Project Advice

Below you will find a couple of extra tips that may be helpful when completing your project. Remember that each of these projects will become part of your final portfolio so it’s important to allow enough time to showcase your best work! 

- One of the most basic elements of keeping a healthy commit history is with the commit message. When getting started with your project, read through [this article](https://chris.beams.io/posts/git-commit/) by Chris Beams on How to Write  a Git Commit Message 
  - Make sure to keep the messages in the imperative mood 

- When naming the files in your project directory, make sure to consider meaningful naming of files, point to specific names and sections of content.
  - For example, instead of naming an image used ‘image1.png’ consider naming it ‘landing_page_img.png’. This will ensure that there are clear file paths kept. 

- Do some extra research on good and bad coding practices, there are a handful of useful articles to read, consider reviewing the following list when getting started:
  - [Writing Your Best Code](https://learn.shayhowe.com/html-css/writing-your-best-code/)
  - [HTML & CSS Coding Best Practices](https://medium.com/@inceptiondj.info/html-css-coding-best-practice-fadb9870a00f)
  - [Google HTML/CSS Style Guide](https://google.github.io/styleguide/htmlcssguide.html#General)

Getting started with your Portfolio Projects can be daunting, planning your project can make it a lot easier to tackle, take small steps to reach the final outcome and enjoy the process! 








https://online.visual-paradigm.com/

https://www.geeksforgeeks.org/clear-screen-python/

https://patorjk.com/software/taag/#p=display&f=Doom&t=Connect%204