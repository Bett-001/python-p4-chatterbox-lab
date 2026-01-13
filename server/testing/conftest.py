#!/usr/bin/env python3

import pytest
from app import app, db

# Create tables immediately when conftest is imported
with app.app_context():
    db.create_all()

@pytest.fixture(scope='session', autouse=True)
def setup_database():
    yield
    with app.app_context():
        db.drop_all()

def pytest_itemcollected(item):
    par = item.parent.obj
    node = item.obj
    pref = par.__doc__.strip() if par.__doc__ else par.__class__.__name__
    suf = node.__doc__.strip() if node.__doc__ else node.__name__
    if pref or suf:
        item._nodeid = ' '.join((pref, suf))