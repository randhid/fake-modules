import asyncio
import sys

from viam.components.arm import Arm
from viam.module.module import Module
from fake_arm import FakeArm

from viam.components.arm import Arm
from viam.resource.registry import Registry, ResourceCreatorRegistration

from fake_arm import FakeArm

async def main(address: str):
    """This function creates and starts a new module, after adding all desired resources.
    Resources must be pre-registered. For an example, see the `__init__.py` file.
    Args:
        address (str): The address to serve the module on
    """

    Registry.register_resource_creator(Arm.SUBTYPE, FakeArm.MODEL, ResourceCreatorRegistration(FakeArm.new, FakeArm.validate))

    module = Module(address)
    module.add_model_from_registry(Arm.SUBTYPE, FakeArm.MODEL)
    await module.start()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise Exception("Need socket path as command line argument")

    asyncio.run(main(sys.argv[1]))
