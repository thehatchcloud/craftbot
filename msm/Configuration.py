class Configuration(object):
    """Provides access to the MSM app configurations"""

    def __init__(self):
        self.settings = {}
        self.config_file = '/etc/msm.conf'

        with (open(self.config_file, 'r')) as conf_file:
            for line in conf_file.readlines():
                if line.startswith("#") or (not line.rstrip()):
                    continue
                
                setting = line.split('=')
                self.settings[setting[0]] = setting[1].rstrip().replace('"', '')
        
        self.default_server_properties = {
            'spawn-protection': '16',
            'max-tick-time': '60000',
            'query.port': '25565',
            'generator-settings': '',
            'sync-chunk-writes': 'true',
            'force-gamemode': 'false',
            'allow-nether': 'true',
            'enforce-whitelist': 'true',
            'gamemode': 'creative',
            'broadcast-console-to-ops': 'true',
            'enable-query': 'false',
            'player-idle-timeout': '0',
            'text-filtering-config': '',
            'difficulty': 'easy',
            'spawn-monsters': 'false',
            'broadcast-rcon-to-ops': 'true',
            'op-permission-level': '4',
            'pvp': 'true',
            'msm-version': 'minecraft/1.7.10',
            'entity-broadcast-range-percentage': '100',
            'snooper-enabled': 'true',
            'allow-cheats': 'true',
            'level-type': 'default',
            'hardcore': 'false',
            'enable-status': 'true',
            'enable-command-block': 'true',
            'max-players': '20',
            'network-compression-threshold': '256',
            'resource-pack-sha1': '',
            'max-world-size': '29999984',
            'function-permission-level': '2',
            'rcon.port': '25575',
            'server-port': '25565',
            'debug': 'false',
            'server-ip': '',
            'spawn-npcs': 'true',
            'allow-flight': 'false',
            'level-name': 'world',
            'view-distance': '10',
            'resource-pack': '',
            'spawn-animals': 'true',
            'white-list': 'false',
            'rcon.password': '',
            'generate-structures': 'true',
            'max-build-height': '256',
            'online-mode': 'true',
            'level-seed': '',
            'use-native-transport': 'true',
            'prevent-proxy-connections': 'false',
            'enable-jmx-monitoring': 'false',
            'enable-rcon': 'true',
            'rate-limit': '0',
            'motd': 'Autism Up'
        }
