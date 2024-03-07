import asyncio
from typing import Any, Dict, Optional, Tuple

from viam.components.arm import Arm
from viam.rpc.server import Server

from viam.components.arm import Arm, Pose, JointPositions, KinematicsFileFormat

class FakeArm(Arm):
    def __init__(self, name: str):
        super(FakeArm, self).__init__(name)

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


async def main():
   srv = Server(components=[FakeArm("WHOOPSIE")])
   await srv.serve()

if __name__ == "__main__":
   asyncio.run(main())
