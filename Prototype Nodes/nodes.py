from ryven.NENV import *
from random import random


# your node definitions go here
class NodeBase(Node):

    def __init__(self, params):
        super().__init__(params)
        self.val = None

        # self.num_inputs = 0
        # self.actions['add input'] = {'method': self.add_operand_input}
        #
        # version = 'v0.0'

    init_inputs = [
        NodeOutputBP(),
         # NodeInputBP(dtype=dtypes.Data(size='l')),
         # NodeInputBP(dtype=dtypes.Data(size='l')),
    ]

    init_outputs = [
        NodeOutputBP(),
    ]

    def place_event(self):
        self.update()
        # for i in range(len(self.inputs)):
        #     self.register_new_operand_input(i)

    # def add_operand_input(self):
    #     self.create_input_dt(dtype=dtypes.Data(size='s'))
    #     self.register_new_operand_input(self.num_inputs)
    #     self.update()

    # def remove_operand_input(self, index):
    #     self.delete_input(index)
    #     self.num_inputs -= 1
    #     # del self.actions[f'remove input {index}']
    #     self.rebuild_remove_actions()
    #     self.update()

    # def register_new_operand_input(self, index):
    #     self.actions[f'remove input {index}'] = {
    #         'method': self.remove_operand_input,
    #         'data': index
    #     }
    #     self.num_inputs += 1

    # def rebuild_remove_actions(self):
    #
    #     remove_keys = []
    #     for k, v in self.actions.items():
    #         if k.startswith('remove input'):
    #             remove_keys.append(k)
    #
    #     for k in remove_keys:
    #         del self.actions[k]
    #
    #     for i in range(self.num_inputs):
    #         self.actions[f'remove input {i}'] = {'method': self.remove_operand_input, 'data': i}

    def update_event(self, inp=-1):
        self.set_output_val(0, self.input(0))

        self.val = self.input(0)
        if self.session.gui:
            self.main_widget().show_val(self.val)

    def apply_op(self, elements: list):
        return None

    def view_place_event(self):
        self.main_widget().show_val(self.val)

    # here we could add some stuff for all nodes below...


# Infromation about project: IFCPROJECT, IFCOWNERHISTORY etc.

class IFCBuilding(NodeBase):
    title = 'IFCBUILDING'
    init_inputs = [
        NodeInputBP(dtype=dtypes.String(default="#1", size='m'), label='OwnIFCID'),
        NodeInputBP(dtype=dtypes.String(default="", size='l'), label='GlobalId'),
        NodeInputBP(dtype=dtypes.String(default="$", size='m'), label='OwnerHistory'),
        NodeInputBP(dtype=dtypes.String(default="IfcBuilding", size='m'), label='Name'),
        NodeInputBP(dtype=dtypes.String(default="$", size='m'), label='Description'),
        NodeInputBP(dtype=dtypes.String(default="$", size='m'), label='ObjectType'),
        NodeInputBP(dtype=dtypes.String(default="$", size='m'), label='ObjectPlacement'),
        NodeInputBP(dtype=dtypes.String(default="$", size='m'), label='Representation'),
        NodeInputBP(dtype=dtypes.String(default="$", size='m'), label='LongName'),
        NodeInputBP(dtype=dtypes.String(default="$", size='m'), label='CompositionType'),
        NodeInputBP(dtype=dtypes.String(default="$", size='m'), label='ElevationOfRefHeight'),
        NodeInputBP(dtype=dtypes.String(default="$", size='m'), label='ElevationOfTerrain'),
        NodeInputBP(dtype=dtypes.String(default="$", size='m'), label='BuildingAddress'),
    ]
    init_outputs = [NodeOutputBP(label='OwnIFCID')
                    ]
    color = '#aabb44'

    # def update_event(self, inp=-1):
    #     self.set_output_val(0,  self.input(0)) # "#1")

    # def update_event(self, inp=-1):
    #     if self.input(0):
    #         OwnIFCID = self.input(0)
    #         self.set_output_val(OwnIFCID)


