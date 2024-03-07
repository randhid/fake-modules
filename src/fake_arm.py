from locale import normalize
from operator import truediv
from random import random
from time import sleep
from typing import ClassVar, Mapping, Any, Dict, Optional, Tuple
from typing_extensions import Self


from viam.module.types import Reconfigurable
from viam.proto.app.robot import ComponentConfig
from viam.proto.common import ResourceName, Vector3
from viam.resource.base import ResourceBase
from viam.resource.types import Model, ModelFamily

from viam.components.arm import Arm, Pose, JointPositions, KinematicsFileFormat
from viam.logging import getLogger

LOGGER = getLogger(__name__)

class fake_arm(Arm, Reconfigurable):
    MODEL: ClassVar[Model] = Model(ModelFamily("rand", "fake"), "arm")
    
    pose: Pose(x=0,y=0,z=0, o_x=0, o_y=0, o_z=1, theta=0)
    joints : JointPositions(values=[0,0,0,0,0,0])
    ismoving = False

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
        return Pose(x=1, y=2, z=3, o_x=0, oy=1, o_z=0, theta=45)

    
    async def move_to_position(
        self,
        pose: Pose,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ):
        x= random.uniform(0,1)
        y= random.uniform(0,1)
        z= random.uniform(0,1)
        
        ovec = Vector3(x=random.uniform(0,1), y=random.uniform(0,1), z=random.uniform(0,1))
        o_x = ovec.x / (ovec.x*ovec.x + ovec.y*ovec.y + ovec.z+ovec.z)
        o_y = ovec.y / (ovec.x*ovec.x + ovec.y*ovec.y + ovec.z+ovec.z)
        o_z = ovec.z / (ovec.x*ovec.x + ovec.y*ovec.y + ovec.z+ovec.z)

        theta = random.uniform(0,1)
        self.is_moving = True
        sleep(0.5)
        self.ismoving = False
        self.pose = Pose(x=x,y=y, z=z, o_x=o_x, o_y=o_y, o_z=o_z, theta=theta)

    
    async def move_to_joint_positions(
        self,
        positions: JointPositions,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ):
        new_joints = JointPositions(random.uniform(0,1), random.uniform(0,1),random.uniform(0,1),random.uniform(0,1),random.uniform(0,1),random.uniform(0,1))
        self.is_moving = True
        sleep(0.5)
        self.ismoving = False
        self.joints = new_joints

    async def get_joint_positions(
        self,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> JointPositions:
        values = [1,2,3,4,5,6]
        return  JointPositions(values=values)

    
    async def stop(
        self,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ):
        self.ismoving = False

    
    async def is_moving(self) -> bool:
        return self.ismoving

    
    async def get_kinematics(self, *, timeout: Optional[float] = None, **kwargs) -> Tuple[KinematicsFileFormat.ValueType, bytes]:
        f = open("src/dofbot.json", "rb")

        data = f.read()
        f.close()
        return (KinematicsFileFormat.KINEMATICS_FILE_FORMAT_SVA, data)

