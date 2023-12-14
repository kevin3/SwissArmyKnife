#update conda first
conda update -n base -c defaults conda

conda create -n tensorflow_cpu pip python=3.8
activate tensorflow_cpu
conda install tensorflow keras matplotlib seaborn scikit-learn jupyter
jupyter notebook

conda create -n tensorflow_gpu pip python=3.8
activate tensorflow_gpu
conda install tensorflow-gpu keras-gpu matplotlib seaborn scikit-learn jupyter
jupyter notebook

conda create -n pytorch_310 python=3.10
conda activate pytorch_310
conda install opencv jupyter matplotlib pandas seaborn scikit-learn tqdm pytorch torchvision torchaudio pytorch-cuda=12.1 -c pytorch -c nvidia
