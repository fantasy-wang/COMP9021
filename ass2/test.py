'''
Tests for UNSW COMP9021 Assignment 2 (2019T1)

---------- Tests by Eric Martin ----------

>>> from tangram import *
>>> are_valid(available_coloured_pieces(open('files/eric/pieces_A.xml')))
True
>>> are_valid(available_coloured_pieces(open('files/eric/pieces_AA.xml')))
True
>>> are_valid(available_coloured_pieces(open('files/eric/incorrect_pieces_1.xml')))
False
>>> are_valid(available_coloured_pieces(open('files/eric/incorrect_pieces_2.xml')))
False
>>> are_valid(available_coloured_pieces(open('files/eric/incorrect_pieces_3.xml')))
False
>>> are_valid(available_coloured_pieces(open('files/eric/incorrect_pieces_4.xml')))
False

>>> are_identical_sets_of_coloured_pieces(
...    available_coloured_pieces(open('files/eric/pieces_A.xml')),
...    available_coloured_pieces(open('files/eric/pieces_AA.xml')))
True
>>> are_identical_sets_of_coloured_pieces(
...    available_coloured_pieces(open('files/eric/pieces_A.xml')),
...    available_coloured_pieces(open('files/eric/shape_A_1.xml')))
False

>>> is_solution(
...    available_coloured_pieces(open('files/eric/tangram_A_1_a.xml')),
...    available_coloured_pieces(open('files/eric/shape_A_1.xml')))
True
>>> is_solution(
...    available_coloured_pieces(open('files/eric/tangram_A_1_b.xml')),
...    available_coloured_pieces(open('files/eric/shape_A_1.xml')))
True
>>> is_solution(
...    available_coloured_pieces(open('files/eric/tangram_A_2_a.xml')),
...    available_coloured_pieces(open('files/eric/shape_A_2.xml')))
True
>>> is_solution(
...    available_coloured_pieces(open('files/eric/tangram_A_2_b.xml')),
...    available_coloured_pieces(open('files/eric/shape_A_2.xml')))
True
>>> is_solution(
...    available_coloured_pieces(open('files/eric/tangram_A_2_a.xml')),
...    available_coloured_pieces(open('files/eric/shape_A_1.xml')))
False

---------- Tests by Kieran Owens ----------

>>> are_valid(available_coloured_pieces(open('files/kieran/_pieces_A.xml')))
True
>>> are_valid(available_coloured_pieces(open('files/kieran/_pieces_AA.xml')))
True
>>> are_valid(available_coloured_pieces(open('files/kieran/_pieces_AAf.xml')))
True
>>> are_valid(available_coloured_pieces(open('files/kieran/_pieces_B.xml')))
True
>>> are_valid(available_coloured_pieces(open('files/kieran/_pieces_BB.xml')))
True

>>> are_identical_sets_of_coloured_pieces(
...    available_coloured_pieces(open('files/kieran/_pieces_A.xml')),
...    available_coloured_pieces(open('files/kieran/_pieces_AA.xml')))
True
>>> are_identical_sets_of_coloured_pieces(
...    available_coloured_pieces(open('files/kieran/_pieces_B.xml')),
...    available_coloured_pieces(open('files/kieran/_pieces_BB.xml')))
True
>>> are_identical_sets_of_coloured_pieces(
...    available_coloured_pieces(open('files/kieran/_pieces_A.xml')),
...    available_coloured_pieces(open('files/kieran/_pieces_AAf.xml')))
False
>>> are_identical_sets_of_coloured_pieces(
...    available_coloured_pieces(open('files/kieran/_pieces_AA.xml')),
...    available_coloured_pieces(open('files/kieran/_pieces_AAf.xml')))
False

>>> is_solution(
...    available_coloured_pieces(open('files/kieran/_Tangram_A_1.xml')),
...    available_coloured_pieces(open('files/kieran/_Shape_A_1.xml')))
True
>>> is_solution(
...    available_coloured_pieces(open('files/kieran/_Tangram_A_1f.xml')),
...    available_coloured_pieces(open('files/kieran/_Shape_A_1.xml')))
False
>>> is_solution(
...    available_coloured_pieces(open('files/kieran/_Tangram_A_1ff.xml')),
...    available_coloured_pieces(open('files/kieran/_Shape_A_1.xml')))
False
>>> is_solution(
...    available_coloured_pieces(open('files/kieran/_Tangram_B_1.xml')),
...    available_coloured_pieces(open('files/kieran/_Shape_B_1.xml')))
True
>>> is_solution(
...    available_coloured_pieces(open('files/kieran/_Tangram_A_1.xml')),
...    available_coloured_pieces(open('files/kieran/_Shape_A_1f.xml')))
False

---------- Tests by Sijie Hou ----------

>>> is_solution(
...    available_coloured_pieces(open('files/sijie/tangram.xml')),
...    available_coloured_pieces(open('files/sijie/shape.xml')))
False

---------- Tests by Christopher Lord ----------

>>> are_valid(available_coloured_pieces(open('files/chris/are_valid/not-valid-concave.xml')))
False
>>> are_valid(available_coloured_pieces(open('files/chris/are_valid/not-valid-intersections.xml')))
False
>>> are_valid(available_coloured_pieces(open('files/chris/are_valid/not-valid-intersection-lost-edge.xml')))
False
>>> are_valid(available_coloured_pieces(open('files/chris/are_valid/not-valid-no-pieces.xml')))
False
>>> are_valid(available_coloured_pieces(open('files/chris/are_valid/not-valid-one-side.xml')))
False
>>> are_valid(available_coloured_pieces(open('files/chris/are_valid/not-valid-straight-sides.xml')))
False
>>> are_valid(available_coloured_pieces(open('files/chris/are_valid/not-valid-two-sides.xml')))
False
>>> are_valid(available_coloured_pieces(open('files/chris/are_valid/not-valid-overlapping-points.xml')))
False
>>> are_valid(available_coloured_pieces(open('files/chris/is_solution/A-solution.xml')))
True
>>> are_valid(available_coloured_pieces(open('files/chris/is_solution/A-solution-2.xml')))
True
>>> are_valid(available_coloured_pieces(open('files/chris/is_solution/B-solution.xml')))
True
>>> are_valid(available_coloured_pieces(open('files/chris/is_solution/B-solution-2.xml')))
True
>>> are_valid(available_coloured_pieces(open('files/chris/is_solution/C-solution.xml')))
True
>>> are_valid(available_coloured_pieces(open('files/chris/is_solution/D-solution.xml')))
True
>>> are_valid(available_coloured_pieces(open('files/chris/is_solution/E-solution.xml')))
True
>>> are_valid(available_coloured_pieces(open('files/chris/is_solution/F-solution.xml')))
True
>>> are_valid(available_coloured_pieces(open('files/chris/is_solution/G-solution.xml')))
True
>>> are_valid(available_coloured_pieces(open('files/chris/are_identical_sets_of_coloured_pieces/identical-A1.xml')))
True
>>> are_valid(available_coloured_pieces(open('files/chris/are_identical_sets_of_coloured_pieces/identical-B1.xml')))
True

>>> are_identical_sets_of_coloured_pieces(
...    available_coloured_pieces(open('files/chris/are_identical_sets_of_coloured_pieces/identical-A1.xml')),
...    available_coloured_pieces(open('files/chris/are_identical_sets_of_coloured_pieces/identical-A2.xml')))
True
>>> are_identical_sets_of_coloured_pieces(
...    available_coloured_pieces(open('files/chris/are_identical_sets_of_coloured_pieces/identical-A1.xml')),
...    available_coloured_pieces(open('files/chris/are_identical_sets_of_coloured_pieces/identical-A3.xml')))
True
>>> are_identical_sets_of_coloured_pieces(
...    available_coloured_pieces(open('files/chris/are_identical_sets_of_coloured_pieces/identical-A1.xml')),
...    available_coloured_pieces(open('files/chris/are_identical_sets_of_coloured_pieces/identical-A4.xml')))
True
>>> are_identical_sets_of_coloured_pieces(
...    available_coloured_pieces(open('files/chris/are_identical_sets_of_coloured_pieces/identical-A1.xml')),
...    available_coloured_pieces(open('files/chris/are_identical_sets_of_coloured_pieces/identical-A5.xml')))
True
>>> are_identical_sets_of_coloured_pieces(
...    available_coloured_pieces(open('files/chris/are_identical_sets_of_coloured_pieces/identical-A1.xml')),
...    available_coloured_pieces(open('files/chris/are_identical_sets_of_coloured_pieces/identical-A6.xml')))
True
>>> are_identical_sets_of_coloured_pieces(
...    available_coloured_pieces(open('files/chris/are_identical_sets_of_coloured_pieces/identical-A1.xml')),
...    available_coloured_pieces(open('files/chris/are_identical_sets_of_coloured_pieces/identical-A7.xml')))
True
>>> are_identical_sets_of_coloured_pieces(
...    available_coloured_pieces(open('files/chris/are_identical_sets_of_coloured_pieces/identical-A1.xml')),
...    available_coloured_pieces(open('files/chris/are_identical_sets_of_coloured_pieces/identical-A8.xml')))
True
>>> are_identical_sets_of_coloured_pieces(
...    available_coloured_pieces(open('files/chris/are_identical_sets_of_coloured_pieces/identical-A1.xml')),
...    available_coloured_pieces(open('files/chris/are_identical_sets_of_coloured_pieces/not-identical-A.xml')))
False
>>> are_identical_sets_of_coloured_pieces(
...    available_coloured_pieces(open('files/chris/are_identical_sets_of_coloured_pieces/identical-B1.xml')),
...    available_coloured_pieces(open('files/chris/are_identical_sets_of_coloured_pieces/identical-B2.xml')))
True
>>> are_identical_sets_of_coloured_pieces(
...    available_coloured_pieces(open('files/chris/are_identical_sets_of_coloured_pieces/identical-B1.xml')),
...    available_coloured_pieces(open('files/chris/are_identical_sets_of_coloured_pieces/not-identical-B-different-colours.xml')))
False
>>> are_identical_sets_of_coloured_pieces(
...    available_coloured_pieces(open('files/chris/are_identical_sets_of_coloured_pieces/identical-B1.xml')),
...    available_coloured_pieces(open('files/chris/are_identical_sets_of_coloured_pieces/not-identical-B-different-area.xml')))
False
>>> are_identical_sets_of_coloured_pieces(
...    available_coloured_pieces(open('files/chris/are_identical_sets_of_coloured_pieces/identical-B1.xml')),
...    available_coloured_pieces(open('files/chris/are_identical_sets_of_coloured_pieces/not-identical-B-different-points.xml')))
False

>>> is_solution(
...    available_coloured_pieces(open('files/chris/is_solution/A-solution.xml')),
...    available_coloured_pieces(open('files/chris/is_solution/A-shape.xml')))
True
>>> is_solution(
...    available_coloured_pieces(open('files/chris/is_solution/A-solution-2.xml')),
...    available_coloured_pieces(open('files/chris/is_solution/A-shape.xml')))
True
>>> is_solution(
...    available_coloured_pieces(open('files/chris/is_solution/A-not-solution-outside.xml')),
...    available_coloured_pieces(open('files/chris/is_solution/A-shape.xml')))
False
>>> is_solution(
...    available_coloured_pieces(open('files/chris/is_solution/A-not-solution-outside-2.xml')),
...    available_coloured_pieces(open('files/chris/is_solution/A-shape.xml')))
False
>>> is_solution(
...    available_coloured_pieces(open('files/chris/is_solution/B-solution.xml')),
...    available_coloured_pieces(open('files/chris/is_solution/B-shape.xml')))
True
>>> is_solution(
...    available_coloured_pieces(open('files/chris/is_solution/B-solution-2.xml')),
...    available_coloured_pieces(open('files/chris/is_solution/B-shape.xml')))
True
>>> is_solution(
...    available_coloured_pieces(open('files/chris/is_solution/B-not-solution-invalid-area.xml')),
...    available_coloured_pieces(open('files/chris/is_solution/B-shape.xml')))
False
>>> is_solution(
...    available_coloured_pieces(open('files/chris/is_solution/B-not-solution-invalid-ontop.xml')),
...    available_coloured_pieces(open('files/chris/is_solution/B-shape.xml')))
False
>>> is_solution(
...    available_coloured_pieces(open('files/chris/is_solution/B-not-solution-invalid-outside.xml')),
...    available_coloured_pieces(open('files/chris/is_solution/B-shape.xml')))
False
>>> is_solution(
...    available_coloured_pieces(open('files/chris/is_solution/B-not-solution-invalid-overlap.xml')),
...    available_coloured_pieces(open('files/chris/is_solution/B-shape.xml')))
False
>>> is_solution(
...    available_coloured_pieces(open('files/chris/is_solution/C-solution.xml')),
...    available_coloured_pieces(open('files/chris/is_solution/C-shape.xml')))
True
>>> is_solution(
...    available_coloured_pieces(open('files/chris/is_solution/C-not-solution-invalid-ontop-all.xml')),
...    available_coloured_pieces(open('files/chris/is_solution/C-shape.xml')))
False
>>> is_solution(
...    available_coloured_pieces(open('files/chris/is_solution/C-not-solution-invalid-ontop.xml')),
...    available_coloured_pieces(open('files/chris/is_solution/C-shape.xml')))
False
>>> is_solution(
...    available_coloured_pieces(open('files/chris/is_solution/C-not-solution-invalid-ontop-all-middle.xml')),
...    available_coloured_pieces(open('files/chris/is_solution/C-shape.xml')))
False
>>> is_solution(
...    available_coloured_pieces(open('files/chris/is_solution/D-solution.xml')),
...    available_coloured_pieces(open('files/chris/is_solution/D-shape.xml')))
True
>>> is_solution(
...    available_coloured_pieces(open('files/chris/is_solution/D-not-solution-outside.xml')),
...    available_coloured_pieces(open('files/chris/is_solution/D-shape.xml')))
False
>>> is_solution(
...    available_coloured_pieces(open('files/chris/is_solution/E-solution.xml')),
...    available_coloured_pieces(open('files/chris/is_solution/E-shape.xml')))
True
>>> is_solution(
...    available_coloured_pieces(open('files/chris/is_solution/E-not-solution-outside.xml')),
...    available_coloured_pieces(open('files/chris/is_solution/E-shape.xml')))
False
>>> is_solution(
...    available_coloured_pieces(open('files/chris/is_solution/F-solution.xml')),
...    available_coloured_pieces(open('files/chris/is_solution/F-shape.xml')))
True
>>> is_solution(
...    available_coloured_pieces(open('files/chris/is_solution/F-not-solution-outside-hole.xml')),
...    available_coloured_pieces(open('files/chris/is_solution/F-shape.xml')))
False
>>> is_solution(
...    available_coloured_pieces(open('files/chris/is_solution/G-solution.xml')),
...    available_coloured_pieces(open('files/chris/is_solution/G-shape.xml')))
True
>>> is_solution(
...    available_coloured_pieces(open('files/daisy/tangram_A_1.xml')),
...    available_coloured_pieces(open('files/daisy/shape_A.xml')))
True
>>> is_solution(
...    available_coloured_pieces(open('files/daisy/tangram_A_2.xml')),
...    available_coloured_pieces(open('files/daisy/shape_A.xml')))
False
'''

if __name__ == '__main__':
    import doctest
    doctest.testmod()
