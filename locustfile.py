#!/usr/bin/python

import random
from locust import HttpUser, TaskSet, between


def index(l):
    l.client.get("/productpage")


class UserBehavior(TaskSet):

    def on_start(self):
        index(self)

    tasks = {index: 1}


class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    # wait_time = between(1, 10)
    wait_time = constant_throughput(0.1)
