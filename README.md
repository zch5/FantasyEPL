# FantasyEPL

## Plan
### What does the league entail?
#### A once a season draft where the user that wins by having the combined most points between players (bench players only half count)
Each team consists of 11 field players and 5 bench players
11 field players must include:
- 1 Goalkeeper
- 4 Defenders
- 4 Midfielders
- 2 Forwards

The bench has no limit on player's positions.
Each fantasy team can have a maximum of 3 players from any select EPL side.

#### How does user management work?
When first visiting the page, a screen will show league stats, as well as a login button. This login button will give users the chance to login. Once they login, they will have the ability to ask permission to join the league, draft a team, and edit team data.

#### What will a user be able to customize their team with?
They will be able to give their team a custom team name, and either an image or color.

#### How will the draft work?
The admin user will be able to set up a draft at a certain time. At the point, all users with a team will be redirected to the draft room. Each user will be given a random number which will determine the draft order. The draft is a snake draft. Each user will have 30 seconds to choose a player. When it is that user's turn, they will be shown the same screen, but each player profile will have a button that gives the ability to draft that player. Checks will be conducted to make sure that the player is eligible to join the team. After drafting the player, the user will have the buttons removed from their screen and the draft will move on to the next player.

### What technologies will be used to accomplish this project?
#### Data will be stored in a MySQL database
#### Controller will be built in Python
#### JavaScript, HTML, CSS, Jinja for frontend

## Steps
### Database Organization
#### Table of Users
- username (primary key)
- password
#### Table of Teams
- team_name (primary key)
- username (foreign key)
#### Table of Players
- player_id (primary key)
- fantasy_team_name (foreign key)

## Misc.
### Terminology
- Player -> An individual that plays in the EPL
- User -> An individual that plays in fantasy league
