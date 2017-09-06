#Author-
#Description-Read and Write Attributes in a Fusion 360 design

# Author-Patrick Rainsberry
# Description-Calculates bolt holes

# Importing  Fusion Commands
from .FusionTaggerCommand import FusionTaggerCommand
from .FusionParameterTaggerCommand import FusionParameterTaggerCommand
from .FusionTaggerViewerCommand import FusionTaggerViewerCommand
from .FusionTaggerImporterCommand import FusionTaggerImporterCommand
from .CloseAllCommand import CloseAllCommand

commands = []
command_definitions = []

# Define parameters for 1st command
cmd = {
    'cmd_name': 'Tag Geometry',
    'cmd_description': 'Create Attributes',
    'cmd_id': 'cmdID_FusionTagger',
    'cmd_resources': './resources',
    'workspace': 'FusionSolidEnvironment',
    'toolbar_panel_id': 'FusionTagger',
    'command_promoted': True,
    'class': FusionTaggerCommand
}
command_definitions.append(cmd)

# Define parameters for 1st command
cmd = {
    'cmd_name': 'Tag Parameters',
    'cmd_description': 'Create Attributes on user parameters',
    'cmd_id': 'cmdID_FusionParameterTagger',
    'cmd_resources': './resources',
    'workspace': 'FusionSolidEnvironment',
    'toolbar_panel_id': 'FusionTagger',
    'class': FusionParameterTaggerCommand
}
command_definitions.append(cmd)

# Define parameters for 1st command
cmd = {
    'cmd_name': 'View Attributes',
    'cmd_description': 'View Attributes in design',
    'cmd_id': 'cmdID_FusionTaggerViewerCommand',
    'cmd_resources': './resources',
    'workspace': 'FusionSolidEnvironment',
    'toolbar_panel_id': 'FusionTagger',
    'class': FusionTaggerViewerCommand
}
command_definitions.append(cmd)

# Define parameters for 1st command
cmd = {
    'cmd_name': 'Tag Files from csv',
    'cmd_description': 'import attribute values from a csv file',
    'cmd_id': 'cmdID_FusionTaggerImporterCommand',
    'cmd_resources': './resources',
    'workspace': 'FusionSolidEnvironment',
    'toolbar_panel_id': 'FusionTagger',
    'class': FusionTaggerImporterCommand
}
command_definitions.append(cmd)

# Define parameters for 3rd command
cmd = {
    'cmd_name': 'Close All Documents',
    'cmd_description': 'NOTE: This closes all documents WITHOUT prompting to save',
    'cmd_id': 'cmdID_Close_Docs',
    'cmd_resources': './resources',
    'workspace': 'FusionSolidEnvironment',
    'toolbar_panel_id': 'FusionTagger',
    'command_visible': False,
    'class': CloseAllCommand
}
command_definitions.append(cmd)

# Set to True to display various useful messages when debugging your app
debug = False


# Don't change anything below here:
for cmd_def in command_definitions:
    command = cmd_def['class'](cmd_def, debug)
    commands.append(command)


def run(context):
    for run_command in commands:
        run_command.on_run()


def stop(context):
    for stop_command in commands:
        stop_command.on_stop()
