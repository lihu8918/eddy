# -*- coding: utf-8 -*-

##########################################################################
#                                                                        #
#  Eddy: a graphical editor for the construction of Graphol ontologies.  #
#  Copyright (C) 2015 Daniele Pantaleone <danielepantaleone@me.com>      #
#                                                                        #
#  This program is free software: you can redistribute it and/or modify  #
#  it under the terms of the GNU General Public License as published by  #
#  the Free Software Foundation, either version 3 of the License, or     #
#  (at your option) any later version.                                   #
#                                                                        #
#  This program is distributed in the hope that it will be useful,       #
#  but WITHOUT ANY WARRANTY; without even the implied warranty of        #
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the          #
#  GNU General Public License for more details.                          #
#                                                                        #
#  You should have received a copy of the GNU General Public License     #
#  along with this program. If not, see <http://www.gnu.org/licenses/>.  #
#                                                                        #
#  #####################                          #####################  #
#                                                                        #
#  Graphol is developed by members of the DASI-lab group of the          #
#  Dipartimento di Ingegneria Informatica, Automatica e Gestionale       #
#  A.Ruberti at Sapienza University of Rome: http://www.dis.uniroma1.it/ #
#                                                                        #
#     - Domenico Lembo <lembo@dis.uniroma1.it>                           #
#     - Valerio Santarelli <santarelli@dis.uniroma1.it>                  #
#     - Domenico Fabio Savo <savo@dis.uniroma1.it>                       #
#     - Marco Console <console@dis.uniroma1.it>                          #
#                                                                        #
##########################################################################


from mockito import when

from eddy.core.datatypes import OWLSyntax
from eddy.core.exceptions import MalformedDiagramError
from eddy.core.export import OWLExporter
from eddy.core.functions import expandPath, isEmpty
from eddy.core.items import ConceptNode, RoleNode, InclusionEdge, AttributeNode, RangeRestrictionNode, InputEdge
from tests import EddyTestCase


class Test_Translation(EddyTestCase):

    def setUp(self):
        """
        Setup Translation specific test environment.
        """
        super().setUp()

    def init(self, path=None):
        """
        Additional specific test case initialiation tasks.
        :type path: str
        """
        if path:
            self.scene = self.mainwindow.createSceneFromGrapholFile(expandPath(path))
        else:
            self.scene = self.mainwindow.createScene(5000, 5000)

        self.mainview = self.mainwindow.createView(self.scene)
        self.subwindow = self.mainwindow.createSubWindow(self.mainview)
        self.subwindow.showMaximized()
        self.mainwindow.mdi.setActiveSubWindow(self.subwindow)
        self.mainwindow.mdi.update()

        when(self.scene.settings).value('scene/snap_to_grid', False, bool).thenReturn(False)

    ####################################################################################################################
    #                                                                                                                  #
    #   EXAMPLE FILES                                                                                                  #
    #                                                                                                                  #
    ####################################################################################################################

    def test_animals_graphol_to_owl(self):
        # GIVEN
        self.init('@examples/Animals.graphol')
        # WHEN
        translator = OWLExporter(scene=self.scene, ontoIRI='IRI', ontoPrefix='PREFIX')
        translator.work()
        # THEN
        translation = translator.export(OWLSyntax.Functional)
        self.assertIsInstance(translation, str)
        self.assertFalse(isEmpty(translation))

    def test_family_graphol_to_owl(self):
        # GIVEN
        self.init('@examples/Family.graphol')
        # WHEN
        translator = OWLExporter(scene=self.scene, ontoIRI='IRI', ontoPrefix='PREFIX')
        translator.work()
        # THEN
        translation = translator.export(OWLSyntax.Functional)
        self.assertIsInstance(translation, str)
        self.assertFalse(isEmpty(translation))

    def test_pizza_graphol_to_owl(self):
        # GIVEN
        self.init('@examples/Pizza.graphol')
        # WHEN
        translator = OWLExporter(scene=self.scene, ontoIRI='IRI', ontoPrefix='PREFIX')
        translator.work()
        # THEN
        translation = translator.export(OWLSyntax.Functional)
        self.assertIsInstance(translation, str)
        self.assertFalse(isEmpty(translation))

    ####################################################################################################################
    #                                                                                                                  #
    #   TEST MALFORMED                                                                                                 #
    #                                                                                                                  #
    ####################################################################################################################

    def test_invalid_isa(self):
        # GIVEN
        self.init()
        n0 = ConceptNode(scene=self.scene)
        n1 = RoleNode(scene=self.scene)
        e0 = InclusionEdge(scene=self.scene, source=n0, target=n1)
        self.scene.addItem(n0)
        self.scene.addItem(n1)
        self.scene.addItem(e0)
        # WHEN
        translator = OWLExporter(scene=self.scene, ontoIRI='IRI', ontoPrefix='PREFIX')
        # THEN
        self.assertRaises(MalformedDiagramError, translator.run)

    def test_invalid_equivalence(self):
        # GIVEN
        self.init()
        n0 = ConceptNode(scene=self.scene)
        n1 = RoleNode(scene=self.scene)
        e0 = InclusionEdge(scene=self.scene, source=n0, target=n1, complete=True)
        self.scene.addItem(n0)
        self.scene.addItem(n1)
        self.scene.addItem(e0)
        # WHEN
        translator = OWLExporter(scene=self.scene, ontoIRI='IRI', ontoPrefix='PREFIX')
        # THEN
        self.assertRaises(MalformedDiagramError, translator.run)

    def test_invalid_functional(self):
        # GIVEN
        self.init()
        n0 = AttributeNode(scene=self.scene)
        n1 = RangeRestrictionNode(scene=self.scene)
        e0 = InputEdge(scene=self.scene, source=n0, target=n1, functional=True)
        self.scene.addItem(n0)
        self.scene.addItem(n1)
        self.scene.addItem(e0)
        # WHEN
        translator = OWLExporter(scene=self.scene, ontoIRI='IRI', ontoPrefix='PREFIX')
        # THEN
        self.assertRaises(MalformedDiagramError, translator.run)