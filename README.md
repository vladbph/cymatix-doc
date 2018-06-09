# [zCymatix](http://www.zcymatix.com) Natural Language Understanding(NLU) Voice/text UI & Expert Systems Platform 
# [Sign Up](https://nlp2.zcymatix.com/) 
# [Dashboard Android App](https://play.google.com/store/apps/details?id=com.zcymatix.demo)
#### Applications:
- Healthcare
- Finance
- Electronics
- Wearables/IoT
- Automotive
- Web sites for blind people
- Interactive (Voice/text controlled) Web sites. 
- Emails/text scans and more
 

Table of Contents
=================
   * [Features Highlights](#features-highlights)
   * ['Hello Word' Example](#hello-word-example)
   * [Project Layers](#project-layers)
   * [Project ID](#project-id)
   * [Training time](#training-time)
   * [Project WEB UI indicators](#project-web-ui-indicators)
   * [NLU service REST API](#nlu-service-rest-api)
      * [Launch request](#launch-request)
      * [Inference example](#inference-example)
      * [List of response codes](#list-of-response-codes)
   * [.train section](#train-section)
   * [.prompt section](#prompt-section)
   * [.define section](#define-section)
   * [.list section](#list-section)
   * [Slots (parameters)](#slots-parameters)
   * [Introduction to Layers](#introduction-to-layers)
   * [Dialogs](#dialogs)
      * [AI system asks questions](#ai-system-asks-questions)
         * [.gate section](#gate-section)
      * [User asks questions](#user-asks-questions)
   * [.regex section](#regex-section)
      * [Replacement](#replacement)
      * [Lookup lables](#lookup-lables)
   * [Prompt label](#prompt-label)
      * [Prefix <strong>"#"</strong>](#prefix-)
      * [Prefix <strong>"?#"</strong>](#prefix--1)
      * [Prefix <strong>"$"</strong>](#prefix--2)
      * [Prefix <strong>"?$"</strong>](#prefix--3)
      * [Prefix <strong>"."</strong>](#prefix--4)
      * [Prefix <strong>"?."</strong>](#prefix--5)
      * [Empty label prefix](#empty-label-prefix)
      * [Prefix <strong>"?"</strong>](#prefix--6)
      * [Prompt label value access by index](#prompt-label-value-access-by-index)
   * [PIZZA2 BOT Example](#pizza2-bot-example)
      * [Layer 1 Slots](#layer-1-slots)
      * [Layer 2 Pizza](#layer-2-pizza)
      * [Layer 3 Bot](#layer-3-bot)
      * [Pizza project Final Inference](#pizza-project-final-inference)
   * [Inference history](#inference-history)
   * [How to control inference history](#how-to-control-inference-history)
      * [Intent Prefixes](#intent-prefixes)
      * [Empty prefix](#empty-prefix)
      * [R~ prefix. Return command](#r-prefix-return-command)
      * [F~ prefix. Infere and Forget command](#f-prefix-infere-and-forget-command)
      * [P~ prefix. One step back command](#p-prefix-one-step-back-command)
      * [B~ prefix. Two steps back command](#b-prefix-two-steps-back-command)
      * [C~ prefix. Change slot value command](#c-prefix-change-slot-value-command)
      * [X~ prefix. Clean previous history command](#x-prefix-clean-previous-history-command)
      * [I~ prefix. Clean previous history and restart command](#i-prefix-clean-previous-history-and-restart-command)
   * [Idioms interpretation. Intent prefix ~](#idioms-interpretation-intent-prefix-)
   * [Remove slot value from inference history. $del command](#remove-slot-value-from-inference-history-del-command)
   * [Indirect references it or <code>there</code>](#indirect-references-it-or-there)
   * [.gate2 section](#gate2-section)
   * [.script section](#script-section)
   * [.vars section](#vars-section)
   * [.slist section](#slist-section)
   * [Events, States, Sensors Information Embedding](#events-states-sensors-information-embedding)
   * [Multiple language support](#multiple-language-support)
   * [Comments in training files](#comments-in-training-files)
   * [Long lines continuation](#long-lines-continuation)
   * [Unknown word marker](#unknown-word-marker)
   * [Placement slot inference](#placement-slot-inference)
   * [Expert systems support](#expert-systems-support)
   * [Recommendations, tips and tricks](#recommendations-tips-and-tricks)
   * [Optional configuration parameters](#optional-configuration-parameters)
   * [Advanced configuration parameters](#advanced-configuration-parameters)



#### Machine learning NLU system designed for dialogues and expert systems. The platform utilizes proprietary Toth(Train Of Thought) technology for conversation flow tracking and supports many other features...
### ___"...Context IS everything ..."___
# Features Highlights
- ***`Train Of Thought technology`***
    * Maintains a train of thought of the conversation using proprietary mechanism and inferences history
- ***`Session-based conversation instances`***  Memory and context is kept on the `backend`. Client application does not need to collect inference history(!).
- Ability to create ***`1000s of utterances`*** in minutes
- ***`States, Events and Sensors Data Embedding`*** contextual support
- ***`Scripting support`***
    * Along with `ToTh`, developer may choose to use python scripts that runs on backend to update inferences based on the context. This way client application focuses on the task at hand.
- `Regex` support. Yes, why would you need to use trainable models for simple things.? You may, but you don't have to.
- Idioms interpretation mechanism
    * "I would really want to grab a bite and then go back home" => ``` { 't_intent':'NAVIGATE', 't_stopover':'restaurant', 't_dest':'Home' } ```
- Trainable Lookup labels support
    * "I want BBQ chicken and new york pizza" => "I want PIZZA_KIND and PIZZA_KIND pizza" => ``` { 't_intent':'ORDER_PIZZA', 't_kind':['BBQ chicken', 'new york']```
- NLU tasks:
    - `Self-contained` inferences:
        * __"Play the latest from Def Leppard"__ =>  
            ``` { 't_intent':'PLAY_MUSIC', 't_artist':'Def Leppard', 't_attr':'latest' } ```
        * __"Show flights to Seattle"__ =>  ``` { 't_intent':'SHOW_FLIGHT, 't_dest':'Seattle' } ```
    - `AI Bot asks User` questions. Example: Order pizza bot
        * User> __I am hungry for pizza.__
        * __Bot__> What kind of pizza would you like?
        * User> __I would like BBQ chicken and pepperoni__
        * __Bot__> What toppings would you like?
        * User> __I will go with extra cheese and tomatoes on top__
        * ...
    - `User asks AI bot` questions. Example: Web site 'How To' section:
        * User> __What can you do for me?__
        * __Bot__> I can help you to create AI chat bots, make your website to talk to you and more...
        * User> __how?__
        * __Bot__> First, you need to create a project
        * User> __How?__
        * __Bot__> Create a folder, then create configuration file and training files for me to learn
    - Combination of above
- ***Coreference Resolution*** 
        * 'Where is Seattle'
        * 'Take me there'
- ***`Expert systems support`*** Result of the dialog could be fed into a layer to process conversation outcome.
    * This is not NLU specific feature which enables platform utilization in any field of knowledge
- ***`Multiple language support`***
- NOTE! Platform DOES NOT provide voice recognition services


   ___So, Let's do it!___
# 'Hello Word' Example
Let's demonstrate how 3 lines of text/code makes your first NLU project.
* Create and enter **hello** folder. `Folder name is the name of the project.`
* Create **hello.json** file
```json
{ "data_files":"hello.txt" }
```
* Create **hello.txt** training file
```
.train
    GREETING: (Hello World|hi|hello)
```
***GREETING*** is the ***intent***, 'Hello world' is how you say it. You may ask what if the intent is not specified? Well - this means that utterance 'Hello World' will not have any associations. This is very important point to understand - you can describe things two ways a) by what ***it is*** and b) what ***it is not***. We will come to this later.
So, this is it. Literally, 3 lines of code get you there. The inference of the phrase 'Hello World' will be 
```json
    {"t_intent":"GREETING"}
```
That's it. If you want to see system to respond to you, add:
```
.prompt
    GREETING: Hello my friend
```

To get end-to-end experience go to [zcymatix.com](http://www.zcymatix.com) and sign up. Press ***Sign In*** and then ***Sign Up***. 
***NOTE!*** Please use real e-mail address to be able to receive training completion notification with PROJECT ID. Otherwise you cannot use the service.
![Register](http://www.zcymatix.com/img/signup3.png "Register")

After login, upload the project by choosing your project folder - ***hello***. 
Remember, __project name__ is the name of the __folder__ and configuration file name must be 
`<project name>.json`
![Upload](http://www.zcymatix.com/img/upload_page1.png "Upload")

When project is uploaded, you need to train it. Choose ***Build*** option for that. When project was stopped and/or you want to continue building it, press ***Continue Build***. However, keep in mind that if you changed the training files, continuing building the project DOES NOT always means faster training times. So, we suggest to use ***Build*** option when training files have changed.
Option ***Start/Restart*** launches the project in production mode. It should be used when project has been already built. NOTE! You ___can___ start building the project while it is in launched/production mode (we use these terms interchangeably). Once the building is finished, the project will `go online without distrupting client applications`.
![Launch](http://www.zcymatix.com/img/launch_project1.png "Launch")

# Project Layers
Once a project has been uploaded it will appear in the list of projects. When you click on it, the list of layers will be displayed. Layer `All` represent the whole project. You can either build or train whole project using `All` layer or each layer separately for debug purposes. The menu option for `All` layer is almost the same as each layer. Single layer has `Settings` options reflecting current settings of the layer taken from the configuration file. You can delete the whole project but cannot a selected layer. To do so, you need to upload the updated project from your local machine.
On the picture below, you can see `project id` associated with the project. It is needed for REST API.

![Layer menu](http://www.zcymatix.com/img/layer_page1.png "Launch")

NOTE! Launching all layer of the project separately, does not mean launching the whole project(!). As it was stated above, launching a layer is only for test purposes. You must launch 'All' layer to engage all layers in a stack to run in production mode.

# Project ID
By clicking on the project ID, you will see the REST API to use your project in production.
![Using project id](http://www.zcymatix.com/img/rest_info.png "Launch")

# Training time
Depending on project complexity it may take from few seconds to few hours to train it. When project training/building is finished you will receive e-mail notification with the ***PROJECT ID*** required for ***project launch*** REST request. When training, project's or layer's icon is blinking.

# Project WEB UI indicators
Web interface has color coded icons against project and each layer. 

RED - means that the project is NOT loaded

GREEN - means that the project has been loaded in production mode

YELLOW - indicates that one of the project layer has been loaded, but not the whole project

# NLU service REST API
## Launch request
This is initial handshake request.
***https://nlp2.zcymatix.com/?zcmd=launch&project_id=f38360cd-08c5-482b-8c22-c2bc67194ab8***
Parameters: 
```json
    cmd = launch
    project_id = f38360cd-08c5-482b-8c22-c2bc67194ab8
```
NOTE! `f38360cd-08c5-482b-8c22-c2bc67194ab8` is fake project id
The response contains the dynamic ___session_id___, which must be used in the following inference requests. The response looks like this:
```json
{ "code":200, "msg":"2cb3b87d-e29c-4743-bab1-0fc5cb98db6d"}
```
Session ID in this example is:`2cb3b87d-e29c-4743-bab1-0fc5cb98db6d`
Here is REST API flow diagram:
![REST API workflow](http://www.zcymatix.com/img/REST_workflow.png "REST API workflow")

## Inference example

***<https://nlp2.zcymatix.com/?zcmd=deduce&session_id=2cb3b87d-e29c-4743-bab1-0fc5cb98db6d&query=Hello+World>***
Parameters: 
```json
    cmd = deduce
    session_id = 2cb3b87d-e29c-4743-bab1-0fc5cb98db6d
    query = hello world
```
The response:
```json
{ "code":201, "msg":"{"t_intent":"GREETINGS"}"}
```

## List of response codes
```
List of codes:
    200 - Session id is provided in msg field as a string
    201 - Inference is provided in msg field as a JSON string
    202 - Info is provided in msg field as a string
    102 - Project is loading
    101 - Authentication error
    100 - Invalid parameters
```

It may take few seconds for a project to be launched (if it was not before). If during this time client's inference request comes to the backend, it will respond with the code `102`. ___Client must repeat the request___ until the inference response comes back with the code `201`. 
        This is the 'worst' case scenario, because projects must be loaded in prediction mode for `production` use after training is finished, thus it should be always loaded.
        
# `.train` section 
Alternative name is **`.user`** for readability.
The section contains training samples. Formal syntax is:
```
.train
    <INTENT>: <utterance with or without slot labels>
```
Note, the intent is optional. In this case the utterance may be used to slot fitting:
```
.train
    I want pizza with (extra cheese){t_toppings} and ham{t_toppings}
```
The following example teaches to ingore the utterace all together:
```
.train
    I am not sure what I want
```
This example is quite important to demonstrate the key concept, while building a training set. One thing can be descrided `what it is` and `what it is not`! Keeping this in mind, you can create more accurate training sets.

# `.prompt` section
Alternative name is **`.bot`** for readability.
What if we want AI system to respond to user query? Let's use the 'Hello World' code:
```
.user
    GREETING: Hello World
.prompt
    GREETING: Hello my friend
    GREETING: Hello!
    GREETING: Hi!    
```
By adding section ***.prompt*** we can define user prompts: 
```
INTENT:<PROMPT VARIANT>
```
In the example above GREETING has three variants. They will be selected randomly in order to create more human like interaction. It reads like this - 'when user greets me reply this'. Prompt text may contain slots/parameters values. 
```
.prompt
    NAVIGATE: Ok, I am starting navigation to {t_dest} by {t_car}
```
Where ___t_dest___ and ___t_car___ are slots/parameters.
Prompts purpose is twofold 1. to be able to respond to user. 2. Prompt as a template with slot names to be passed to next layer in the inference pipeline. This mechanism is used in `expert systems` layers.
The idea: You collect all the data from user in the form of slots and their values and then use prompt template to build the 'utterance' for the next model. 
```json
.prompt
    R~READY: {t_param1} {t_param2} {t_param3}...
```
Please, be careful when having multiple layers in non expert system projects. Let's say you have three layer project. Second layer defines a prompt. In such cases `propmt is passed to third layer instead of utterance(!)`

# `.define` section
Let's update ***hello.txt*** file a little. Add ***.define*** section. 
```json
.define
    @hi: Hello|hi
    @guys: guys|folks|World|

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
Please note the last OR in ***@guys*** definition reads like ***empty string***. So, __@guys__ it is either ***guys*** or ***folks*** or ***World*** or ***empty string***. It is similar to regular expression, but limited at the words level only. Examples:
- ***folk(s|)*** is INVALID
- ***(folk|folks)*** is VALID
 
# `.list` section

This section is very much the same as define with different syntax:
```
.list=<define name>
    item1
    item2
    ...
```
Example:
```
.list=us_state
    Alabama
    Alaska
    Arizona
    Arkansas
    California
    ...
```
It is the same as:
```
.define
    @us_state: Alabama|Alaska|Arizona|Arkansas|California|...
```
Imagine you want to train `named entity recognizer`. Usually you get the text file with the list of items. `.list` section lets you quickly transform text file into the training file by adding the section header to the top.

# `Slots` (parameters)
In the training set we can assign intent and mark/label words with slot names for each utterance.
Training file:
```json
.define
    @take: take|bring
    @me: me|us|them
.train
    NAVIGATE: @take @me to Seattle{t_dest} by car{t_transport}
.prompt
    NAVIGATE: Sure, I am starting navigation to {t_dest} by {t_transport}
```

The inference will look like:
```json
{"t_intent":"NAVIGATE", "t_dest":"Seattle", "t_transport":"car"}
```
This way we infere the meaning of the utterance.

# Introduction to Layers
[`zCymatix`](http://www.zcymatix.com) platform is using the concept of ***layers***. Each layer could be responsible for inference of specific things. For example, in case of ordering pizza you may want to infere ***pizza toppings*** and ***pizza kinds*** in separation of the training set that will be using them. Why? Because there may be too many pizza kinds and toppings, meaning that final training data set will grow dramatically if we use each pizza kind and topping explicitly. Of course you can use [`placement slot inference`](#placement-slot-inference), but it is up to developer to decide which way to go. So, it is advisable to have a layer that would be replacing specific pizza kind and topping with something like ***PIZZA_KIND*** and ***PIZZA_TOPPING*** lookup labels. Layer after that, would use them instead of actual values. At the end of the inference cycle they will be resolved to the actual values. The following example starts with more complex configuration file with two layers. Once you have more than one layer you have to name each of them:
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
I'll walk you through. First of all, let's put all the macros in one file ***macros.h*** and include it into both layers. It is optional however. So, let's look at ***kinds.txt*** file. One utterance in particular:
```
I would like to place an order for a small BBQ chicken and large meat pizza
```
For simplicity sake, let's ignore pizza sizes inference.

***kinds.txt***:
```
.train
    I would like to place an order for a small (BBQ chicken){&PIZZA_KIND} and \
    large meat{&PIZZA_KIND} pizza
```
*Intent is not present here, because the purpose of this utterance is to create `sufficient context` to isolate and extract pizza kind:*
***PIZZA_KIND = BBQ chicken***
***PIZZA_KIND = meat***

This is a mechanism to label multiple words with specific `lookup label` and using multiple instance of the label in a single utterance (***Amazon Lex does not allow that***). To explain further, let's look at the next layer and file 
***order_pizza.txt***:
```
.train
    ORDER_PIZZA: I would like to place an order for a small PIZZA_KIND{t_kind} and \
                 large PIZZA_KIND{t_kind} pizza
```
The intent ***ORDER_PIZZA*** present here, because the purpose of this layer is to get ***the intent and slots/parameters values*** that come with it.
***PIZZA_KIND{t_kind}*** marks both instances of the mentioned pizza kinds.
The resulting inference after applying both layers will be:
```json
{
    "t_utt":"i would like to place an order for small BBQ chicken and large meat pizza",
    "t_intent":"ORDER_PIZZA",
    "t_kind":["BBQ chicken", "meat"]
}
```
You could say - ___How about if I have a macro @pizza_kind and put all values there and use training utterance in one single layer?:___
```
.define
    @pizza_kind: BBQ chicken|meat|Hawaiian|...
.train
    ORDER_PIZZA: i would like to place an order for small @pizza_kind{t_kind} and \
                 large @pizza_kind{t_kind} pizza
```
Of course you can! BUT, how many utterances will be produced? ***A LOT!!!*** Imagine if on top you have:
```
.define 
    @i: i|we|they 
    @order: (place|) order for|get|buy
    @small: small|large|medium|
```
```
ORDER_PIZZA: @i would like to @order @small @pizza_kind{t_kind} and \
             @pizza_kind{t_kind} pizza
```
So, this mechanism enables smaller context needed to train the layer to extract and label the pizza kinds. Look - do you need ***all*** words in the example utterance in layer "Pizza kinds"? Not really. So, I would put into training file something like this:
```
.define 
    @pizza_kind: BBQ chicken|meat|pepperoni|Hawaiian
.train
    @small @pizza_kind{&PIZZA_KIND} (and @pizza_kind{&PIZZA_KIND} pizza|)
```
So, having a context consisting only surrounding words is enough? You decide. But be careful though. ***False positives one of the biggest issues in NLU systems***, finding the balance between training time, number of utterances and sufficient context is not easy task to create ***high quality training set.*** [`zCymatix`](http://www.zcymatix.com) platform gives the tools to go either way.
# Dialogs
There are two types of dialogs supported by the platform ***AI system asks questions*** and ***User asks questions***. And third one is the combination of these two.
## AI system asks questions
This type of dialog assumes that AI system knows the set of slots/parameters to collect from user. `Presence of the slots values` is sufficient for the system to consider conversation complete. 
Let's take as example a visit to doctor. 
```
Patient> I have a stomach ache
AI Doctor> Did you take any medications?
Patient> Yes
AI Doctor> What kind of medication did you take?
Patient>...
```
Or
```
Patient> I have a stomach ache
AI Doctor> Did you take any medications?
Patient> No
AI Doctor> How bad is the pain on the scale of 1 to 10?
Patient>...
```
As you can see based on the patient answer, conversation goes different routes. 
Using `toth` flags:
```
    "toth":True
    "intent_to_utterance":true
```
or/and `prompts templates` we can follow __`train of thought`__ of the conversation and use users intents and answers as a context for next inferences. Intents of the previous statements are embedded into next user utterances. It allows to have multiturn dialogs.

Another example: pizza assistant. User can freely provide the information about the pizza without following strict order of the conversation:
```
    User> I want to order some pizza
    Bot> What kind would you like?
    User> I want small BBQ chicken with extra cheese and tomatoes
    Bot> What is the delivery address?
    User>...
    Bot> Here is you order... Should I go ahead and place your order?
    User> you bet!
    Bot> Great, thank you!!!
```
The conversation flow depends on already provided parameters and system would ask only those questions to retrieve missing parameters. So, the conversation could go like this:
```
    User> I want small BBQ chicken with extra cheese and tomatoes on top and my address is ...
    Bot> Here is you order... Should I go ahead and place your order?
    User> Yes
```
There are few things to know before we can create such dialog.

### `.gate` section
Its purpose is to fullfil user query. Gate is a small script for generating new intent based on the inference history. The syntax uses python style `if` statements. It is better to demonstrate on `Pizza` example:
```python
.gate
    'ASK_KIND'        if o.t_intent == 'ORDER_PIZZA' and not hasattr( o, 't_kind' )
    'ASK_SIZE'        if o.t_intent == 'ORDER_PIZZA' and not hasattr( o, 't_size' )
    'ASK_TOPPINGS'    if o.t_intent == 'ORDER_PIZZA' and not hasattr( o, 't_toppings' )
    'ASK_ADDRESS'     if o.t_intent == 'ORDER_PIZZA' and not hasattr( o, 't_address' )
    'ASK_TO_CONFIRM'  if o.t_intent == 'ORDER_PIZZA'
    'R~THANKS_YES'    if o.t_intent == 'ORDER_PIZZA_YES'
    'R~THANKS_NO'     if o.t_intent == 'ORDER_PIZZA_NO'
```
```
.prompt
    ASK_KIND: What kind of pizza would you like?(BBQ chicken, Hawaiian, pepperoni, etc)
    ASK_SIZE: What size? (large, medium, small, etc)
    ASK_TOPPINGS: Anything on top?(ham, cheese, tomatoes, etc)
    ASK_ADDRESS: What is your address?
    ASK_TO_CONFIRM: Your order is {t_size} {t_kind} pizza with {t_topping} \
                     to be delivered to {t_address} Should I go ahead and place the order?
    R~THANKS_YES: Thank you for your order
    R~THANKS_NO: Sure, I will cancel the order for you
```
The intuition is simple. It reads like this - when current intent is ORDER_PIZZA and we still don't know pizza kind - generate intent ASK_KIND to ask user about pizza kind. The actual question is in the `prompt` section.
***ORDER of gates IS important!!!*** Gates are applied in the same order listed in the section.
**Please note a mandatory prefix 'o.' in front of slot and intent label and also single quotes surrounding the intent name.**
Gates are executed in the sequential order and they must be `mutually exclusive`. The sequence of the gates execution stops when first one returns not empty intent. 
Be aware of the following case. It WILL cause a break in the model, because the return value will be always either `INTENT_2` or `INTENT_3`. 
```
.gate
    // ERROR!!!
    'INTENT_2' if o.t_intent == 'INTENT_1' and not hasattr( o, 't_something' ) else 'INTENT_3'
```
Ignore for now prefix ***R~*** of the ***R~THANKS_YES*** and ***R~THANKS_NO***. It has special meaning to be discussed [later](#r-prefix).
It was mentioned earlier that ***prompt's template*** can be used to pass information to the next layer. That would eliminate the need to have scripted ***.gate***. In each particular case developer has to make their judgement call which way to go. Note, though, gates do not require training.
Consider another example:
```
.gate
    'ASK_CITY' if o.t_intent == 'Q42' and not hasattr( o, 't_city' )
```
Keeping in mind that the goal of the gate is to potentially change the intent, the gate above checks if current intent is `Q42`, but the t_city was not provided, return intent which would tell user something like: 'You did not provide the city'. You can argue the rational of this, saying why can't I just train it in such way, so when city is provided one intent is produced and if not provided - another one? Absolutely true. However, we want to keep the options open for developer. Not to mention, that the gate mechanism does not require training.

## User asks questions
The best example of such dialog would be Frequetly Asked Questions of a website. Again toth mechanism allows following handling questions differently depending on the context. Example of our web service:
```
User> What can you do for me?
Service> I am a Natural Language Understanding platform and I can help you to create AI assistants
User> How?
Service> First, you need to create a project
User> How?
Service> Minimalistic project consists of two files - configuration file and training file
```
Training file:
```
.train
    I~INTRO: what can you do for me
    I~INTRO: what is your (purpose|goal|task|agenda)
    I~INTRO: how you can help me
    I~INTRO: how can you help me
    I~INTRO: <...>
    
    DO_CREATE_PROJECT: I~INTRO how?
    DO_CREATE_PROJECT: I~INTRO how is that?
    DO_CREATE_PROJECT: I~INTRO how can I do that?
    DO_CREATE_PROJECT: I~INTRO what should I do?
    DO_CREATE_PROJECT: I~INTRO any guidance (please|)?
    DO_CREATE_PROJECT: <...>
    
    MIN_PROJECT: DO_CREATE_PROJECT how?
    MIN_PROJECT: DO_CREATE_PROJECT how is that?
    MIN_PROJECT: DO_CREATE_PROJECT how can I do that?
    MIN_PROJECT: DO_CREATE_PROJECT any guidance (please|)?
    MIN_PROJECT: <...>

.prompt
    I~INTRO: I am a Natural Language Understanding platform and I can help you to create AI assistants
    DO_CREATE_PROJECT: First, you need to create a project
    MIN_PROJECT: Minimalistic project consists of two files - configuration file and training file
```
As you can see here, the same question 'How?' gives contextual adequate response. Also see [how to control inference history](#how-to-control-inference-history) section for intent prefixes.

# `.regex` section
## Replacement
```
.regex
    &and:\b(?:as well as|and also)\b
```
It is a direct replacement of words in the utterance to simplify training sets. You can use the section to prevent your training set to be extremely large. Please note, there should be one and only one group - `0`, full match. To achive that use non-capturing groups - (?:regex). As in the example above, matching group `0` equals either: 'as well as' or 'and also'. Refer  [here](https://www.regular-expressions.info/refcapture.html) for details. 

More complex example:
```
.regex
    &1 hours and 30 minutes : \bone\s+(?:and|\&)\s+(?:(?:a|the)\s+)?half\s+(?:an?\s+)?h(?:ou)?r?s?\b
```

## Lookup lables
```
.regex
    P_SIZE:\b(?:small|medium|large)\b
```
The actual value of `small`, `medium` or `large` is replaced by `P_SIZE` and passed to the NN layer so that we have less training samples. At the last layer of the model, the values will be restored. See [pizza2 example](#pizza2-bot-example) for more details.
`IMPORTANT!` There must be one group infered by the regular expression(!)

# Prompt label
Prompt is a powerful tool of ___ToTh___ mechanism to control passing information from one inference layer to another. It could be a simple text response corresponding to user query or a ___template which uses collected slot and their values___ to build next 'utterance' for next layer in the pipeline, __IF desired__. Must reiterate this point. Very first inference layer gets user query. The output is either updated utterance or a prompt, which becomes an input to next layer and so on.
```
utterance => 
    Layer1 => 
        updated utterance OR prompt => 
            Layer2 => ... 
                final Layer => prompt
```
__Note! If layer produces a prompt, it is used as an input for the next layer, unless of course layer is final. In that case prompt is what is presented to user as a response to user query.__
Example:
```
Utterance: Take me to Seattle => 
    [Address Layer] => 
        Utterance: Take me to P_PLACE => 
            [Intent layer] => 
                prompt:Sure, I will nagivate you to {t_dest}
                {
                    't_intent':NAVIGATE
                    't_dest':Seattle
                    't_prompt':Sure, I will navigate you to Seattle
                }
```
The values in the template are controlled by prompt's prefixes as described below:

## Prefix __"#"__
Implies using label's ___name___ in the ___most recent inference___. ___NOTE: if value is absent it will be replaced with 'None'___
```
Example: t_name value is in the last inference, t_age is absent
.prompt
    RESULT: {#t_name} {#t_age}
    # The value of RESULT: t_name None
```

## Prefix __"?#"__  
Implies using label's ___name___ in the ___most recent inference___. ___NOTE: if value is absent it will be skipped from the prompt___
```
Example:  t_name value is in the last inference, t_age is absent
.prompt
    RESULT: {?#t_name} {?#t_age}
    # The value of RESULT: t_name 
```

## Prefix __"$"__  
Implies using label's ___name___ in ___whole inference history___. The approach can be used as an input for dialog tracking layers. ___NOTE: if value is absent it will be replaced with 'None'___
```
Example: t_name value is in all whole history, t_age is absent
.prompt
    RESULT: {$t_name} {$t_age}
    # The value of RESULT: t_name None
```

## Prefix __"?$"__  
Implies using label's ___name___ in ___whole inference history___. ___NOTE: if value is absent it will be skipped from the prompt___
```
Example: t_name value is in all whole history, t_age is absent
.prompt
    RESULT: {?$t_name} {?$t_age}
    # The value of RESULT: t_name 
```

## Prefix __"."__ 
Implies using label's ___value___ in the ___most recent inference___. ___NOTE: if value is absent it will be replaced with 'None'___
```
Example: t_name = John is in the last inference. 
.prompt
    GREETING: Hello {.t_name} => Hello John
```

## Prefix __"?."__  
Implies using label's ___value___ in the ___most recent inference___. ___NOTE: if value is absent it will be skipped from the prompt___
```
Example: t_name is absent in the last inference. 
.prompt
    GREETING: Hello {?.t_name} => Hello
```

## Empty label prefix 
Implies using label's ___values___ in ___whole inference history___. ___NOTE: if value is absent it will be replaced with 'None'___
```
Example: t_kind values are in whole inference history, t_kind = BBQ and t_kind = meat
.prompt
    ORDER_PIZZA: Ok, I will place an order of {t_kind} pizza for you => 
    => Ok, I will place an order of BBQ, meat pizza for you
```

## Prefix __"?"__  
Implies using label's ___values___ in ___whole inference history___. ___NOTE: if value is absent it will be skipped from the prompt___
```
Example: t_name is absent in inference history
.prompt
    GREETING: Hello {?t_name} => Hello
```

## Prompt label value access by index  
While building a prompt, the label value can be accessed by index in the inference history, like so: `{t_utt-1}`. Index `-1` refers value of the label `t_utt` of in the previous inference. 
If previous inference is not available, `None` value is used in the prompt. If you want the value to be omitted in such case, use `{?t_utt-1}`.

```
Example: 
.train
    ASKING_AGE: how old are you
    R~RESP_YES: ASKING_AGE (yes|sure|of course)
    R~RESP_NO: ASKING_AGE (no|nope|don't care)
.prompt
    ASKING_AGE: I don't know answer to the question, would you like to forward it to my parents?
    R~RESP_YES: Sure. I am forwarding your question {t_utt-1} to my parents
    R~RESP_NO: Ok, no problem.
```
Side note: this particular example relies on `flag` toth to be enabled

# PIZZA2 BOT Example
Let's consider PIZZA2 BOT example. In this example we will not use scripting part utilizing only ___Neural Networks(NN)___ layers. By no means it should be considered completed, however it showcases many useful features of the platform. The project has 3 layers. 
## Layer 1 Slots
Layer 1 is named "slots" is dedicated to isolate types of the slots - __pizza kind__, __pizza toppings__,  __size__ and __delivery address__. Here is the configuration for the layer:
```json
{
    "layer_name":"slots",
    "data_files":[ "base.h","slots.txt" ],
    "bi_lstm":true,
    "toth":true
}
```
It contains 2 files - ___base.h___ with useful macros, ___slots.txt___ is an actual training file. 
Let's discuss 'bi_lstm' parameter.
```json
"bi_lstm":true
```
Consider sentence: "I would like cheese on top". It is clear that 'cheese' refers to the toppings not the pizza type. We get it only when we see 'on top' which comes at the end of the sentence. ___bi_lstm___ tells framework to 'read' utterances not only ___left to right___ but also ___right to left___ to get this information.

```"toth":true``` will be discussed later 

__slots.txt__ file:
```
.regex
    // Replace and leave it as such
    &and:\b(?:as well as|and also)\b
    // Replace, but finally resolve to actual value
    P_SIZE: (?:@small)
.train
    // The goal is to isolate slot types(!) and replace them by the type name, so next layer - has
    // less samples to be trained with
    (ORDER_PIZZA|) @kind{&P_KIND}
    (ORDER_PIZZA|) @toppings{&P_TOPPINGS} on top
    (ORDER_PIZZA|) @i @want (P_SIZE|) @kind{&P_KIND} @pizza (with|)
    (ORDER_PIZZA|) @i @want @kind{&P_KIND} @and @kind{&P_KIND} @pizza (with|)
    (ORDER_PIZZA|) @i @want @extra @toppings{&P_TOPPINGS} on top
    (ORDER_PIZZA|) @i @want @extra @toppings{&P_TOPPINGS} @and @extra @toppings{&P_TOPPINGS} on top
    (ORDER_PIZZA|) @i @want @pizza with @extra @toppings{&P_TOPPINGS}
    (ORDER_PIZZA|) on top @i @want @extra @toppings{&P_TOPPINGS}
    (ORDER_PIZZA|) add (topping|toppings) @extra @toppings{&P_TOPPINGS}
    (ORDER_PIZZA|) add @toppings{&P_TOPPINGS} on top
    (ORDER_PIZZA|) (my|@the) address is @address{&P_ADDRESS}
    (ORDER_PIZZA|) @i live in @address{&P_ADDRESS}
```
It is not always makes sense to use trainable models in all layers. Sometimes it is sufficient to use direct replacement mechanism like regular expressions. __You can, but you don't have to.__
Developers of knowledge domains are faced with the challenge to come up with as many variations of utterances as possible, so the system can understand all users - the ways they talk. From one side - we want to have lots of utterances to achieve that, but on the other hand it leads to longer training times.
```
.define
    @and: and|also|as well as
.train
    I would like ham @and extra cheese on top 
```
In the example above we would have 3 utterances instead of one because we have 3 variants for ```and```
Lets review regex section.
```    
.define 
    @small: small|medium|large
.regex
    // Prefix & is to indicate simple replacement
    // Ex utterance:  
    // 'I want bbq pizza as well as hawaiian' => 'I want bbq pizza and hawaiian'
    &and: (?:as well as|and also)

    // Lookup label replacement
    // Replace all values of @small definition by P_SIZE.
    // At the end of inference it will be replaced by its origial value.
    // P_SIZE will be used for training instead of all values of @small
    P_SIZE: (?:@small)
```
```&and:(as well as|and also)``` == to replace ```as well as``` and ```and also``` with ```and```. Prefix '&' tells that no need to resolve ```and``` to actual values it replaces in the final inference.
```P_SIZE:@small```  == to replace ```small```, ```medium``` or ```large``` with the type  ```P_SIZE```, which must be resolved to its value in the final inference result. 
___NOTE!___ Regex section is used for both - __training__ and __prediction__ modes.
___NOTE!___ Be careful if your knowledge domain contains names of __movies__, __places__, __songs__ etc. In this case it could backfire at you, because you don't want to modify those names. Consider creation of separate layers that would isolate such names into types like __P_MOVIE_NAME__, __P_SONG_NAME__, etc. so next layer that supposed to infere user intents would not deal with them.
__base.h__ file:
```
.define
    @i: i|we
    @i_want: @i @want
    @pizza: pizza
    @please: please|kindly
    @want: want|need|would like
    @and: and|and also|as well as
    @small: small|large|medium
    @kind: pepperoni|meat|Hawaiian|BBQ|meat|cheese
    @toppings: ham|cheese|tomato|meat|cheese
    @address: seattle|vancouver
    @extra: extra|
    @the: the|a|
    @yes: yes|sure|go ahead|you bet|sure why not
    @no: no|no way|nope|(@i|) changed my mind
```

Original utterance transformation with "SLOTS" layer:
```
I would like to place an order for small pepperoni with extra cheese and ham on top
=>
I would like to place an order for P_SIZE P_KIND with extra P_TOPPINGS and P_TOPPINGS on top
```
Latter is an input utterance to next layer called 'Pizza'

## Layer 2 Pizza

Config for this layer:
```json
{
    "layer_name":"pizza",
    "data_files":["base.h","pizza.txt"],
    "bi_lstm":true,
    "toth":true
}
```

__pizza.txt__ file:
```
.train
    ORDER_PIZZA: @i @want some @pizza @please
    ORDER_PIZZA: @pizza (@please|)
    ORDER_PIZZA: ASK_SIZE P_SIZE{t_size}
    ORDER_PIZZA: ASK_KIND P_KIND{t_kind}
    ORDER_PIZZA: ASK_KIND P_KIND{t_kind} and P_KIND{t_kind}
    ORDER_PIZZA: ASK_TOPPINGS with P_TOPPINGS{t_toppings}
    ORDER_PIZZA: ASK_TOPPINGS with P_TOPPINGS{t_toppings} and P_TOPPINGS{t_toppings}
    ORDER_PIZZA: ASK_TOPPINGS P_TOPPINGS{t_toppings} on top
    ORDER_PIZZA: ASK_TOPPINGS P_TOPPINGS{t_toppings} and P_TOPPINGS{t_toppings} on top
    ORDER_PIZZA: ASK_ADDRESS P_ADDRESS{t_address}
    ORDER_PIZZA: ASK_ADDRESS @i live in P_ADDRESS{t_address}
    R~ORDER_PIZZA_YES: ASK_TO_CONFIRM @yes
    R~ORDER_PIZZA_NO: ASK_TO_CONFIRM @no
.prompt
    // Generate Prompt that contains only one(!) missing slot to train next dialog layer
    // With the prompt definition below one of:
    //   if t_kind is missing
    //   if t_size is missing
    //   if t_toppings is missing
    //   if t_address is missing
    //   if none is missing
    // will be passed to the next layer, which must be trained like this:
    // .train
    //   ASK_KIND: if t_kind is missing
    // See bot.txt file.
    ORDER_PIZZA: if {$!t_kind|t_size|t_toppings|t_address|none} is missing

    // NOTE! Prefix R~(==return) is an instruction to collect all slots values and clean up
    // the inference history, thus to forget what user said before.
    R~ORDER_PIZZA_YES: Thank you for you order :)
    R~ORDER_PIZZA_NO: Sure, may be next time
```
Now time to discuss:
```
"toth":true
```
It tells that the layer wants to receive ___last intent___ as a prefix to the input utterance. This is the essence of __ToTh__ mechanism to communicate contextual information to make inferences more accurate. __NOTE!__ Intents can be generated by any layer in the stack and be passed to the next layer with ```toth``` set to ```true```. Otherwise, current utterance or prompt value is passed to the next layer unchanged. Consider the following training utterance:
```
.train
    ORDER_PIZZA: ASK_TOPPINGS I want pizza with P_TOPPINGS{t_toppings}
```    
It reads like this: when user is prompted to provide pizza toppings(previous intent was ___ASK_TOPPINGS___) and user response is 'I want pizza with cheese', produce ___ORDER_PIZZA___ intent and assign ___t_toppings___ with its value. ```t_toppings = cheese```

Layer 'Pizza' should contain as many utterances as possible to understand any user and the way they talk! The layer collects all slots and their values. 
Now, what is next? Next - is to figure out which question we need to ask. To do so we need to generate prompts, not utterances, because next layer inference is based on the fact which slots we have already collected. This information is stored in the inference history, which is what user said before. See the comments in prompt section above.
```
.prompt
    ORDER_PIZZA: if {$!t_kind|t_size|t_toppings|t_address|none} is missing
```
```{$!t_kind|t_size|t_toppings|t_address|none}``` means look through all inference history and put __slot names__(prefix __'$'__) which are __NOT__ present in the inference history(prefix __'!'__). Last value in the statement is dummy slot name 'None'. It is used for readability purpose only as well as 'if' and 'is missing'. So the prompt's template could just look like this:
```
.prompt
    ORDER_PIZZA: {$!t_kind|t_size|t_toppings|t_address|none}
```
This way we build prompts providing sufficient information to the next layer to decide - what to ask next. 
Layer 'Pizza' generates prompts => utterances for next layer:
```
if t_size is missing
if t_kind is missing
if t_toppings is missing
if t_address is missing
```
Next layer is called 'Bot'.

## Layer 3 Bot
Configuration:
```json
    {
        "layer_name":"bot",
        "data_files":"bot.txt"
    }
```
__bot.txt__ training file is very simple and contains very few 'utterances', which are, in fact, prompts generated by previous layer.
```
.train
    ASK_KIND: if t_kind is missing
    ASK_SIZE: if t_size is missing
    ASK_TOPPINGS: if t_toppings is missing
    ASK_ADDRESS: if t_address is missing
    ASK_TO_CONFIRM: if None is missing
.prompt
    ASK_KIND: What kind of pizza would you like. For example, Hawaiian, BBQ, etc.?
    ASK_SIZE: Small, medium or large?
    ASK_TOPPINGS: What do you want on top. For example: tomato, ham, cheese, etc.?
    ASK_ADDRESS: What is delivery address?
    ASK_TO_CONFIRM: Your order is {?t_cnt} {t_size} {t_kind} pizza with {t_toppings} to \
                     be delivered to {t_address}. Would you like to go ahead with the order?
```
The training set for 'Bot' layer is self-explanatory. Generate ___ASK_KIND___ prompt to user if ___t_kind___ slot is missing and so on. Valid question at this point is: Do I need to create training layer for such simple task? The answer is NO. Alternatively, you can use [.gate](#gate-section-script) section described before to 'script' the same logic, thus skipping training altogether for this type of inference.

## Pizza project Final Inference
Let's review utterance transformation going though all layers of the 'Pizza2' project:
```
// 'Slot' layer
I would like to place an order for small pepperoni with extra cheese and ham on top
where P_SIZE = small, P_KIND = pepperoni, P_TOPPINGS = cheese P_TOPPINGS = ham
=>
// 'Pizza' layer
I would like to place an order for P_SIZE P_KIND with extra P_TOPPINGS and P_TOPPINGS on top
where t_size = small, t_kind = pepperoni, t_toppings = cheese t_toppings = ham
=>
// 'Bot' layer
if t_address is missing
=>
// Prompt to user
What is the delivery address?
```

I hope it is clear why the 1st question is 'What is the delivery address'. It is because user already provided ___t_kind___, ___t_toppings___ and ___t_size___ in the original sentence.

# Inference history
This information is useful to understand platform operation under the hood. Inference history could be simply described as the "things user said before". All inferences are collected in the ```history``` or ```stack```. Those terms will be used interchangeably. The inference history contains:
* Layer's input utterance with predefined slot name ```t_utt```
* Layer's intent with predefined slot name ```t_intent```, if any
* Layer's infered ```slots``` and their ```values```, if any
* Layer's prompt with predefined slot name ```t_prompt```, if any

# How to control inference history

At some point we need to collect all slots values in the stack to build an aggregative inference (pizza order), or may be forget whole inference, because it is self-contained and there is no need to remember it, or go one or more steps back in history when user says "What?" or "Could you repeat it?". Or what if user changed their mind and wants to change the value of a slot? All of above are pieces of __ToTh__ technology. It is done via intent prefixes:
* ## Intent Prefixes
```
<no prefix> - Normal intent. The intent and slots values to be collected in the history
R~ - Return all collected slots values in the inference history and clean the history. "Return" command.
F~ - Do not remember this particular inference in the history - "Infere and forget" command.
P~ - One step back command. 'Can you repeat it please?'
B~ - Two steps back command. 'What did you say before that?'
C~ - Change value of a slot. "Change" command.
X~ - Clean previous inference history and do not save current inference in it.
I~ - Clean previous inference history and save current inference in it. 'Tertis' game effect.
?? - We are open to discuss any other prefixes to control the history.
```
* ## `Empty` prefix
Intent without prefix with infered slots and their values are saved in the inference history.
`ORDER_PIZZA: @i @want some @pizza @please`
where
`t_intent = ORDER_PIZZA` will be kelp in stack until `R~` or `X~` session-based conversation intent comes along to erase it.

* ## `R~` prefix. Return command
In 'Pizza' layer we have:
```
.train
    R~ORDER_PIZZA_YES: ASK_TO_CONFIRM @yes
    R~ORDER_PIZZA_NO: ASK_TO_CONFIRM @no
.prompt:
    R~ORDER_PIZZA_YES: Thank you for you order :)
    R~ORDER_PIZZA_NO: Sure, may be next time
```
Intents with ```'R~'``` prefix tell the framework to collect all slots and their values from history and return them to user as a inference in json format. After that inference history will be erased.
```json
{
    "t_size":"small", 
    "t_kind":"pepperoni", 
    "t_toppings": ["cheese", "ham"]
}
```
* ## `F~` prefix. Infere and Forget command
The prefix is used to prevent saving the inference in the history. For instance: `What time is it?` This is, most likely, self-contained statement and depending on the domain there may be no need to keep it in the history. So, the resulting inference will be returned, and it will not be remembered in the stack.
```json
{
    "t_intent":"GET_TIME",
    "t_prompt":"It is 1:38PM"
}
```
This is actually tricky example. [`zCymatix`](http://www.zcymatix.com) platform does not act on user requests. It only inferes the intents and slots and follows the conversation flows. `t_prompt`'s time value above must be provided by the client application. The framework returns the prompt template from the training set: `"It is {t_time}"`, so user application should replace `t_time` with its value.

* ## `P~` prefix. One step back command
The prefix tells the framework to take last/previous inference in the history and return it. It is useful for cases when user asks, 'What did you say?' 'Repeat please?'.
```
Bot>What type of pizza would you like?
User>What?
Bot>What type of pizza would you like?
```

Please note, if previous intent was either R~ or I~ or X~, there will be no history records available. To have access  previous prompt always - consider training sample:
```
.train
    F~REPEAT:what|what did you say|come again|repeat (please|)|pardon me
.prompt:
    F~REPEAT: *
```
Star `*` symbol tells to grab last value of the `t_prompt` in the history. 

* ## `B~` prefix. Two steps back command
The prefix tells the framework to take `top-1` inference from the history. It is useful for cases when user asks 'What did you say BEFORE that?'

* ## `C~` prefix. Change slot value command
The prefix tells the framework to change the value of the slot in the history
`User> Take me to Seattle`

```json
{
    "t_intent":"NAVIGATE",
    "t_dest":"Seattle"
}
```
```User> No, change it to Vancouver```
```json
{
    "t_intent":"C~NAVIGATE",
    "t_dest":"Vancouver"
}
```
The `t_dest` slot value `Seattle` will be replaced with `Vancouver` directly in the history.

* ## `X~` prefix. Clean previous history command
The prefix should be used if current inference suggests that the previous history must not be kept any longer. ___Current inference is not saved in the history.___
```
.train
    CONFIRMATION:Would you like to proceed with your order?
    R~PLACE_ORDER: CONFIRMATION yes
    X~CANCEL_ORDER: CONFIRMATION no
.prompt
    USER_CONFUSED: I'm sorry
    // Collect all slots values in the collected history of the dialog and return to user
    R~PLACE_ORDER:Thank you for your order. Your order is {t_param1} {t_param2}...
    
    // Wipe out the history
    X~CANCEL_ORDER: Sure, I am canceling your order
```
Note, current inference slots, if any, will be returned to user in the inference. 
This prefix should be used for self-contained inference, meaning it has all information needed to make confident conclusion, plus no further inference should rely on it.

* ## `I~` prefix. Clean previous history and restart command
The prefix should be used if current inference suggests that the previous history must not be kept any longer. ___Current inference is saved in the history.___ Think of this command's effect as 'Tertis' effect.

# Idioms interpretation. Intent prefix `~`

To support truly natural language understanding, we have a mechanism to interpret idioms and enable `slot filling` with semantic values ***not found in the original utterance***. Here is an example:
```
.train
    ~NAV: take me to a place where i can have a nice meal
    ~NAV_01: I am starving, walk me to a closest place where I can have a nice meal
.prompt:
    ~NAV: t_target=restaurant;t_prompt=Sure, I will take you to a {t_target};t_transport=car
    ~NAV_01: t_target=restaurant;t_prompt=Sure, I will take you to a {t_target};t_transport=walk
```
Prefix `~` must be first one in the intent. It __can__ be used in combination with previously described prefixes. For example `~I~NAV`. It means that prompt contains additional slots. `I~` tells framework to restart collecting the history, while previous history will be lost. See [above](#i-prefix-clean-previous-history-and-restart-command).
Please also note the separator `;` between slots-value pairs. 

# Remove slot value from inference history. `$del` command
Lets say you want to delete a slot value from the history. Consider the example:
```
.train
    C~PARKING_HS_MS: I want to park my car for 2{t_time_hour} hours and 15{t_time_min} minutes
    ~C_PARKING_HS: No, I want to park for 3{t_time_hour} hours
    ~C_PARKING_MS: No, I just want to be here for 5{t_time_min} minutes
.prompt:
    C~PARKING_HS_MS: Sure. {t_time_hour} hours and {t_time_min} minutes timer starts now.
    ~C_PARKING_HS: t_time_min = $del; t_prompt = Sure, {t_time_hour} hours timer start now.
    ~C_PARKING_MS: t_time_hour = $del; t_prompt = Sure, {t_time_min} minutes timer start now.
```
In this example user can change his/her mind as many time as desired, and slot values will be updated in history accordingly. Implicetly, ~C_PARKING_HS means that previous t_time_hour and t_time_min should be erased. We are explicitly chaning the value of t_time_hour and implicitly t_time_min.

# Indirect references `it` or `there`

Consider the training samples using `P_PLACE` slot type:
```
.train
    INT_SHOW_PLACE: show me P_PLACE{t_place} (on the map|)
    INT_SHOW_PLACE: where is P_PLACE{t_place}
    INT_SHOW_PLACE: I am looking for P_PLACE{t_place}
    INT_DISTANCE_INFO: how far is P_PLACE{t_dest}
    INT_NAVIGATE/t_place/t_dest:take me there
```
First four training samples rely on explicit place name we want to see or check the distance to. Last one has an intent and a list of slot names to look in the history to choose to resolve `it`:
`INT_NAVIGATE/t_place/t_dest:take me there`
Why list of slots? The intuition is this - search for either `t_place` or `t_dest` in that order in the inference history and put its value to substitute `there`.
![Conventional "it"/"there" reolution](http://www.zcymatix.com/img/session_memory_01.png "Conventional it/there reolution")
As you can see, you have to collect inferences in client application and resolve the value of 'it'. With zCymatix platform all done automatically on backend side.

![zCymatix "it"/"there" reolution](http://www.zcymatix.com/img/session_memory_02.png "zCymatix it/there reolution")

# `.gate2` section
Its purpose is to fullfil user query. It contains python script executed AFTER inference is made, that is intent and slot values are known. Important to remember the scope of available data. Object `o` as a Namespace object containing all inferences data from the collected history. Object `c` same as object `o`, but containing only current inference data. IMPORTANT!

__`o.t_intent`__ - has a string value of the current intent.
__`o.t_prev_intent`__ - has a string value of previous intent.

All other values of the slots are lists(!). Example: `o.t_target = ['Seattle', 'Los Angeles'].`
So if you want to access the last value, do it like this: 
`o.t_target[ -1 ]`

# `.script` section
Its purpose to define global python methods and data within one layer. These methods are accessible from `.gate` and `.gate2` sections in runtime mode. This is sandboxed environment. Builtin set of function is limited to:
```
'hasattr', 'isinstance', 'len', 'vars', 'min', 'max', 'int', 'long', 'float', 'complex', 'list', 
'dict', 'str', 'unicode', 'tuple', 'set', 'False', 'True', 'None', 'oct', 'bin', 'bool', 
'to_json', 'to_namespace', 'to_dict', 'read', 'write'
```
Most of the functions are standard builtin. Custom methods and data exposed by plaform:
__`to_json( obj )`__ - to convert an object to a json string.
__`to_namespace( obj )`__ - to convert dict to Namespace object
__`read( session_id, file_name, data_string, shared = True )`__ - read from __shared__ or __private__ data storage. Private data storage is associated with an instance of the application.
__`write( session_id, file_name, data_string, shared = True )`__ - write to __shared__ or __private__ data storage
__`z_sid`__ - is the __local__ variable, `token/session_id`, that must be passed with `read` and `write` functions calls.
```
Example:
        write( z_sid, 'my_file.json', to_json( my_app_obj ), shared = True )
```
Data structures declared in this sections should be treated as `shared data` of the application, which can be saved/retrived to/from persisant memory via available methods: `read` and `write`

# `.vars` section
Its purpose to allocate variables declared in local context of python script.

# `.slist` section
The purpose is the same as `.list` section. In addition, global list variable in python environment is created. Example:
```
.slist = allergy_type
    Eggs
    Milk
    Peanuts
    Tree nuts
    Fish
```
as a result global variable __`g_allergy_type`__ is created in global context of python script making it visible from `.gate`, `.gate2` and `.script` sections:
```
g_allery_type = [
    'Eggs',
    'Milk',
    'Peanuts',
    'Tree nuts',
    'Fish'
]

```

# Events, States, Sensors Information Embedding
Contextual information embedding into utterances and prompts is the foundation of ToTh technology.
Language operates by `symbols`. All words are the symbols, which are inherently indirect references to things that we can experience and understand. Keeping this in mind, we can `encode` any `contextual information` such as `events` or `states` or even `sensors information` using symbols, which we can use in the `training set` expanding our samples with those symbols. 
Let's review an example:
```
I have my phone that controls multi room home music system via WiFi and 
I say: "Play Def Leppard". It seems that it is self-contained and clear statement 
telling that I want to play music:) But there is a problem - where to play it? 
In which room? I did not say it explicitly. 
```
Going step by step, phone gets my intent:
```json
{
    "t_intent":"PLAY_MUSIC",
    "t_artist":"Def Leppard"
}
```
now it needs to decide where to play the music or should we ask user? Sure, we may ask, but what if we take the challenge of figuring out automatically. Assuming that we have speaker's `proximity sensor data` available on the phone - there are two ways to solve this. I said - `it needs to decide` meaning that the  __`phone`__ having the intent and proximity info to the closest speaker(let's say it is `living room`) starts playing music there. Problem solved! Yes... but. This is `not 'good'` solution and here is why: 
1. The decision is made by client device 
2. The decision is based on hardcoded logic

With [`zCymatix`](http://www.zcymatix.com) platform it is possible to encode and use sensor's real-time data "when I am in living" room as symbol `__living_room__`:
```
.train
    PLAY_MUSIC: __living_room__{t_location} play P_ARTIST{t_artist}
```
and the inference would be:
```json
{
    "t_intent":"PLAY_MUSIC",
    "t_artist":"Def Leppard",
    "t_location":"__living_room__"
}
```
So what? Here the advantages:
1. Client device `did NOT make the decision` where to play the music, but merely provided encoded sensor information or in this case it is a state - "where am I at the moment" == `living room`.
2. This is `not hardcoded logic`, because the model which infered the intent and slots `resides on the backend` and can be trained or re-trained at any time, so there is no need to "install new version" of the application just because of some changes in logic.

    __NOTE!__ You need to train your models with encoded events/states and modify user utterance in prediction mode.

This makes client application __cleaner, focusing on its task__ and `backend` takes care of the session, its history and the context. In our example my phone would only __`act`__ on the intent by playing `Def Leppard` in `living room`.

# Multiple language support
In order to support other languages besides English, all you have to do is to add 'lang' field (ISO 639-1 and ISO alpha-2) into any of the layers of you project configurationISO:
```
[
    {
        "data_files":<...>
        "lang":"es-mx"
    }
]
```

# Comments in training files
Comment must start from a new line and be prefixed with either `#` or `//`

# Long lines continuation
Use backslash `\` to break long line. NOTE, white spaces on next line are ignored.

# Unknown word marker
__`<UNK>`__ is used in training sets to mark words that are not in the vocabulary of the training set.

# Placement slot inference
`Placement slot inference` is used when we don't know all the values of the slot type. That is the type of the slot is not complete or unknown. Training set must include utterances that create sufficient, high probability context to be sure that unknown word is something that we are looking for at some particular place in the utterance. We will not be discussing here whether this is good or bad way leaving it to developers.
Example:
```
.define
    @pizza_kind: BBQ chicken|Hawaiian|<UNK>|<UNK> <UNK>
.train
    ORDER_PIZZA:I would like to order @pizza_kind{t_kind}
```
User> I want to order blah pizza
```json
{
    "t_intent":"ORDER_PIZZA",
    "t_kind":"blah"
}
```
# Expert systems support
The platform support a layer type, which goal is not related to NLU. You may decide to collect slots values and feed them to expert layer to infer additional information. Example: Doctor patient use case. Patient comes to a doctor and the assistent app asks a set of questions. Patient's answers are collected as a slot values and as a prompt passed to expert system layer to make a diagnosys.

# Recommendations, tips and tricks
- Before starting creating a `project` or `knowledge domain` important to remember:
There are two ways to describe something. __`What it IS`__ and __`what it IS NOT`__. Remember __Hello__ example in this tutorial? Does not matter what you say, it will `always` produce `GREETING` intent! Why? Because the example does not have any alternative samples to tell apart 'Hello World' from any other things user may say. Consider the example:
    ```
    .train
        INT_FLIGHT_INFO:show me flights to Seattle{t_dest}
        don't show me flights to Seattle
    ```
    Second sample does not have an intent or slots to infere. This means that this statement will be __`just ignored`__ and no inference will be made, __if we wish__. So, the training process will teach the model to remember the difference between these samples.

- Do not use intent names that can be confused for words. I recommend using something like `INT_DO_SOMETHING`. 

- Name intents describing "what to do next", rather then what already happened. While following train of though of the dialog, it is much easier.

- Do not use slot types names that can be confused for words. I recommend using something like `PIZZA_KIND` or similar

- Slot name template is __`t_<name>`__ keeping in mind that __`t_intent`__, __`t_prev_intent`__, __`t_utt`__ and __`t_prompt`__ are reserved.

- Slot inference. Consider two training sets:
 `Single layer project` which attempts not to use slot types isolation step:
    ```
        .train
            INT_NAVIGATE:take me to (Los Angeles){t_dest} and to (New York){t_dest}
    ```
    with inference for the sample above:
    ```json
        {
            "t_intent":"INT_NAVIGATE",
            "t_dest":["Los", "Angeles", "New", "York"]
        }
    ```
    vs `Two layers project` which uses type definition layer and a separate slot value inference layer:
    ```
        # Layer 1 - type training
        .train 
            take me to (Los Angeles){&P_PLACE} and to (New York){&P_PLACE}
    ```
    ```
        # Layer 2 - intents and slots inference
        .train
            INT_NAVIGATE:take me to P_PLACE{t_dest} and to P_PLACE{t_dest}
    ```
    with inference for the sample:
    ```json
        {
            "t_intent":"INT_NAVIGATE",
            "t_dest":["Los Angeles", "New York"]
        }
    ```
    You can see the advantage of second approach, where names are correctly isolated.
    
- [`zCymatix`](http://www.zcymatix.com) platform __does not__ provide `voice recognition services`. For web applications we recommend using [`Google service`](https://cloud.google.com/speech/), since it is superior of other products available on the market today. See also available solutions for [Android](https://developer.android.com/reference/android/speech/SpeechRecognizer.html) and [iOS](https://developer.apple.com/documentation/speech).

# Optional configuration parameters

__NOTE__! If the meaning of the parameters are not clear, keep the defaults or drop me a note. 

- Depth of the model. By default, `1`
    ```
    "n_lstm":1
    ```

- Bidirectional LSTM models. By default, `true`.  
    ```
    "bi_lstm":true
    ```
    Example :
    ```
    I want ABC{t_pizza_type} pizza
    I want ABC{t_pizza_topping} on top
    ```
    Unless `bi_lstm` is enabled, model will not be able to tell that in first case `ABC` refers to a `pizza type` and in second, to `pizza toppings`. It is sort of look ahead. There is an alternative though - enable convolutional layer.

- Confidence level. By default, `0.9` - 90%. Level to consider inference reliable. If infered intent has lower probability, it will be replaced with `error_intent` if it is set.
    ```
    "confidence":0.9
    ```
- Learning rate value. By default, `0.01`. 
    ```
    "lr":0.01
    ```
- Minimum Learning rate value. By default, `0.001`. 
    ```
    "lr_min":0.001
    ```
- Learning rate increase factor value. By default, `0.01`. 
    ```
    "lr_increase_factor":0.01
    ```
- Learning rate reduce factor value. By default, `-0.2`. 
    ```
    "lr_reduce_factor":-0.2
    ```
- Number of training epoches before reducing learning rate by `lr_reduce_factor`. By default, `3`. 
    ```
    "not_converge_max_epochs":3
    ```
- To enable passing previous intent in the history as utterance prefix. By default, it is `true`
    ```
    "toth":false
    ```
- Toth fallback mode . By default, it is `true`. If true, and the inference probability of the intent is lower than confidence level, `toth` mode will be turned off for this inference.
    ```
    "toth_fallback_mode":true
    ```
- A layer can be optionally included into the inference pipeline. When `accept_r_intents_only` is True , only  `R~` prefixed intent produced by one of the __previous layers__ will enable this layer to be included in the inference. By default, is it `False`.  This is useful for expert system layers, where it should not be a part of collecting slots values, but rather when we need to process the whole collection of the slots.
    ```
    "accept_r_intents_only":true
    ```
- It is possible to change `vendor` name since you are the `vendor` of this project or knowledge domain
    ```
    "vendor":"zCymatix"
    ```
- To change version number of the training set define `version` parameter.
    ```
    "version":"0000.0000.0000"
    ```
- To include vendor name into the inferences. By default, it is `False`
    ```
    "include_vendor":false
    ```
- To include version number into the inferences. By default, it is `False`
    ```
    "include_version":false
    ```
- To include layer name into the inferences. By default, it is `False`
    ```
    "include_layer_name":false
    ```
- To include intents into the inferences. By default, it is `True`
    ```
    "include_intents":true
    ```
- To include prompt into the inferences. By default, it is `True`
    ```
    "include_prompts":true
    ```
- To include utterance into the inferences. By default, it is `True`
    ```
    "include_utt":true
    ```
- To keep last intent only in the inferences. By default, it is `True`
    ```
    "keep_last_intent":true
    ```
- To keep last prompt only in the inferences. By default, it is `True`
    ```
    "keep_last_prompt":true
    ```
- To keep last utterance only in the inferences. By default, it is `True`
    ```
    "keep_last_utterance":true
    ```
- To convert the intent value to an utterance for the next layer in the inference pipeline. By default, it is `False`. 
    ```
    "intent_to_utterance":false
    ```
    This is quite useful feature. Example: We want to interpret user's loose answer that would be considered `yes` or `no`.
    ```
    .train
        INT_YES:I guess so|it is rather yes then no|...
    ```
    If the intent was `INT_YES` it will become an utterance for next layer(!) reducing training set of this layer to deal only with `INT_YES` or `INT_NO`
    Alternatively, prompt mechanism can be used to achieve the same result, however this feature flag saves additional typing. I will not suggest which one is better. It depends on the application.
    ```
    .train
        INT_YES:I guess so|it is rather yes then no|...
    .prompt
        // Utterance for the next layer will be the intent itself taken 
        // from the current inference
        INT_YES: {.t_intent}
    ```
    See [Prefix "."](#prefix--4)

# Advanced configuration parameters
__NOTE!__ If the meaning of the parameters are not clear, keep the defaults or drop me a note.
- To force backend to use GPUs for training. Default is CPU.
    ```
    "hw":"gpu"
    ```
- Accuracy metrics to be used for training. By default: `accuracy`, `loss` and `validation accuracy` are used.
    ```
    "accuracy_metrics":[ "acc", "loss", "val_acc" ]
    ```
- Accuracy metrics to stop training early. Defaults in the same order: `accuracy = 1.0`, `accuracy_loss = 0.01`, `validatoion_accuracy = 1.0`, `validation_loss = 0.01`
    ```
    "stop_accuracy_metrics":[ 1.0, 0.01, 1.0, 0.01 ]
    ```
- The training model by default, returns sequences of labels. However, in case when you have a layer which deals with only intents without any slots it makes sense to change it to disable the sequence, thus to return only final result. It leads to faster training times.
    ```
    "return_sequences":true
    ```
    Example:
    ```
    .train
        INT_YES: sure|yes|of course|I would say so|...
        INT_NO: no|nope|I don't think so|negative|no way|...
    ```

- Number of epochs to train. By default, it is `100000`
    ```
    "n_epochs":100000
    ```
- Embedding vector size. By default, it is `50`
    ```
    "emb_dimension":50
    ```
- Number of hidden units. By default, it is `100`
    ```
    "n_hidden":100
    ```
- Dropout coefficient for feature vector. By default, it is `0.1`
    ```
    "dropout_W":0.1
    ```
- Dropout coefficient for hidden units. By default, it is `0.1`
    ```
    "dropout_U":0.1
    ```
- Optimizer name. By default, `Adam`
    ```
    "optimizer":"Adam"
    ```
- List of optimizers and their parameters. Defaults are listed below.
    ```
    "optimizers":[
        'SGD(lr = 0.0001, decay = 0.000001, momentum = 0.9, nesterov = True)',
        'Adam(lr = 0.01, decay = 0.000001, beta_1 = 0.9, beta_2 = 0.999)',
        'Nadam(lr = 0.001, beta_1 = 0.9, beta_2 = 0.999, epsilon = 1e-08, schedule_decay = 0.000001)',
        'RMSprop(lr = 0.001, rho = 0.9, epsilon = 1e-08, decay = 0.0)',
        'Adagrad(lr = 0.01, epsilon = 1e-08, decay = 0.0)',
        'Adadelta(lr = 1.0, rho = 0.95, epsilon = 1e-08, decay = 0.0)',
        'Adamax(lr = 0.002, beta_1 = 0.9, beta_2 = 0.999, epsilon = 1e-08, decay = 0.0)'    
    ]
    ```
- Use convolutional layer. By default, `false`. See the description [here](https://keras.io/layers/convolutional/#conv1d)
    ```
    "conv":false
    ```
- Convolutional layer outputs. By default, `128`. See the description [here](https://keras.io/layers/convolutional/#conv1d)
    ```
    "conv_outputs":128
    ```    
- Convolutional layer kernel size. By default, `5`. See the description [here](https://keras.io/layers/convolutional/#conv1d)
    ```
    "conv_kernel_size ":128
    ```    
- Convolutional layer activation function. By default, `relu`. See the description [here](https://keras.io/layers/convolutional/#conv1d)
    ```
    "conv_activation ":"relu"
    ```    
- Convolutional layer padding method. By default, `same`. See the description [here](https://keras.io/layers/convolutional/#conv1d)
    ```
    "conv_padding ":"same"
    ```
- Dropout layer value. By default, `0.0`.
    ```
    "dropout_layer_value ":0.0
    ```
- Include signle words into training set. By default, `false`. If true, all single words are added to the training set without any labels.
    ```
    "include_single_words":false
    ```
- Include intent names into training set. By default, `false`. If true, all intents are added to the training set without any labels.
    ```
    "include_intent_words":false
    ```
- Error intent. By default, ``. If set, this is the intent to be used if inference probability did not reach confidence level.
    ```
    "error_intent":""
    ```
    
    
    
