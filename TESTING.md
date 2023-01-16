* [Testing](#testing)
    * [Validator Testing](#validator-testing)
    * [Automated Testing](#automaten-testing)
    * [Manual Testing](#manual-testing)
    * [Bugs](#bugs)
    * [Unsolved Bugs](#unsolved-bugs)

---

## Testing

### **Validator Testing**

  * **HTML**

  * **CSS**

  * **Python PEP8**

  * **Lighthouse**

### **Automated Testing**


### **Manual Testing**

### **Site Navigation**

| Element                | Action        | Expected Result                                                    | Pass/Fail |
| ---------------------- | ------------- | ------------------------------------------------------------------ | --------- |
| **Main navbar**        |               |                                                                    |           |
| Home Link              | Click         | Redirect to homepage                                               | Pass      |
| Browse Art Dropdown    | Click         | Display menu link 'Past Challenges'                                | Pass      |
| Past Challenges Link   | Click         | Redirect to Past Challenges page                                   | Pass      |
| Signup Link            | Click         | Redirect to signup page                                            | Pass      |
| Signup Link            | Display       | Not visible to logged in user                                      | Pass      |
| Login Link             | Click         | Redirect to login page                                             | Pass      |
| Login Link             | Display       | Not visible to logged in user                                      | Pass      |
| Logout Link            | Click         | Direct to logout confirmation page                                 | Pass      |
| Logout Link            | Display       | Only visible to logged in user                                     | Pass      |
| **Main Navbar Mobile** | Responsive    | Collapses on smaller screen sizes <575px                           | Pass      |
| Collapsed navigation   | Click/Display | Identical links, expected results are the same as above            | Pass      |
| **User Navigation**    |               |                                                                    |           |
| Dropdown user menu     | Click         | Displays links to user profile pages "Your posts" and "Favourites" | Pass      |
| Your Posts Link        | Click         | Redirect to logged in users profile page                           | Pass      |
| Favourites             | Click         | Redirect to logged in users favourites in profile page             | Pass      |

### **Home and Past Challenges Pages**

| Element                    | Action  | Expected result                                                                                     | Pass/Fail |
| -------------------------- | ------- | --------------------------------------------------------------------------------------------------- | --------- |
| **Homepage**               | Display | Display challenges with 'Active' status, e.g challenges that are not older then 48 hours            | Pass      |
| **Past Challenges** page   | Display | Display challenges with 'Inactive' status, e.g challenges that are older then 48 hours              | Pass      |
| Active Challenge Card      | Display | Display a badge with text "NEW! + todays date" if challenge is posted the same date as current date | Pass      |
| Active Challenge Card      | Display | Display how much time has passed since challenge was posted                                         | Pass      |
| Browse Artwork Button Link | Click   | Redirect user to the post list page displaying the user submissions for that challenge              | Pass      |
| Submit Button Link         | Click   | Redirect user to the post submission form page if user is logged in                                 | Pass      |
| Submit Button Link         | Click   | Redirect user to Sign In page if user is not logged in                                              | Pass      |
| Submit Button Link         | Display | Not displaying on 'Inactive' challenges                                                             | Pass      |





### Bugs

#### 
  * **Fix** - 

#### 
  * **Expected** - 
  * **Testing** - 
  * **Fix** - 

#### 
  * **Expected** -
  * **Testing** - 
  * **Result** - .
  * **Fix** - 


### Unsolved bugs
No known unsolved bugs.
 
---