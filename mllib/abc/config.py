import json
from typing import Union

import yaml

DELIM = ","


class Config:
    _identify = None
    _overwritten = {}

    def __init__(self, **kwargs):
        for f, v in self:
            if f in kwargs:
                kv = kwargs.get(f)
                if v != kv:
                    setattr(self, f, kv)
                    self._overwritten[f] = v

    def __iter__(self):
        for k in set(self.__class__.__dict__.keys()).union(set(self.__dict__.keys())):
            if k[0] != "_":
                yield k, getattr(self, k)

    def __str__(self):
        string = ""
        for k, v in self:
            if hasattr(v, "_identify"):
                string += f"{k}:\n"
                string += "".join([f"--{vsub}\n" for vsub in str(v).split("\n")])
            else:
                string += f"{k}:{v}\n"
        return string[:-1]

    @staticmethod
    def parse(arg):
        if isinstance(arg, str) and DELIM in arg:
            arg = arg.split(DELIM)
            if len(arg) == 0:
                arg = ""
            else:
                arg = tuple(arg)
        elif isinstance(arg, str) and arg.isdigit():
            return int(arg)
        elif isinstance(arg, str) and arg.lower() == "true":
            arg = True
        elif isinstance(arg, str) and arg.lower() == "false":
            arg = False
        return arg

    def to_dict(self):
        data = {}
        for k, v in self:
            if hasattr(v, "_identify"):
                data[k] = v.to_dict()
            else:
                data[k] = v
        return data

    def dump_json(self, file):
        json.dump(self.to_dict(), open(file, "w"))

    def dump_yaml(self, file):
        yaml.dump(self.to_dict(), open(file, "w"), default_flow_style=False)

    @classmethod
    def load(cls, fp_name_dict: Union[str, dict]):
        raise NotImplementedError()

    @classmethod
    def from_dict(cls, config_dict):
        config = cls()
        config.update(config_dict)
        return config

    def update(self, updates: dict):
        for k, orig_v in self:
            if k in updates:
                v = updates.pop(k)
                if isinstance(v, dict) and hasattr(orig_v, "_identify"):
                    orig_v.update(v)
                else:
                    setattr(self, k, v)
