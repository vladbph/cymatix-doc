```diff 
+ Please watch the repo updates. I am in process of creating documentation and examples
```

# zCymatix Natural Language Understanding(NLU) Voice/text UI platform (www.zcymatix.com)

For:

    - Healthcare 
    - Finance
    - Electronics
    - Wearables
    - Automotive
    - Web sites for blind
    - ...

### Machine learning NLU system designed for dialogues and expert systems. The platform uses Toth(Train Of Thought) contextual method of conversation flow tracking as well as many powerful features...
### ___...Context IS everything ...___
## Features Highlights
- Train Of Thought technology
    * Literaly maintains train of thought of the conversation
- State of the Art deduction pipeline to efficiently resolve ambiguity
- Ability to create 1000s of utterances in few minutes
- Supports method of embedding states, events, sensors information to maintain flow of the conversation
- Regex layer support. Yes, why would you need to use ML for simple things.? You may, but you don't have to
- Optional scripting support.
    * All layers of the pipeline are ML layers, however if desired, scripting can be used to make changes based on the context. See examples.
- Idioms interpretation mechanism
    * "I would really want to grab a bite and then go back home" => ``` { 't_intent':'NAVIGATE', 't_stopover':'restaurant', 't_destination':'Home' } ```
- Lookup labels support
    * "I want bbq chicken and new york pizza" => "I want PIZZA_KIND and PIZZA_KIND pizza" => ``` { 't_intent':'ORDER_PIZZA', 't_kind':['bbq chicken', 'new york']```
- NLU tasks supported:
    - Self-contained deductions, not contextual
        * __"Play the latest from Def Leppard"__ =>  ``` { 't_intent':'PLAY_MUSIC', 't_artist':'Def Leppard' } ```
        * __"Take me to Seattle"__ =>  ``` { 't_intent':'NAVIGATE, 't_destination':'Seattle' } ```
    - AI Bot asks user questions. Example: Order pizza bot
        * User> __I am hungry for pizza.__
        * __Bot__> What kind of pizza would you like?
        * User> __I would like bbq chicken and pepperoni__
        * __Bot__> What toppings would you like?
        * User> __I will go with extra cheese and tomatoes on top__
        * ...
        ...
    - User asks AI bot questions. Example: Web site 'How To' section:
        * User> __What can you do for me?__
        * __Bot__> I can help you to create a system that answers your question
        * User> __Nice, how?__
        * __Bot__> First, you need to create a project
        * User> __How?__
        * __Bot__> Create a folder. Name it as a project name. Create config file and at least one training file
    - Combination of above
- Indirect subject referencing
    * Notion of 'it/there'
        * 'Where is Seattle'
        * 'Take me there'
- Expert system support. Result of the dialog is fed into a layer to process conversation outcome.
    
   So, Let's do it!
