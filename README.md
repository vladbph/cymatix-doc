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

#### Machine learning NLU system designed for dialogues and expert systems. The platform uses Toth(Train Of Thought) contextual method of conversation flow tracking and many other features...
### ___"...Context IS everything ..."___
## Features Highlights
- ***Train Of Thought technology***
    * Literaly maintains a train of thought of the conversation
- State of the Art ***deduction pipeline*** to efficiently resolve ambiguity
- Ability to create ***1000s of utterances*** in few minutes
- Supports method of ***embedding states, events, sensors information to maintain flow of the conversation***
- Conversation instance with the ***context is maintained on the backend*** leaving client focusing only on the application itself
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
- ***Indirect*** subject referencing
    * Notion of ***'it/there'***
        * 'Where is Seattle'
        * 'Take me there'
- ***Expert system support.*** Result of the dialog could be fed into a layer to process conversation outcome.
    * This is not NLU specific feature enabling the platform utilization in any field of knowledge
    
   ### So, Let's do it!
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

# 2. Using prompts example

What if I want AI system to respond to user query, how should I do that? Let's use the 'Hello World' code. Simple:
```
.train
    GREETING: Hello World
.prompt
    GREETING = Hello my friend
    GREETING = Hello!
    GREETING = Hi!    
```
Add section ***.prompt*** and then: 
```
INTENT=<PROMPT VARIANT>
```
In example above you can see that GREETING has three variants. They will be selected randomly in order to create more human like interraction. It reads like this - 'when user greets me reply this'. Prompt text may contain slots/parameters values. 
```
.prompts
    NAVIGATE: Ok, I am starting navigation to {t_destination} by {t_car}
```
Where ___t_destination___ and ___t_car___ are known slots/parameters. See section 4 for the example.
Prompts purpose is to be able to respond to user. Also prompt mechanism can be used to pass modified data to next deduction layer. This mechanism is a key for creating expert systems.
The idea: You collect all the data from user in the form of slot values and then use prompt template to build the 'utterance' for the next model. 
```json
.prompts
    R$READY = {t_param1} {t_param2} {t_param3}...
```

# 3. Using macros
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
Please note the last OR in ***@guys*** definition reads like ***guys*** or ***folks*** or ***World*** or ***empty string***. Granularity of regular expression feature ___is limited to the words___. Example:
***folk(s|)*** is INVALID
***(folk|folks)*** is VALID

# 4. Using Slots (== parameters)
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
# 5. Introduction to Layers
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
    I would like to place an order for a small (bbq chicken){&PIZZA_KIND} and \
    large meat{&PIZZA_KIND} pizza
```
*Intent is not present here, because the purpose of this utterance is to extract and label pizza kind:*
***PIZZA_KIND = bbq chicken***
***PIZZA_KIND = meat***

This is a mechanism to label multiple words with specific label and using multiple instance of the label in a single utterance(***Amazon Lex does not allow that***). To explain further lets take a look at the next layer and file 
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
    "t_utt":"i would like to place an order for small bbq chicken and large meat pizza",
    "t_intent":"ORDER_PIZZA",
    "t_kind":["bbq chicken", "meat"]
}
```
You could say - ___How about if I have a macro @pizza_kind and put all values there and use training utterance in one single layer?:___
```
.define
    @pizza_kind = bbq chicken|meat|hawaiian|...
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
So this mechanism enables smaller context needed to train the layer to extract and label the pizza kinds. Look - do you need ***all*** words in the example utterance in layer "Pizza kinds"? Not really. So I would put into training file something like this:
```
.define 
    @pizza_kind = bbq chicken|meat|pepperoni|hawaiian
.train
    @small @pizza_kind{&PIZZA_KIND} (and @pizza_kind{&PIZZA_KIND} pizza|)
