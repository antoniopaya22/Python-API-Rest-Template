"""App entry point."""
import unittest
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from api import app, db

manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

@manager.command
def run():
    app.run(host='0.0.0.0')

@manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('./test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

if __name__ == '__main__':
    manager.run()