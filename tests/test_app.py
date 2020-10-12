from .context import forest_route_optimizer

def test_app(capsys, example_fixture):
    # pylint: disable=W0612,W0613
    forest_route_optimizer.Blueprint.run()
    captured = capsys.readouterr()

    assert "Hello World..." in captured.out
