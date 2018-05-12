"""
test_config1: Configuration file
"""
class ConfigBase():
    SECRET_KEY = 'your-secret-key'
    DEBUG = False

class ConfigDevelopement(ConfigBase):
    """For developement.Inherit from ConfigBase and override some values"""
    DEBUG = True

class ConfigProduction(ConfigBase):
    """production.Inherit from ConfigBase and override some values"""
    SECRET_KEY = 'production-secret-key'

# You can choose to load a particular configuration class:

app.config.from_object('test_config1.ConfigDevelopement') # modulename.classname

# To store sensitive data in a dedicated folder which is not under source control, you can use the instance folders with from_pyfile(filename|modulename). For example,
app = Flask(__name__)
app.config.from_object('test_config1.ConfigDevelopement')
    # Default confiuration settings
app.config.from_pyfile('local/config_local.py', silent=True)
    # Override the defaults or additional settings
    # silent = True: Ignore if such file exists

# You can also override the default settings, through an environment variable (which holds a configuration filename) with from_env(envvar_name). For example,
# Load from an  environment variable which holds the configuration filename
# Set the environment variable 'EXTRA_SETTING' as follows before running the app:
# Export EXTRA_SETTINGS = test_config2.py
app.config.from_envvar('EXTRA_SETTINGS', silent=True)
    # Override existsing values
    # silent = True: Ignore if not such environment variable exists

"""
test_config2: More configuration loaded via environement setting
"""
USERNAME = 'peter'