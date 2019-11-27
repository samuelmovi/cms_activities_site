# ACTIVITIES SITE
Customizable DjangoCMS web application geared towards personal or community sites that would like to publish 
information about their "activities", whatever they might be.
 
Even though many, if not all, of the functionality of these plugins could have been achieved by using 3rd-party 
plugins, every single functionality in this project is implemented with its own custom plugins. I did that as a 
learning experience, and because I prefer my software lean. And and I like knowing how it does what it does.


## Requirements
- Python 3.7
- Django 2.2.3
- DjangoCMS 3.7.0
- FontAwesome5
- W3.CSS
- jQuery
- Docker, Docker-Compose

## Installation
- Clone the repository
- `sudo docker-compose up`
- `sudo docker-compose run web bash`
- From within the containers shell:
    - `python manage.py makemigrations *`
    - `python manage.py migrate`
    - Run tests: `python manage.py test`
    - Create admin user: `python manage.py createsuperuser`
    - Start server: `python manage.py runserver 0.0.0.0:8000`

## Usage
- Create one page per type of activity
- Create all other as sub-pages of that page
- Add Card Grid showcasing subpages


## Layout
It's a single-column responsive design. The final composition is up to the designer, but with the built-in components:
- Contact Bar
- Photo Carousel
- Navigation Bar
- Content: Tex Bubbles and Card Grids
- Footer: with Contact Form

## Pages Types

### Activity pages
Their structure is:
- Photo Carousel in carousel area
- 2 Text Bubbles in content area(for activity description, and for service details)
- Contact Form in footer


## Plugins

### Top Contact Bar
Top, sticky, responsive bar displaying the site's favicon on the left, and a list of icons for the different contact 
options: social media, telephone, email, etc.

Usage:
- Add `contact_bar_plugin` to your template. It will hold the contacts
- Add `social_contact`s to the bar until satisfied
    - Name
    - Link: link to social profile, or `mailto:` for email and `tel:` for phone numbers
    - Text
    - Icon: FontAwesome class name (`fa-twitter`, `fa-whatsapp`, `fa-facebook`, `fa-envelope`, `fa-phone-square`, etc.)

Mind the number of icons, as it can mess with the bar rendering in smaller screens. You can change the css value for 
the responsive break in `activites_site/static/css/style.css`.


### Photo Carousel
It add a minimalistic photo carousel, with a delay of 1.5 seconds.
Usage:
- Add a `PhotoCarousel` container to the page.
- Add as many `CarouselPhotos` to the `PhotoCarousel` as you need.

### Navigation Bar
TODO

### Text Bubble
Simple plugin that adds a blob of text inside of a round-corner colored "bubble".
The text allows for simple html tags, for structure.
The bubble is preceded by an `h2` title header.

### Activity Cards Grid
Create compact cards for any of the activities in the site (or anything else you want, really).
When clicked on, they display a modal window with an excerpt from the activity, and a link.

Usage:
- Add the activity card container to the page
- Add as many activity cards to it as you need:
    - Name: unique name for the container
    - Title: text displayed on the card, and as the title of the modal windows
    - Text: excerpt from the activity (1000 characters)
    - Image: used fot the card
    - Link: href for the link at the bottom of the modal window

### Contact Form
Displays a contact form for the site.
The fields are:
- Name 
- Email
- Arrival date: with a date-picker
- Party size: number picker
- Reference: how they found you
- Experiences: text area for them to describe in length what they want (1000 characters)










## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
