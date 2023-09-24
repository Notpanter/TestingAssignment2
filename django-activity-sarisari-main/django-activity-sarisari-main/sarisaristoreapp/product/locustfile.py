from locust import HttpUser, task, between

class MyUser(HttpUser):
    wait_time = between(2, 5)

    @task(1)
    def view_homepage(self):
        self.client.get("/product")  # Use the path defined in your urls.py

    @task(2)
    def view_upload(self):
        self.client.get("product/upload/")  # Use the path defined in your urls.py

    @task(3)
    def view_update(self):
        # Replace <product_id> with an actual product ID for testing
        self.client.get("/update/3")  # Use the path defined in your urls.py