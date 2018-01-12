"""
Copyright 2017 NREL

Licensed under the Apache License, Version 2.0 (the "License"); you may not use
this file except in compliance with the License. You may obtain a copy of the
License at http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed
under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.
"""

from floris.base_object import BaseObject

class BaseObjectTest():
    def test_all(self):
        test_object_instantiation()

def test_object_instantiation():
    """
    The class should initialize with the standard inputs
    """
    assert BaseObject() is not None
