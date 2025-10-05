# Product Catalog Project

This is a simple Django project that models products, categories, and tags. It features a user-facing page that allows searching and filtering products by their description, category, and associated tags, demonstrating proficiency in Django models, querysets, and views.

## Core Features
-   **Data Models:** `Product`, `Category`, and `Tag` models with correct `ForeignKey` and `ManyToManyField` relationships.
-   **Admin Interface:** A fully configured Django admin panel for easy and efficient data population.
-   **Search & Filter:** A single page application allowing users to combine search (by description) and filters (by category and tags) to find products.

---

## Setup and Run Instructions

Follow these steps to get the project running on your local machine.

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/ppa21/project_catalog.git
    cd project_catalog
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    # On macOS/Linux:
    source venv/bin/activate
    # On Windows:
    venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Apply database migrations:**
    ```bash
    python manage.py migrate
    ```

5.  **Create a superuser to access the admin panel:**
    ```bash
    python manage.py createsuperuser
    ```
    (Follow the on-screen prompts to set a username and password).

6.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```

The application will now be running at `http://127.0.0.1:8000/`.

---

## Data Population

After setting up and running the project, you must populate the database with sample data using the Django admin interface.

1.  Navigate to the admin panel at: `http://127.0.0.1:8000/admin/`
2.  Log in with the superuser credentials you created during the setup process.
3.  Use the interface to create the required data:
    *   **Create at least 5 Categories** (e.g., "Electronics", "Books", "Home Goods").
    *   **Create at least 10 Tags** (e.g., "On Sale", "New", "Bestseller", "Eco-friendly").
    *   **Create at least 20 Products**, assigning a category and one or more tags to each.

Once the data is populated, the main page at `http://127.0.0.1:8000/` will display the products and filtering functionality.

---

## AI Policy Attribution

In adherence to the AI policy, this section outlines how AI tools were utilized during the development of this project.

My primary technical background is in Java/SpringBoot. To efficiently bridge my knowledge to the Python/Django stack for this assignment, I used an AI assistant in the following capacities:

*   **As a Syntax and Idiom Reference:** To quickly look up the Django-equivalent way of performing tasks I am familiar with in other frameworks (e.g., "How to create a many-to-many relationship in Django models"). This was more efficient than searching through documentation for specific syntax.
*   **As a Sounding Board:** After writing a piece of code, I would sometimes ask the AI to review it or confirm if my approach was a valid way to solve the problem in Django. This helped validate my logic and accelerate my learning.
*   **For Debugging Assistance:** To help identify potential errors or suggest troubleshooting steps for issues I encountered.

Crucially, **the core logic, project structure, and final implementation are my own.** AI was a supplementary tool for learning and validation, not for generating the solution. I have a full and complete understanding of all the code submitted and am prepared to discuss it in detail.
