# smart-feed

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
amazon-web-services<br />
bootstrap<br />
css3<br />
django<br />
ec2<br />
html5<br />
lambda<br />
sql<br />
twilio<br />
