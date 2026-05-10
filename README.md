# Krishna Ki Bekary (Flask)

A modern brownie bakery website built with Python Flask, animated CSS, and SQLite.

## Features

- Pink-themed responsive design with motion and soft gradients
- User and admin login systems
- Menu browsing, shopping cart, and checkout flow
- SQLite database for orders, payments, and login accounts
- Order confirmation, delivery tracking, and admin status updates

## Run locally

1. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
2. Start the app:
   ```bash
   python app.py
   ```
3. Open your browser:
   ```bash
   http://localhost:5000
   ```

## Deploy to Render

This project includes `render.yaml`, so Render can deploy it as a Python web service.

1. Push this folder to a GitHub repository.
2. In Render, choose **New +** then **Blueprint**.
3. Connect the GitHub repository.
4. Render will read `render.yaml`, install `requirements.txt`, and start the app with:
   ```bash
   gunicorn app:app
   ```

The included `render.yaml` uses Render's free web service plan for a simple demo deployment. SQLite works for testing, but data can reset when the service restarts or redeploys. For a real bakery site, use Render Postgres or add a persistent disk and set `DATABASE_PATH`.

## Demo credentials

- Admin: `admin@example.com` / `admin123`
- User: `user@example.com` / `user123`
