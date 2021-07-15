.. _roughness:

Roughness
---------

.. figure:: img/Roughness1.png
   :scale: 50 %
   :alt: Roughness Widget

   Roughness Widget

The roughness widget creates a new raster based on the calculated roughness from an input DEM raster.

Usage
^^^^^

#. | Select the input DEM raster. You can either select from imported rasters using the Input
   | combo box or select one from your PC (1).
#. | Select the output roughness raster location. You can either type in the absolute file path
   | yourself or pick one with a dialog (2).
#. Start the calculation (4)

If you want to use the created roughness raster in your LSAT Project you need to import it using the
:doc:`Import Raster Widget</DATA/Import/ImportRaster>`.

Clicking on Cancel (5) closes the widget.

Input and Output
^^^^^^^^^^^^^^^^
+------------+---------------------------------------------------------------+
|  Input     | Digital Elevation Model raster dataset (.tif)                 |
+------------+---------------------------------------------------------------+
|  Output    | Roughness raster dataset (.tif)                               |
+------------+---------------------------------------------------------------+ 