class IFCOwnerhistory(NodeBase):
    title = 'IFCOWNERHISTORY'
    init_inputs = [
        NodeInputBP(dtype=dtypes.String(default="#2", size='m'), label='OwnIFCID'),
        NodeInputBP(dtype=dtypes.String(default="#", size='m'), label='OwningUser'),
        NodeInputBP(dtype=dtypes.String(default="#", size='m'), label='OwningApplication'),
        NodeInputBP(dtype=dtypes.String(default="$", size='m'), label='State'),
        NodeInputBP(dtype=dtypes.String(default=".ADDED.", size='m'), label='ChangeAction'),
        NodeInputBP(dtype=dtypes.String(default="$", size='l'), label='LastModifiedDate'),
        NodeInputBP(dtype=dtypes.String(default="$", size='m'), label='LastModifyingUser'),
        NodeInputBP(dtype=dtypes.String(default="$", size='m'), label='LastModifyingApplication'),
        NodeInputBP(dtype=dtypes.String(default="$", size='l'), label='CreationDate'),
    ]
    init_outputs = [
        NodeOutputBP(label='OwnIFCID')
    ]
    color = '#aabb44'

    # def update_event(self, inp=-1):
    #     if self.input(0):
    #         OwnIFCID = self.input(0)
    #         self.set_output_val(OwnIFCID)


class IFCPersonandorganization(NodeBase):
    title = 'IFCPERSONANDORGANIZATION'
    init_inputs = [
        NodeInputBP(dtype=dtypes.String(default="#5", size='m'), label='OwnIFCID'),
        NodeInputBP(dtype=dtypes.String(default="#", size='m'), label='ThePerson'),
        NodeInputBP(dtype=dtypes.String(default="#", size='m'), label='TheOrganization'),
        NodeInputBP(dtype=dtypes.String(default="$", size='m'), label='Roles')
    ]
    init_outputs = [
        NodeOutputBP(label='OwnIFCID')
    ]
    color = '#aabb44'


class IFCApplication(NodeBase):
    title = 'IFCAPPLICATION'
    init_inputs = [
        NodeInputBP(dtype=dtypes.String(default="#6", size='m'), label='OwnIFCID'),
        NodeInputBP(dtype=dtypes.String(default="#", size='m'), label='ApplicationDeveloper'),
        NodeInputBP(dtype=dtypes.String(default="0.0.0.0", size='m'), label='Version'),
        NodeInputBP(dtype=dtypes.String(default="", size='l'), label='ApplicationFullName'),
        NodeInputBP(dtype=dtypes.String(default="", size='l'), label='ApplicationIdentifier')
    ]
    init_outputs = [
        NodeOutputBP(label='OwnIFCID')
    ]
    color = '#aabb44'


class IfcPerson(NodeBase):
    title = 'IFCPERSON'
    init_inputs = [
        NodeInputBP(dtype=dtypes.String(default="#", size='m'), label='OwnIFCID'),
        NodeInputBP(dtype=dtypes.String(default="$", size='m'), label='Identification'),
        NodeInputBP(dtype=dtypes.String(default="$", size='m'), label='FamilyName'),
        NodeInputBP(dtype=dtypes.String(default="$", size='m'), label='GivenName'),
        NodeInputBP(dtype=dtypes.String(default="$", size='m'), label='MiddleNames'),
        NodeInputBP(dtype=dtypes.String(default="$", size='m'), label='PrefixTitles'),
        NodeInputBP(dtype=dtypes.String(default="$", size='m'), label='SuffixTitles'),
        NodeInputBP(dtype=dtypes.String(default="$", size='m'), label='Roles'),
        NodeInputBP(dtype=dtypes.String(default="$", size='m'), label='Addresses')
    ]
    init_outputs = [
        NodeOutputBP(label='OwnIFCID')
    ]
    color = '#aabb44'


