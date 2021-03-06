from typing import Any, Dict, Optional, Tuple
from src.extend.config_dataclass.server_config import ServerConfig
from src.extend.config_dataclass.client_config import ClientConfig
from src.extend.config_dataclass.database_config import DataBaseConfig

import ujson as json
import os.path
import aiofiles


async def read_client_config() -> str:
    """
    read client config
    Returns: str
    """
    async with aiofiles.open(os.path.abspath(path="config/client.json").replace("lib/", "")) as file:
        return await file.read()


async def read_server_config() -> str:
    """
    read server config
    """
    async with aiofiles.open(os.path.abspath(path="config/server.json").replace("lib/", "")) as file:
        return await file.read()


async def read_database_config() -> str:
    """
    read database config
    """
    async with aiofiles.open(os.path.abspath(path="config/database.json").replace("lib/", "")) as file:
        return await file.read()





async def set_config() -> Tuple[ServerConfig, ClientConfig, DataBaseConfig]:
    """
    build config server and client and  package in data class
    Returns: (ServerConfig,ClientConfig)
    """
    server_config: Dict[str, Any] = json.loads(await read_server_config())
    client_config: Dict[str, Any] = json.loads(await read_client_config())
    database_config: Dict[str, Any] = json.loads(await read_database_config())
    port: Optional[int] = server_config.get("port")
    host: Optional[str] = server_config.get("host")
    support_ssl: Optional[bool] = server_config.get("support_ssl")
    path_to_html: Optional[str] = server_config.get("path_to_html")
    path_to_ssl: Optional[str] = server_config.get("path_to_ssl")
    name: Optional[str] = client_config.get("name")
    app_api_id: Optional[str] = client_config.get("app_api_id")
    app_api_hash: Optional[str] = client_config.get("app_api_hash")
    test_configuration: Optional[str] = client_config.get("test_configuration")
    product_configuration: Optional[str] = client_config.get("product_configuration")
    message_on_trigger: Optional[str] = client_config.get("response_message_on_trigger")
    trigger: Optional[str] = client_config.get("trigger_username")
    port_database: Optional[int] = database_config.get("port")
    host_database: Optional[str] = database_config.get("host")
    postgres_user: Optional[str] = database_config.get("postgres_user")
    postgres_password: Optional[str] = database_config.get("postgres_password")
    need_update: Optional[bool] = database_config.get("need_update")
    return ServerConfig(host=host, port=port, path_to_html=path_to_html, support_ssl=support_ssl,
                        path_to_ssl=path_to_ssl), \
           ClientConfig(name=name, app_api_id=app_api_id,
                        app_api_hash=app_api_hash,
                        test_configuration=test_configuration,
                        product_configuration=product_configuration, trigger_username=trigger,
                        message_on_trigger=message_on_trigger), \
           DataBaseConfig(port=port_database, host=host_database, postgres_user=postgres_user,
                          postgres_password=postgres_password, need_update=need_update)
