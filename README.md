# Seoda By Sophie

| ![Screen Size Responsiveness](/assets/readme_images/responsive_screens.png) |
|:--:|
|Seoda By Sophie|

**Seoda By Sophie** is an retailer of hand-made resin earrings based in Limerick, Ireland. With this website the business aims to move from selling on third-party stores and begin to offer their products to customers directly.

The website makes use of the high quality content already produced by the active social media presence of the business and adds extras to create an engaging experience from start to finish for customers.

When making purchases, a card number of 4242 4242 4242 4242 with expiry date 04/24 and security code 242 can be used to test checkout functionality.

The live site can be found [here](https://seoda-by-sophie-35b513cfd1a1.herokuapp.com/)

# Table of Contents
- [About](#seoda-by-sophie)
- [Features](#features)
- [Design](#design)
- [Agile](#agile-implementation)
- [Tools and Technologies](#tools-and-technologies)
- [Marketing](#marketing)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)

# Features

Here is a brief overview of the site features, it is recommended to explore the site to get a better idea of the experience.

## Navigation

| ![Main Nav](/assets/readme_images/nav_main.png) |
|:--:|
|Main Navbar|

| ![Mobile Nav](/assets/readme_images/nav-mobile.png) |
|:--:|
|Mobile Navbar|

## Footer

| ![Footer](/assets/readme_images/footer.png) |
|:--:|
|Footer including copyright, newsletter signup and social media links|

## Landing Page

| ![Landing Page](/assets/readme_images/landing_page.png) |
|:--:|
|Landing page including link to all products page|

## All Products

| ![Products Page](/assets/readme_images/products_page.png) |
|:--:|
|All products page including links to product, product info and filtering tools|

## Product Details

| ![Product Details](/assets/readme_images/product_detail.png) |
|:--:|
|Product Details including image, product info and link to add to basket. Links also present for admin to edit or delete products.|

## Basket

| ![Basket](/assets/readme_images/basket.png) |
|:--:|
|Basket including product summary, price breakdown and controls to adjust order|

## Checkout

| ![Checkout](/assets/readme_images/checkout.png) |
|:--:|
|Checkout including order summary, shipping form and stripe payment integration|

## About

| ![About](/assets/readme_images/about.png) |
|:--:|
|About page with info on business and testimonials|

## FAQs

| ![FAQs](/assets/readme_images/faqs.png) |
|:--:|
|FAQs page with questions and answers|

# Design
The design process was structured using the five planes of UX - **Strategy, Scope, Structure, Skeleton & Surface**. Each Section is discussed more in depth in the Design document in the repository, which can be found [here](DESIGN.md).

The colour palette was based on existing business logos seen on the current [Etsy shop](https://www.etsy.com/ie/shop/SeodabySophie) and outlined below

| ![Final Color Palette](/assets/readme_images/color_palette.png) |
|:--:|
|Colour Palette|

# Agile Implementation
An Agile methodology was used in the development of this site, structuring and scheduling the workflow. Work was broken into sprints with the MVP being the completion of outlined user stories. These were categorised as 'must have' or 'should have' in order to efficiently allocate time to the project.

The implementation of this process can be seen clearly on my [GitHub project board](https://github.com/users/eosull/projects/8).

User stories were tracked using a google sheet containing links to Github project, epics and issues where further info such as milestones, labels and priorities can be seen:
[User Story Tracking](https://docs.google.com/spreadsheets/d/1cLw34TLgnHsWQUCyxNQNolB0Wog3KuQlkmCOjkjQZpg/edit?usp=sharing)

## Sprints

Sprints are outlined below, follow GitHub link for each for more in depth information.

### Sprint 1 - [GitHub Link](https://github.com/eosull/Seoda-By-Sophie/milestone/2)
This sprint consisted of project setup, authentication, base template and products setup.

### Sprint 2 - [GitHub Link](https://github.com/eosull/Seoda-By-Sophie/milestone/3)
This sprint consisted of the creation of basket functionality and addition of feature for site admin to edit content on site

### Sprint 3 - [GitHub Link](https://github.com/eosull/Seoda-By-Sophie/milestone/4)
This Sprint covered the completion of CRUD functionality for site admin as well as the implementation of a secure checkout process using Stripe and a full user profile app.

### Sprint 4 - [GitHub Link](https://github.com/eosull/Seoda-By-Sophie/milestone/5)
This sprint covered the completion of MVP tasks for the site including contact forms, newsletter, custom FAQs site SEO and deployment.

### Final Sprint - [GitHub Link](https://github.com/eosull/Seoda-By-Sophie/milestone/6)
This sprint covered the final project submission for CI PP5 E-Commerce Project

# Marketing
Seoda By Sophie is a small business run by one individual and the goal is to turn a hobby into a profit-making enterprise. As a result the web marketing strategies chosen are free and low-cost/targeted expense. The main strands of this campaign are:

  - SEO and content marketing
  - Organic Social Media marketing
  - Scheduled Paid Social Media marketing
  - Email Newsletter subscription

## SEO
The implementation of SEO best practices in this site are as follows:
  - Use of semantic HTML
  - Avoiding keyword stuffing
  - Adding meta information in head element
  - Ensuring images have alt descriptions
  - Adding rel attribute with noopener to external links

Key words included short-tail and long-tail and were decided on using a combination of google search recommendations, google trends and free features of [wordtracker.com](https://www.wordtracker.com/)

2 additional files, sitemap.xml and robots.txt, were added to assist search engines like Google understand the website structure and state the scope of the SEO search to be carried out.

##  Social Media
Seoda By Sophie has two main social media presences; [Instagram](https://www.instagram.com/seodabysophie/) and [Facebook](https://www.facebook.com/profile.php?id=61552129821660).

An Instagram account was already created for the business and contains photos of products, customer testimonials and informational content

| ![Instagram](/assets/readme_images/ig_screenshot.png) |
|:--:|
|Instagram Page|

A Facebook business page was created while creating this website and contains business info and a link to the online store

| ![Facebook Page 1](/assets/readme_images/fb_screenshot_1.png) |
|:--:|
|Instagram Page 1|

| ![Facebook Page 2](/assets/readme_images/fb_screenshot_2.png) |
|:--:|
|Facebook Page 2|

These social media pages are intended to engage with customers and share content that organically grows an audience. This free form of marketing is the most useful to the business at its current stage. 

Paid or sponsored posts will be used strategically to market products, such as coming up to gift-buying periods like Valentines Day and Christmas or when products are low in stock and it is a customer's last chance to buy.

## Newsletter
A newsletter was implemented in the footer of the site using Mailchimp. This gives a user a chance to subscribe to hear about new products or promotions and is a cost-effective method of marketing to customers who are interested in the products offered on the site.

# Tools and Technologies
- [HTML5](https://en.wikipedia.org/wiki/HTML): Markup Language
- [CSS3](https://en.wikipedia.org/wiki/CSS): Styling
- [Javascript](https://en.wikipedia.org/wiki/JavaScript): Dynamic site content
- [Python](https://www.python.org/): Used in conjunction with Django to render site
- [Django 4.2](https://docs.djangoproject.com/en/4.2/): Database-orientated framework to build site
  - [Django AllAuth](https://django-allauth.readthedocs.io/en/latest/): Django application to handle account management
  - [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/): Django application to handle form rendering
- [Bootstrap](https://getbootstrap.com/): Front-end toolkit
- [Elephantsql](https://www.elephantsql.com/): PostgreSQL database hosting
- [AWS](https://aws.amazon.com/): Hosting of Media and Static files
- [Psycopg2](https://pypi.org/project/psycopg2/): PostgreSQL database adapter for Python
- [Google Fonts](https://fonts.google.com/): Import fonts to use on site
- [Bootstrap Icons](https://icons.getbootstrap.com/) Icons on the site
- [LucidChart](https://www.lucidchart.com/): Diagrams, flowcharts and wireframes 
- [Code Institute Student Template](https://github.com/Code-Institute-Org/gitpod-full-template): Template for repository

# Testing
Testing was completed throughout the development of the site as can be seen in the [Testing](TESTING.md) file. This included manual tests for functionality, accessibility, code validation and site goals.

# Deployment

**Database (ElephantSQL) Setup**
1. Create New Instance for project with free Tiny Turtle plan
2. Select EU-West-1 (Ireland) Data Centre
3. URL from instance summary to be used in Heroku configs

**AWS Setup**
1. Create new bucket
2. Choose closest available server (EU-West)
3. Enable ACLs for object ownership setting with bucket owner preferred
4. Uncheck block all public access
5. Enable static website hosting in properties
6. Copy following code into CORs configuration:
	[ { "AllowedHeaders": [ "Authorization" ], "AllowedMethods": [ "GET" ], "AllowedOrigins": [ "*" ], "ExposeHeaders": [] } ]
7. Generate policy statement using generator and add to settings
8. Add list permissions for everyone
9. IAM:
	  - User groups
	  - Create new manage-seoda-by-sophie group
	  - Create policy for all s3 access using bucket arn
	  - Attach policy to created group
	  - Create new user
	  - Add user to group
	  - Download user credentials as csv
10. User credentials to be used in Heroku configs

**IDE Setup**
1. Install dj_database_url and psycopg2 to connect to database
2. Import dj_database_url and os in settings.py file
3. Set ElephantSQL url as default database in settings.py
4. Migrate database models to new database
5. Create new superuser
6. Delete ElephantSQL url from settings
7. Add if statement in settings so app uses ElephantSQL url if url in heroku settings
8. Install Gunicorn to act as webserver
9. Add Procfile at base directory
10. Add heroku hostname to ALLOWED_HOSTS in settings.py
11. Update settings.py to take secret key from heroku vars
12. Install boto3 and django-storages. Add storages to installed apps
13. Add bucket name, server region and secret key (from heroku vars) to settings
14. Add S3 domain name for storage of static files
15. Add custom_storages.py file
16. Add staticfile and media file storage settings
17. Add media and static urls

**Heroku Deployment**
1. Create Heroku App
2. In ‘settings’ tab add config var DATABASE_URL with value of ElephantSQL URL
3. Add Disable_collectstatic=1 to config var for initial deploy
4. Generate new secret key and add to config vars
5. Add AWS keys to config vars
6. Add USE_AWS set to true to config vars
7. Remove Disable_collectstatic var for deployment
8. Link Heroku app to GitHub repository and set automatic deployment up

**Forking**
1. Navigate to the [GitHub Repository](https://github.com/eosull/Seoda-by-sophie) and click 'fork' in the top right of the page

**Cloning**
1. Navigate to the [GitHub Repository](https://github.com/eosull/Seoda-by-sophie) and click the green 'code' dropdown
2. Choose your format from HTTPS, SSH or GitHub CLI and copy
3. Open your terminal in your IDE and use git clone followed by this link


# Credits

## Code/Resource References
- Commit messages formatted based on [Conventional Commit Standards](https://www.conventionalcommits.org/en/v1.0.0/#summary) - useful cheatsheet for formatting these messages by Github user Zekfad [Here](https://gist.github.com/Zekfad/f51cb06ac76e2457f11c80ed705c95a3)
- Creation of Entity Relationship Diagram was completed using LucidChart resources [Youtube tutorial](https://www.youtube.com/watch?v=QpdhBUYk7Kk&ab_channel=LucidSoftware) and [associated article](https://www.lucidchart.com/pages/how-to-draw-ERD).

## Media
- Site colour palette generated using [Colormind](http://colormind.io/)
- Site Favicon generated using [Favicon.io](assets/favicon/favicon.ico)
- Site responsiveness mock up generated using [Am I Responsive](https://ui.dev/amiresponsive)
