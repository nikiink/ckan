from ckan.lib.helpers import HelperAttributeDict
from flask.blueprints import Blueprint
from flask.wrappers import Response
from werkzeug.local import LocalProxy
from typing import Any, Dict, Tuple, Union
from flask.ctx import _AppCtxGlobals
from flask_multistatic import MultiStaticFlask
from werkzeug.routing import Rule

def make_flask_stack(conf: Dict) -> Any: ...
def get_locale() -> str: ...
def ckan_before_request() -> None: ...
def ckan_after_request(response: Response) -> Response: ...
def helper_functions() -> Dict[str, HelperAttributeDict]: ...
def c_object() -> Dict[str, LocalProxy]: ...

class CKAN_Rule(Rule): ...
class CKAN_AppCtxGlobals(_AppCtxGlobals): ...

class CKANFlask(MultiStaticFlask):
    app_name: str
    def can_handle_request(
        self, environ: Any
    ) -> Union[Tuple[bool, str], Tuple[bool, str, str]]: ...
    def register_extension_blueprint(
        self, blueprint: Blueprint, **kwargs: Dict
    ): ...