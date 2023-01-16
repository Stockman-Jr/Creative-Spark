# CreativeSpark

CreativeSpark is a website created for artist's of all skill levels, where daily drawing challenges will be provided for the community to participate in!
As most artists know, the more you draw the better you'll get, and purpose of this website is to provide artists with inspiration, since there are times you will run empty. 
A fun way to get ideas and improve your drawing skills!
Join the community and get tons of inspiration by participating in our drawing challenges and browsing amazing art submitted by your fellow artists! 


- - - 

## Table of Contents

* [User Stories](#user-stories)
* [Agile Methodology](#agile-methodology)
* [Design](#design)
* [Features](#features)
    * [Existing Features](#existing-features)
    * [Future Features](#future-features)
* [Testing](#testing)
    * [Validator Testing](#validator-testing)
    * [Manual Testing](#manual-testing)
    * [Bugs](#bugs)
    * [Unsolved Bugs](#unsolved-bugs)
* [Technologies Used](#technologies-used)
  * [Main Languages](#main-languages)
  * [Frameworks, Libraries & Programs](#frameworks-libraries--programs)
* [Deployment](#deployment)
* [Credits](#credits)
  * [Code](#code)

  
- - -
## User Stories

### As an unauthenticated user, I can:
  * Easily navigate around the application to view most content.
  * Click the 'Signup' navigation link to register and become a member.
  * View all challenges as well as posts submitted to each challenge.
  * View full posts.
  * View comments.


### As an authenticated user, I can:
  * Perform all tasks mentioned above.
  * Submit art to participate in challenges.
  * Leave comments on posts.
  * Like and unlike posts.
  * Add posts to favourites.
  * View other users profile pages.
  * Utilise my profile page to view my uploaded posts and my favourited posts.
  * Utilise my profile page update the title and caption of posts I uploaded.
  * Utilise my profile page to delete posts I uploaded.


### As a site admin, I can:
  * Perform all tasks mentioned above.
  * Approve user posts.
  * Delete comments, posts and challenges.


- - -

# Agile Methodology
An agile approach was implemented for this project with a Github projects kanban board which can be found [here](https://github.com/users/Stockman-Jr/projects/2).

An issue template was created for adding User Stories. Each User Story was added with a label of priority using the: **Must Have**, **Should Have** or **Could Have**.

For some of the User Stories an acceptance criteria was also added using the: **Given**, **When**, **Then**, **And** statements.

---

# Design

---
# Features

### Existing Features

#### Landing Page
![Header](assets/images/header-nav.png)
  * The landing page features the header with navigation links, text with introduction to the website and a list of active challenges the users can participate in.


#### Navigation
  * The navigation is simple but also provides the user with many options to navigate the page, and is passed down to all pages of the application through base.html.
  * For an unauthenticated user the navigation is in the header, featuring "Home", "Browse Art" with a dropdown link to inactive challenges, "Sign Up" and "Sign in".

  ![Unauth Navigation](assets/images/unauth-nav.png)

  *  For an authenticated user, the same navigation menu is available except 
    "Sign out" is available instead of "Sign Up/Sign In".
    This navigation is also responsive as it collapses on small screens.

  ![Auth Nav](assets/images/authenticated-nav.png)

  ![Mobile Nav](assets/images/mobile-nav.png)

  * Authenticated users will also have a user navigation available to them on all pages, displaying their profile picture with a dropdown menu in the right corner of the page.
    This user menu includes "Your Posts" and "Favourites", which navigates the user to their profile page.

    ![User Menu](assets/images/user-profile-menu.png)



#### Challenges
  * Challenges are displayed in bootstrap cards with a featured image, the drawing prompt and one or two button links.
  The cards provides the user with simple but clear information about the drawing challenge.
  * All challenges are open for submissions for 48 hours from the moment they are posted. The active challenges are displayed in the "Home" page, and the inactive challenges are displayed in the "Past Challenges" page.
  * An active challenge will display a badge with the text display with "New" and todays date if the challenge was posted the same day as the current date.
  Since challenges are time constrained, info about how much time has passed since it was posted will also be provided for the user.
  The button link "Browse Art" will direct the user to a page showing all the posts uploaded in that particular challenge, and the link with "Submit" will direct to user to the post submission form.
  ![Active Challenge](assets/images/challenge-card.png)
  * Inactive challenges are available for users to browse in the "Past Challenges" page with similar but less information.
  The submit button will not be available as users cannot participate in inactive challenges.
  ![Inctive Challenge](assets/images/inactive-challenge.png)


#### Browsing Artwork / Post List
  * When the user clicks the "Browse Artwork" link on a challenge, they will be redirected to a page displaying all the posts submitted to that challenge.
  * All user posts are displayed in bootstrap cards, and features the artwork, like button with like count, as well as information about the post.
  * Provided that the user is authenticated, they can interact with the like button to like or unlike a post and view the creator of the post's profile page by clicking on the avatar/username.
  ![Post Cards](assets/images/post-list-cards.png)
  * Hovering over the post's image will display a magnifying glass, and allows the user to view the full post by clicking on it.
  ![Image Hover](assets/images/card-img-hover.png)
  ---

#### **Full post view**
![Post Detail Modal](assets/images/post-detail-modal.png)
  * The full view of the post is displayed in a bootstrap modal, and features a larger preview of the artwork, more information, a favourite button and a comment section.
  * Provided that the user is authenticated, they can add a post to favourites by clicking on the favourite button. The user can also add comments.
  * Comments will be displayed directly upon submit without page refresh.
  * If user is not authenticated, they can view comments for that posts but the comment form is replaced with text including links to sign in page and sign up page.
  ![Unauth Modal](assets/images/unauth-modal.png)
---
#### User Profiles
  * Registered members will have access to their own profile page, well as    
   other users profile pages.
  * The logged in users personal profile page is accessible in the user menu in the top right corner, and links to other users profile pages are provided throughout the application. 
  For example when looking at your or others facourite posts, browsing posts and viewing full posts.
  * All profile pages includes a simple navigation with links to two galleries, a gallery displaying the users uploaded posts and one to show the users favourited posts.
  * The logged in users personal profile page will include two interactable icon links, 
  a trashcan which allows the user to delete their posts and an edit icon which allows the user to update their post.
  * The purpose of profile pages are to allow easy access to the users uploaded content to view, edit and delete
---
### Future Features
  * If provided more time, I would have wanted to create a "Winners" page, which would feature the most liked posts from every drawing challenge that's ended.
  * Give users the ability to update their profile, for example changing their profile picture and adding a bio.



---

## Testing

Testing documentation can be found [here](https://github.com/Stockman-Jr/Creative-Spark/blob/main/TESTING.md)


 
---

## Technologies Used

### Main Languages
  * HTML 5
  * CSS3
  * JavaScript
  * Python
  

### Frameworks, Libraries & Programs
  * Django - Main python framework used to to develop the application
  * JQuery - Was used in combination with AJAX to read, update and send data for comments and likes.
  * Bootstrap - For designing the html templates and speeding up the process of creating a responsive site.
  * [GitHub](https://github.com/) - To save and store files for the website.
  * Git - For version control.
  * [Fontawesome](https://fontawesome.com/) - For adding icons.
  * [Google Fonts](https://fonts.google.com/)
  * [Heroku](https://www.heroku.com/) - For deploying the project
  * [Am I Responsive?](https://ui.dev/amiresponsive) - To display website on different devices.
  * [ElephantSQL]() - Was used as the database for this project
  * [Cloudinary](https://cloudinary.com/) - For hosting media files


---

## Deployment


---

## Credits

### Code
  * [Stackoverflow](https://stackoverflow.com/)