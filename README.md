# GitFit

* This is an Exercise Gamification App built by Team B-29 during the Spring 2021 semester of CS3240. The app is called “GitFit” and it essentially allows users to complete different types of workouts of various difficulty levels, earn points for completed workouts, submit their own workouts, etc.
* Team Members: Rodas Addis, Burhan Chaudhry, Ajay Desai, Alice Innis, Jefferson J. Pan

### Common Requirements:
* Google User Account: The primary way that users login to the app is by using their google user account. When accessing the app, a welcome page will show up and the user will be prompted to login to their google account before accessing the app. 
* Meaningful Functionality based on Login: Users can keep track of their workout progress, enter their weight and height, and make posts on a forum which displays their name under their post.
* Third-Party API: The Youtube Data API was used and incorporated in this project. This can be seen by going into the “search” folder of the project and then by looking at the views.py file of this folder. On the website, go to the home page and click on “Search Youtube” and then you’ll be directed to a page with a search bar. You will be able to search up a video from Youtube that you can watch.
* Tools and Frameworks: The project was built in Python3 and in the Django framework, hosted with Heroku, and used Travis-CI for continuous integration testing. 
Database Engine - The database for the project is PostgreSQL.

### Exercise Gamification Requirements:
* Gamification - Users who complete workouts are able to earn xp. When going to the “Workouts” page of the application, and choosing a workout. There will then be a list of workouts shown on the page, pick one and there will be a “Complete” button that the user can click on and earn xp. This xp can be viewed through the “Progress Tracker” on the top-menu bar.
* Account Information - Each user has a “Profile section” that can be accessed from the top-menu bar. This section will show the user’s progress and they can also input their height and weight.
* User Interaction - There is a forum for the website. This can be accessed by going to the home page and scrolling down to “Share Your Thoughts”. Click on “Post Your Thoughts” and a page with a list of forums will be displayed. Users can either create a new forum and title it or they can click on a pre-existing forum and make a new post on it. These posts will be displayed for other users to read through and respond.

### Cool Feature: 
* There is a “Challenges” section of the app that has QR codes that can be scanned and a challenging workout will be given.


