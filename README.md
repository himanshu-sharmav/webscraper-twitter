Web Scraper for Twitter Trending Topics

This project is a Django-based web application designed to scrape trending topics from Twitter using Selenium and store the retrieved data in a MongoDB database. Users can initiate the scraping process and view the results through a user-friendly web interface.
Features

    Scrape Twitter Trending Topics: Utilizes Selenium to navigate Twitter and extract the latest trending topics.
    Data Storage: Stores scraped data in MongoDB for efficient retrieval and management.
    Web Interface: Allows users to trigger the scraping process and view results directly from the browser.

Prerequisites

Before setting up the project, ensure you have the following installed:

    Python 3.x: The application is built with Python and requires Python 3.x to run.
    Django: A high-level Python web framework used for developing the web application.
    Selenium: A tool for automating web browsers, used here for web scraping.
    MongoDB: A NoSQL database for storing the scraped data.
    Google Chrome: The web browser used by Selenium for scraping.
    ChromeDriver: A separate executable that Selenium uses to control Chrome.

Installation

Follow these steps to set up the project:

    Clone the Repository:

git clone https://github.com/himanshu-sharmav/webscraper-twitter.git
cd webscraper-twitter

Set Up a Virtual Environment (Optional but recommended):

python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

Install Dependencies:

Ensure that pip is updated:

pip install --upgrade pip

Then, install the required packages:

pip install -r requirements.txt

Configure MongoDB:

    Ensure MongoDB is installed and running on your system.
    By default, the application connects to a MongoDB instance running on mongodb://localhost:27017/.
    If your MongoDB configuration differs, update the connection settings in the Django settings file accordingly.

Set Up ChromeDriver:

    Download the ChromeDriver that matches your installed version of Google Chrome from the official site.
    Place the chromedriver executable in a directory included in your system's PATH, or specify its location in the Selenium configuration within the project.

Apply Database Migrations:

python manage.py migrate

Run the Development Server:

    python manage.py runserver

    Access the application at http://127.0.0.1:8000/ in your web browser.

Usage

    Access the Web Interface:

    Navigate to http://127.0.0.1:8000/ in your browser.

    Initiate Scraping:

    Click the "Run Script" button on the homepage to start the scraping process.

    View Scraped Data:

    After the scraping completes, the trending topics retrieved from Twitter will be displayed on the web interface.

Deployment

For a demonstration of the project in action, you can watch the following video:

Project Demo
Contributing

Contributions are welcome! To contribute:

    Fork the Repository:

    Click the "Fork" button at the top right of the repository page to create a copy under your GitHub account.

    Create a Feature Branch:

git checkout -b feature/YourFeatureName

Commit Your Changes:

git commit -m 'Add some feature'

Push to Your Fork:

    git push origin feature/YourFeatureName

    Submit a Pull Request:

    Open a pull request to the main repository with a description of your changes.

License

This project is licensed under the MIT License. See the LICENSE file for more details.
Acknowledgments

    Selenium: For providing the tools to automate web browsing and scraping.
    Django: For the robust web framework that powers this application.
    MongoDB: For the flexible NoSQL database solution