class IfcOrganisation(NodeBase):
    title = 'IFCORGANIZATION'
    init_inputs = [
        NodeInputBP(dtype=dtypes.String(default="#", size='m'), label='OwnIFCID'),
        NodeInputBP(dtype=dtypes.String(default="$", size='m'), label='Identification'),
        NodeInputBP(dtype=dtypes.String(default="", size='l'), label='Name'),
        NodeInputBP(dtype=dtypes.String(default="$", size='m'), label='Description'),
        NodeInputBP(dtype=dtypes.String(default="$", size='m'), label='Roles'),
        NodeInputBP(dtype=dtypes.String(default="$", size='m'), label='Addresses')
    ]
    init_outputs = [
        NodeOutputBP(label='OwnIFCID')
    ]
    color = '#aabb44'


class IfcProject(NodeBase):
    title = 'IFCPROJECT'
    init_inputs = [
        NodeInputBP(dtype=dtypes.String(default="#", size='m'), label='OwnIFCID'),
        NodeInputBP(dtype=dtypes.String(default="", size='l'), label='GlobalId'),
        NodeInputBP(dtype=dtypes.String(default="#", size='m'), label='OwnerHistory'),
        NodeInputBP(dtype=dtypes.String(default="", size='l'), label='Name'),
        NodeInputBP(dtype=dtypes.String(default="$", size='m'), label='Description'),
        NodeInputBP(dtype=dtypes.String(default="$", size='m'), label='ObjectType'),
        NodeInputBP(dtype=dtypes.String(default="$", size='m'), label='LongName'),
        NodeInputBP(dtype=dtypes.String(default="$", size='m'), label='Phase'),
        NodeInputBP(dtype=dtypes.String(default="#", size='m'), label='RepresentationContexts'),
        NodeInputBP(dtype=dtypes.String(default="#", size='m'), label='UnitsInContext')
    ]
    init_outputs = [
        NodeOutputBP(label='OwnIFCID')
    ]
    color = '#aabb44'


class IfcGeometricRepresentationContext(NodeBase):
    title = 'IFCGEOMETRICREPRESENTATIONCONTEXT'
    init_inputs = [
        NodeInputBP(dtype=dtypes.String(default="#", size='m'), label='OwnIFCID'),
        NodeInputBP(dtype=dtypes.String(default="$", size='m'), label='ContextIdentifier'),
        NodeInputBP(dtype=dtypes.String(default="", size='m'), label='ContextType'),
        NodeInputBP(dtype=dtypes.String(default="$", size='m'), label='CoordinateSpaceDimension'),
        NodeInputBP(dtype=dtypes.String(default="$", size='m'), label='Precision'),
        NodeInputBP(dtype=dtypes.String(default="$", size='m'), label='WorldCoordinateSystem'),
        NodeInputBP(dtype=dtypes.String(default="$", size='m'), label='TrueNorth')
    ]
    init_outputs = [
        NodeOutputBP(label='OwnIFCID')
    ]
    color = '#aabb44'


class IfcGeometricRepresentationSubContext(NodeBase):
    title = 'IFCGEOMETRICREPRESENTATIONSUBCONTEXT'
    init_inputs = [
        NodeInputBP(dtype=dtypes.String(default="#", size='m'), label='OwnIFCID'),
        NodeInputBP(dtype=dtypes.String(default="$", size='m'), label='ContextIdentifier'),
        NodeInputBP(dtype=dtypes.String(default="", size='m'), label='ContextType'),
        NodeInputBP(dtype=dtypes.String(default="$", size='m'), label='CoordinateSpaceDimension'),
        NodeInputBP(dtype=dtypes.String(default="$", size='m'), label='Precision'),
        NodeInputBP(dtype=dtypes.String(default="$", size='m'), label='WorldCoordinateSystem'),
        NodeInputBP(dtype=dtypes.String(default="$", size='m'), label='TrueNorth'),
        NodeInputBP(dtype=dtypes.String(default="", size='m'), label='ParentContext'),
        NodeInputBP(dtype=dtypes.String(default="$", size='m'), label='TargetScale'),
        NodeInputBP(dtype=dtypes.String(default="$", size='m'), label='TargetView'),
        NodeInputBP(dtype=dtypes.String(default="$", size='m'), label='UserDefinedTargetView')
    ]
    init_outputs = [
        NodeOutputBP(label='OwnIFCID')
    ]
    color = '#aabb44'


