from qgis.core import QgsVectorLayer, QgsPointXY, QgsGeometry

# Set coordinates for Gwadar layer
gwadar_layer = QgsProject.instance().mapLayersByName("Gwadar")[0]
gwadar_feature = gwadar_layer.getFeature(0)  # Assuming there's only one feature in the layer
gwadar_geometry = QgsGeometry.fromPointXY(QgsPointXY(62.3315, 25.1216))
gwadar_layer.startEditing()
gwadar_feature.setGeometry(gwadar_geometry)
gwadar_layer.updateFeature(gwadar_feature)
gwadar_layer.commitChanges()

# Set coordinates for Islamabad layer
islamabad_layer = QgsProject.instance().mapLayersByName("Islamabad")[0]
islamabad_feature = islamabad_layer.getFeature(0)  # Assuming there's only one feature in the layer
islamabad_geometry = QgsGeometry.fromPointXY(QgsPointXY(73.0479, 33.6844))
islamabad_layer.startEditing()
islamabad_feature.setGeometry(islamabad_geometry)
islamabad_layer.updateFeature(islamabad_feature)
islamabad_layer.commitChanges()
