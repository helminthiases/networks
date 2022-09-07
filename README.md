<br>

* [Network Engines](#network-engines)
  * [NetworkX](#networkx)
  * [Apache Spark GraphFrames/GraphX](#apache-spark-graphframesgraphx)

* [Development Notes](#development-notes)

<br>

## Geographic Co&ouml;rdinates
**Equivalent, or merely neighbouring?**

<br>

The soil transmitted helminth project relies on the ESPEN data sets.  A key set of ESPEN data sets issues, raised within the 
project scope, is in relation to site identification codes, i.e.,

* Survey sites that have the same co&ouml;rdinate values have different site identification codes.

* Survey sites whose longitude or latitude values differ by fractions of a point, e.g.,<br>
  > Point A: (*longitude* 33.87212, *latitude* -2.031722)
  > 
  > Point B: (*longitude* 33.872115, *latitude* -2.0317217)


&nbsp; &nbsp; &nbsp; &nbsp; generally have different site identification codes.

* Many observations do not have a site identification code.

The aim herein is to explore methods for determining which co&ouml;rdinate points are more or less equivalent, and 
subsequently generate identification codes.

<br>

### Network Engines

In the end, ``NetworkX`` is the most feasible because **(a)** it has fewer dependencies compared to GraphFrames, **(b)** it 
is [well-supported](https://networkx.org/documentation/stable/developer/about_us.html#support) and 
[well-maintained](https://github.com/networkx/networkx/releases), and 
**(c)** [accelerated graph analytics](https://www.nvidia.com/en-us/glossary/data-science/networkx/) via GPU, for very large
networks, is an option.


#### PYTHON NetworkX

The graphs.ipynb notebook: <br>
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/helminthiases/networks/blob/develop/notebooks/graphs.ipynb)

The approach described in this notebook is the approach followed in [infections](https://www.github.com/helminthiases/infections).


#### APACHE SPARK GraphFrames/GraphX

* Unload [`graphframes-0.8.2-spark3.2-s_2.12.jar`](https://repos.spark-packages.org/graphframes/graphframes/0.8.2-spark3.2-s_2.12/graphframes-0.8.2-spark3.2-s_2.12.jar) 
  & [`0.8.2-spark3.2-s_2.12.zip`](https://github.com/graphframes/graphframes/archive/1cd7abb0f424fd76d76ea07438e6486f44fbb440.zip) 
  at  [``graphframes``](https://spark-packages.org/package/graphframes/graphframes)

* Add ``graphframes-0.8.2-spark3.2-s_2.12.jar`` to ``spark/jars/``, i.e., to the directory of 
  de-archived [spark files](https://www.apache.org/dyn/closer.lua/spark/spark-3.2.1/spark-3.2.1-bin-hadoop3.2.tgz).

* In relation to a python conda environment, whilst ``graphframes`` maintenance is inconsistent manually upgrade ``graphframes`` within a conda environment
  * Unzip `0.8.2-spark3.2-s_2.12.zip` outwith a conda environment's directory. 
  * Transfer ``graphframes-0.8.2/python/graphframes`` &rarr; ``lib/site-packages/graphframes``; the latter being a sub-directory of the conda environment's directory.
  * Ascertain that all members of the directories  ``graphframes`` & ``graphframes-0.8.2.dist-info``, in ``lib/site-packages``, point/refer to ``0.8.2``.

<br>

### Development Notes

Using an Anaconda environment named ``spark``

````shell
  conda create --prefix ~/spark
  conda activate spark
  conda install -c anaconda python==3.8.13
````

The key packages are ``pandas``, ``numpy``, ``findspark``, ``geopandas``, ``jupyterlab`` (``pywin32``, ``nodejs``), 
``matplotlib``, ``networkx``, and ``graphframes``.  In terms of the requirements file

````shell
pip freeze -r docs/filter.txt > requirements.txt
````

<br>
<br>

<br>
<br>

<br>
<br>

<br>
<br>