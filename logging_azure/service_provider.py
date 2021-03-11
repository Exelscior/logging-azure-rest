from typing import Type

from injector import Injector, Binder, T


def configure(binder: Binder) -> None:
    from .configuration import AzureLogServiceConfiguration

    binder.bind(AzureLogServiceConfiguration, AzureLogServiceConfiguration.build())


__injector = Injector(configure)


def provide(class_: Type[T]):
    return __injector.get(class_)
