import requests
import pytest


@pytest.fixture(autouse=True)
def disable_network_calls(monkeypatch):
    def disable_get():
        raise RuntimeError("Do not use the network")

    monkeypatch.setattr(requests, "get", lambda *args, **kwargs: disable_get())