```
So having a context consisting only surrounding words is enough? You decide. But be careful though. ***False positives one of the biggest issues in NLU systems***, finding the balance between training time, number of utterances and sufficient context is not easy task to create ***high quality training set.*** zCymatix platform gives the tools to go either way.
# 6. Dialogs
There are two types of dialogs supported by the platform ***Loose Dialogs*** and ***Strict dialogs***. And third one is the combination of these two.
## 6.1 Loose Dialogs
AI System asks user questions - for example: ordering pizza. As a user I can freely provide the information I have about the pizza I want without following scricted flow of the conversation:
```
    User> I want to order some pizza
    Bot> What kind would you like?
    User> I want small bbq chicken with extra cheese and tomatoes
    Bot> What is the delivery address?
    User>...
    Bot> Here is you order... Should I go ahead and place your order?
    User> you bet!
    Bot> Great, thank you!!!
```
In such conversation there is no strict sequence of questions to be ask. The conversation flow depends on already provided parameters and system would ask only those questions helping to get missing parameters. So the converation could go like this:
```
    User> I want to small bbq chicken with extra cheese and tomatoes on top and my address is ...
    Bot> Here is you order... Should I go ahead and place your order?
    User> Yes
```

There are few things to know before we can create such dialog.
### 6.1.1 Prototype section
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
This section creates a link between a ***list of intents and corresponding list of slots/parameters*** to be collected by asking user set of questions to consider conversation complete.

### 6.1.2 'Gates' section (script)

Syntax is using python style `if` statements. It is better to demostrate using Pizza example:
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
    ASK_KIND = What kind of pizza would you like?(bbq chicken, hawaiian, pepperoni, etc)
    ASK_SIZE = What size? (large, medium, small, etc)
    ASK_TOPPINGS = Anything on top?(ham, cheese, tomatoes, etc)
    ASK_ADDRESS = What is your address?
    ASK_TO_CONFIRM = Your order is {t_size} {t_kind} pizza with {t_topping} \
                     to be delivered to {t_address} Should I go ahead and place the order?
    R$THANKS_YES = Thank you for your order
    R$THANKS_NO = Sure, I will cancel the order for you
```
The intuition is simple. It reads like this - when current intent is ORDER_PIZZA and we still don't know pizza kind - generate intent ASK_KIND to ask user about pizza kind from the prompt section.
***ORDER of gates IS important!!!*** Gates are applied in the same order listed in the section
**Please note a mandatory prefix 'o.' in front of slot and intent label and also single quites surrounding the intent name.**
Please ignore for now prefix ***R$*** of the ***R$THANKS_YES*** and ***R$THANKS_NO***. It has special meaning to be discussed later.
It was mentioned earlier that ***prompt's template*** can be used to pass information to the next layer. That would eliminate the need to have scripted ***.gates***. In each particular case developer has to make the judgement call which way to go. Note, though, gates do not require training.

# 7. Prompt label prefixes:
Prompt is a powerful tool of ___ToTh___ mechanism to control passing information from one deduction layer to another. It could be a simple text response corresponding to user query or a ___template which uses collected slot and their values___ to build next 'utterance' for next layer in the pipeline, __IF desired__. Must reiterate this point. Very first deduction layer gets user query. The output is either updated utterance or a prompt, which becomes an input to next layer and so on.
```
utterance => 
    Layer1 => 
        updated utterance OR prompt => 
            Layer2 => ... 
                final Layer => prompt
```
__Note! If layer produces a prompt, it is used as an input for the next layer, unless of couse layer is final. In that case prompt is what is presented to user as a responce to user query.__
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

1. Prefix __"#label_name"__  implies using label's ___name___ instead of ___value___ in the ___most recent deduction___. ___NOTE: if value is absent it will be replaced with 'None'___
```
Example: t_name value is in the last deduction, t_age is absent
.prompt
    RESULT = {#t_name} {#t_age}
    # The value of RESULT = t_name None
```

2. Prefix __"?#label name"__  implies using label's ___name___ instead of ___value___ in the ___most recent deduction___. ___NOTE: if value is absent it will be skipped from the prompt___
```
Example:  t_name value is in the last deduction, t_age is absent
.prompt
    RESULT = {?#t_name} {?#t_age}
    # The value of RESULT = t_name 
```

