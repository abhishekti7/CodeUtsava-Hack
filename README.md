# CodeUtsava 3.0 Hackathon
[![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![PyPI status](https://img.shields.io/pypi/status/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/)
[![PyPI license](https://img.shields.io/pypi/l/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/)
[![GitHub release](https://img.shields.io/github/release/Naereen/StrapDown.js.svg)](https://GitHub.com/Naereen/StrapDown.js/releases/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)


#### *"Mental pain is less dramatic than physical pain, but it is more common and also harder to bear."* -C.S. Lewis


Depression in India, or in the rest of the world for that matter, is a state of mental health that is rarely ever acknowledged by people. People are afraid to admit this state of mental sickness for fear of society. According to the *World Health Organisation*, around **6.9%** of the Indian population is facing depression, anxiety or some state of mental sickness.

Our project, *'Here To Hear'* is basically an Alexa skill which runs on the Amazon Echo devices. This skill aims at detecting and analysing symptoms of depression or anxiety in the user.

### Features:
- Mood evaluation by the Alexa bot.
- Suicidal behaviour detection and prevention.
- Social Media Sentiment Analysis to dig up evidence of mental sickness, if any.
- Intelligent Suggestions by the Alexa AI to improve user's mood.
- Informs emergency contact via text if user is sad or in extreme cases, shows suicidal tendencies.
- Displays helpful information on the Alexa app.

### Technology Stack:

1. **Frontend** :
  - Amazon Alexa
2. **Backend** :
  - Alexa Skills Kit
  - Flask-Ask
  - Python
3. **Infrastructure**:
 - Amazon API Gateway
 - AWS Lambda

### How to Run:

1. **Create Virtual Environment** :
  - python3 -m virtualenv env
  - source env/bin/activate
2. **Install Requirements** : 
  - pip3 install -r requirements.txt
  - pip3 install -r requirements3.txt
  - sudo snap install ngrok
3. **Run voice.py** :
  - python3 voice.py
4.  **Run ngrok in a new terminal**
  - ngrok http 5000
