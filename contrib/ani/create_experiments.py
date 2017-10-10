import sqlite3
import json

conn = sqlite3.connect('exps.db')

c = conn.cursor()

# c.execute('''
# INSERT INTO experiment (model_folder, num_epochs, kwargs_json, status)
# VALUES ('full_run', 10000, '{}', 'READY')
# ''')

# d = {
#   'activation': 'gaussian'
# }
# kwargs_json = json.dumps(d)
# c.execute('''
# INSERT INTO experiment (model_folder, num_epochs, kwargs_json, status)
# VALUES ('gaussian_full_run', 10000, ?, 'READY')
# ''', (kwargs_json,))
#
# d = {
#   'activation': 'gaussian',
#   'data_length': 6,
# }
# kwargs_json = json.dumps(d)
# c.execute('''
# INSERT INTO experiment (model_folder, num_epochs, kwargs_json, status)
# VALUES ('gaussian_small_run', 10000, ?, 'READY')
# ''', (kwargs_json,))
#
# d = {
#   'data_length': 6,
# }
# kwargs_json = json.dumps(d)
# c.execute('''
# INSERT INTO experiment (model_folder, num_epochs, kwargs_json, status)
# VALUES ('gaussian_small_run', 10000, ?, 'READY')
# ''', (kwargs_json,))


d = {
  'activation': 'relu',
  'data_length': 4,
  'batch_norms': [False, True, True]
}
kwargs_json = json.dumps(d)
c.execute('''
INSERT INTO experiment (model_folder, num_epochs, kwargs_json, status)
VALUES ('batch_normftt_relu_gdb4', 10000, ?, 'READY')
''', (kwargs_json,))

d = {
  'activation': 'elu',
  'data_length': 4,
  'batch_norms': [False, True, True]
}
kwargs_json = json.dumps(d)
c.execute('''
INSERT INTO experiment (model_folder, num_epochs, kwargs_json, status)
VALUES ('batch_normftt_elu_4', 10000, ?, 'READY')
''', (kwargs_json,))

d = {
  'activation': 'relu',
  'data_length': 4,
  'batch_norms': [True, True, True]
}
kwargs_json = json.dumps(d)
c.execute('''
INSERT INTO experiment (model_folder, num_epochs, kwargs_json, status)
VALUES ('batch_normttt_relu_gdb4', 10000, ?, 'READY')
''', (kwargs_json,))

d = {
  'activation': 'relu',
  'data_length': 4,
  'batch_norms': [False, False, True]
}
kwargs_json = json.dumps(d)
c.execute('''
INSERT INTO experiment (model_folder, num_epochs, kwargs_json, status)
VALUES ('batch_normfft_relu_gdb4', 10000, ?, 'READY')
''', (kwargs_json,))

conn.commit()
conn.close()
