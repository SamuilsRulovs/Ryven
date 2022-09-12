from ryven.NENV import *
from random import random


# your node definitions go here
class NodeBase(Node):

    def __init__(self, params):
        super().__init__(params)

        # here we could add some stuff for all nodes below...


class IFCDirection3D(NodeBase):
    """Generate a random number in a given range"""
    # this __doc__ string will be displayed as tooltip in the editor

    title = 'IFCDIRECTION'
    init_inputs = [
        NodeInputBP(dtype=dtypes.Integer(default=0, bounds=(0, 1)), label='scale'),
        NodeInputBP(dtype=dtypes.Integer(default=0, bounds=(0, 1)), label='scale'),
        NodeInputBP(dtype=dtypes.Integer(default=0, bounds=(0, 1)), label='scale'),
    ]
    init_outputs = [
        NodeOutputBP(),
    ]
    color = '#aabb44'


class IFCDirection2D(NodeBase):
    """Generate a random number in a given range"""
    # this __doc__ string will be displayed as tooltip in the editor

    title = 'IFCDIRECTION'
    init_inputs = [
        NodeInputBP(dtype=dtypes.Integer(default=0, bounds=(0, 1)), label='scale'),
        NodeInputBP(dtype=dtypes.Integer(default=0, bounds=(0, 1)), label='scale'),
    ]
    init_outputs = [
        NodeOutputBP(),
    ]
    color = '#aabb44'


class IFCCartesianPoint3D(NodeBase):
    """Generate a random number in a given range"""
    # this __doc__ string will be displayed as tooltip in the editor

    title = 'IFCDIRECTION'
    init_inputs = [
        NodeInputBP(dtype=dtypes.Float(default=0, bounds=(-1000, 1000)), label='scale'),
        NodeInputBP(dtype=dtypes.Float(default=0, bounds=(-1000, 1000)), label='scale'),
        NodeInputBP(dtype=dtypes.Float(default=0, bounds=(-1000, 1000)), label='scale')
    ]
    init_outputs = [
        NodeOutputBP(),
    ]
    color = '#aabb44'


class IFCCartesianPoint2D(NodeBase):
    """Generate a random number in a given range"""
    # this __doc__ string will be displayed as tooltip in the editor

    title = 'IFCCARTESIANPOINT'
    init_inputs = [
        NodeInputBP(dtype=dtypes.Float(default=0, bounds=(-1000, 1000)), label='scale'),
        NodeInputBP(dtype=dtypes.Float(default=0, bounds=(-1000, 1000)), label='scale'),
    ]
    init_outputs = [
        NodeOutputBP(),
    ]
    color = '#aabb44'


class IFCPolylop(NodeBase):
    title = 'IFCPOLYLOOP'
    init_inputs = [IFCCartesianPoint3D,
                   IFCCartesianPoint3D,
                   IFCCartesianPoint3D
                   ]


export_nodes(
    IFCDirection3D,
    IFCDirection2D,
    IFCCartesianPoint3D,
    IFCCartesianPoint2D
)
