from pyramid.config import Configurator
from sqlalchemy.pool import NullPool

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('myproject.models')
    config.include('pyramid_chameleon')
    config.include('pyramid_jinja2')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_settings({
        'sqlalchemy.poolclass': NullPool,  # disable pooling
        'sqlalchemy.pool_recycle': 60,  # timeout connection after 60s
    })
    config.add_route('home', '/')
    config.scan()
    return config.make_wsgi_app()
