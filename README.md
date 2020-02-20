A platform where people want to give for free, an unwanted item 
A platform where the free item can be taken by another person that needs it
A free and user-friendly platform where exchange happens

<h1 align="center">
  <a href="" target="_blank"><img src="" width=100 height=100 alt="logo"/></a>
</h1>

<div align="center">

# Re-Use Gang
</div>
<div align="center">
</div>

## Table of Contents

* [What?](#what)
* [Why?](#why)
* [How?](#how)
* [UX](#ux)
    * [Strategy: Why and what?](#why-and-what)
        * [1. Primary target audience](#1-primary-target-audience)
        * [2. Who is the project for?](#2-who-is-the-project-for)
        * [3. What are the main goals?](#3-what-are-the-main-goals)
        * [4. What are the goals and needs of the user?](#4-what-are-the-goals-and-needs-of-the-user)
        * [5. What are the goals and needs of the business?](#5-what-are-the-goals-and-needs-of-the-business)
        * [6. Research](#6-research)
        * [7. Planning](#7-planning)
        * [User Stories](#user-stories)
    * [Scope plane: How?](#scope-plane-how)
    * [Structure plane: Organisation and functionality](#structure-plane-organisation-and-functionality)
        * [1.Existing Features](#1-existing-features)
        * [2.Features Left to Implement](#2-features-left-to-implement)
    * [Skeleton plane: Presentation and navigation](#skeleton-plane-presentation-and-navigation)
        * [Wireframes](#wireframes)
    * [Surface: Design](#surface-design)
        * [1. Color Scheme](#1-color-scheme)
        * [2. Font](#2-font)
        * [3. Logo](#3-logo)
* [Testing](#testing)
* [Technology Used](#technology-used)    
* [Deployment](#deployment)
* [Credits](#credits)
    * [Special Thanks & Acknowledgements](#special-thanks--acknowledgements)

# What?
“Give...Reuse” OR “Re-Use Gang” OR “Recycling Rocks!”

A platform where people want to give for free, an unwanted item 

A platform where the free item can be taken by another person that needs it

A free and user-friendly platform where exchange happens

# Why?

Because our society has become so monetarised

Because we all use so many items for a certain time only

Because all of us need to declutter our houses sometimes

Because we would not be able to sell many used items

Because so many of us already give to charities their used items

Because charities are already cluttered with used items, cannot and refuse often to take more

Because we do not always need to buy new items which will only be used for a certain time

Because many of us would not mind re-using a used item for a certain time also (child bike)

Because so many of us already buy used items in charity shops

Because an item can be re-used for long before being considered completely useless

Because the small parts of a used and broken item can be useful for some people to make or fix another item

Because we, humans, consume and throw away too much

Because our planet does not have more space for thrown away items and should throw them back at us

Because so many of us love exchanging with other people


# How?
- Simple login feature for users
- User can add an item to give away by filling a form (CREATE)
- Categories for an item to give: name, description, image, location, is urgent to dispose of, category of items
(Kids, clothes, home, books, others)
- User can remove an item by marking it as taken (DELETE)
- User can edit an item card by updating its description or confirm it’s still available after a certain time (UPDATE)
- Users can view all items being available at a certain time (RETRIEVE/READ)
- Users can search items by location or category (RETRIEVE/READ)
- Will have two collections of data: users and items
- All activities of CRUD can be performed by the user on their own records

[Back to Top](#table-of-contents) 

# UX
## Strategy plane: Why and what?

### 1. Primary target audience

General people, probably more from a local community. People who are already concerned about planet and environment and want to be part of a community of exchange

### 2. Who is the project for?

A local town or community where people can exchange easily their items. The project can be promoted and managed by a local zero waste association run by volunteers.
  
### 3. What are the main goals?

- A platform where people want to give for free, an unwanted item 
- A platform where the free item can be taken by another person that needs it
- A very simple and user-friendly platform where exchange happens effectively and that does not turn away people

### 4. What are the goals and needs of the user?

- A user wants to either give away a used but now unwanted item
- A user needs an item and would be interested to have one already used before
- Both users want to be able to do the exchange without much stress and complexity
- Need for an efficient and quick exchange while having the beautiful opportunity to have human contact
- Users might also want to get more information about the organisation or network so they might engage

### 5. What are the goals and needs of the business?

- To use the online platform to promote and help reuse and recycle within its members
- To have an online easy platform to use with a unique and beautiful design to attract REusers...
- To raise awareness among the larger community that giving away and REuse is fun, cool and trendy!
- To encourage community exchange which is started online but often continue within the community by more engagement
- To have local charities and charity shops participating by either giving away or taking used items
- To have less items being thrown away and less consumption
- To follow up with community events related to freeREuse like Clothes Swap for adults or kids, repair cafes
- While the platform being promoted locally, the goal of organisation would be to expand its geographical engagement

[Back to Top](#table-of-contents) 

### 6. Research

#### Who else is building this?
- https://freecycle.net/: Information page about Freecycle concept
- https://www.freecycle.org/: Global and main website where free exchange happens
- https://www.freetradeireland.ie/: Local free exchange website
- http://www.freeuse.org/
- Any Facebook page that offer this type of free items exchange: people who want to give away send a Facebook post on the page. Since no record of available items anywhere, other users would need to scroll down on Facebook page to find old posted items

#### How are they doing it?
- An information page about Freecycle network and concept of reuse, recycle for free, explaining the best practices of being a local network member
- Global network has hundreds of smaller groups where you become a member before you can view posts
- To add item, member has to send post to offer item and send another post to want item
- Post is sent to server via a form with dropdown options of offering or searching, group location, brief description, more precise location of member, text area for more description. Image can be attached to post
- Once published, the member can manage his posts to edit, cancel and delete it or mark it as gone and delete it
- Post is then published to the group by order of latest published
- User login system 
- All items showing as card
- Search option by user type (household, business, school) and then refined search by item category. 
- User can also search by item name and location. 
- Map added to show user location 
- Item owner contact details only showing to user if logged in.
- Can view all items posted by same user.

#### What are the pros of what they are doing?
- User login system
- I like the idea of only showing contact details of item owner when other users are logged in, for privacy reasons.
- Responding to a post about a given item directly send email to item owner and all further contacts are done privately. Not sure if I can do it using my acquired knowledge so far.
- Having an extra page where users can find more information about the concept and history of the free reuse movement.
- An interactive map showing the location of the user as shown on the item being given away
- Search option by categories and location
- Rules for using the network and offering or wanting items
- Having a moderator
- Non-liability disclaimer of the network advising its members that  they use groups at their own risk and to watch their personal information and security when exchanging an item

#### What could they do better?
- On one website, to make sure items are removed once taken away
- Improve responsive design of one website
- Add search option with different categories on one website
- Decluttering the heavy content which is not useful to the users
- Moderator on one website, no moderator or rules on other website

[Back to Top](#table-of-contents) 

## 7. Planning

#### What relevant content should we deliver that fits our demographic?
- Quick description of the idea/concept
- About/information page about organisation/network and idea/concept behind website
- List of items being given away and available for taking: including image
- A search option with 4 drop down menu of different categories
- A button to sign up/log in
- A button to add item to be given away
- A button to want used item
- A button where to find user’s existing posts and where it can be edited or deleted
- Form to add item with 5 fields: To offer or to want, Item name, Item description, is or not urgent
- Form to edit or delete a post with used item

#### How can we make the content easily tracked and catalogued in an intuitive way?
Using database with clear collections and categories

#### Is the technology known and used appropriate? 
- JS will be used for all interactive movements and click of users
- Python will be used as syntax to fetch and send information between front-end and database
- Flask will be used to add information on html using templating language 
- the data will be recorded and rendered using MongoDB, noSQL database.

#### User expectations
1. List of available items showing before even logging in
2. Taken items to be removed from the list
3. Search option to find available items quicker depending of the category
4. Simple user login system not asking for much information or action of user
5. An easy to navigate website with accessible, updated and informative brief description
6. Links to take user if need to learn more
7. Rules of the network, liability information

#### Why are we so special? What additional value will it add to what is existing?
- Belongs to a specific local community vs global
- Run by a local organisation already engaged in the community
- Fun and trendy way of exchanging items compared to charity shops
- Clear and brief information about concept with links to other websites if needed
- Quick and easy to search and view available items before signing up
- Quick and easy to log in, add an item, edit it, delete it
- Nice and clear UX design

#### Importance and feasibility table:
TODO: will import table

TODO:Will add user stories here
##### As a general user, I am expecting:
* 

##### As a user aged between 6 and 10 years old, I am expecting:
* 

##### As a parent of child user, I am expecting:
* 

##### As a developer, I want:
* 

[Back to Top](#table-of-contents) 

## Scope plane: How?

### 1. Which features?

1. List of items showing as cards
2. Search option with categories
3. User login allowing all CRUD
4. Page about concept behind website
5. Non-Liability disclaimer, Rules
6. Links to organisation website and Facebook page for more contact

### 2. Content requirements
- Input form for adding, editing and deleting items to pass on MongoDB - with two collections: users and items
- CRUD activities

[Back to Top](#table-of-contents) 

## Structure plane: Organisation and functionality?

### 1. Organisation of functionality and content
a) One main page: find quick and useful information, log in and contact others
- From main page, user can view list of available items where necessary information is showing
- From main page, user can log in on modal and be re-directed again to main page with available items
- From main page, user can view each item, toggle down separate sections (image, description, contact…)
- From main page, user can click on contacting item owner which throws a modal to write and send email
- From main page, user can click to view his profile or his latest posts

b) User page: separated to avoid too much information on the same page and mixing different information
- User does not need to visit his user page at each visit, might only be for updating details or items given
- User can update his email address or location
- User can update or remove given items

c) Third page about concept, zero-waste organisation, rules of the group, non-liability disclaimer

### 2. Consistency of elements and relationships?
Regular use of pop up modals so user does not have to go from one page to another and get lost in the navigation

### 3. Is it learnable and intuitive for the user
- Can the user understand and easily navigate through the system when using it for the first time?
- Intuitive/learnable: Follow website convention with a top navbar, a footer, hyperlinked buttons for user to navigate quickly around
- Consistent: navbar is the same on all pages, color theme and font will follow along, icons and categories will be the same for each item given
- Visible: navigation will be large enough so quickly visible to any user and easy to click on
- Feedback for user: Buttons change colors when hovered, loader while data is loading during a search, error message pop up if form not correctly filled

## Features
### 1. Existing Features:
* Feature 1 - 

### 2. Features Left to Implement:
* 

[Back to Top](#table-of-contents) 

### 4. Information architecture
- Information architecture
- Linear flow from one page to another 
- Non-linear flow where user can do different tasks via pop up modals
- Navbar and hyperlinks available on each page to keep user alerted

### 5. Data structure
Data model with two collections where User Name creates relationship between collections

TODO: will import table
	
## Skeleton plane: Presentation and navigation? 
### 1. Wireframes
TODO: add wireframes

I used Balsamiq tool for the wireframes and attached them to the directory in assets. 
I spent a considerable amount of time doing wireframes in details as I had no clue of design before and wanted to have a clear idea of how the website looked like.

- [Home]()
- 

The skeleton plane: 
- How will our information be represented, and how will the user navigate to the information and the features?
- how the information should be implemented?
- How will the user navigate through the information and the features?
- How will the content relate to each other? What relationships will the content have?
- What has priority? What has top priority? What has lower priority?
- And based on those priorities, where do we position the content?
- How do we navigate to those higher and lower priorities?

## Surface plane: How does it look like?
- What colors?
- What typography are we going to put in place?
- What images? What design elements?
- What animations, if any? What transitions?
- What other effects are going to be in place?

## Design
### 1. Color scheme

### 2. Font
Special Elite, Nanum Pen script, Cabin sketch(opposite of permanent), Chewy

Kaushan Script
Bangers
Indie Flower

### 3. Logo

[Back to Top](#table-of-contents) 

# Testing

## Final and official testing:
  * [W3 MarkUp validation](https://validator.w3.org)
  * [W3 CSS validation](https://jigsaw.w3.org/css-validator/)

I checked the validity of my code at different times and received few errors on HTML markup which I worked on correcting. I did not get any errors with my CSS.


## General testing:
As I did not have a lot of time and I was not really expert in Jasmine or any automating testing, I decided to do all the testing manually via the browser and Chrome Developer tools.
My strategy is very simple: as soon as I write a line of code, I open the page in my browser to test it, make sure it works until I am fully happy with what I see and how it functions. 

For each feature I was working on, I tried to preview it in Chrome Dev tools to understand quickly which HTML element, CSS styling or Bootstrap class would cause a certain effect and correct it as soon as possible. 
This also allowed me to fully comprehend the languages, to work by small tasks and push to GitHub only after I made the whole feature was working well.

Once I was quite happy with the design and the site responsiveness, I moved to Javascript and performed the same manual tests as above. 


## Testing in different browsers:
I used Google Chrome as my primary browser and constantly tested it on my mobile phone also using the same browser. 
I also tested the game on Safari via an iMac with a very big screen and an iPod touch with probably the smallest screen regularly and never found any specific issue. 

## General testing and learning experiences for the code itself:

### 1. 
* __Goal__: 

* __Result__: 

### 2. :
* __Goal__: 
* __Implementation__: 

* __Issue and new implementation__: 
* __Issue and new implementation__:
    
* __Result__:
    

## Issues found and solved

### 1. 
* __Issue__: 
* __Fix__: 
    
* __Verdict__: 




[Back to Top](#table-of-contents) 

# Technologies Used
- [GitPod](gitpod.io) - I used __GitPod__ as my IDE for the development of this website.
- __HTML__ language is used to create the structure of the website and game.
- __CSS__ language is used to add styling on the structure of the website.
- [BootstrapCDN](https://www.bootstrapcdn.com/) - The website is using __Bootstrap4__ as the basic structure and grid of the website and to increase the responsiveness of the website.
- [jQuery](https://jquery.com/) and [Popper.js](https://popper.js.org/) - The website uses __jQuery__ and __Popper.js__ to bring in Javascript which makes the navbar responsive
- __Javascript__ functioning language is used to fetch external data and add interactivity on the website so the game functions based on user's actions
- [jQuery](https://jquery.com/) - I used jQuery to avoid repeating same actions on the DOM when buttons were clicked
- [FontAwesome](https://kit.fontawesome.com/f7e192f540.js) - The website is using __Font Awesome__ to display the social media icons in my footer
- [Google Fonts](https://fonts.google.com/)- The website uses __1 Google font__- Url imported in CSS
- [AutoPrefixer](https://autoprefixer.github.io/) - I have used __AutoPrefixer__ to make sure the css code worked on all browsers
- [Tiny.jpg](https://tinyjpg.com) - I have used __Tinyjpg__ to compress logo image of the website to increase the website loading on browser
- [ColorSpace](https://mycolor.space) - I have used __ColorSpace__ to find matching colors for the website
- [Balsamiq](https://balsamiq.cloud) - I have used __Balsamic__ to build the wireframes which I then exported to the IDE
- [Favicon converter](https://favicon.io/favicon-converter/) - I used Favicon converter to convert the logo into a favicon which I was able to insert in the asset folder and I tested it to be working
- [Sweetalert2](https://sweetalert2.github.io/)
- [Unicorn Revealer](https://chrome.google.com/webstore/detail/unicorn-revealer/lmlkphhdlngaicolpmaakfmhplagoaln?hl=en-GB)
- [Lunapic](https://www2.lunapic.com/editor/) - to make the logo transparent

# Media and Content origin
- Taglines: [BrandonGaille](https://brandongaille.com/list-45-catchy-recycling-slogans-and-great-taglines/)
- Photos:
- Photo by Kevin Jarrett on Unsplash
- Photo by Susanne Jutzeler from Pexels
- Photo by Afta Putta Gunawan from Pexels
- Photo by Jon Watkins from FreeImages
- Photo by Griszka Niewiadomski from FreeImages
- Photo by Alaa Hassan from FreeImages

#### Other Resources:

# Deployment
I have been using the Integrated development environment (IDE) [GitPod](gitpod.io) to develop this milestone project.
As I used it for the first time and Code Institute changed the preferred IDE for the whole course, I was lucky to avail of the full template prepared by Code Institute at the time.

I went to Code Institute [full template repository](https://github.com/Code-Institute-Org/gitpod-full-template), cloned it and created my own repository with the template ready. From there, I opened GitPod which started a workspace.

From that point, I could add, commit any update of my code and push it to the remote repository so it could be regularly backed up and accessed by others.

## Enabling GitHub Pages to publish site from master as a publishing source

* Opened up GitHub in the browser.
* Signed in using username and password.
* Selected my repositories.
* Navigated to [FlagGame repository](https://github.com/mkuti/FlagGame_milestone_2).
* In the top navigation clicked 'settings'.
* Scrolled down to the GitHub Pages area.
* Selected 'Master Branch' from the 'Source' dropdown menu.
* Clicked to confirm my selection.
* Your site is published [https://mkuti.github.io/FlagGame_milestone_2/](https://mkuti.github.io/FlagGame_milestone_2/)

When I submitted this Milestone project, I confirmed that the Development Branch and Master Branch are identical.

## How to run code locally

1. On GitHub, navigate to the main page of the repository
2. Under the repository name, click Clone or download
3. In the Clone with HTTPs section, click to copy the clone URL for the repository
4. Using favorite IDE, open Terminal
5. Change the current working directory to the desired file location
6. Type git clone, and then paste the URL you copied in Step 2 when git clone: [https://github.com/YOUR-USERNAME/YOUR-REPOSITORY ](https://github.com/YOUR-USERNAME/YOUR-REPOSITORY)
7. Press Enter > Your local clone will be created.

### Credits


# Special thanks



##### Disclaimer:
The content of the website is for educational purposes only.

[Back to Top](#table-of-contents) 