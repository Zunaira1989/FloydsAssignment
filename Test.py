import unittest
import Floyds

class TestFloydWarshall(unittest.TestCase):
    def test_floydWarshall(self): # unit test for resursive function
        # create a simple input graph
        graph = [[0, 7, Floyds.NO_PATH, 8],
             [Floyds.NO_PATH, 0, 5, Floyds.NO_PATH],
             [Floyds.NO_PATH, Floyds.NO_PATH, 0,   2],
             [Floyds.NO_PATH, Floyds.NO_PATH, Floyds.NO_PATH, 0]
             ]
        
        # expected output after running the floydWarshall algorithm
        expected_output = [
            [0, 7, 12, 8],
            [Floyds.NO_PATH, 0, 5, 7],
            [Floyds.NO_PATH, Floyds.NO_PATH, 0, 2],
            [Floyds.NO_PATH, Floyds.NO_PATH, Floyds.NO_PATH, 0]
        ]
        
        # run the floydWarshall algorithm on the input graph
        result = Floyds.floydWarshall(graph, 0)
        
        # check if the result matches the expected output
        self.assertEqual(result, expected_output)
    
    def test_floydWarshallIterative(self): # unit test for iterative function
    # create a simple input graph
        graph = [[0, 7, Floyds.NO_PATH, 8],
            [Floyds.NO_PATH, 0, 5, Floyds.NO_PATH],
            [Floyds.NO_PATH, Floyds.NO_PATH, 0,   2],
            [Floyds.NO_PATH, Floyds.NO_PATH, Floyds.NO_PATH, 0]
            ]
        
        # expected output after running the floydWarshallIterative algorithm
        expected_output = [
            [0, 7, 12, 8],
            [Floyds.NO_PATH, 0, 5, 7],
            [Floyds.NO_PATH, Floyds.NO_PATH, 0, 2],
            [Floyds.NO_PATH, Floyds.NO_PATH, Floyds.NO_PATH, 0]
        ]
        
        # run the floydWarshallIterative algorithm on the input graph
        result = Floyds.floydWarshallIterative(graph)
        
        # check if the result matches the expected output
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()