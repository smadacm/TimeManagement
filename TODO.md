Functionality
=====
- Dashboard
    - Async
        - Edit Task Notes (easier to get to than moving to edit-task page)
        - Complete Task
        - Unobtrusively add severity to add-task form
        - Make dashboard update asynchronously
    - Modularized
        - More panels
        - User able to setup and arrange panels
- Task Search

Code
====
- Dashboard modular views cleanup
- Including JS and CSS
    - Sucks
    - Figure out something better
    - Preferably some kind of hook-based system that can render in post-process middleware
    - Need to support less/sass
    - Maybe this: http://django-compressor.readthedocs.org/
    - And this: https://github.com/torchbox/django-libsass
- Dynamic (read: db-driven) menu
    - Maybe with hooks!
- Move Overhead to its own repo
    - include with git submodule or in requirements.txt
- Port to Python 3 and/or 6
- Figure out and excuse to use the antigravity package

Pretty
======
- Login is ugly
- Project, Client, and Task CRUD forms are ugly
- Add some kind of non-modal, flying JS box that swoops in from the top for most messages
- Add some kind of attention-getting error message box for forms, but still non-modal
