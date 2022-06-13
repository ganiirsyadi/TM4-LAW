from locust import HttpUser, between, task

NPM = "1906350616"

class WebsiteUser(HttpUser):
    wait_time = between(5, 15)
    
    @task
    def index(self):
        self.client.get(f"/read/{NPM}")
