# [zCymatix](http://www.zcymatix.com) Natural Language Understanding(NLU) Voice/text UI & Expert Systems Platform 
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
   * [Training time](#training-time)
   * [Use NLU service via REST API](#use-nlu-service-via-rest-api)
      * [Launch request](#launch-request)
      * [Deduction example](#deduction-example)
      * [List of response codes](#list-of-response-codes)
   * [Use Web interface for verification](#use-web-interface-for-verification)
   * [Using prompts](#using-prompts)
   * [Using macros](#using-macros)
   * [Using Slots (parameters)](#using-slots-parameters)
   * [Introduction to Layers](#introduction-to-layers)
   * [Dialogs](#dialogs)
      * [Loose Dialogs](#loose-dialogs)
         * [Prototype section](#prototype-section)
         * [Gates section (script)](#gates-section-script)
      * [Strict Dialogs](#strict-dialogs)
   * [Regex section](#regex-section)
      * [Irreversable replacement](#irreversable-replacement)
      * [Reversable replacement or lookup lables](#reversable-replacement-or-lookup-lables)
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
      * [Pizza project Final Deduction](#pizza-project-final-deduction)
   * [Deduction history](#deduction-history)
   * [How to control deduction history](#how-to-control-deduction-history)
      * [Intent Prefixes](#intent-prefixes)
      * [Empty prefix](#empty-prefix)
      * [R$ prefix. Return command](#r-prefix-return-command)
      * [F$ prefix. Deduce and Forget command](#f-prefix-deduce-and-forget-command)
      * [B$ prefix. Step back command](#b-prefix-step-back-command)
      * [C$ prefix. Change slot value command](#c-prefix-change-slot-value-command)
      * [X$ prefix. Reset command](#x-prefix-reset-command)
   * [Indirect references it or <code>there</code>](#indirect-references-it-or-there)
   * [Events, States, Sensors Information Embedding](#events-states-sensors-information-embedding)
   * [Comments in training files](#comments-in-training-files)
   * [Long lines continuation](#long-lines-continuation)
   * [Unkown word marker](#unkown-word-marker)
   * [Placement slot deduction](#placement-slot-deduction)
   * [Recommendations, tips and tricks](#recommendations-tips-and-tricks)
   * [Optional configuration parameters](#optional-configuration-parameters)
   * [Advanced configuration parameters](#advanced-configuration-parameters)


#### Machine learning NLU system designed for dialogues and expert systems. The platform utilizes proprietary Toth(Train Of Thought) technology for conversation flow tracking and supports many other features...
### ___"...Context IS everything ..."___
# Features Highlights
- ***`Train Of Thought technology`***
    * Literally maintains a train of thought of the conversation
- State of the Art ***`deduction pipeline`*** to efficiently resolve ambiguity
- Ability to create ***`1000s of utterances`*** in minutes
- ___`States, Events and Sensors Data Embedding`___ contextual support
- ___`Session based conversation instances`___  Context is maintained on the `backend` leaving client focusing only on the application itself
- `Regex` layer support. Yes, why would you need to use ML for simple things.? You may, but you don't have to
- Optional `scripting support`.
    * All layers of the pipeline are ML layers, however if desired, scripting can be used to make contextual changes.
- Idioms interpretation mechanism
    * "I would really want to grab a bite and then go back home" => ``` { 't_intent':'NAVIGATE', 't_stopover':'restaurant', 't_destination':'Home' } ```
- Lookup labels support
    * "I want BBQ chicken and new york pizza" => "I want PIZZA_KIND and PIZZA_KIND pizza" => ``` { 't_intent':'ORDER_PIZZA', 't_kind':['BBQ chicken', 'new york']```
- NLU tasks:
    - `Self-contained` deductions:
        * __"Play the latest from Def Leppard"__ =>  
            ``` { 't_intent':'PLAY_MUSIC', 't_artist':'Def Leppard', 't_attr':'latest' } ```
        * __"Show flights to Seattle"__ =>  ``` { 't_intent':'SHOW_FLIGHT, 't_destination':'Seattle' } ```
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
- ***Indirect*** subject referencing
    * Notion of ***`it/there`***
        * 'Where is Seattle'
        * 'Take me there'
- ***`Expert systems support`*** Result of the dialog could be fed into a layer to process conversation outcome.
    * This is not NLU specific feature which enables platform utilization in any field of knowledge
- Platform DOES NOT provide voice recognition servives

   ___So, Let's do it!___
# 'Hello Word' Example
* Create and enter **hello** folder. `Folder name is the name of the project.`
* Create **hello.json** file
```json
{ "data_files":"hello.txt" }
```
* Create **hello.txt** training file
```
.train
    GREETING:Hello World
```
***GREETING*** is the ***intent***, 'Hello world' is how you say it. You may ask what if the intent is not specified? Well - this means that utterance 'Hello World' will not have any associations. This is very important point to understand - you can describe things two ways a) by what ***it is*** and b) what ***it is not***. We will come to this later.
So, this is it. Literally, 3 lines of code get you there. The deduction of the phrase 'Hello World' will be 
```json
    {"t_intent":"GREETING"}
```
To get E2E how-to experience go to [zcymatix.com](http://www.zcymatix.com) and sign up. Press ***Sign In*** and then ***Sign Up***. 
***NOTE!*** Please use real e-mail address to be able to receive training completion notification with PROJECT ID. Otherwise you cannot use the service.
![Register](http://www.zcymatix.com/img/signup.png "Register")

After login, upload the project by choosing your project folder - ***hello***. Remember, __project name__ is the name of the __folder__
![Upload](http://www.zcymatix.com/img/upload_page.png "Upload")

When project is uploaded, you need to train it. Choose ***Training*** option and press launch.
![Launch](http://www.zcymatix.com/img/launch_project.png "Launch")

# Training time
Depending on project complexity it may take from few seconds to few hours to train it. When project training/building is finished you will receive e-mail notification with the ***PROJECT ID*** required for ***project launch*** REST request. 

# Use NLU service via REST API
## Launch request
This is initial handshake request.
***https://nlp2.zcymatix.com/?cmd=launch&project_id=f38360cd-08c5-482b-8c22-c2bc67194ab8***
Parameters: 
```json
    cmd = launch
    project_id = f38360cd-08c5-482b-8c22-c2bc67194ab8
```
NOTE! `f38360cd-08c5-482b-8c22-c2bc67194ab8` is fake project id
The response contains the dynamic ___session_id___, which must be used in the the following deduction requests. The response looks like this:
```json
{ "code":200, "msg":"2cb3b87d-e29c-4743-bab1-0fc5cb98db6d"}
```
Session ID in this example is:`2cb3b87d-e29c-4743-bab1-0fc5cb98db6d`


## Deduction example

***<https://nlp2.zcymatix.com/?cmd=deduce&session_id=2cb3b87d-e29c-4743-bab1-0fc5cb98db6d&query=Hello+World>***
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
    201 - Deduction is provided in msg field as a JSON string
    202 - Info is provided in msg field as a string
    102 - Project is loading
    101 - Authentication error
    100 - Invalid parameters
```

It may take few seconds for a project to be launched(if it was not before). If during this time client's deduction request comes to the backend, it will respond with the code `102`. ___Client must repeat the request___ until the deduction response comes back with the code `201`. 
        This is the 'worst' case scenario, because projects must be loaded in prediction mode for `production` use after training is finished, thus it should be always loaded.

    
# Use Web interface for verification

![Deduction](http://www.zcymatix.com/img/deduction_page.png "Deduction")

# Using `prompts` 

What if we want AI system to respond to user query? Let's use the 'Hello World' code:
```
.train
    GREETING: Hello World
.prompt
    GREETING = Hello my friend
    GREETING = Hello!
    GREETING = Hi!    
```
By adding section ***.prompt*** we can define user prompts: 
```
INTENT=<PROMPT VARIANT>
```
In the example above GREETING has three variants. They will be selected randomly in order to create more human like interaction. It reads like this - 'when user greets me reply this'. Prompt text may contain slots/parameters values. 
```
.prompts
    NAVIGATE: Ok, I am starting navigation to {t_destination} by {t_car}
```
Where ___t_destination___ and ___t_car___ are slots/parameters.
Prompts purpose is twofold 1. to be able to respond to user. 2. Prompt as a template with slot names to be passed to next layer in the deduction pipeline. This mechanism is used in `expert systems` layers.
The idea: You collect all the data from user in the form of slots and their values and then use prompt template to build the 'utterance' for the next model. 
```json
.prompts
    R$READY = {t_param1} {t_param2} {t_param3}...
```

# Using `macros`
Let's update ***hello.txt*** file a little. Add ***.define*** section. 
```json
.define
    @hi = Hello|hi
    @guys = guys|folks|World|

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

# Using `Slots` (parameters)
In the training set we can assign intent and mark/label words with slot names for each utterance.
Training file:
```json
.define
    @take = take|bring
    @me = me|us|them
.train
    NAVIGATE: @take @me to Seattle{t_destination} by car{t_transport}
.prompt
    NAVIGATE = Sure, I am starting navigation to {t_destination} by {t_transport}
```

The deduction will look like:
```json
{"t_intent":"NAVIGATE", "t_destination":"Seattle", "t_transport":"car"}
```
This way we deduce the meaning of the utterance.

# Introduction to Layers
[`zCymatix`](http://www.zcymatix.com) platform is using the concept of ***layers***. Each layer could be responsible for deduction of specific things. For example, in case of ordering pizza you may want to deduce ***pizza toppings*** and ***pizza kinds*** in separation of the training set that will be using them. Why? Because there maybe too many pizza kinds and toppings, meaning that final training data set will grow dramatically if we use each pizza kind and topping explicitly. Of course one can use [`placement slot deduction`](#placement-slot-deduction), but it is upto developer to decide which way to go. So, it is advisable to have a layer that would be replacing specific pizza kind and topping with something like ***PIZZA_KIND*** and ***PIZZA_TOPPING*** lookup labels. Layer after that, would use them instead of actual values. At the end of the deduction cycle they will be resolved to the actual values. The following example starts with more complex configuration file with two layer. Once you have more than one layer you have to name each of them:
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
I would like to place an order for a small BBQ chicken and large meat pizza
```
For simplicity sake, let's ignore pizza sizes deduction.

***kinds.txt***:
```
.train
    I would like to place an order for a small (BBQ chicken){&PIZZA_KIND} and \
    large meat{&PIZZA_KIND} pizza
```
*Intent is not present here, because the purpose of this utterance is to create `sufficient context` to isolate and extract pizza kind:*
***PIZZA_KIND = BBQ chicken***
***PIZZA_KIND = meat***

This is a mechanism to label multiple words with specific `lookup label` and using multiple instance of the label in a single utterance (***Amazon Lex does not allow that***). To explain further, lets take a look at the next layer and file 
***order_pizza.txt***:
```
.train
    ORDER_PIZZA: I would like to place an order for a small PIZZA_KIND{t_kind} and \
                 large PIZZA_KIND{t_kind} pizza
```
The intent ***ORDER_PIZZA*** present here, because the purpose of this layer is to get ***the intent and slots/parameters values*** that come with it.
***PIZZA_KIND{t_kind}*** marks both instances of the mentioned pizza kinds.
The resulting deduction after applying both layers will be:
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
    @pizza_kind = BBQ chicken|meat|Hawaiian|...
.train
    ORDER_PIZZA: i would like to place an order for small @pizza_kind{t_kind} and \
                 large @pizza_kind{t_kind} pizza
```
Of course you can! BUT, how many utterances will be produced? ***A LOT!!!*** Imagine if on top you have:
```
.define 
    @i = i|we|they 
    @order = (place|) order for|get|buy
    @small = small|large|medium|
```
```
ORDER_PIZZA: @i would like to @order @small @pizza_kind{t_kind} and \
             @pizza_kind{t_kind} pizza
```
So, this mechanism enables smaller context needed to train the layer to extract and label the pizza kinds. Look - do you need ***all*** words in the example utterance in layer "Pizza kinds"? Not really. So,I would put into training file something like this:
```
.define 
    @pizza_kind = BBQ chicken|meat|pepperoni|Hawaiian
.train
    @small @pizza_kind{&PIZZA_KIND} (and @pizza_kind{&PIZZA_KIND} pizza|)
```
So, having a context consisting only surrounding words is enough? You decide. But be careful though. ***False positives one of the biggest issues in NLU systems***, finding the balance between training time, number of utterances and sufficient context is not easy task to create ***high quality training set.*** [`zCymatix`](http://www.zcymatix.com) platform gives the tools to go either way.
# Dialogs
There are two types of dialogs supported by the platform ***Loose Dialogs*** and ***Strict dialogs***. And third one is the combination of these two.
## Loose Dialogs
This type of dialog assumes that AI system knows the set of slots/parameters to collect from user. `Presence of the slots values` is sufficient for the system to consider conversation complete. Example: ordering pizza. User can freely provide the information about the pizza without following script flow of the conversation:
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
In such conversation there is no strict sequence of questions to be ask. The conversation flow depends on already provided parameters and system would ask only those questions helping to get missing parameters. So, the conversation could go like this:
```
    User> I want small BBQ chicken with extra cheese and tomatoes on top and my address is ...
    Bot> Here is you order... Should I go ahead and place your order?
    User> Yes
```
There are few things to know before we can create such dialog.
### Prototype section
Syntax:
```
.protos
    <List of intents separated by commas> : <list of slot names separated by commas>
```
Pizza example:
```
.protos
    ORDER_PIZZA, ORDER_PIZZA_YES, ORDER_PIZZA_NO: t_kind, t_size, t_toppings, t_address
```
This section creates a link between a ***list of intents and corresponding list of slots***. Once all slot values are collected the conversation is considered complete.

### `Gates` section (script)
Gates are the condictions to produce new intent. The syntax uses python style `if` statements. It is better to demonstrate on `Pizza` example:
```python
.gates
    'ASK_KIND'        if o.t_intent == 'ORDER_PIZZA' and o.t_kind is None
    'ASK_SIZE'        if o.t_intent == 'ORDER_PIZZA' and o.t_size is None
    'ASK_TOPPINGS'    if o.t_intent == 'ORDER_PIZZA' and o.t_toppings is None
    'ASK_ADDRESS'     if o.t_intent == 'ORDER_PIZZA' and o.t_address is None
    'ASK_TO_CONFIRM'  if o.t_intent == 'ORDER_PIZZA'
    'R$THANKS_YES'    if o.t_intent == 'ORDER_PIZZA_YES'
    'R$THANKS_NO'     if o.t_intent == 'ORDER_PIZZA_NO'
```
```
.prompts
    ASK_KIND = What kind of pizza would you like?(BBQ chicken, Hawaiian, pepperoni, etc)
    ASK_SIZE = What size? (large, medium, small, etc)
    ASK_TOPPINGS = Anything on top?(ham, cheese, tomatoes, etc)
    ASK_ADDRESS = What is your address?
    ASK_TO_CONFIRM = Your order is {t_size} {t_kind} pizza with {t_topping} \
                     to be delivered to {t_address} Should I go ahead and place the order?
    R$THANKS_YES = Thank you for your order
    R$THANKS_NO = Sure, I will cancel the order for you
```
The intuition is simple. It reads like this - when current intent is ORDER_PIZZA and we still don't know pizza kind - generate intent ASK_KIND to ask user about pizza kind. The actual question is in the `prompt` section.
***ORDER of gates IS important!!!*** Gates are applied in the same order listed in the section
**Please note a mandatory prefix 'o.' in front of slot and intent label and also single quotes surrounding the intent name.**
Please ignore for now prefix ***R$*** of the ***R$THANKS_YES*** and ***R$THANKS_NO***. It has special meaning to be discussed [later](#r-prefix).
It was mentioned earlier that ***prompt's template*** can be used to pass information to the next layer. That would eliminate the need to have scripted ***.gates***. In each particular case developer has to make the judgement call which way to go. Note, though, gates do not require training.

## Strict Dialogs
Strict dialog resembles traversing desicion tree. The idea is to ask questions based on the `values of previous answers`, __not on the fact that the value of the slot was provided or not__, unlike loose dialog, pizza example.
Let's take as example visit to doctor. 
```
Patient> I have a stomach ache
Doctor> Did you take any medications?
Patient> Yes
Doctor> What kind of medication did you take?
Patient>...
```
Or
```
Patient> I have a stomach ache
Doctor> Did you take any medications?
Patient> No
Doctor> How bad is the pain on the scale of 1 to 10?
Patient>...
```
As you can see based on the patient answer, conversation goes different routes. 
Using `toth` and `intent_to_utterance` flags:
```
    "toth":True
    "intent_to_utterance":true
```
or/and `prompts templates` we can follow __`train of thought`__ of the conversation and use users answers as a context for next deductions.

# Regex section
## Irreversable replacement
```
.regex
    &and:(as well as|and also)
```
It is direct replacement of words in the utterance to simplify training sets.

## Reversable replacement or lookup lables
```
.define
    @small = small|medium|large
.regex
    P_SIZE:@small
    P_ADDRESS: <regex to search for address>
```
The actual value of `small`, `medium` or `large` is replaced by `P_SIZE` and passed to the NN layer so that we have less training samples. At the last layer of the model, the values will be restored. See [pizza2 example](#pizza2-bot-example) for more details.

# Prompt label
Prompt is a powerful tool of ___ToTh___ mechanism to control passing information from one deduction layer to another. It could be a simple text response corresponding to user query or a ___template which uses collected slot and their values___ to build next 'utterance' for next layer in the pipeline, __IF desired__. Must reiterate this point. Very first deduction layer gets user query. The output is either updated utterance or a prompt, which becomes an input to next layer and so on.
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
                prompt:Sure, I will nagivate you to {t_destination}
                {
                    't_intent':NAVIGATE
                    't_destination':Seattle
                    't_prompt':Sure, I will navigate you to Seattle
                }
```
The values in the template are controlled by prompt's prefixes as described below:

## Prefix __"#"__
Implies using label's ___name___ in the ___most recent deduction___. ___NOTE: if value is absent it will be replaced with 'None'___
```
Example: t_name value is in the last deduction, t_age is absent
.prompt
    RESULT = {#t_name} {#t_age}
    # The value of RESULT = t_name None
```

## Prefix __"?#"__  
Implies using label's ___name___ in the ___most recent deduction___. ___NOTE: if value is absent it will be skipped from the prompt___
```
Example:  t_name value is in the last deduction, t_age is absent
.prompt
    RESULT = {?#t_name} {?#t_age}
    # The value of RESULT = t_name 
```

## Prefix __"$"__  
Implies using label's ___name___ in ___whole deduction history___. The approatch can be used as an input for dialog tracking layers. ___NOTE: if value is absent it will be replaced with 'None'___
```
Example: t_name value is in all whole history, t_age is absent
.prompt
    RESULT = {$t_name} {$t_age}
    # The value of RESULT = t_name None
```

## Prefix __"?$"__  
Implies using label's ___name___ in ___whole deduction history___. ___NOTE: if value is absent it will be skipped from the prompt___
```
Example: t_name value is in all whole history, t_age is absent
.prompt
    RESULT = {?$t_name} {?$t_age}
    # The value of RESULT = t_name 
```

## Prefix __"."__ 
Implies using label's ___value___ in the ___most recent deduction___. ___NOTE: if value is absent it will be replaced with 'None'___
```
Example: t_name = John is in the last deduction. 
.prompt
    GREETING = Hello {.t_name} => Hello John
```

## Prefix __"?."__  
Implies using label's ___value___ in the ___most recent deduction___. ___NOTE: if value is absent it will be skipped from the prompt___
```
Example: t_name is absent in the last deduction. 
.prompt
    GREETING = Hello {?.t_name} => Hello
```

## Empty label prefix 
Implies using label's ___values___ in ___whole deduction history___. ___NOTE: if value is absent it will be replaced with 'None'___
```
Example: t_kind values are in whole deduction history, t_kind = BBQ and t_kind = meat
.prompt
    ORDER_PIZZA = Ok, I will place an order of {t_kind} pizza for you => 
    => Ok, I will place an order of BBQ, meat pizza for you
```

## Prefix __"?"__  
Implies using label's ___values___ in ___whole deduction history___. ___NOTE: if value is absent it will be skipped from the prompt___
```
Example: t_name is absent in deduction history
.prompt
    GREETING = Hello {?t_name} => Hello
```

## Prompt label value access by index  
While building a prompt, the label value can be accessed by index in the deduction history, like so: `{t_utt-1}`. Index `-1` refers value of the label `t_utt` of in the previous deduction. 
If previous deduction is not available, `None` value is used in the prompt. If you want the value to be ommited in such case use `{?t_utt-1}`

```
Example: 
.train
    ASKING_AGE: how old are you
    R$RESP_YES: ASKING_AGE (yes|sure|of course)
    R$RESP_NO: ASKING_AGE (no|nope|don't care)
.prompt
    ASKING_AGE: I don't know answer to the question, would you like to forward it to my parents?
    R$RESP_YES: Sure. I am forwarding your question {t_utt-1} to my parents
    R$RESP_NO: Ok, no problem.
```
Side note: this particular example relies on `flag` toth to be enabled

# PIZZA2 BOT Example
Let's consider PIZZA2 BOT example. In this example we will not use scripting part utilizing only ___Neural Networks(NN)___ layers. This implementation is also can be classified as [`loose dialog`](#loose-dialogs) type. By no means it should be considered completed, however it showcases many useful features of the platform. The project has 3 layers. 
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
    &and:(as well as|and also)
    // Replace, but finally resolve to actual value
    P_SIZE:@small
.train
    // The goal is isolate slot types(!) and replace them by the type name, so next layer - has
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
It is not always makes sense to use machine learning training models in all layers. Sometimes it is sufficient to use direct replacement mechanism like regular expressions. __You can, but you don't have to.__
Developers of knowledge domains are faced with the challenge to come up with as many variations of utterances as possible, so the system can understand all users - the ways they talk. From one side - we want to have lots of utterances to achieve that, but on the other hand it leads to longer training times.
```
.define
    @and = and|also|as well as
.train
    I would like ham @and extra cheese on top 
```
In the example above we would have 3 utterances instead of one because we have 3 variants for ```and```
Lets review regex section.
```    
.define 
    @small = small|medium|large
.regex
    // Replace and leave it as such
    &and:(as well as|and also)
    // Replace, but finally resolve to actual value
    P_SIZE:@small
```
```&and:(as well as|and also)``` == to replace ```as well as``` and ```and also``` with ```and```. Prefix '&' tells that no need to resolve ```and``` to actual values it replaces in the final deduction.
```P_SIZE:@small```  == to replace ```small```, ```medium``` or ```large``` with the type  ```P_SIZE```, which must be resolved to its value in the final deduction result. 
___NOTE!___ Regex section is used for both - __training__ and __prediction__ modes.
___NOTE!___ Be careful if your knowledge domain contains names of __movies__, __places__, __songs__ etc. In this case it could backfire at you, because you don't want to modify those names. Consider creation of separate layers that would isolate such names into types like __P_MOVIE_NAME__, __P_SONG_NAME__, etc. so next layer that supposed to deduce user intents would not deal with them.
__base.h__ file:
```
.define
    @i = i|we
    @i_want = @i @want
    @pizza = pizza
    @please = please|kindly
    @want = want|need|would like
    @and = and|and also|as well as
    @small = small|large|medium
    @kind = pepperoni|meat|Hawaiian|BBQ|meat|cheese
    @toppings = ham|cheese|tomato|meat|cheese
    @address = seattle|vancouver
    @extra = extra|
    @the = the|a|
    @yes = yes|sure|go ahead|you bet|sure why not
    @no = no|no way|nope|(@i|) changed my mind
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
    R$ORDER_PIZZA_YES: ASK_TO_CONFIRM @yes
    R$ORDER_PIZZA_NO: ASK_TO_CONFIRM @no
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
    ORDER_PIZZA = if {$!t_kind|t_size|t_toppings|t_address|none} is missing

    // NOTE! Prefix R$(==return) is an instruction to collect all slots values and clean up
    // the deduction history, thus to forget what user said before.
    R$ORDER_PIZZA_YES = Thank you for you order :)
    R$ORDER_PIZZA_NO = Sure, maybe next time
```
Now time to discuss:
```
"toth":true
```
It tells that ___this___ layer wants to receive ___last intent___ as a prefix to the input utterance. This is the essence of __ToTh__ mechanism to communicate contextual information to make deductions more accurate. __NOTE!__ Intents can be generated by any layers in the stack and be passed to next layer with ```toth``` set to ```true```. Otherwise, current utterance or prompt value is passed to the next layer. Consider the following training utterance:
```
.train
    ORDER_PIZZA: ASK_TOPPINGS I want pizza with P_TOPPINGS{t_toppings}
```    
It reads like this: when user is prompted to provide pizza toppings(previous intent was ___ASK_TOPPINGS___) and user response is 'I want pizza with cheese', generate intent ___ORDER_PIZZA___ and assign ___t_toppings___ with the value. In this case: ```t_toppings = cheese```

Layer 'Pizza' should contain as many utterances as possible to understand any user and the way they talk! The layer collects all slots and their values. 
Now, what is next? Next - is to figure out which question we need to ask. To do so we need to generate prompts, not utterances, because next layer deduction is based on the fact which slots we have already collected. This information is stored in the deduction history, which is what user said before. See the comments in prompt section above.
```
.prompt
    ORDER_PIZZA = if {$!t_kind|t_size|t_toppings|t_address|none} is missing
```
```{$!t_kind|t_size|t_toppings|t_address|none}``` means look through all deduction history and put __slot names__(prefix __'$'__) which are __NOT__ present in the deduction history(prefix __'!'__). Last value in the statement is dummy slot name 'None'. It is used for readability purpose only as well as 'if' and 'is missing'. So the prompt's template could just look like this:
```
.prompt
    ORDER_PIZZA = {$!t_kind|t_size|t_toppings|t_address|none}
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
    ASK_KIND = What kind of pizza would you like. For example, Hawaiian, BBQ, etc.?
    ASK_SIZE = Small, medium or large?
    ASK_TOPPINGS = What do you want on top. For example: tomato, ham, cheese, etc.?
    ASK_ADDRESS = What is delivery address?
    ASK_TO_CONFIRM = Your order is {?t_cnt} {t_size} {t_kind} pizza with {t_toppings} to \
                     be delivered to {t_address}. Would you like to go ahead with the order?
```
The training set for 'Bot' layer is self explainatory. Generate ___ASK_KIND___ prompt to user if ___t_kind___ slot is missing and so on. Valid question at this point is: Do I need to create training layer for such simple task? The answer is NO. Alternatively, you can use [___.gates___](#gates-section-script) section described before to 'script' the same logic, thus skipping training altogether for this type of deduction.

## Pizza project Final Deduction
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

# Deduction history
This information is useful to understand platform operation under the hood. Deduction history could be simply described as the "things user said before". All deductions are collected in the ```history``` or ```stack```. Those terms will be used interchangeably. The deduction history contains:
* Layer's input utterance with predefined slot name ```t_utt```
* Layer's intent with predefined slot name ```t_intent```, if any
* Layer's deduced ```slots``` and their ```values```, if any
* Layer's prompt with predefined slot name ```t_prompt```, if any

# How to control deduction history

At some point we need to collect all slots values in the stack to build a aggregative deduction(pizza order), or may be forget whole deduction, because it is self-contained and there is no need to remember it, or go one or more steps back in history when user says "What?" or "Could you repeat it?". Or what if user changed their mind and wants to change the value of a slot? All of above are pieces of __ToTh__ technology. It is done via intent prefixes:
* ## Intent Prefixes
```
<no prefix> - Normal intent. The intent and slots values to be collected in the history
R$ - Return all collected slots values in the deduction history and clean the history. "Return" command.
F$ - Do not remember this particular deduction in the history - "Deduce and forget" command.
B$ - Step back in the deduction stack. "Back" command.
C$ - Change value of a slot. "Change" command.
X$ - Clean the deduction history. "Cross" command.
?? - We are open to discuss any other prefixes to control the history.
```
* ## `Empty` prefix
Intent without prefix with deduced slots and their values are saved in the deduction history.
`ORDER_PIZZA: @i @want some @pizza @please`
where
`t_intent = ORDER_PIZZA` will be kelp in stack until `R$` or `X$` session based conversation intent comes along to erase it.

* ## `R$` prefix. Return command
In 'Pizza' layer we have:
```
.train
    R$ORDER_PIZZA_YES: ASK_TO_CONFIRM @yes
    R$ORDER_PIZZA_NO: ASK_TO_CONFIRM @no
.prompt:
    R$ORDER_PIZZA_YES = Thank you for you order :)
    R$ORDER_PIZZA_NO = Sure, maybe next time
```
Intents with ```'R$'``` prefix tell the framework to collect all slots and their values from history and return them to user as a deduction in json format. After that deduction history will be erased.
```json
{
    "t_size":"small", 
    "t_kind":"pepperoni", 
    "t_toppings": ["cheese", "ham"]
}
```
* ## `F$` prefix. Deduce and Forget command
```F$``` prefix is used to prevent saving the deduction in the history. For instance: `What time is it?` This is, most likely, self-contained statement and depending on the domain there maybe no need to keep it in the history. So, the resulting deduction will be returned and it will not be remembered in the stack.
```json
{
    "t_intent":"GET_TIME",
    "t_prompt":"It is 1:38PM"
}
```
This is actually tricky example. [`zCymatix`](http://www.zcymatix.com) platform does not act on user requests. It only deduces the intents and slots and follows the conversation flows. `t_prompt`'s time value above must be provided by the client application. The framework returns the prompt template from the training set: `"It is {t_time}"`, so user application should replace `t_time` with its value.

* ## `B$` prefix. Step back command
`B$` prefix tells the framework to go back one step in the history and return that deduction. It is useful for cases when user asks 'Please repeat that.' or 'Could you repeat it please?'
```
Bot>What type of pizza would you like?
User>What?
Bot>What type of pizza would you like?
```

There is an alternative to achieve the same result. Consider training sample:
```
.train
    F$REPEAT:what|what did you say|come again|repeat (please|)|pardon me
.prompt:
    F$REPEAT = *
```
Star `*` symbol used a value of the prompt means to grab `t_prompt` last value from the history. It is up to you to choose which method to use.

* ## `C$` prefix. Change slot value command
`C$` prefix tells the framework to change the value of the slot in the history
`User> Take me to Seattle`

```json
{
    "t_intent":"NAVIGATE",
    "t_destination":"Seattle"
}
```
```User> No, change it to Vancouver```
```json
{
    "t_intent":"C$NAVIGATE",
    "t_destination":"Vancouver"
}
```
The `t_destination` slot value `Seattle` will be replaced with `Vancouver` directly in the history

* ## `X$` prefix. Reset command
`X$` prefix is for testing purposes. But if you find it useful in other cases, you can use it without restrictions.

# Indirect references `it` or `there`

Consider the training samples using `P_PLACE` slot type:
```
.train
    INT_SHOW_PLACE: show me P_PLACE{t_place} (on the map|)
    INT_SHOW_PLACE: where is P_PLACE{t_place}
    INT_SHOW_PLACE: I am looking for P_PLACE{t_place}
    INT_DISTANCE_INFO: how far is P_PLACE{t_destination}
    INT_NAVIGATE/t_place/t_destination:take me there
```
First four training samples rely on explicit place name we want to see or check the distance to. Last one has an intent and a list of slot names to look in the history to choose to resolve `it`:
`INT_NAVIGATE/t_place/t_destination:take me there`
Why list of slots? The intuition is this - search for either `t_place` or `t_destination` in that order in the deduction history and put its value to substitute `there`.

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
and the deduction would be:
```json
{
    "t_intent":"PLAY_MUSIC",
    "t_artist":"Def Leppard",
    "t_location":"__living_room__"
}
```
So what? Here the advantages:
1. Client device `did NOT make the decision` where to play the music, but merely provided encoded sensor information or in this case it is a state - "where am I at the moment" == `living room`.
2. This is `not hardcoded logic`, because the model which deduced the intent and slots `resides on the backend` and can be trained or re-trained at any time, so there is no need to "install new version" of the application just because of some changes in logic.

    __NOTE!__ You need to train your models with encoded events/states and modify user utterance in prediction mode.

This makes client application __cleaner, focusing on its task__ and `backend` takes care of the session, its history and the context. In our example my phone would only __`act`__ on the intent by playing `Def Leppard` in `living room`.

# Comments in training files
Comment must start from a new line and be prefixed with either `#` or `//`

# Long lines continuation
Use backslash `\` to break long line. NOTE, white spaces on next line are ignored.

# Unkown word marker
__`<UNK>`__ is used in training sets to mark words that are not in the vocabulary of the training set.

# Placement slot deduction
`Placement slot deduction` is used when we don't know all the values of the slot type. That is the type of the slot is not complete or unknown. Training set must include utterances that create sufficient, high probability context to be sure that unkown word is something that we are looking for at some particular place in the utterance. We will not be dicussing here whether this is good or bad way leaving it to developers.
Example:
```
.define
    @pizza_kind = BBQ chicken|Hawaiian|<UNK>|<UNK> <UNK>
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

# Recommendations, tips and tricks
- Before starting creating a `project` or `knowledge domain` important to remember:
There are two ways to describe something. __`What it IS`__ and __`what it IS NOT`__. Remember __Hello__ example in this tutorial? Does not matter what you say, it will `always` produce `GREETING` intent! Why? Because the example does not have any alternative samples to tell apart 'Hello World' from any other things user may say. Consider the example:
    ```
    .train
        INT_FLIGHT_INFO:show me flights to Seattle{t_destination}
        don't show me flights to Seattle
    ```
    Second sample does not have an intent or slots to deduce. This means that this statement will be __`just ignored`__ and no deduction will be made, __if we wish__. So, the training process will teach the model to remember the difference between these samples.

- Do not use intent names that can be confused for words. I recommend using something like `INT_DO_SOMETHING` or `INT_SOMETHING_HAPPENED`

- Do not use slot types names that can be confused for words. I recommend using something like `PIZZA_KIND` or similar

- Slot name template is __`t_<name>`__ keeping in mind that __`t_intent`__, __`t_utt`__ and __`t_prompt`__ are reserved.

- Slot deduction. Consider two training sets:
 `Single layer project` which attempts not to use slot types isolation step:
    ```
        .train
            INT_NAVIGATE:take me to (Los Angeles){t_target} and to (New York){target}
    ```
    with deduction for the sample above:
    ```json
        {
            "t_intent":"INT_NAVIGATE",
            "t_destination":["Los", "Angeles", "New", "York"]
        }
    ```
    vs `Two layers project` which uses type definition layer and a separate slot value deduction layer:
    ```
        # Layer 1 - type training
        .train 
            take me to (Los Angeles){&P_PLACE} and to (New York){&P_PLACE}
    ```
    ```
        # Layer 2 - intents and slots deduction
        .train
            INT_NAVIGATE:take me to P_PLACE{t_destination} and to P_PLACE{t_destination}
    ```
    with deduction for the sample:
    ```json
        {
            "t_intent":"INT_NAVIGATE",
            "t_destination":["Los Angeles", "New York"]
        }
    ```
    You can see the advantage of second approach, where names are correctly isolated.
    
- [`zCymatix`](http://www.zcymatix.com) platform __does not__ provide `voice recognition services`. For web applications we recommend using [`Google service`](https://cloud.google.com/speech/), since it is superior of other products available on the market today. See also available solutions for [Android](https://developer.android.com/reference/android/speech/SpeechRecognizer.html) and [iOS](https://developer.apple.com/documentation/speech).

# Optional configuration parameters

__NOTE__! If the meaning of the parameters are not clear, keep the defaults or drop me a note. 

- To use bidirectional LSTM models. By default, it is unidirectional model.
    ```
    "bi_lstm":false
    ```
- To enable passing previous intent in the history as utterance prefix. By default, it is `False`
    ```
    "toth":true
    ```
- A layer can be optionally inlcuded into the deduction pipeline. When `accept_r_intents_only` is True , only  `R$` prefixed intent produced by one of the __previous layers__ will enable this layer to be included in the deduction. By default, is it `False`.  This is useful for expert system layers, where it should not be a part of collecting slots values, but rather when we need to process the whole collection of the slots.
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
- To include vendor name into the deductions. By default, it is `False`
    ```
    "include_vendor":false
    ```
- To include version number into the deductions. By default, it is `False`
    ```
    "include_version":false
    ```
- To include layer name into the deductions. By default, it is `False`
    ```
    "include_layer_name":false
    ```
- To include intents into the deductions. By default,it is `True`
    ```
    "include_intents":true
    ```
- To include prompt into the deductions. By default, it is `True`
    ```
    "include_prompts":true
    ```
- To include utterance into the deductions. By default, it is `True`
    ```
    "include_utt":true
    ```
- To keep last intent only in the deductions. By default, it is `True`
    ```
    "keep_last_intent":true
    ```
- To keep last prompt only in the deductions. By default, it is `True`
    ```
    "keep_last_prompt":true
    ```
- To keep last utterance only in the deductions. By default, it is `True`
    ```
    "keep_last_utterance":true
    ```
- To convert the intent value to an utterance for the next layer in the deduction pipeline. By default, it is `False`. 
    ```
    "intent_to_utterance":talse
    ```
    This is quite useful feature. Example: We want to interpret user's loose answer that would be considered `yes` or `no`.
    ```
    .train
        INT_YES:I guess so|it is rather yes then no|...
    ```
    If the intent was `INT_YES` it will become an utterance for next layer(!) reducing training set of this layer to deal only with `INT_YES` or `INT_NO`

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

Prompt label prefixes