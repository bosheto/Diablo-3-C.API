# Diablo-3-C.API
## Introduction
A python3 module for accessing the Diablo 3 Comunity API

## Table of contents
* [Instalation]('#instalation')
* [Requirements]('#requirements')
* [API]('#api')
  * [Usage]('#usage')
  * [get carrer profile]('#get-career-profile')
  * [get hero profile]('#get-hero-profile')
  * [get item data]('#get-item-data')
 * [Credits]('#credits')
 
 ## Instalation
 Just download the source code or fork the repository
 
 ## Requirements
 Requires ujson module, get it using pip install ujson
 
 ## API
 In this section we will go over the api commands
 you should check out the blizzard api site for information on the Diablo3 Community API 
 https://dev.battle.net/io-docs
 
 ## Usage
    
    # Import the api
    from request import API
    
    # Create API object
    api = API(api_key=', locale='')
    # Exaple locale 'en_US'
    
    # Get the career_profile data
    output = api.get_career_profile(battleTag)
    
    
  
 ## get carrer profile
 The get_career_function(battleTag) returns career profile information takes a BattleTag string ex. 'Example#0000' 

     out = api.get_career_function('Example#0000')
     print(out['battleTag'])  
     'Example#0000'
     
 ## get hero profile 
 The get get_hero_profie(battleTag, heroId) returns a hero information takes a BattleTag string and a hero id int
 you get the hero id from the return of get_career_profile
 
     out = api.get_hero_profile('Example#0000', 00000000)
     print(out['name'])
     'Hero name'
     
 ## get item data 
 The get_item_data(itemdata) function returns the item data for a given item takes itemdata string
     
     out = api.get_item_data('example item data')
     print(out['name'])
     'Sly Shot'
     
 ## Credits 
 A big thank you to blizzard for providing the API 
 