class IfcShapeRepresentation(NodeBase):
    title = 'IFCSHAPEREPRESENTATION'
    init_inputs = [
        NodeInputBP(dtype=dtypes.String(default="#", size='m'), label='OwnIFCID'),
        NodeInputBP(dtype=dtypes.String(default="$", size='m'), label='ContextOfItems'),
        NodeInputBP(dtype=dtypes.String(default="$", size='m'), label='RepresentationIdentifier'),
        NodeInputBP(dtype=dtypes.String(default="$", size='m'), label='RepresentationType'),
        NodeInputBP(dtype=dtypes.String(default="$", size='m'), label='Items')
    ]
    init_outputs = [
        NodeOutputBP(label='OwnIFCID')
    ]
    color = '#aabb44'


class IfcProductDefinitionShape(NodeBase):
    title = 'IFCPRODUCTDEFINITIONSHAPE'
    init_inputs = [
        NodeInputBP(dtype=dtypes.String(default="#", size='m'), label='OwnIFCID'),
        NodeInputBP(dtype=dtypes.String(default="$", size='m'), label='Name'),
        NodeInputBP(dtype=dtypes.String(default="$", size='m'), label='Description'),
        NodeInputBP(dtype=dtypes.String(default="$", size='m'), label='Representations'),
    ]
    init_outputs = [
        NodeOutputBP(label='OwnIFCID')
    ]
    color = '#aabb44'


class IfcRelAggregates(NodeBase):
    title = 'IFCRELAGGREGATES'
    init_inputs = [
        NodeInputBP(dtype=dtypes.String(default="#", size='m'), label='OwnIFCID'),
        NodeInputBP(dtype=dtypes.String(default="", size='l'), label='GlobalId'),
        NodeInputBP(dtype=dtypes.String(default="$", size='m'), label='OwnerHistory'),
        NodeInputBP(dtype=dtypes.String(default="$", size='m'), label='Name'),
        NodeInputBP(dtype=dtypes.String(default="$", size='m'), label='Description'),
        NodeInputBP(dtype=dtypes.String(default="$", size='m'), label='RelatingObject'),
        NodeInputBP(dtype=dtypes.String(default="$", size='m'), label='RelatedObjects'),
    ]
    init_outputs = [
        NodeOutputBP(label='OwnIFCID')
    ]
    color = '#aabb44'


class IfcBuildingElementProxy(NodeBase):
    title = 'IFCBUILDINGELEMENTPROXY'
    init_inputs = [
        NodeInputBP(dtype=dtypes.String(default="#", size='m'), label='OwnIFCID'),
        NodeInputBP(dtype=dtypes.String(default="$", size='l'), label='GlobalId'),
        NodeInputBP(dtype=dtypes.String(default="$", size='m'), label='OwnerHistory'),
        NodeInputBP(dtype=dtypes.String(default="$", size='m'), label='Name'),
        NodeInputBP(dtype=dtypes.String(default="$", size='m'), label='Description'),
        NodeInputBP(dtype=dtypes.String(default="$", size='m'), label='ObjectType'),
        NodeInputBP(dtype=dtypes.String(default="$", size='m'), label='ObjectPlacement'),
        NodeInputBP(dtype=dtypes.String(default="$", size='m'), label='Representation'),
        NodeInputBP(dtype=dtypes.String(default="$", size='m'), label='Tag'),
        NodeInputBP(dtype=dtypes.String(default="$", size='m'), label='PredefinedType'),
    ]
    init_outputs = [
        NodeOutputBP(label='OwnIFCID')
    ]
    color = '#aabb44'


class IfcRelContainedInSpatialStructure(NodeBase):
    title = 'IFCRELCONTAINEDINSPATIALSTRUCTURE'
    init_inputs = [
        NodeInputBP(dtype=dtypes.String(default="#", size='m'), label='OwnIFCID'),
        NodeInputBP(dtype=dtypes.String(default="", size='l'), label='GlobalId'),
        NodeInputBP(dtype=dtypes.String(default="$", size='m'), label='OwnerHistory'),
        NodeInputBP(dtype=dtypes.String(default="$", size='m'), label='Name'),
        NodeInputBP(dtype=dtypes.String(default="$", size='m'), label='Description'),
        NodeInputBP(dtype=dtypes.String(default="$", size='m'), label='RelatedElements'),
        NodeInputBP(dtype=dtypes.String(default="$", size='m'), label='RelatingStructure'),
    ]
    init_outputs = [
        NodeOutputBP(label='OwnIFCID')
    ]
    color = '#aabb44'


