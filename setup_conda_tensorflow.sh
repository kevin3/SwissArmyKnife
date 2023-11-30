#update conda first
conda update -n base -c defaults conda

conda create -n tensorflow_cpu pip python=3.8
activate tensorflow_cpu
conda install tensorflow keras matplotlib seaborn scikit-learn

conda create -n tensorflow_gpu pip python=3.8
activate tensorflow_gpu
conda install tensorflow-gpu keras-gpu matplotlib seaborn scikit-learn
