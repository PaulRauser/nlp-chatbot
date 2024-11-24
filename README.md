# Chatbot - Nürburgring 24h (Nürbot)
**Paul Rauser - 768084**

## Architecture / Overview
The bot consists of 5 major components:
- **RASA model server**: The core of the bot - handles Natural Language Understanding, 
mapping of user input to specific actions and much more
- **RASA actions server**: Enables communication with database, API calls, and
handling custom logic
- **SQLite DB**: Saves various detail information, links for images and user inputs
for development
- **Intermediary Flask Server**: Used to connect frontend and Rasa model and also
to save user inputs in database for further development
- React Frontend: User can enter data in chat UI; responses from the model are
rendered depending on the response type

The components work together closely to enable seamless usage of the bot and all 
its features. 
The components work together in the following ways:
- React frontend sends user input data as JSON to Flask server
- Flaks server saves user input in database so the data can be used to further train 
the bot
- Flask converts the calls into a format Rasa can understand and forwards requests to rasa
- Rasa performs NLU on the input and maps the input to a specific output
- If needed, Rasa calls the custom action server executing the required action
- The action server either sends a reply back to Flask directly or hands back
to Rasa to handle the reply. The custom actions also include all API calls and
communication with the database
- Flask hands back the data from Rasa to the Frontend
- In the frontend the data is rendered based on the type specified in Rasa (text,
image, buttons, custom-format)

## How to start
To work with the Bot, all components (not including the database / APIs) need
to be started correctly. 

Preconditions:
- A virtual environment running Python 3.8 (or other compatible versions)
- A working Rasa installation
- An installation of Flask
- An installation of node and npm (for the frontend)

Startup procedure:
1. Navigate to /backend and enter the venv; go to /rasa and run `rasa run --enable-api --cors "*"`
2. In a separate terminal tab navigate to backend/rasa and run `rasa run actions`
3. In a third terminal tab navigate to backend/server and run `python3 app.py`
4. In a fourth tab (doesn't need venv running) navigate to /frontend and run `npm run dev`

**Important**: venv should be started in /backend, calls to rasa should be executed in /rasa \
**Note**: A trained model is part of the Git repo, to retrain run `rasa train` in /rasa

## Facts

### Rasa features
- 30 intents
- 80+ hardcoded utters
- 30+ dynamic and flexible utters 
- 4 types of recognized entities
- 5 constantly adjusting slots
- 8 custom actions 
- 3 major dynamic stories - focus on strong NLU to enable replies to all
questions at any point in the conversation
- 3 sets of rules for custom actions, basic interactions and linear interactions
- 27 total rules
- 280+ NLU examples in 3 categories
- 3 lookup tables
- 4 different types of possible responses (text, images, buttons and a custom
format for links)

### Custom features
- Use of Database to store detailed information
- Use of Wikipedia API to get additional info
- Use of custom actions to interact with database, APIs, generate dynamic replies, 
dynamically set slots, remember previous intents, etc.
- Input processing to recognize substrings in user inputs and potentially spelling errors

### Frontend features
- Frontend is configured to handle all types of responses (new response types / custom)
responses can easily be configured
- Frontend displays the certainty score of the bot for every user query
- Differnt themes for added customizability  

More can be found in the project code.

## Capabilities
The bot is designed to answer an array of questions about the Nürburgring 24h race. 
The possible questions are classified into 3 groups.
- Basic communication
- Linear communication 
- Complex communication

### Basic communication:
- Great the bot
- Say goodbye
- Say thank you
- Ask the bot if it is a bot (challenge)
- Ask the bot what it can do
- Ask the bot who created it
- Ask the bot what technology it uses
- Ask for recommendations
- Report a found bug
- Provide feedback to the bot

These basic functionalities are important because users might ask them, 
however they are only covered rudimentary since the focus of the bot is not
to provide a good smalltalking experience but to answer the most urgent questions
about the Nürburgring 24h race.  
However the bot is designed in a way that smalltalk capabilities can be extended easily 
without interfering with the other communication types. This is mainly enabled by the
large amount of NLU exmamples making it easy for the bot to distinguish between the different
inputs a user might provide.

### Linear communication:
- Ask about highlights
- Ask about the evolution / history of the race
- Ask about the location of the race
- Ask about the schedule of the race
- Ask about how weather can influence the race
- Ask about fun facts
- Ask about information about the track
- Ask about where to get tickets
- Ask about where you can stay during the race (accommodation)
- Ask about the regulations of the cars
- Ask about where you can park during the race

For a majority of these communications the intents are stored so the user
can later ask the bot to tell them more.
For each communication several replies are possible. These can include text,
images and custom links. \
The questions in this list are backed with a large amount of NLU examples to ensure adding
more questions won't break other features.

### Complex communication:
- Ask about the drivers, cars and teams in the race
- Ask about the details of any of the drivers, cars and drivers the bots lists
- Ask the bot to tell you more - This will repeat the previously recognized intents actions

All these communication options depend on the concrete data the user enters.
The bot will recognize if the user wants to know about teams, cars or drivers based on the input.
To not clutter the bot with intents, this option is just handled in one intent.
Additionally asking about specific cars, drivers and teams is handled in one intent respectively 
covering around 10 different options per intent.
The creation of the response is handled by custom actions that either call the database, call an
API and dynamically modify the response data based on the request.
The replies include text, images, links and also buttons. The bot is set up in a way
that these options could be extendend easily for example by introducing new custom
response formats or adjusting API calls and the data in the database.

For the 'tell me more' intent two custom actions are needed. One that saves the previous intent for a specified
list of intents and one that, when the 'tell me more' intent is recognized re-triggers the
actions of the previous intent.
This way any intent that should have the 'tell me more' feature needs to be extended by just one line in 
the rules.

### Fallback
If the confidence of the bot regarding the users message is below a certain threshold, a fallback
will be triggered asking the user to rephrase.

## Possible improvements
- Basic user authentication
- More advanced database queries for even more detailed questions / answers
- Use user inputs and manual intent mapping for improved NLU and to figure out which features
users really need and use frequently 