3. Prefix __"$label_name"__  implies using label's ___name___ instead of ___value___ in ___whole deduction history___. The approatch can be used as an input for dialog traking layers. ___NOTE: if value is absent it will be replaced with 'None'___
```
Example: t_name value is in all whole history, t_age is absent
.prompt
    RESULT = {$t_name} {$t_age}
    # The value of RESULT = t_name None
```

4. Prefix __"?$label_name"__  implies using label's ___name___ instead of ___value___ in ___whole deduction history___. ___NOTE: if value is absent it will be skipped from the prompt___
```
Example: t_name value is in all whole history, t_age is absent
.prompt
    RESULT = {?$t_name} {?$t_age}
    # The value of RESULT = t_name 
```

5. Prefix: __".label_name"__ implies using label's ___value___ in the ___most recent deduction___. ___NOTE: if value is absent it will be replaced with 'None'___
```
Example: t_name = John is in the last deduction. 
.prompt
    GREETING = Hello {.t_name} => Hello John
```

6. Prefix: __"?.label_name"__  implies using label's ___value___ in the ___most recent deduction___. ___NOTE: if value is absent it will be skipped from the prompt___
```
Example: t_name is absent in the last deduction. 
.prompt
    GREETING = Hello {?.t_name} => Hello
```

7. Empty prefix implies using label's ___values___ in ___whole deduction history___. ___NOTE: if value is absent it will be replaced with 'None'___
```
Example: t_kind values are in whole deduction history, t_kind = bbq and t_kind = meat
.prompt
    ORDER_PIZZA = Ok, I will place an order of {t_kind} pizza for you => 
    => Ok, I will place an order of bbq, meat pizza for you
```

8. Prefix: __"?label_name"__  implies using label's ___values___ in ___whole deduction history___. ___NOTE: if value is absent it will be skipped from the prompt___
```
Example: t_name is absent in deduction history
.prompt
    GREETING = Hello {?t_name} => Hello
```

==================================
TODOs:

Compare
```
Single layer:
    take me to (Los Angeles){t_target} and to (New York){target} 
    => t_target = ['Los', 'Angeles', 'New', 'York']
and
layer 1: type training
    take me to (Los Angeles){&P_PLACE} and to (New York){&P_PLACE} 
    => lookup table P_PLACE:0 = 'Los Angeles' and P_PLACE:1 = 'New York'
layer 2:
    NAVIGATE: take me to P_PLACE{t_destination} and to P_PLACE{t_destination}
    => t_destination = ['Los Angeles', 'New York']
```

# 8. PIZZA2 BOT Example
Let's consider PIZZA2 BOT example. In this example we will not use scipting part utilizing only ___Neural Networks(NN)___ layers. By no means it should be considered completed, however it showcases many usefull features of the platform. The project has 3 layers. 
### Layer 1 - Slots
Layer 1 is named "slots" is dedicated to isolate types of the slots - __pizza kind__, __pizza toppings__,  __size__ and __delivery address__. Here is the configuration for the layer:
```
{
    "layer_name":"slots",
    "data_files":[ "base.h","slots.txt" ],
    "bi_lstm":true,
    "toth":true
}
```
It contains 2 files - ___base.h___ with useful macros, ___slots.txt___ is an actual training file. 
Let's discuss 'bi_lstm' parameter.
```
"bi_lstm":true
```
Consider sentences: "I would like cheese on top". It is clear that 'cheese' refers to the toppings not the pizza type. We get it only when we see 'on top' which comes at the end of the sentence. ___bi_lstm___ tells framework to 'read' utterances not only ___left to right___ but also ___right to left___ to get this information.

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
Developers of knowledge domains are faced with the challege to come up with as many variations of utterances as possible so the system can understand all users - the ways they talk. From one side - we want to have lots of utterances to achive that, but on the other hand it leads to longer training times.
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
___NOTE!___ Be careful if your knowledge domain contains names of __movies__, __places__, __songs__ etc. In this case it could backfire at you, because you don't want to modify those names. Consider creation of separate layers that would isolate such names into types like __P_MOVIE_NAME__, __P_SONG_NAME__, etc so next layer that supposed to deduce user intents would not deal with them.
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
    @kind = pepperoni|meat|hawaiian|bbq|meat|cheese
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

