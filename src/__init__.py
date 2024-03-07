"""
This file registers the model with the Python SDK.
"""

from viam.components.arm import Arm
from viam.resource.registry import Registry, ResourceCreatorRegistration

from .fake_arm import fake_arm

Registry.register_resource_creator(Arm.SUBTYPE, fake_arm.MODEL, ResourceCreatorRegistration(fake_arm.new, fake_arm.validate))
