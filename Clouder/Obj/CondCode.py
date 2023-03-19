from typing import Any


class CondCode(object):
    good: Any | None = "200"
    bad : Any | None = "400"
    unbind : Any | None = "404"