### Layer 2 - Pizza

Config for this layer:
```
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
    // With the prompt dedinition below one of:
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
    R$ORDER_PIZZA_NO = Sure, may be next time
```
Now time to discuss:
```
"toth":true
```
It tells that ___this___ layer wants to receive ___last intent___ intent as a prefix to the input utterance. This is the essence of __ToTh__ mechanism to communicate contextual information to make deductions more accurate. __NOTE!__ Intents can be generaged by any layers in the stack and be passed to next layer with ```toth``` set to ```true```. Otherwise, current utterance or prompt value(See explanation if Chapter 7) is passed to the next layer. Consider the following training utterance:
```
.train
    ORDER_PIZZA: ASK_TOPPINGS i want pizza with P_TOPPINGS{t_toppings}
```    
It reads like this: when user is prompted to provide pizza toppings(previous intent was ___ASK_TOPPINGS___) and user response is 'I want pizza with cheese', generate intent ___ORDER_PIZZA___ and assign ___t_toppings___ with the value. In this case: ```t_toppings = cheese```

Layer 'Pizza' should contain as many utterances as possible to understand any user and the way they talk! The layer collects all slots and their values. 
Now, what is next? Next - is to figure out which question we need to ask. To do so we need to generate prompts, not utterances, because next layer deduction is based on the fact which slots we have already collected. This information is stored in the deduction history, which is what user said before kind of thing. See the comments in prompt section above.
```
.prompt
    ORDER_PIZZA = if {$!t_kind|t_size|t_toppings|t_address|none} is missing
```
```{$!t_kind|t_size|t_toppings|t_address|none}``` means look through all deduction history(prefix __'$'__) and replace with a __slot name__ that is __NOT__ present in the deduction history(prefix __'!'__). Last value in the statement is dummy slot name 'None'. It is used for readability purpose only as well as 'if' and 'is missing'. So the prompt template could just look like this:
```
.prompt
    ORDER_PIZZA = {$!t_kind|t_size|t_toppings|t_address|none}
```
This way we costruct prompts providing sufficient information to the next layer to decide - what to ask next. 
Layer 'Pizza' generates prompts => utterances for next layer:
```
if t_size is missing
if t_kind is missing
if t_toppings is missing
if t_address is missing
```
Next layer is called 'Bot'.

### Layer 3 - Bot
Configuration:
```
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
    ASK_KIND = What kind of pizza would you like. For example, hawaiian, bbq, etc.?
    ASK_SIZE = Small, medium or large?
    ASK_TOPPINGS = What do you want on top. For example: tomato, ham, cheese, etc.?
    ASK_ADDRESS = What is delivery address?
    ASK_TO_CONFIRM = Your order is {?t_cnt} {t_size} {t_kind} pizza with {t_toppings} to \
                     be delivered to {t_address}. Would you like to go ahead with the order?
```
The training set for 'Bot' layer is self explainatory. Generate ___ASK_KIND___ prompt to user if ___t_kind___ slot is missing and so on. Valid question at this point is: Do I need to create training layer for such simple task? The answer is NO. Alternatevly you can use ___.gates___ section described before to 'script' the same logic, thus skipping training altogether for this type of deduction.

## Pizza project Final Deduction
Let's review utterance transformation going though all layers of the 'Pizza' project:
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

I hope it is clear why the 1st quesion is 'What is the delivery address'. It is because user already provided ___t_kind___, ___t_toppings___ and ___t_size___ in the origincal sentence.

## Deduction history
This information is useful to understand platform operation under the hood. Deduction history could be simply described as the "things user said before". All deductions are collected in the ```history``` or ```stack```. Those terms will be used interchangeably. The deduction history contains:
* Layer's input utterance with predefined slot name ```t_utt```
* Layer's intent with predefined slot name ```t_intent```, if any
* Layer's deduced ```slots``` and their ```values```, if any
* Layer's prompt with predefined slot name ```t_prompt```, if any

