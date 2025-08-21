
Validation Matrix
=================

.. _validation_matrix:

This section provides validation information for robosapiensIO toolkit features across different example implementations.

.. |ok| image:: ../../assets/ok.png
   :height: 2ex
.. |nok| image:: ../../assets/_nok.png
   :height: 2ex
.. |uk| image:: ../../assets/thinking.png
   :height: 2ex

Feature Validation Matrix
-------------------------

The following matrix shows the validation status of robosapiensIO features across different example projects:

.. csv-table:: Feature Validation Status
   :file: validation.csv
   :header-rows: 1
   :class: longtable
   :widths: 15, 20, 25, 15, 15, 15, 15

Legend
------

* |ok| **Supported/Working**: Feature is fully implemented and tested
* |nok| **Not Supported**: Feature is not yet implemented or not working
* |uk| **Under Investigation**: Feature status is being evaluated

Example Projects
----------------

* **hello world**: Basic example implementation
* **hello worldv2**: Enhanced version with additional features  
* **Distributed Deployment**: Advanced version with full feature set
* **NTNU**: Real-world case study implementation

Testing Framework
-----------------

All examples and tutorials are validated using our continuous integration pipeline to ensure they work as expected.

.. note::
   For detailed validation results, please refer to the project's CI/CD pipeline results.