import yaml

from senabase.starterpack.database import PostgreSQLHandler
from senabase.starterpack.log import SimpleLogger

try:
    log = SimpleLogger()
    log.configure('proto')

    with open('./bin/cfg/cfg.yaml') as f:
        cfg = yaml.load(f, Loader=yaml.FullLoader)
        cfg_pgh = cfg['pg']
        pgh = PostgreSQLHandler(**cfg_pgh)

        q1 = 'select now()'
        rs = pgh.get(q1)
        log.d(rs)
except Exception as ex:
    log.e(ex)
