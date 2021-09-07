from typing import Any, Callable, Dict, Optional, Text

class Dependencies(object):
    constructors: Dict[Text, Callable[..., Any]] = {}

    def __init__(
        self,
        register_resources_fn: Optional[Callable[..., None]] = None
    ) -> None:
        self.dependencies: Dict[Text, Any] = {}

        if register_resources_fn:
            register_resources_fn()

    def get_dependency(self, name: Text, use_cached: bool = True, **kwargs: Any) -> Any:
        if name not in self.dependencies or not use_cached:
            constructor = self.constructors.get(name)
            if not constructor:
                raise Exception("Unknown dependency: {}".format(name))
            self.dependencies[name] = constructor(self, **kwargs)
        return self.dependencies[name]

    @classmethod
    def register_resource(cls, name: Text, constructor: Callable[..., Any]) -> None:
        cls.constructors[name] = constructor

    def resources(self):
        return self.constructors.keys()