## How to control deduction history

At some point we need to collect all slots values in the stack to build a aggregative deduction(pizza order), or forget a deduction, because it is self contained and there is no need to remember it, or go one or more steps back in history when user says "What?" or "Could you repeat it?". All of above are pieces of __ToTh__ method. It is done via intent prefixes:

* ### Intent Prefixes
```
<no prefix> - Normal intent. The intent and slots values to be collected in the history
R$ - Return all collected slots values in the deduction history and clean the history. "Return" command.
F$ - Do not remember this particular deduction in the history - "Deduce and forget" command.
B$ - Step back in the deduction stack. "Back" command.
C$ - Change value of a slot. "Change" command.
X$ - Clean the deduction history. "Cross" command.
?? - We are open to discuss any other prefixes to control the history.
```
* ### `Empty` prefix
Intent without prefix with deduced slots and their values are saved in the deduction in the history.
`ORDER_PIZZA: @i @want some @pizza @please`
where
`t_intent = ORDER_PIZZA` will be kelp in stack until `R$' intent comes along


* ### `R$` prefix
In 'Pizza' layer we have:
```
.train
    R$ORDER_PIZZA_YES: ASK_TO_CONFIRM @yes
    R$ORDER_PIZZA_NO: ASK_TO_CONFIRM @no
.prompt:
    R$ORDER_PIZZA_YES = Thank you for you order :)
    R$ORDER_PIZZA_NO = Sure, may be next time
```
Intents with ```'R$'``` prefix tell the framework to collect all slots and their values and return them to user as a deduction in json format:
```
{
    "t_size":"small", 
    "t_kind":"pepperoni", 
    "t_toppings": ["cheese", "ham"]
}
```
* ### `F$` prefix
```F$``` prefix is used to prevent saving the deduction in the history. For instance: `What time is it?` This is, most likely, self contained statement and depending on the domain there may be no need to keep it in the history. So the resulting deduction will be returned and it will not be remembered in the stack.
```
{
    "t_intent":"GET_TIME",
    "t_prompt":"It is 1:38PM"
}
```
This is actually tricky example. __zCymatix platform does not act on user requests__. It only deduces the intents and slots and follows the conversation flows => `t_prompt`'s time value must be provided by the client application. The framework returns the prompt template from the training set: `"It is {t_time}"`, so user application should replace `t_time` with its value

* ### `B$` prefix
`B$` prefix tells the framework to go back one step in the history and return that deduction. It is usefull for cases when user asks 'Please repeat that.' or 'Could you repeat it please?'
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
`*` means to use the last value of `t_prompt` saved in the history. It is up to you to choose which method to use.

* ### `C$` prefix
`C$` prefix tells the framework to change the value of the slot in the history
```
User> Take me to Seattle
{
    "t_intent":"NAVIGATE",
    "t_destination":"Seattle"
}

User> No, change it to Vancouver
{
    "t_intent":"C$NAVIGATE",
    "t_destination":"Vancouver"
}
```
The `t_destination` slot value `Seattle` will be replaced with 'Vancouver' in the history stack

* ### `X$` prefix
`X$` prefix is for testing purposes. But if you find it useful in other cases, you can use it without restrictions.

# 9. Handling `it` or `there` or frequetly used indirect references

Consider the training samples:
```
.train
    I_SHOW_PLACE: show me P_PLACE{t_place} (on the map|)
    I_SHOW_PLACE: where is P_PLACE{t_place}
    I_SHOW_PLACE: I am looking for P_PLACE{t_place}
    I_DISTANCE_INFO: how far is P_PLACE{t_destination}
    I_NAVIGATE/t_place/t_destinationr:take me there
```
First four training samples reply on explict name of the place we want to see or check the distance to. Last one has an intent and list of slot names to look in the history to choose to resolve `it`:
`I_NAVIGATE/t_place/t_destinationr:take me there`
Why list of slots? The intuition is - search for either `t_place` or `t_destination`, whichever comes first in te

