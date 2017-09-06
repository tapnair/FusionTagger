import adsk.core
import adsk.fusion
import traceback

import os
from os.path import expanduser
import csv

from .Fusion360Utilities.Fusion360Utilities import get_app_objects
from .Fusion360Utilities.Fusion360CommandBase import Fusion360CommandBase


# Function to convert a csv file to a list of dictionaries.  Takes in one variable called "data_file_name"
def csv_dict_list(data_file_name):
    csv_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data', data_file_name)

    # Open variable-based csv, iterate over the rows and map values to a list of dictionaries containing key/value pairs
    reader = csv.DictReader(open(csv_file, 'r'))
    dict_list = []
    for line in reader:
        dict_list.append(line)
    return dict_list


# TODO make number an optional match field?
def tag_folder(root_folder, attribute_list, group_name):

    for folder in root_folder.dataFolders:

        tag_folder(folder, attribute_list)

    for file in root_folder.dataFiles:

        if file.fileExtension == "f3d":
            match = next((l for l in attribute_list if l['Part Number'] == file.name), None)

            if match is not None:
                open_doc(file)
                tag_active_doc(match, group_name)


def open_doc(data_file):
    app = adsk.core.Application.get()

    try:
        document = app.documents.open(data_file, True)
        if document is not None:
            document.activate()
    except:
        pass


def tag_active_doc(attribute_dict, group_name):

    ao = get_app_objects()

    root_comp = ao['root_comp']

    for key, value in attribute_dict.items():

        root_comp.attributes.add(group_name, key, value)


# Class for a Fusion 360 Command
# Place your program logic here
# Delete the line that says "pass" for any method you want to use
class FusionTaggerImporterCommand(Fusion360CommandBase):

    # Run whenever a user makes any change to a value or selection in the addin UI
    # Commands in here will be run through the Fusion processor and changes will be reflected in  Fusion graphics area
    def on_preview(self, command, inputs, args, input_values):
        pass

    # Run after the command is finished.
    # Can be used to launch another command automatically or do other clean up.
    def on_destroy(self, command, inputs, reason, input_values):
        pass

    # Run when any input is changed.
    # Can be used to check a value and then update the add-in UI accordingly
    def on_input_changed(self, command_, command_inputs, changed_input, input_values):
        pass

    # Run when the user presses OK
    # This is typically where your main program logic would go
    def on_execute(self, command, inputs, args, input_values):

        # todo get csv input
        # data_file_name = os.path.dirname(os.path.realpath(__file__))

        # TODO Remove defaults
        data_file_name = '/Users/rainsbp/Library/Application Support/Autodesk/Autodesk Fusion 360/API/AddIns/OverNightComposites'
        data_file_name += '/Fusion_360_Metadata.csv'

        attribute_list = csv_dict_list(data_file_name)

        app = adsk.core.Application.get()
        tag_folder(app.data.activeProject.rootFolder, attribute_list, input_values['attribute_group'])

        close_command = get_app_objects()['ui'].commandDefinitions.itemById('cmdID_Close_Docs')
        close_command.execute()

    # Run when the user selects your command icon from the Fusion 360 UI
    # Typically used to create and display a command dialog box
    # The following is a basic sample of a dialog UI
    def on_create(self, command, command_inputs):

        command_inputs.addStringValueInput('attribute_group', 'Group', 'ONC')