# Units


class IFCUnitAssignment(NodeBase):
    """Generate a random number in a given range"""
    # this __doc__ string will be displayed as tooltip in the editor

    title = 'IFCUNITASSIGNMENT'
    init_inputs = [
        NodeInputBP(dtype=dtypes.String(default="#", size='m'), label='OwnIFCID'),
        NodeInputBP(dtype=dtypes.String(default="#", size='m'), label='Units')
    ]
    init_outputs = [
        NodeOutputBP(label='OwnIFCID')
    ]
    color = '#aabb44'


class IfcSIUnit(NodeBase):
    """Generate a random number in a given range"""
    # this __doc__ string will be displayed as tooltip in the editor

    title = 'IFCSIUNIT'
    init_inputs = [
        NodeInputBP(dtype=dtypes.String(default="#", size='m'), label='OwnIFCID'),
        NodeInputBP(dtype=dtypes.String(default="#", size='m'), label='Dimensions'),
        NodeInputBP(dtype=dtypes.String(default="#", size='m'), label='UnitType'),
        NodeInputBP(dtype=dtypes.String(default="#", size='m'), label='Prefix'),
        NodeInputBP(dtype=dtypes.String(default="#", size='m'), label='Name')
    ]
    init_outputs = [
        NodeOutputBP(label='OwnIFCID')
    ]
    color = '#aabb44'


class IfcConversionBasedUnit(NodeBase):
    """Generate a random number in a given range"""
    # this __doc__ string will be displayed as tooltip in the editor

    title = 'IFCCONVERSIONBASEDUNIT'
    init_inputs = [
        NodeInputBP(dtype=dtypes.String(default="#", size='m'), label='OwnIFCID'),
        NodeInputBP(dtype=dtypes.String(default="#", size='m'), label='Dimensions'),
        NodeInputBP(dtype=dtypes.String(default="#", size='m'), label='UnitType'),
        NodeInputBP(dtype=dtypes.String(default="#", size='m'), label='Name'),
        NodeInputBP(dtype=dtypes.String(default="#", size='m'), label='ConversionFactor')
    ]
    init_outputs = [
        NodeOutputBP(label='OwnIFCID')
    ]
    color = '#aabb44'


class IfcMeasureWithUnit(NodeBase):
    """Generate a random number in a given range"""
    # this __doc__ string will be displayed as tooltip in the editor

    title = 'IFCMEASUREWITHUNIT'
    init_inputs = [
        NodeInputBP(dtype=dtypes.String(default="#", size='m'), label='OwnIFCID'),
        NodeInputBP(dtype=dtypes.String(default="$", size='l'), label='ValueComponent'),
        NodeInputBP(dtype=dtypes.String(default="$", size='m'), label='UnitComponent'),
    ]
    # Something is wrong
    init_outputs = [
        NodeOutputBP(label='OwnIFCID')
    ]
    color = '#aabb44'


# Placements

class IfcAxis2Placement3D(NodeBase):
    """Generate a random number in a given range"""
    # this __doc__ string will be displayed as tooltip in the editor

    title = 'IFCAXIS2PLACEMENT3D'
    init_inputs = [
        NodeInputBP(dtype=dtypes.String(default="#", size='m'), label='OwnIFCID'),
        NodeInputBP(dtype=dtypes.String(default="$", size='m'), label='Location'),
        NodeInputBP(dtype=dtypes.String(default="$", size='m'), label='Axis'),
        NodeInputBP(dtype=dtypes.String(default="$", size='m'), label='RefDirection')
    ]
    init_outputs = [
        NodeOutputBP(label='OwnIFCID')
    ]
    color = '#aabb44'


