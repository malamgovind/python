from unittest.mock import Mock

database = Mock()

database.save()

database.save.assert_called_once()

print("Mock Passed")