'''

Examples of usage and demonstration of abilities of BIRCH algorithm in cluster analysis.

Copyright (C) 2015    Andrei Novikov (spb.andr@yandex.ru)

pyclustering is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

pyclustering is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

'''

from pyclustering.clustering.birch import birch;

from pyclustering.support.cftree import measurement_type;

from pyclustering.support import read_sample;
from pyclustering.support import draw_clusters;
from pyclustering.support import timedcall;

from pyclustering.samples.definitions import SIMPLE_SAMPLES, FCPS_SAMPLES;

def template_clustering(number_clusters, path, branching_factor = 5, max_node_entries = 5, initial_diameter = 0.0, type_measurement = measurement_type.CENTROID_EUCLIDIAN_DISTANCE, entry_size_limit = 200, ccore = True):
    sample = read_sample(path);
    
    birch_instance = birch(sample, number_clusters, branching_factor, max_node_entries, initial_diameter, type_measurement, entry_size_limit, ccore)
    (ticks, result) = timedcall(birch_instance.process);
    
    print("Sample: ", path, "\t\tExecution time: ", ticks, "\n");
    
    clusters = birch_instance.get_clusters();
    draw_clusters(sample, clusters);
    
    
def cluster_sample1():
    template_clustering(2, SIMPLE_SAMPLES.SAMPLE_SIMPLE1);
    template_clustering(2, SIMPLE_SAMPLES.SAMPLE_SIMPLE1, 5, 5, 0.1, measurement_type.CENTROID_EUCLIDIAN_DISTANCE, 2);      # only two entries available

def cluster_sample2():
    template_clustering(3, SIMPLE_SAMPLES.SAMPLE_SIMPLE2);
    
def cluster_sample3():
    template_clustering(4, SIMPLE_SAMPLES.SAMPLE_SIMPLE3);
    
def cluster_sample4():
    template_clustering(5, SIMPLE_SAMPLES.SAMPLE_SIMPLE4);
    
def cluster_sample5():
    template_clustering(4, SIMPLE_SAMPLES.SAMPLE_SIMPLE5);
    
def cluster_elongate():
    template_clustering(2, SIMPLE_SAMPLES.SAMPLE_ELONGATE);

def cluster_lsun():
    template_clustering(3, FCPS_SAMPLES.SAMPLE_LSUN);
    template_clustering(3, FCPS_SAMPLES.SAMPLE_LSUN, 5, 5, 0.2, measurement_type.CENTROID_MANHATTAN_DISTANCE, 200);         # not correct, but almost good result
    
def cluster_target():
    template_clustering(6, FCPS_SAMPLES.SAMPLE_TARGET);
    template_clustering(6, FCPS_SAMPLES.SAMPLE_TARGET, 5, 10, 0.5, measurement_type.CENTROID_MANHATTAN_DISTANCE, 200);       # interesting - sliced cake.
    template_clustering(6, FCPS_SAMPLES.SAMPLE_TARGET, 50, 100, 0.5, measurement_type.VARIANCE_INCREASE_DISTANCE, 200);      # interesting - sliced cake.

def cluster_two_diamonds():
    template_clustering(2, FCPS_SAMPLES.SAMPLE_TWO_DIAMONDS);  

def cluster_wing_nut():
    template_clustering(2, FCPS_SAMPLES.SAMPLE_WING_NUT);
    template_clustering(2, FCPS_SAMPLES.SAMPLE_WING_NUT, 5, 5, 0.1, measurement_type.CENTROID_EUCLIDIAN_DISTANCE, 800);     # not correct, but almost good result
    
def cluster_chainlink():
    template_clustering(2, FCPS_SAMPLES.SAMPLE_CHAINLINK);     
    
def cluster_hepta():
    template_clustering(7, FCPS_SAMPLES.SAMPLE_HEPTA); 
    
def cluster_tetra():
    template_clustering(4, FCPS_SAMPLES.SAMPLE_TETRA);    
    
def cluster_engy_time():
    template_clustering(2, FCPS_SAMPLES.SAMPLE_ENGY_TIME);  # one cluster is allocated
    template_clustering(2, FCPS_SAMPLES.SAMPLE_ENGY_TIME, 10, 10, 0.05, measurement_type.VARIANCE_INCREASE_DISTANCE, 500);  # good result
    
    
cluster_sample1();
cluster_sample2();
cluster_sample3();
cluster_sample4();
cluster_sample5();
cluster_elongate();
cluster_lsun();
cluster_target();
cluster_two_diamonds();
cluster_wing_nut();
cluster_chainlink();
cluster_hepta();
cluster_tetra();
cluster_engy_time();