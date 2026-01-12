
import pytest

from app import app

def test_header_present(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("h1")
    header = dash_duo.find_element('h1')
    assert header is not None
    assert "Pink Morsel" in header.text

def test_graph_present(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#sales_graph")
    graph = dash_duo.find_element('#sales_graph')
    assert graph is not None

def test_radio_present(dash_duo):
    dash_duo.start_server(app)
    radio = dash_duo.find_element('#radio_items')
    assert radio is not None

