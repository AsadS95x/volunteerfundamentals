# volunteerfundamentals
QA Fundamentals Project 

Use Case: A small website for volunteers to see what upcoming events are 
available as well as a platform for them to sign up to volunteer.

Website should allow Staff to update, remove or add events. As well 
as be able to see which volunteers have signed up to help out.

Basic Functionality at the moment, to show proof of concept. Fully working Home page with a variety of buttons. 
NOT ALL FUNCTIONS HAVE A BUTTON !!!

Register/Add Volunteer - Allows you to add a new volunteer
Update Volunteer  -  alllows you to amend or change a voluneers details
To delete a volunteer - you need to type in the at the end of the url /delvol/[volid]
Where vol id is the volunteer id number

Register/add Event - Self explantory, further details will be added in later on, such as events description 
 and time, as well as event lead details. 
 Update Event - amend or change event details for an existing event
 Delete Event - done through URL also by /deleteevent/[eventid]
 
 Assign Volunteers - can be assigned to specific events. 
 Show Assignmnets - Displays volunteers id and the event id for their assigned event.
 
 Currently functioning many-many table, but minor issues needs resolved. Delete Functionalty onthe assoication table not present.
 
 gunicorn installed - can be launched wtih gunicorn -b 5000 ipaddress aplication:app
 


