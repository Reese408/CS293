# CNC Construction Web Application/Final Project

## Overview

The **CNC Construction** web application is designed to showcase available construction projects, allowing users to submit quote requests. It provides a user-friendly platform with authentication and session management, built using **Django** for the backend and **HTML/CSS/JavaScript** for the frontend.

This app allows users to register, log in, submit quote requests for projects, and manage their submissions through a dynamic, responsive interface.

## Features

- **Custom User Authentication**: Email-based login and user management with a custom user model.
- **Project Listings**: Users can view available construction and pool projects.
- **Quote Submission**: Logged-in users can submit quote requests for specific projects.
- **Role-Based Permissions**: Admin users (superusers) can manage other users and view all quote requests.
- **Responsive Design**: The application adapts to different screen sizes, ensuring a smooth user experience across devices.

## Distinctiveness and Complexity

### Distinctiveness: What Makes This Project Stand Out?

This **CNC Construction Web Application** stands out due to its **integration of custom user management** and **project-specific quote handling**. Unlike simpler applications, this project involves **multiple interrelated components**, from **user authentication** to **dynamic project listings** and **quote request management**.

One of the key distinguishing factors of this project is the **custom user authentication model**. In many Django applications, the default `User` model is used, which typically relies on a username and password combination for authentication. In this project, however, I’ve implemented a **custom user model** using `AbstractBaseUser` to allow **email-based authentication**. This is a more modern approach and better reflects real-world scenarios where emails are often the primary identifiers for users. Additionally, the project includes role-based user permissions, ensuring that **admin users** have access to more advanced features (such as user management and quote request oversight), while **regular users** can only manage their own quote requests.

Another notable feature is the **quote submission and management system**. In contrast to projects where users can only view items (such as listings or details), this project allows users to **submit dynamic data** (i.e., a quote request), **edit it**, and **view it** in real-time. This creates an engaging user experience, as users can interact with the system beyond just browsing or viewing static content. The quotes are associated with the user who submits them, ensuring that each user has access only to their submissions and can edit or delete them as needed. This level of interactivity and the ability to track **stateful user-submitted data** is a major distinguishing feature from basic project management or listing applications.

The inclusion of **project categories**, such as **Pool Construction**, **Home Renovation**, and **Landscape Design**, further adds complexity and specificity to the application. These categories are not just used for display purposes; they influence how users interact with the platform and submit their quotes. By segmenting projects into distinct types, the app allows users to tailor their requests more specifically, which is a **more nuanced approach** than simply submitting a generic quote request for an unspecified project.

### Complexity: Why This Project Was Challenging to Build

This project was complex to build for several reasons, each of which stems from the need to integrate multiple interconnected systems, manage data dynamically, and enforce business rules through code.

1. **Custom User Model with Email Authentication**:
   Implementing a custom user model in Django can be difficult due to the complexities of overriding Django’s default user system. By using `AbstractBaseUser` and `PermissionsMixin`, I had to ensure the authentication system worked smoothly with **email-based login** rather than the default username-based login. Additionally, integrating **role-based permissions** (e.g., differentiating between admin and regular users) required careful handling of Django’s built-in permission framework. Designing this system involved learning how to extend the default user model properly, as well as handling various edge cases related to user creation, password hashing, and authentication flow.

2. **Quote Submission and Management**:
   Managing quote submissions introduces another layer of complexity. Each quote is linked to a specific user, but at the same time, the quote needs to contain a lot of dynamic content: the **project type**, **location**, **budget**, and **details**. The system must validate and handle this data securely. One of the most complex parts was ensuring that a user could **edit** or **delete** their quote submissions, but **only while logged in**. This required me to carefully manage user sessions and restrict access to ensure that only authenticated users could modify their own data. Moreover, Django’s **`ForeignKey`** relationships had to be carefully set up to ensure proper data integrity between users and quote requests.

3. **Responsive Design for Mobile & Desktop**:
   Ensuring that the application worked seamlessly on both desktop and mobile devices added another layer of complexity. I used **HTML**, **CSS**, and **JavaScript** to create a **responsive interface** that adapts to various screen sizes. The design had to be intuitive and user-friendly, requiring careful attention to layout, navigation, and interactivity. This was especially challenging when trying to balance **aesthetic design** with **functionality**, making sure the application was not only easy to use but also visually appealing across different devices.

