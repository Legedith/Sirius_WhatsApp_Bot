# Sirius
A simple assistant for Whatsapp

## Usage
Clone repo, chromedriver should be in the same folder (Download appropriate version from [here](https://chromedriver.chromium.org/downloads)). Only requirement is selenium. Install it with pip. Open your whatsapp and make a new group named "Sirius".
Alternatively, in the script change 'name' to any group or contact name you already have in your phone.  
Use as follows : Sirius command parameters.  
To change the invocation, set phrase to whatever you want. Please not as of now most things are case sensitive.

### Commands 
#### 1. spam / crucio 
For spamming the message in same group/chat  
Usage: Sirius crucio &lt;message&gt; &lt;count&gt;

#### 2. spam.big / sectumsempra
For spamming someone else's chat  
Usage: Sirius sectumsempra &lt;person/group name&gt; &lt;message&gt; &lt;count&gt;

#### 3. google / alohomora
Sends a google link fot the search query  
Usage: Sirius alohomora &lt;query&gt;

#### 4. youtube / accio
Sends the link of video searched  
Usage: Sirius accio &lt;song/ or any other title you wanna search on youtube&gt;

#### 5. change / apparate
Access the bot from some other chat  
Usage: Sirius apparate &lt;group/person name&gt;

#### 6. rename / disapparate
Rename the bot  
Usage: Sirius disapparate &lt;new name&gt;

#### 7. mode / snape
Change the mode from scanning outgoing to incoming messages  
Usage: Sirius snape &lt;name&gt; in/out

#### 8. urban
Gets the meaning of a query from Urban Dictionary
Usage: Sirius urban &lt;query&gt;
  
#### 9. wiki
Gets the definition from wikipedia via query
Usage: Sirius wiki &lt;query&gt;

#### 10. cantis / soundcloud
Gets the song link from soundlcoud
Usage: Sirius cantis &lt;query&gt;

#### 11. response
Generate random responses
Usage: Sirius response / Sirius response stop
