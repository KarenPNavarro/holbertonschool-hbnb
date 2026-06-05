Author @KarenPNavarro for Holberton School

**HBnB Evolution**

A simpler version of an AirBnB style App. Users can sign up, lists places to stay, leave reviews and use tags for amenities. 

**What does this project do?**

*User Management*: Users can register, update their profiles, and be identified as either regular users or administrators.

*Place Management*: Users can list properties (places) they own, specifying details such as name, description, price, and location (latitude and longitude). Each place can also have a list of amenities.

*Review Management*: Users can leave reviews for places they have visited, including a rating and a comment.

*Amenity Management*: The application will manage amenities that can be associated with places.

**How the HBnB App organized**

It has three layers. Each has an specific job and can only talk to the layer directly below it through the facade.

*Presentation Layer*: This includes the services and API through which users interact with the system.

*Business Logic Layer*: This contains the models and the core logic of the application.

*Persistence Layer*: This is responsible for storing and retrieving data from the database.

**The main building blocks**

User — a person using the app.
Place — a property someone lists.
Review — feedback (a rating and comment) on a place.
Amenity — a feature a place offers.

All four share a common base that gives every object a unique ID and created_at /
updated_at timestamps.

**Whats in the project?**
High-Level Package Diagram *package_diagram.md*
Create a high-level package diagram that illustrates the three-layer architecture of the application and the communication between these layers via the facade pattern.

Detailed Class Diagram for Business Logic Layer *class_diagram.md*
Design a detailed class diagram for the Business Logic layer, focusing on the User, Place, Review, and Amenity entities, including their attributes, methods, and relationships. Ensure to include the relationships between Places and Amenities.
S
equence Diagrams for API Calls *sequence_diagrams.md*
Develop sequence diagrams for at least four different API calls to show the interaction between the layers and the flow of information. Suggested API calls include user registration, place creation, review submission, and fetching a list of places.

Documentation Compilation *README.md*
Compile all diagrams and explanatory notes into a comprehensive technical document.

The diagrams are written in Mermaid, which GitHub renders automatically, open the .md files in your browser to see the pictures.