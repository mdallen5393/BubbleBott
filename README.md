# PROJECT: Hack Sprint - BubbleBott

Holberton School Tulsa Hack Sprint

## DESCRIPTION

Holberton's Hack Sprint is a project that is meant to use all of the skills students have developed over the course of the first two trimesters at Holberton.  The result is a minimum viable product that must follow the given theme: BUBBLES.

Enter **BubbleBott**.

BubbleBott is an application that allows for the storage of links, ideas, and resources related to specific topics.  BubbleBott is meant to be a Discord or Slack Bot that interacts with an AWS EC2 server hosting a Python Flask App that interacts with a NoSQL Firestore database.

All users have basic my perform basic CRUD operations: creating, reading, updating, and deleting bubbles and/or their associated resources.

## USAGE: Python App

Clone the repository and add the following aliases to your `~/.bashrc` file:

* `alias bubble="{path/to/repository} bubble"`
* `alias bubble="{path/to/repository} pop"`
* `alias bubble="{path/to/repository} add"`

### To list all bubbles

`$ bubble`

### To list all resources in an existing bubble

`$ bubble {bubble_name}`

Ex: `$ bubble firestore` will list all resources contained within the "firestore" database.

### To add a new bubble

`$ bubble {bubble_name} {owner} {description}`

Ex: `$ bubble firestore 'Matthew Allen' 'This is a firestore bubble'` will create a bubble named "firestore".

### To add a new resource to an existing bubble

`$ add {bubble_name} {owner} {description} {content}`

Ex: `$ add firestore 'Clayton Christian' 'Great firestore resource' 'www.examplefirestoreresource.com'` adds the resource under an auto-generated index.

### Deleting a bubble

`$ pop {bubble_name}`

Ex: `$ pop firestore` will delete the "firestore" bubble.

### Deleting a resource

`$ pop {bubble_name} {index}`

Ex: `$ pop firestore 0` will delete the zeroth resource from the "firestore" database.

## AUTHORS

* Matthew Allen
    [Github](https://github.com/mdallen5393)
* Clayton Christian
    [Github](https://github.com/claybowl)
