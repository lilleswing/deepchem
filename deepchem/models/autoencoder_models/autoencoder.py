"""
TODO(LESWING) Remove h5py dependency
TODO(LESWING) Remove keras dependency
"""

from deepchem.models import Model
from deepchem.models.autoencoder_models.model import MoleculeVAE
from deepchem.trans.transformers import zinc_charset
import os


class TensorflowMoleculeEncoder(Model):
  def __init__(self,
               model_dir=None,
               verbose=True,
               charset=zinc_charset,
               latent_rep_size=292):
    """
        TODO(LESWING) Convert Dataset.[X,y,w] from the h5.py format.
        TODO(LESWING) default to a charset constructed via Zinc -- it should be a superset
        of other charsets
        :param model_dir:
        :param verbose:
        :param charset: list of chars
        :param latent_rep_size:
        """
    super(TensorflowMoleculeEncoder, self).__init__(
      model_dir=model_dir, verbose=verbose)
    weights_file = os.path.join(model_dir, "model.h5")
    if os.path.isfile(weights_file):
      m = MoleculeVAE()
      m.load(charset, weights_file, latent_rep_size=latent_rep_size)
      self.model = m
    else:
      # TODO (LESWING) Lazy Load
      raise ValueError("Model file %s doesn't exist" % weights_file)

  def fit(self, dataset, nb_epoch=10, batch_size=50, **kwargs):
    """
        TODO(LESWING) Test
        """
    self.model.autoencoder.fit(
      dataset.X,
      dataset.X,
      shuffle=True,
      nb_epoch=10,
      batch_size=50,
      callbacks=[],
      validation_data=(dataset.y, dataset.y))

  def predict_on_batch(self, X):
    """
        TODO(LESWING) Test
        """
    x_latent = self.model.encoder.predict(X)
    return x_latent

  def get_num_tasks(self):
    """
    Get number of tasks.
    """
    return 1


class TensorflowMoleculeDecoder(Model):
  def __init__(self,
               model_dir=None,
               verbose=True,
               charset=zinc_charset,
               latent_rep_size=292):
    """
        TODO(LESWING) Convert Dataset.[X,y,w] from the h5.py format.
        TODO(LESWING) default to a charset constructed via Zinc -- it should be a superset
        of other charsets
        :param model_dir:
        :param verbose:
        :param charset: list of chars
        :param latent_rep_size:
        """
    super(TensorflowMoleculeDecoder, self).__init__(
      model_dir=model_dir, verbose=verbose)
    weights_file = os.path.join(model_dir, "model.h5")
    if os.path.isfile(weights_file):
      m = MoleculeVAE()
      m.load(charset, weights_file, latent_rep_size=latent_rep_size)
      self.model = m
    else:
      # TODO (LESWING) Lazy Load
      raise ValueError("Model file %s doesn't exist" % weights_file)

  def fit(self, dataset, nb_epoch=10, batch_size=50, **kwargs):
    """
    TODO(LESWING) Test
    """
    raise ValueError("Only can read in Cached Models")

  def predict_on_batch(self, X):
    """
        TODO(LESWING) Test
        """
    x_latent = self.model.decoder.predict(X)
    return x_latent