# Copyright (c) Microsoft Corporation
# Licensed under the MIT License.

"""Defines the Fairness Manager class."""

from raitools._managers.base_manager import BaseManager


class FairnessManager(BaseManager):
    def __init__(self):
        pass

    def add(self, sensitive_features):
        raise NotImplementedError(
            "Add not implemented for FairnessManager")

    def compute(self):
        pass

    def get(self):
        raise NotImplementedError(
            "Get not implemented for FairnessManager")

    def list(self):
        pass

    @property
    def name(self):
        """Get the name of the fairness manager.

        :return: The name of the fairness manager.
        :rtype: str
        """
        return "fairness"

    def save(self, path):
        raise NotImplementedError(
            "Save not implemented for FairnessManager")

    @staticmethod
    def load(path):
        raise NotImplementedError(
            "Load not implemented for FairnessManager")