class IfcLocalPlacement(NodeBase):
    """Generate a random number in a given range"""
    # this __doc__ string will be displayed as tooltip in the editor

    title = 'IFCLOCALPLACEMENT'
    init_inputs = [
        NodeInputBP(dtype=dtypes.String(default="#", size='m'), label='OwnIFCID'),
        NodeInputBP(dtype=dtypes.String(default="$", size='m'), label='PlacementRelTo'),
        NodeInputBP(dtype=dtypes.String(default="$", size='m'), label='RelativePlacement'),
        NodeInputBP(dtype=dtypes.String(default="$", size='m'), label='scale')
    ]
    init_outputs = [
        NodeOutputBP(label='OwnIFCID')
    ]
    color = '#aabb44'


class IFCDirection3D(NodeBase):
    """Generate a random number in a given range"""
    # this __doc__ string will be displayed as tooltip in the editor

    title = 'IFCDIRECTION3D'
    init_inputs = [
        NodeInputBP(dtype=dtypes.String(default="#", size='m'), label='OwnIFCID'),
        NodeInputBP(dtype=dtypes.Integer(default=0, bounds=(0, 1)), label='scale'),
        NodeInputBP(dtype=dtypes.Integer(default=0, bounds=(0, 1)), label='scale'),
        NodeInputBP(dtype=dtypes.Integer(default=0, bounds=(0, 1)), label='scale'),
    ]
    init_outputs = [
        NodeOutputBP(label='OwnIFCID')
    ]
    color = '#aabb44'


class IFCDirection2D(NodeBase):
    """Generate a random number in a given range"""
    # this __doc__ string will be displayed as tooltip in the editor

    title = 'IFCDIRECTION2D'
    init_inputs = [
        NodeInputBP(dtype=dtypes.String(default="#", size='m'), label='OwnIFCID'),
        NodeInputBP(dtype=dtypes.Integer(default=0, bounds=(0, 1)), label='scale'),
        NodeInputBP(dtype=dtypes.Integer(default=0, bounds=(0, 1)), label='scale'),
    ]
    init_outputs = [
        NodeOutputBP(label='OwnIFCID'),
    ]
    color = '#aabb44'


class IFCCartesianPoint3D(NodeBase):
    """Generate a random number in a given range"""
    # this __doc__ string will be displayed as tooltip in the editor

    title = 'IFCCARTESIANPOINT3D'
    init_inputs = [
        NodeInputBP(dtype=dtypes.String(default="#", size='m'), label='OwnIFCID'),
        NodeInputBP(dtype=dtypes.Float(default=0., bounds=(-1000., 1000.)), label='Coordinates'),
        NodeInputBP(dtype=dtypes.Float(default=0., bounds=(-1000., 1000.)), label='Coordinates'),
        NodeInputBP(dtype=dtypes.Float(default=0., bounds=(-1000., 1000.)), label='Coordinates'),
    ]
    init_outputs = [
        NodeOutputBP(label='OwnIFCID'),
    ]
    color = '#aabb44'


class IFCCartesianPoint2D(NodeBase):
    """Generate a random number in a given range"""
    # this __doc__ string will be displayed as tooltip in the editor

    title = 'IFCCARTESIANPOINT2D'
    init_inputs = [
        NodeInputBP(dtype=dtypes.String(default="#", size='m'), label='OwnIFCID'),
        NodeInputBP(dtype=dtypes.Float(default=0., bounds=(-1000., 1000.)), label='scale'),
        NodeInputBP(dtype=dtypes.Float(default=0., bounds=(-1000., 1000.)), label='scale'),
    ]
    init_outputs = [
        NodeOutputBP(label='OwnIFCID'),
    ]
    color = '#aabb44'


class IfcCartesianPointList3D(NodeBase):
    """Generate a random number in a given range"""
    # this __doc__ string will be displayed as tooltip in the editor

    title = 'IFCCARTESIANPOINTLIST3D'
    init_inputs = [
        NodeInputBP(dtype=dtypes.String(default="#", size='m'), label='OwnIFCID'),
        NodeInputBP(dtype=dtypes.String(default="", size='l'), label='CoordList'),
        NodeInputBP(dtype=dtypes.String(default="", size='l'), label='TagList'),
    ]
    init_outputs = [
        NodeOutputBP(label='OwnIFCID'),
    ]
    color = '#aabb44'


