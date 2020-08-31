rm -r ./tmp/minigo_base


../../../venv/bin/python3.6 main.py bootstrap --working-dir=./tmp/minigo_base --model-save-path=./tmp/minigo_base/models/000000-bootstrap





../../../venv/bin/python3.6 main.py selfplay ./tmp/minigo_base/models/000000-bootstrap --num_readouts=1000 -v 3 --output-dir=./tmp/minigo_base/data/selfplay/000000-bootstrap/local_worker


../../../venv/bin/python3.6 main.py multi-selfplay 10000 ./tmp/minigo_base --num_readouts=1000 -v 3





../../../venv/bin/python3.6 main.py train-dir ./tmp/minigo_base ./tmp/minigo_base/data/selfplay /tmp/minigo_base/models/000001-first

../../../venv/bin/python3.6 main.py multi-train-dir 10000 ./tmp/minigo_base ./tmp/minigo_base/models/000001-first





../../../venv/bin/python3 main.py gtp -l /tmp/minigo_base/models/000001-first --num_readouts=10000 -v 3


../../../venv/bin/python3.6 -m tensorboard.main --logdir /tmp/minigo_base/


"args" : ["selfplay", "/tmp/minigo_base/models/000000-bootstrap", "--num_readouts=10", "-v 3", "--output-dir=/tmp/minigo_base/data/selfplay/000000-bootstrap/local_worker"]


"args" : ["train-dir", "/tmp/minigo_base", "/tmp/minigo_base/data/selfplay/000000-bootstrap/local_worker", " /tmp/minigo_base/models/000001-first"]

"args" : ["gtp", "-l", "/tmp/minigo_base/models/000001-first", "--num_readouts=10", "-v 3"]