# 1. 'Hello Word' Example.
* Create and enter **hello** folder
* Create **hello.json** file
```json
{ "data_files":"hello.txt" }
```
* Create **hello.txt** training file
```
.train
    GREETING:Hello World
```
***GREETING*** is the ***intent***, 'Hello world' is how you say it. You may ask what if the intent is not specified? Well - this means that utterance 'Hello World' will not have any learnt associations. This is very important point to understand - you can describe things two ways a) by what ***it is*** and b) what ***it is not***. We will come to this later.
So, that's it. Literally, 3 lines of code get you there. The deduction of the phrase 'Hello World' will be 
```json
    {"t_intent":"GREETING"}
```
BTW, to convert deduction to an object in Python:
```
    import json
    from argparse import Namespace
    obj = json.loads( "{'t_intent':'GREETING'}', object_hook = lambda d: Namespace( **d ) )
```
To get E2E how-to feeling go to www.zcymatix.com and sign up. Press ***Sign In*** and then ***Sign Up***. 
### ***NOTE!*** Please use real e-mail address to be able to receive training completion notification with PROJECT ID. Oherwise you cannot use the service.
![Register](http://www.zcymatix.com/img/signup.png "Register")

After login, upload the project by choosing your project folder - ***hello***. Remember - **folder name ___IS___ the project name**
![Upload](http://www.zcymatix.com/img/upload_page.png "Upload")

When project is uploaded, you need to train it. Choose ***Training*** option and press launch.
![Launch](http://www.zcymatix.com/img/launch_project.png "Launch")

Depending on project complexity it may take from few seconds to few hours to train it. When project training/building is finished you will receive the e-mail with the ***PROJECT ID***. Please store it, because you need to pass it with ***project launch*** request to the server.
What's next after project training is finished? Two options:
1. __Use NLU service via REST api.__
    * ***Project Launch request:***
        ***<https://nlp2.zcymatix.com/?action=launch&project_id=c7df223a3b97>***
        Parameters: 
        ```json
            action = launch
            project_id = c7df223a3b97 // Example value
        ```
        The responce has fixed format consisting of two fields ***code*** and ***msg***:
        ```json
        { "code":200, "msg":"806bb67b"}
        ```
        In the responce you will receive dynamic ___session_id___ which has to be used in deduction requests. Given value 806bb67b is an example.
    * ***Deduction:***
        ***<https://nlp2.zcymatix.com/?action=deduce&session_id=806bb67b&query=hello+world>***
        Parameters: 
        ```json
            action = deduce
            session_id = 806bb67b // Example value
        ```
        The responce:
        ```json
        { "code":201, "msg":"{"t_intent":"GREETINGS"}"}
        ```
        ```
        List of codes:
            200 - Session id is provided in msg field as a string
            201 - Deduction is provided in msg field as a JSON string
            202 - Info is provided in msg field as a string
            101 - Authentication error
            100 - Invalid parameters
        ```
        
    
2. __Use Web interface for training verification:__

![Deduction](http://www.zcymatix.com/img/deduction_page.png "Deduction")

# 2. Using macros
Let's update ***hello.txt*** file a little. Add ***.define*** section. 
```json
# Define section contains macros.
.define
    @hi = Hello|hi
    @guys = guys|folks|World|

# Training section contains utterances
.train
    GREETING:@hi @guys
```
In this example we define two macros ***@hi*** and ***@guys***. The resulting training set will be:
```json
GREETING:hi folks
GREETING:hi World
GREETING:hi guys
GREETING:Hello folks
GREETING:Hello World
GREETING:Hello guys
GREETING:Hello
GREETING:hi
```
Please note the last OR in ***@guys*** definition reads like ***guys*** or ***folks*** or ***World*** or ***empty string***. Granularity of regular expression feature is limited to the words. Example:
***folk(s|)*** is INVALID
***(folk|folks)*** is VALID

# 3. Using Slots (== parameters)
Training file:
```json
.define
    @take = take|bring
    @me = me|us|them
.train
    NAVIGATE: @take @me to Seattle{t_destination} by car{t_transport}
```

The deduction will look like:
```json
{"t_intent":"NAVIGATE", "t_destination":"Seattle", "t_transport":"car"}
```
# 3. Introduction to Layers
zCymatix platform is using the concept of ***layers***. Each layer could be responsible for deduction of specific things. For example, in case of ordering pizza you may want to deduce ***pizza toppings*** and ***pizza kinds*** in separation of the training set that will be using them. Why? Because there may be too many pizza kinds and toppings, meaning that final training data set will grow dramatically if we use each pizza kind and topping exlicetly. So it is advisable to have a layer that would be replacing specific pizza kind and topping with something like ***PIZZA_KIND*** and ***PIZZA_TOPPING*** labels. Layer after that, would use these lookup labels instead of actual values. The final deduction will resolve the actual values. The following example starts with more complex configuration file with two layer. Once you have more than one layer you have to name them:
```json
[
    {
        "layer_name":"Pizza kinds",
        "data_files":["kinds", "macros.h"]
    },
    {
        "layer_name":"Ordering pizza",
        "data_files":["order_pizza.txt", "macros.h"]
    }
]
```
I'll walk you through. First of all, let's put all the macros in one file ***macros.h*** and include it into both layers. It is optional however. So, let's take a look at ***kinds.txt*** file. One utterance in particular:
```
I would like to place an order for a small bbq chicken and large meat pizza
```
For simplicity sake, let's ignore pizza sizes deduction.

***kinds.txt***:
```
.train
    I would like to place an order for a small (bbq chicken){&PIZZA_KIND} and large meat{&PIZZA_KIND} pizza
```
*Intent is not present here, because the purpose of this utterance is to extract and label pizza kind:*
***PIZZA_KIND = bbq chicken***
***PIZZA_KIND = meat***

This is a mechanism to label multiple words with specific label and using multiple instance of the label in a single utterance(***Amazon Lex does not allow that***). To explain further lets take a look at the next layer and file 
***order_pizza.txt***:
```
.train
    ORDER_PIZZA: I would like to place an order for a small PIZZA_KIND{t_kind} and large PIZZA_KIND{t_kind} pizza
```
The intent ***ORDER_PIZZA*** present here, because the purpose of this layer is to get ***the intent and slots/parameters values*** that come with it.
***PIZZA_KIND{t_kind}*** marks both instances of the mentioned pizza kinds
The resulting deduction after applying both layers will be:
```json
{
    "t_utt":"i would like to place an order for small bbq chicken and large meat pizza",
    "t_intent":"ORDER_PIZZA",
    "t_kind":["bbq chicken", "meat"]
}
```
You could say - ___How about if I have a macro @pizza_kind and put all values there and use training utterance in one single layer?:___
```
ORDER_PIZZA: i would like to place an order for small @pizza_kind{t_kind} and large @pizza_kind{t_kind} pizza
```
Of course you can! BUT, how many utterances will be produced? ***A LOT!!!*** Imagine if on top you have:
```
.define 
    @i = i|we|they 
    @order = (place|) order for|get|buy
    @small = small|large|medium|
```
```
ORDER_PIZZA: @i would like to @order @small @pizza_kind{t_kind} and @pizza_kind{t_kind} pizza
```
So this mechanism enables smaller context needed to train the layer to extract and label the pizza kinds. Look - do you need ***all*** words in the example utterance in layer "Pizza kinds"? Not really. So I would put into training file something like this:
```
.define 
    @pizza_kind = bbq chicken|meat|pepperoni|hawaiian
.train
    @small @pizza_kind{&PIZZA_KIND} (and @pizza_kind{&PIZZA_KIND} pizza|)
```
So having a context consisting only surrounding words is enough? You decide. But be careful though. ***False positives one of the biggest issues in NLU systems***, finding the balance between training time, number of utterances and sufficient context is not easy task to create ***high quality training set.*** zCymatix platform gives the tools to go either way.
# 4. Dialogs
## 4.1 Loose Dialogs
There are two ways to hande dialogs/conversations. Both require enabling of ***ToTh(Train of Thougth)*** mechanism. For that you need to add the following parameter `"toth":true`
```json
[
    {
        "layer_name":"Pizza kinds",
        "data_files":["kinds", "macros.h"],
        "toth":true
    },
    {
        "layer_name":"Ordering pizza",
        "data_files":["order_pizza.txt", "macros.h"]
    }
]
```
Toth mechanism enables including previous intent as a prefix to utterance. Example:
```
How many would you like?
```
This question is not self-contained. It implies having the knowledge of previous information. Knowing that we are ordering pizza creates the context required to make sense out of it. What is you see this instead?
```
.train
    ORDER_PIZZA How many would you like?
```
Please note there is no ___':'___ sign after the intent meaning that it is treated as a 'word' in the utterance.
