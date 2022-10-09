# SmartFeed - TAMU Datathon

### Inspiration
In today’s world where social media has such a significant impact in our lives, there is so much of information expressed by users online. From trivial things like the weather to controversial topics like politics and war- users rely on social media to express their views on any topic they desire. It is fascinating to note that different topics can have different kinds of reactions from different users- some may feel excited about it, others may get offended by it whereas some may be completely neutral or unaware about the topic altogether. This is why it is important to be able to extract the underlying sentiment behind such data posted on the internet today.

This project focuses on analyzing the underlying sentiments behind categorized tweets from Twitter.

### What it does
Data is extracted from Twitter and the training model identifies the underlying sentiment behind these tweets. This is then displayed to the users depending on what category of tweets they want to see and also what underlying sentiments. The workflow is as follows: 
- Allows new users to register by creating an account. Existing users can log in by providing their username and password. 
- The user can choose to view tweets from a variety of topics such as soccer, food, Hollywood, etc. Additionally, the user can search for a topic which is of his interest. The user can also select from the drop down if they wish to see positive, negative or all sentiments pertaining to the selected topic.
- The latest tweets of the topic selected will be displayed with their details.

### How we built it
The following technologies have been used and these individual components have been integrated together to give us the desired outcome: 
- AWS EC2, Lambda and API Gateway • MySQL Database 
- Django framework with HTML and CSS for the frontend 
- Twilio for sending text messages to users on their mobile devices

### Challenges we ran into
- Training the backend model
- Since our team mostly comprises of data science/ML developers and enthusiasts, we struggled a bit with the front-end side of things.

### Accomplishments that we're proud of
- Successfully scraped Twitter’s data and can display the tweets based on a specified category. 
- The model is efficiently able to segregate positive, negative and neutral tweets from a given topic.

### What we learned
- How AWS technologies are integrated together effectively
- The ease of working with the Django Framework
- How to train a model to effectively extract the required data

### What's next for SmartFeed
We aim to scrape data from other social networking sites as well such as Reddit. This will scale up our project and allow us to cover more data for better results.

### Built With:

* HTML: Page layout has been designed using HTML.
* CSS: CSS has been used for the designing part.
* Python: All the project design has been written in python.
* MySql: MySQL database has been used as a database for the project.
* Django: Django framework used as front-end.
* AWS EC2: Website is hosted on Amazon EC2 and S3
* Twilio: Messaging service used to send tweets to the user’s phone.


### Application Flow
* Existing users can log in by entering their username and password.

<img width="1440" alt="Screen Shot 2022-10-09 at 12 48 01 PM" src="https://user-images.githubusercontent.com/61991774/194769443-1b8adb86-fc0e-456b-95b7-e6f487fa3ed9.png">

* New users can register by creating an account. The user needs to enter his details here in order to create an account.

<img width="1440" alt="Screen Shot 2022-10-09 at 1 00 44 PM" src="https://user-images.githubusercontent.com/61991774/194769809-cef36294-d1c2-4842-ad93-1a57c391c85c.png">

* Once logged in, the user is presented with a variety of topics to view tweets of. If the user doesn't see his topic of interest, he can search for it by typing in the text box and clicking on "Submit". The user can enter multiple topics by clicking on "Add another topic".

<img width="1423" alt="Screen Shot 2022-10-09 at 1 05 02 PM" src="https://user-images.githubusercontent.com/61991774/194770008-254a4a21-c41a-4bbb-ba9b-955a3b3bde31.png">

* On the next page, the user is prompted to select one of the topics he selected in the previous page. He can also select the vibe of the requested tweets- positive, negative, neutral or all. The user can then enter his phone number (which must be pre-verified on Twilio) and then he will receive text messages of the requested tweets on that number. 

<img width="1435" alt="Screen Shot 2022-10-09 at 1 07 04 PM" src="https://user-images.githubusercontent.com/61991774/194770152-50f37ff4-80bb-4bc3-b0c3-61d523b55395.png">

* In the end, the user can see the requested tweets with the desired vibe he selected.

<img width="1440" alt="image" src="https://user-images.githubusercontent.com/69919392/194770770-80c07db7-37ba-42c0-bffd-5666e3d2974e.png">
