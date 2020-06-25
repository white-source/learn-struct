print(__doc__)

# Authors: Vlad Niculae, Alexandre Gramfort
# License: BSD 3 clause

import ssl
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context
    

import matplotlib.pyplot as plt
from sklearn.datasets import fetch_olivetti_faces
from sklearn import decomposition

n_row, n_col = 2, 4
n_components = n_row * n_col
image_shape = (64, 64)

# #############################################################################
# Load faces data
dataset = fetch_olivetti_faces(shuffle=True)
faces = dataset.data 

n_samples, n_features = faces.shape
faces -= faces.mean(axis=1).reshape(n_samples, -1)

def plot_gallery(title, images, n_col=n_col, n_row=n_row):
    plt.figure(figsize=(2. * n_col, 2.26 * n_row))
    plt.suptitle(title, size=16)

    for i, comp in enumerate(images):
        plt.subplot(n_row, n_col, i + 1)
        vmax = max(comp.max(), -comp.min())
        plt.imshow(comp.reshape(image_shape), cmap=plt.cm.gray,
                   interpolation='nearest',
                   vmin=-vmax, vmax=vmax)
        plt.xticks(())
        plt.yticks(())
    plt.subplots_adjust(0.01, 0.05, 0.99, 0.93, 0.04, 0.)


plot_gallery("Olivetti faces", faces[:n_components])

estimator = decomposition.PCA(n_components=n_components, svd_solver='randomized',
                              whiten=True)
estimator.fit(faces)
plot_gallery('Eigen faces', estimator.components_[:n_components])

plt.show()
