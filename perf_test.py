import random
from locust import HttpUser, between, task

NPM = "1906350616"

class WebsiteUser(HttpUser):
    wait_time = between(5, 15)
    
    @task
    def get_mahasiswa_no_cache(self):
        self.client.get(f"/read/{NPM}")

    @task
    def get_mahasiswa_with_cache(self):
        trx_id = random.randint(1, 100)
        self.client.get(f"/read/{NPM}/99")
