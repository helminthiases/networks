<br>

Mapping geographic coordinates

<br>


### Development Notes

````shell
pip freeze -r docs/filter.txt > requirements.txt
````


<br>
<br>

### Network Engines

In the end, ``NetworkX`` is the most feasible because (a) it has fewer dependencies compared to GraphFrames, (b) it 
is [well-supported](https://networkx.org/documentation/stable/developer/about_us.html#support) and 
[well-maintained](https://github.com/networkx/networkx/releases), and 
(c) [accelerated graph analytics](https://www.nvidia.com/en-us/glossary/data-science/networkx/) via GPU, for very large
networks, is an option.

<br>

#### NetworkX

The graphs.ipynb notebook: <br>
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/helminthiases/networks/blob/develop/notebooks/graphs.ipynb)

<br>

#### Apache Spark GraphFrames/GraphX

* [``graphframes``](https://spark-packages.org/package/graphframes/graphframes)

* Add ``graphframes-0.8.2-spark3.2-s_2.12`` to ``spark/jars/``
  * the jar is [graphframes-0.8.2-spark3.2-s_2.12.jar](https://repos.spark-packages.org/graphframes/graphframes/0.8.2-spark3.2-s_2.12/graphframes-0.8.2-spark3.2-s_2.12.jar)

* Manually upgrade ``graphframes`` within a conda environment
  * Unload [0.8.2-spark3.2-s_2.12](https://github.com/graphframes/graphframes/archive/1cd7abb0f424fd76d76ea07438e6486f44fbb440.zip)
  * Unzip `0.8.2-spark3.2-s_2.12`, than transfer ``graphframes-0.8.2/python/graphframes`` &rarr; ``lib/site-packages/graphframes``
  * Ascertain that all members of directories  ``graphframes`` & ``graphframes-0.8.2.dist-info``, in ``lib/site-packages``, point/refer to ``0.8.2`` 

<br>
<br>

<br>
<br>

<br>
<br>

<br>
<br>