4. **Database Relationships and Data Integrity**:
   This application involves multiple models with interdependent relationships, notably between the `CustomUser` model and the `QuoteRequest` model. Ensuring that these relationships were properly defined in the database and that **referential integrity** was maintained was crucial. Each `QuoteRequest` has a foreign key relationship to the user who submitted it, which ensures that data is accurately tied together. Additionally, implementing the logic to only allow users to see and edit their own submissions required extra care in query design and permission handling.

5. **Role-Based Access Control**:
   Managing user permissions and roles within Django was particularly challenging. While regular users can only interact with their own quote requests, **admin users** can manage all users and submissions. The use of Django’s built-in **PermissionsMixin** to create custom permissions for different roles ensured that the application adhered to this requirement. This level of access control required writing custom views and decorators to restrict user access based on roles, which added to the overall complexity of the app.

6. **Real-Time Data Management**:
   The requirement for users to edit or delete their submitted quotes means that the application must handle real-time data updates efficiently. In addition to dealing with database operations, I had to ensure that the application properly reflected these changes in the user interface without causing confusion or errors. For instance, when a user submits a quote request, the data needs to be immediately available to them for editing, and the UI should provide clear feedback when changes are saved or when an error occurs.

### Conclusion: Why This Project is Both Unique and Complex

In sum, the **CNC Construction Web Application** is unique and complex due to its integration of **email-based authentication**, **role-based user permissions**, and **dynamic quote management**. These elements work together to create a platform that is not only **interactive** but also **secure** and **responsive**. The challenges I faced throughout the development process, from designing custom user models to managing dynamic, user-submitted data, required careful planning and problem-solving. The result is a highly functional web application that goes beyond basic CRUD operations, making it a valuable learning experience and a project worth sharing.

---

## File Structure

### `web/`
Contains the main web application logic.

- **`app.py`**: Contains the backend logic for the application:
    - Handles user registration, login, and session management.
    - Routes for submitting, viewing, and editing quote requests.
    - Displays projects and ensures users can only access their own quote submissions.

- **`models.py`**: Defines the application's data models:
    - **CustomUser**: A custom user model that extends `AbstractBaseUser` and `PermissionsMixin` for email-based login and user permissions.
    - **QuoteRequest**: A model to manage user-submitted quote requests for various project types (e.g., pool construction, home renovations).
    - **MyModel**: An example model to show how other models might be structured.

### `CustomUserManager`

The `CustomUserManager` class is a custom manager for creating user accounts. It defines two main methods:

- `create_user(email, password=None, **extra_fields)`: Creates and returns a regular user with an email and password.
- `create_superuser(email, password=None, **extra_fields)`: Creates and returns a superuser with email and password.

### Explanation of Changes:
- I incorporated the new models (`CustomUserManager`, `CustomUser`, `QuoteRequest`, `MyModel`) under the **`models.py`** section of the README.
- Each model has its own description followed by the Python code block for easy readability and clarity.
- I included a brief summary of the models and their responsibilities to make the section easier to understand.
- **`requirements.txt`**: Lists all Python dependencies:
    - `Django`: The web framework used for building the app.

- **`templates/`**: Contains HTML files used to render dynamic pages:
    - **`index.html`**: Displays the available projects.
    - **`login.html`**: Login page for users.
    - **`register.html`**: Registration page for users.
    - **`quote.html`**: Page for submitting a quote request.
    - **`submitted.html`**: Displays submitted quotes for editing or viewing.
    - **`construction.html`**: Displays construction project listings.
    - **`pools.html`**: Displays pool project listings.
    - **`layout.html`**: Base layout template used by all pages for consistent structure.

- **`static/`**: Contains static assets such as stylesheets and JavaScript:
    - **`css/`**: CSS files for page styling.
    - **`js/`**: JavaScript files for interactivity and dynamic content.

# How to Run the Application

The **CNC Construction** web application is designed to showcase the various construction and pool projects offered by CNC Construction. The application provides users with the ability to explore available projects and request quotes for the ones they are interested in.

If the user is logged in, they will have access to a quote submission form, where they can submit their quote request for a particular project. After submission, the user can also edit or update their quote request — but this functionality is only available to logged-in users.

---

### Prerequisites

Make sure you have **Python 3.x** and **pip** installed. You’ll also need to have **Django** and other dependencies listed in `requirements.txt`.

### directions of setting up the project

-Change the file directory to "Final" by "cd Final" in the terminal of the file directory after this you will need to migrate the models of the project. 
-To do this you must perfrom "python manage.py makemigrations" and then proceed with "python manage.py migrate" after these two actions are perfromed your backend of the project is ready.
-then you can run "python manage.py runserver" to access the server and copy the local adress given in the terminal, then paste into google.
