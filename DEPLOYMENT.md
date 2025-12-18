# Deploying Shopkart to PythonAnywhere (Free)

This guide will help you put your Shopkart project on the internet using PythonAnywhere.

## Step 1: Prepare Your Project
1.  **Check `requirements.txt`**: Ensure this file exists in your `shopkart` folder and lists all libraries (`django`, `pillow`, `razorpay`).
2.  **Allowed Hosts**:
    In `settings.py`, update `ALLOWED_HOSTS` to allow your future domain:
    ```python
    ALLOWED_HOSTS = ['yourusername.pythonanywhere.com', '127.0.0.1']
    ```

## Step 2: Create a PythonAnywhere Account
1.  Go to [www.pythonanywhere.com](https://www.pythonanywhere.com/).
2.  Sign up for a **Beginner (Free)** account.

## Step 3: Upload Your Code
1.  Go to the **Dashboard** -> **Files**.
2.  You can upload your files directly or use a ZIP file.
    *   *Tip*: Zip your `shopkart` folder (the one containing `manage.py`, `shopkart`, `templates`, etc.) and upload it.
    *   Open a **Bash Console**, type `unzip shopkart.zip`, and move files if needed.

## Step 4: Set Up Virtual Environment
1.  Open a **Bash Console** on PythonAnywhere.
2.  Create a virtual environment:
    ```bash
    mkvirtualenv --python=/usr/bin/python3.10 myenv
    ```
3.  Install your dependencies:
    ```bash
    pip install django pillow razorpay
    ```

## Step 5: Configure Web App
1.  Go to the **Web** tab on the Dashboard.
2.  **Add a new web app**:
    *   Click **Next**.
    *   Select **Manual Configuration** (NOT Django, Manual gives more control).
    *   Select **Python 3.10**.
3.  **Virtualenv**:
    *   Enter the path to your virtualenv (e.g., `/home/yourusername/.virtualenvs/myenv`).
4.  **Source code**:
    *   Enter the path to your project folder (e.g., `/home/yourusername/shopkart`).

## Step 6: Configure WSGI File
1.  In the **Web** tab, scroll to **Code** -> **WSGI configuration file**.
2.  Click the link to edit it.
3.  Delete everything and paste this (replace `yourusername`!):

    ```python
    import os
    import sys

    # path to your project folder
    path = '/home/yourusername/shopkart'
    if path not in sys.path:
        sys.path.append(path)

    os.environ['DJANGO_SETTINGS_MODULE'] = 'shopkart.settings'

    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()
    ```
4.  **Save** the file.

## Step 7: Static Files (Images/CSS)
Since `DEBUG` will be False in production (recommended), you need to serve static files separately.
1.  In **Web** tab -> **Static files**:
    *   **URL**: `/static/`
    *   **Directory**: `/home/yourusername/shopkart/static`
    *   **URL**: `/media/`
    *   **Directory**: `/home/yourusername/shopkart/media`

## Step 8: Finalize
1.  Go back to the top of the **Web** tab.
2.  Click **Reload <yourusername>.pythonanywhere.com**.
3.  Visit your link!

## Troubleshooting
*   **Something invalid?** Check the **Error Log** link on the Web tab.
*   **Database error?** You might need to run `python manage.py migrate` in the PythonAnywhere console.
*   **Images missing?** Check the Static Files paths in Step 7.
