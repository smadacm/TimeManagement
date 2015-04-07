Models
======
- Client
    - Need a default
    - Fields
        - Name
        - User (Many-to-Many)
- Project
    - Need a default
    - Fields
        - Name
        - Company
        - Priority
- Task
    - Fields
        - Name
        - Notes
        - Project
        - Severity
        - Required Effort
        - Due
        - Dependents (Many-to-Many)
- ClientNotes
    - Fields
        - User
        - Client
        - Note
        
Views
=====
- Dashboard
    - Async
        - Get Client List
        - Get Project List
            - client id
        - Edit Task Notes (easier to get to than moving to edit-task page)
        - Complete Task
- Project Details
- Client Details
- Project Edit
- Client Edit
- Task Search
- Login
