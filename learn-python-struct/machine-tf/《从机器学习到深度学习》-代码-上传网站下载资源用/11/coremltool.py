from sklearn.linear_model import LinearRegression

# Train a model
model = LinearRegression()
model.fit([[1, 2], [3, 4]], [0, 1])

# Convert and save the scikit-learn model
import coremltools
coreml_model = coremltools.converters.sklearn.convert(
    model, ["feature1", "feature2"], "label")

coreml_model.save('sample.mlmodel')
