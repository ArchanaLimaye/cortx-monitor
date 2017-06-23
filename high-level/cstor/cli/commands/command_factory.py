#!/usr/bin/python
# -*- coding: utf-8 -*-

""" File containing factory class implementation for the different
subcommands supported by cstor command
"""

# Do NOT modify or remove this copyright and confidentiality notice

# Copyright 2015 Seagate Technology LLC or one of its affiliates.
#
# The code contained herein is CONFIDENTIAL to Seagate Technology LLC.
# Portions may also be trade secret. Any use, duplication, derivation,
# distribution or disclosure of this code, for any reason, not expressly
# authorized in writing by Seagate Technology LLC is prohibited.
# All rights are expressly reserved by Seagate Technology LLC.
# __author__ = Bhupesh Pant

# Import System Modules

import argparse

# Import Local Modules

from cstor.cli.commands.power import Power
from cstor.cli.commands.support_bundle import SupportBundle
from cstor.cli.commands.status import Status
from cstor.cli.commands.s3admin import S3Admin
from cstor.cli.commands.user_mgmt import UserMgmt


class Factory(object):
    """ Factory implementation to make the main cstor script
    agnostic to what sub-command is being called. As per the
    sub-command the object corresponding to that sub-command
    will be created and sent back to the main cstor script
    """

    @staticmethod
    def parse_args():
        """ Defining argparser for the main cstor command and
        including the argparser for sub-commands as the subparser
        to the main parser.
        Parser for any new subcommand to be added, should be added here
        """
        parser = argparse.ArgumentParser(description='CStor CLI command')
        subparsers = parser.add_subparsers()
        # Adding Power Command Support
        Power.add_args(subparsers)
        # Adding Bundle Command Support
        SupportBundle.add_args(subparsers)
        # Adding status Command Support
        Status.add_args(subparsers)
        # Adding S3Admin Command support
        S3Admin.add_args(subparsers)
        # Adding user_mgmt Command Support
        UserMgmt.add_args(subparsers)

        args = parser.parse_args()
        return args

    @staticmethod
    def get_subcmd():
        """ Returns the object created for the subcommand
        which was invoked by the user through CLI
        """
        args = Factory.parse_args()
        return args.func(args)
