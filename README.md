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
```
.regex
    &restaurant:place where I can eat
vs
.regex
    restaurant:place where I can eat
```
It/there
```
NAVIGATE/t_destination/t_stopover:take me there
```
Intent Prefixes:
```
R$ - return all collected values in history
B$ - step back
C$ - change value
```
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
```
Use case: user asks - What did you say?
.train
	REPEAT:What did you say
.prompt:
	REPEAT = *
```
