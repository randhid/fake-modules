from typing import ClassVar, Mapping, Any, Dict, Optional, Tuple
from typing_extensions import Self

from viam.module.types import Reconfigurable
from viam.proto.app.robot import ComponentConfig
from viam.proto.common import ResourceName, Vector3
from viam.resource.base import ResourceBase
from viam.resource.types import Model, ModelFamily

from viam.components.arm import Arm, Pose, JointPositions, KinematicsFileFormat
from viam.logging import getLogger

import time
import asyncio

LOGGER = getLogger(__name__)

class fake_arm(Arm, Reconfigurable):
    MODEL: ClassVar[Model] = Model(ModelFamily("rand", "fake"), "arm")
    
    # create any class parameters here, 'some_pin' is used as an example (change/add as needed)
    some_pin: int

    # Constructor
    @classmethod
    def new(cls, config: ComponentConfig, dependencies: Mapping[ResourceName, ResourceBase]) -> Self:
        my_class = cls(config.name)
        my_class.reconfigure(config, dependencies)
        return my_class

    # Validates JSON Configuration
    @classmethod
    def validate(cls, config: ComponentConfig):
        return

    # Handles attribute reconfiguration
    def reconfigure(self, config: ComponentConfig, dependencies: Mapping[ResourceName, ResourceBase]):
        return

    """ Implement the methods the Viam RDK defines for the Arm API (rdk:components:arm) """

    
    async def get_end_position(
        self,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> Pose:
        pass

    
    async def move_to_position(
        self,
        pose: Pose,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ):
        pass

    
    async def move_to_joint_positions(
        self,
        positions: JointPositions,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ):
        pass

    
    async def get_joint_positions(
        self,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> JointPositions:
        values = [1,2,3,4,5]
        return  JointPositions(values=values)

    
    async def stop(
        self,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ):
        pass

    
    async def is_moving(self) -> bool:
        pass

    
    async def get_kinematics(self, *, timeout: Optional[float] = None) -> Tuple[KinematicsFileFormat.ValueType, bytes]:
        f = open("src/dofbot.json", "rb")

        data = f.read()
        f.close()
        return (KinematicsFileFormat.KINEMATICS_FILE_FORMAT_SVA, data)

