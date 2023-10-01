# Something Like Design Process

## Strategy
The strategy plane focuses on what the project aims to acheive, and for whom. Following design thinking practices a problem statement was generated to summarise the needs of a user:

- *As an owner of a small-batch jewellery making business am trying to sell my hand-crafted resin earrings. I currently sell these items using third-party craft selling sites and small stores in my local area. This means my products and their marketing are partly in the hands of another party and as a consequence I do not feel I have full control over the potential income that could be generated from the products. It is difficult to grow my business to the next level from a hobby/side-project without having independence to display, market and sell my products the way I would like.*

Considering how these needs could be met was key in developing the strategy for this project. The business owner's key need is independence and control over marketing and sales. Therefore, the central goal of the site is to **provide a platform for business owner to control and manage content and sell directly to customers**.

## Scope
Building on from the strategy and the goal outlined above, the scope of the project is concerned with the features to be included in the project.

### User Experience
The site should be:
- Intuitive and easily navigable
- Provide feedback to user actions
- Responsive to different screen sizes
- Accessible

### Functionality
The main functionalities of the site are as follows:
- A user can browse and purchase products
- A user can create a profile to save shipping info
- A user can track past orders via email and order history
- A user can learn about the business and get in contact with them
- An admin can add, edit and delete products
- An admin can add, edit and delete FAQs

### Content
The site should contain the following core content:
- Products with information, pictures and stock levels
- Information about business such as testimonials and FAQs

The implementation of these features successfully is the MVP for this project and are intended to be built on once they have been acheived. Implemented features and future additions will be detailed further in [Features Section](#features).

## Structure
The structure of the site was designed with two parts in mind; information design and the interaction design. Information design is concerned with how the information is structured on the site and the interaction design is concerned with how the user navigates this.

The site is designed so the user lands on the home page but is invited to the products page. Certain features are only accessible to authorised users. Unauthorised users will have access to read functionality, whereas create, edit and delete functionality will be limited to users with an account.

The nav elements will always be accessible via the header on the site. Feedback is provided for any action that creates or alters content via the use of confirmation messages.

| ![Information Design Flowchart ](/assets/readme_images/sbs_information.png) |
|:--:|
|Information Design Flowchart|

An entity relationship diagram was created for the purpose of meeting the MVP of the project. Each of these have a primary ID key and multiple foreign keys. The relationships are outlined in diagram below:

| ![Data Model ERD mk.1](/assets/readme_images/sbs_erd.png) |
|:--:|
|Data Model ERD|

## Skeleton
A simple wireframe of the site was created to visualise navigation, layout and design.

| ![Landing Page Wireframe](/assets/readme_images/sbs_landing.png) |
|:--:|
|Landing Page Wireframe|

| ![Product Page Wireframe](/assets/readme_images/sbs_product.png) |
|:--:|
|Product Page Wireframe|

| ![Profile Page Wireframe](/assets/readme_images/sbs_profile.png) |
|:--:|
|Profile Page Wireframe|

| ![Basket Wireframe](/assets/readme_images/sbs_basket.png) |
|:--:|
|Basket Wireframe|

| ![Checkout Wireframe](/assets/readme_images/sbs_checkout.png) |
|:--:|
|Checkout Wireframe|


## Surface

### Colour Scheme
The site has core colouring of an white with a tint of pink, with a blend of light pink and blue for headers, cards and buttons. Site text is black. Color scheme is detailed here:

| ![Color Palette](/assets/readme_images/color_palette.png) |
|:--:|
|Seoda By Sophie Color Palette|

### Font Styling
Google Fonts was used to import fonts. Oswald was used for headings and important content with Quicksand used for body text and site content.

### Images
All of the images were taken from the current online store of Seoda By Sophie on [Etsy](https://www.etsy.com/ie/shop/SeodabySophie)