class IfcDimensionalExponents(NodeBase):
    """Generate a random number in a given range"""
    # this __doc__ string will be displayed as tooltip in the editor

    title = 'IFCDIMENSIONALEXPONENTS'
    init_inputs = [
        NodeInputBP(dtype=dtypes.String(default="#", size='m'), label='OwnIFCID'),
        NodeInputBP(dtype=dtypes.Float(default=0., bounds=(-1000., 1000.)), label='LengthExponent'),
        NodeInputBP(dtype=dtypes.Float(default=0., bounds=(-1000., 1000.)), label='MassExponent'),
        NodeInputBP(dtype=dtypes.Float(default=0., bounds=(-1000., 1000.)), label='TimeExponent'),
        NodeInputBP(dtype=dtypes.Float(default=0., bounds=(-1000., 1000.)), label='ElectricCurrentExponent'),
        NodeInputBP(dtype=dtypes.Float(default=0., bounds=(-1000., 1000.)), label='ThermodynamicTemperatureExponent'),
        NodeInputBP(dtype=dtypes.Float(default=0., bounds=(-1000., 1000.)), label='AmountOfSubstanceExponent'),
        NodeInputBP(dtype=dtypes.Float(default=0., bounds=(-1000., 1000.)), label='LuminousIntensityExponent'),
    ]
    init_outputs = [
        NodeOutputBP(label='OwnIFCID'),
    ]
    color = '#aabb44'


class IFCPolylop(NodeBase):
    title = 'IFCPOLYLOOP'
    init_inputs = [
        NodeInputBP(dtype=dtypes.String(default="#", size='m'), label='OwnIFCID'),
        NodeInputBP(dtype=dtypes.String(default="#", size='m'), label='IFCID'),
        NodeInputBP(dtype=dtypes.String(default="#", size='m'), label='IFCID'),
        NodeInputBP(dtype=dtypes.String(default="#", size='m'), label='IFCID')
    ]
    init_outputs = [
        NodeOutputBP(NodeInputBP(dtype=dtypes.String(default="#", size='m'), label='OwnIFCID'))
    ]
    color = '#aabb44'


class IfcTriangulatedFaceSet(NodeBase):
    title = 'IFCTRIANGULATEDFACESET'
    init_inputs = [
        NodeInputBP(dtype=dtypes.String(default="#", size='m'), label='OwnIFCID'),
        NodeInputBP(dtype=dtypes.String(default="#", size='m'), label='Coordinates'),
        NodeInputBP(dtype=dtypes.String(default="$", size='m'), label='Normals'),
        NodeInputBP(dtype=dtypes.String(default="$", size='m'), label='Closed'),
        NodeInputBP(dtype=dtypes.String(default="#", size='l'), label='CoordIndex'),
        NodeInputBP(dtype=dtypes.String(default="$", size='m'), label='PnIndex')
    ]
    init_outputs = [
        NodeOutputBP(NodeInputBP(dtype=dtypes.String(default="#", size='m'), label='OwnIFCID'))
    ]
    color = '#aabb44'


export_nodes(
    IFCBuilding,
    IFCOwnerhistory,
    IFCPersonandorganization,
    IFCApplication,
    IfcPerson,
    IfcOrganisation,
    IfcProject,
    IfcGeometricRepresentationContext,
    IfcGeometricRepresentationSubContext,
    IfcShapeRepresentation,
    IfcProductDefinitionShape,
    IfcRelAggregates,
    IfcBuildingElementProxy,
    IfcRelContainedInSpatialStructure,

    IFCUnitAssignment,
    IfcSIUnit,
    IfcConversionBasedUnit,
    IfcMeasureWithUnit,

    IfcAxis2Placement3D,
    IfcLocalPlacement,
    IFCDirection3D,
    IFCDirection2D,
    IFCCartesianPoint3D,
    IFCCartesianPoint2D,
    IfcCartesianPointList3D,
    IfcDimensionalExponents,
    IFCPolylop,
    IfcTriangulatedFaceSet
)
