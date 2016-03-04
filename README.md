![Eddy](/eddy/ui/artwork/banner.png?raw=true)

Eddy is a graphical editor for the construction of Graphol ontologies. Eddy features a design environment specifically 
thought out for generating Graphol ontologies through ad-hoc functionalities. Drawing features allow designers to 
comfortably edit ontologies in a central viewport area, while two lateral docking areas contains specifically-tailored 
widgets for editing, navigation and inspection of the diagram. 

In order to support interaction with third-party tools such as OWL 2 reasoners and editors like [Protégé], Eddy is able 
to export the produced Graphol ontology into an OWL 2 ontology. Other simpler exporting file formats, like PDF, are 
also currently provided.

Eddy is written in [Python] and make use of the [PyQt5] python bindings for the cross-platform [Qt5] framework. 

### About Graphol

[Graphol] is a language for the diagrammatic representation of Description Logic (DL) ontologies, developed by members 
of the DASI-lab group of the [Dipartimento di Ingegneria Informatica, Automatica e Gestionale "A.Ruberti"] at [Sapienza] 
University of Rome. Graphol offers a completely visual representation of ontologies to users, in order to help 
understanding by people who are not skilled in logic. Graphol provides designers with simple graphical primitives for 
ontology editing, avoiding complex textual syntax. Graphol's basic components are inspired by Entity Relationship (ER) 
diagrams, thus ontologies that can be rendered as ER diagrams have in Graphol a similar diagrammatic shape.

* [Domenico Lembo](http://www.dis.uniroma1.it/~lembo/)                         
* [Valerio Santarelli](http://www.dis.uniroma1.it/~dottoratoii/students/valerio-santarelli)           
* [Domenico Fabio Savo](http://www.dis.uniroma1.it/~savo/)                       
* [Marco Console](http://www.dis.uniroma1.it/~dottoratoii/students/marco-console)                 

### Screenshot

![screenshot](/eddy/ui/artwork/shot01.png?raw=true)

### License

Eddy is licensed under the GNU General Public License v3. See the LICENSE file included with the distribution.

### Build status

# [![circleci](https://avatars0.githubusercontent.com/u/1231870?v=2&s=50)](https://circleci.com/) Circle CI [![Circle CI](https://circleci.com/gh/danielepantaleone/eddy/tree/master.svg?style=svg&circle-token=d4611bacee6dca791faf8b03502ffabdeb099ffe)](https://circleci.com/gh/danielepantaleone/eddy/tree/master)

### Resources

* [Source code](https://github.com/danielepantaleone/eddy)
* [Bug tracker](https://github.com/danielepantaleone/eddy/issues)
* [Graphol website](http://www.dis.uniroma1.it/~graphol/)

[Dipartimento di Ingegneria Informatica, Automatica e Gestionale "A.Ruberti"]: http://www.dis.uniroma1.it/en
[Sapienza]: http://en.uniroma1.it/
[Graphol]: http://www.dis.uniroma1.it/~graphol/
[Python]: https://www.python.org/
[PyQt5]: https://riverbankcomputing.com/software/pyqt/intro
[Qt5]: http://www.qt.io/
[Protégé]: http://protege.stanford.edu/