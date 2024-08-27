# BookShop

# Bookshop Django Application

This is a Django-based web application for managing a bookshop. The application allows users to browse books, search for specific titles, comment on books, and access book data via a REST API. The app also includes user authentication for features like commenting and managing account settings.

## Features

### 1. Book Listing and Detail Pages
- Users can browse a list of available books.
- Each book has a detailed page that includes the title, author, description, price, published date, and cover image.

### 2. Search Functionality
- Users can search for books by title or author.
- The search bar is available on the book listing page.

### 3. Commenting System
- Authenticated users can leave comments on book detail pages.
- Comments can be viewed by all users but only the author of the comment can delete it.

### 5. RESTful API
- The application provides a RESTful API built with the Django REST framework.
- The API allows for CRUD operations on books, authors, and comments.
- JSON responses are provided for easy integration with other systems.

### 6. Admin Panel
- Django's built-in admin interface is available for managing books, authors, and comments.
- Admins can add, edit, and delete books and authors from the admin panel.
