# Software Requirements

## Vision

- League of Legends is a fast-paced MOBA game, once the pre-match stage is complete and enemy team composition is revealed, a player has to start planning their build path for the entire match. Every and champion has an ideal build path that brings out the best of the character, but they still need to keep in mind who are they facing on the opposite side.  A player often has to do lots of mental math in order to figure out what should they go for and in which order, while keeping in mind the frequent adjustment and changes that champions and items go through almost every other week. Avid players also need to keep track of their activities and achievements.

- League Advisor Web App provides access to information regarding all of the game's current champions and items. It provides recommended item builds based on the user's team and enemy team composition, and allows users to keep track of their in-game account stats.

## Scope (In/Out)

### IN

- The app will provide a list of champions and items.
- The app will provide detailed information about every and each available item and champion.
- The app will provide the role of each hero or in other word the point of strength.
- The app will provide optimal items build for a selected champion without context.
- The app will provide optimal items build for a selected champion within two teams context.
- The app will be in sync with and show the user's account stats.

### OUT

- The app will not support other Riot Games game accounts.

## Minimum Viable Product

- An About section that provides the user with information on how the web app can enrich their experience with the game.
- A feature that allows the user to register and link their in-game account to their Web App account.
- A dashboard page that displays user account status and available features.
- A champion Browser feature that displays information about available champions.
- An items Browser feature that displays information about available items.
- A feature that recommends the optimal items build for a champion.
- A feature that elects the statistically superior build path for a champion based on the player's team and enemy team compositions and most commonly bought items in similar situations.

## What are your stretch goals?

- Provide account linking computability on all servers.
- Automate detecting and pulling patch notes on each update.
- Add champion skills to browser feature.
- Add champion skins to browser feature.
- Integrate Summoner Icons for user account creation.

## Functional Requirements

List the functionality of your product. This will consist of tasks such as the following:

- An admin can create and delete user accounts
- An admin can trigger data update.
- A user can create an app account and link it to their in-game account.
- A user can browse through all items and champions.
- A user can choose a champion to view their optimal items build.
- A user can choose two teams and receive the optimal build for their champion accordingly.
- A user can view their account stats and information.

## Data Flow

- User interactions on the app will send a request to the API.
- The API will check if the data is present in the database.
- If it is, it will be returned to the app as a response.
- If it is not, the API will send a request to Third-party API and store data in the database.
- The API will respond to the app with the requested data.

## Non-Functional Requirements

### Security

- Users must be authenticated in order to use app features. They have to log in with their credentials into their own accounts and will only be able to view their linked account info.
- All API server to Third-party API requests will send API Key in headers params.

### Testability

- Backend functionalities will be tested to receive, store and respond with the expected data type and content.
- Frontend functionalities will be tested to trigger the corresponding events as expected, fetch the correct data in the expected shape and send it to the API server accordingly.
