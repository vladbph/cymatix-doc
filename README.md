# Please watch the repo for updates. I am in process creating documentation and examples. 

### zCymatix Natural Language Understanding(NLU) Voice/text UI platform for

    - Healthcare 
    - Finance
    - Electronics
    - Wearables
    - Automotive
    - ...

### Machine learning NLU system designed for dialogues and expert systems. The platform uses Toth(Train Of Thought) method of conversation flow tracking as well as many powerful features...
## Features Highlights
- State of the Art deduction pipeline to efficiently resolve ambiguity
- Train Of Thought technology
- Ability to create 1000s of utterances in few minutes
- Supports method of embedding states, events, sensors information to maintain flow of the conversation
- Regex layer support. Yes, why would you need to use ML for simple things.? You may, but you don't have to.
- Idioms interpretation mechanism
- Machine learning lookup labels support
- NLU tasks supported:
    - Self-contained deductions
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
- Expert system support. Result of the dialog is fed into a layer to process conversation outcome.
    
   So, Let's do it!
# 'Hello Word' Example.
* Create and enter **hello** folder
* Create **hello.json** file
```
{
    "data_files":"hello.txt"
}
```
* Create **hello.txt** training file
```
.train
GREETING:Hello World
```
That's it. Literally, 3 lines(Ok, 5 if consider beautification) of code would get you there. To get E2E how-to feeling go to www.zcymatix.com and sign up. Press ***Sign In*** and then ***Sign Up***. 
***NOTE!*** Please use real e-mail address to be able to receive training completion notification.
![Register](http://www.zcymatix.com/img/signup.png "Register")

After login, upload the project by choosing ***hello*** folder
![Upload](http://www.zcymatix.com/img/upload_page.png "Upload")

When project is uploaded, you need to train it. Choose ***Training*** option and press launch.
![Launch](http://www.zcymatix.com/img/launch_project.png "Launch")

Depending on project complexity it may take from few seconds to few hours to train your project. 
What's next after project training is finished? Two options:
* Use REST api. 
    * Login:
        <https://nlp2.zcymatix.com/?action=launch&project_id=project_id>
        
        In the responce you will receive ___session_id___
    * Deduction:
        <https://nlp2.zcymatix.com/?action=deduce&session_id=session id&query=hello+world>
    
* Use deduction page to verify the training
![Deduction](http://www.zcymatix.com/img/deduction_page.png "Deduction")



   
 
