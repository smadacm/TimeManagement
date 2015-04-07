Time Management System
======================

The basic concept is there are many clients with many projects composed of many tasks, each assigned to a given person.
This is not intended to serve as a large corporate organizer, but more as a tool to help individuals stay abreast of their obligations.
I built this to keep myself organized, so it may not be perfect for everybody.
Everything I wrote is licensed MIT, as far as I'm concerned.
I've tried to keep with only projects licensed MIT, but if I've missed something, I'll correct what I need to as soon as I know.

This project uses
- Python ( http://www.python.org )
- Django ( http://www.djangoproject.com )
- Bootstrap ( http://www.getbootstrap.com )
- Flatly Bootstrap theme ( https://bootswatch.com/flatly/ )
- jQuery ( http://www.jquery.com )


To install on Linux:

    $ git clone <url>
    $ cd TimeManagement
    $ virtualenv venv
    $ source venv/bin/activate
    $ ./reset.sh
    $ python manage.py runserver
    
Mac's should be relatively the same.
The reset.sh script should be easily adaptable to a simple batch file
