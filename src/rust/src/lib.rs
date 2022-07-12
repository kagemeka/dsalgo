#![feature(once_cell)]
// #![allow(dead_code)]
pub mod a_star_search;
pub mod aa_tree;
pub mod ab_tree;
pub mod abs_diff;
pub mod accumulate;
pub mod adaptive_heap_sort;
pub mod addressable_heap;
pub mod adjacency_list_graph;
pub mod adjacency_list_to_directed_edges;
pub mod adjacency_matrix_graph;
pub mod af_heap;
pub mod aho_corasick;
pub mod algebraic_structure;
pub mod algebraic_structure_impl;
pub mod algebraic_structure_std;
pub mod all_pairs_shortest_path;
pub mod analysis;
pub mod analysis_search;
pub mod apsp_johnson_dense;
pub mod apsp_johnson_sparse;
pub mod arborescence;
pub mod argsort;
pub mod arithmetic_series;
pub mod array_compression_unique_binary_search;
pub mod articulation_point;
pub mod articulation_points_detection_chain_decomposition;
pub mod articulation_points_detection_lowlink;
pub mod automorphism;
pub mod auxiliary_tree;
pub mod avl_tree;
pub mod avl_tree_node;
pub mod avl_tree_tmp;
pub mod b_plus_tree;
pub mod b_star_tree;
pub mod balanced_tree;
pub mod ball_tree;
pub mod barrett_reduction;
pub mod batcher_odd_even_mergesort;
pub mod bead_sort;
pub mod beatty_sequence;
pub mod bellman_ford;
pub mod bellman_ford_dense;
pub mod bellman_ford_tree;
pub mod bidirected_graph;
pub mod bijection;
pub mod binary_function;
pub mod binary_gcd;
pub mod binary_heap;
pub mod binary_heap_std_impl_priority_queue;
pub mod binary_min_heap;
pub mod binary_min_heap_impl_priority_queue;
pub mod binary_relation;
pub mod binary_search;
pub mod binary_search_on_sequence;
pub mod binary_tree;
pub mod binary_tree_node;
pub mod binomial_heap;
pub mod bisection_analysis;
pub mod bit_array;
pub mod bit_length_primitive;
pub mod bit_set;
pub mod bit_vector;
pub mod bitonic_sort;
pub mod bitops;
pub mod check_two_circles_intersection;
pub mod rle; 
pub mod coordinates_compression;
pub mod least_common_multiple_of_prime_factorization;
pub mod digits_sum;
pub mod run_length_encoding;
pub mod number_of_nodes_reachable_into_cycle_bfs_rev_edges;
pub mod number_of_nodes_reachable_into_cycle_dfs_recurse;
pub mod sum_of_xor_prod_of_all_subsets_in_array_modular;
pub mod bk_tree;
pub mod block_cut_tree;
pub mod block_sort;
pub mod borsuk_ulam;
pub mod brent_cycle_detection;
pub mod bridge_detection_chain_decomposition;
pub mod bridge_detection_lowlink;
pub mod bridge_finding;
pub mod bubble_sort;
pub mod bucket_sort;
pub mod sum_of_all_pairs_xor_in_array_modular;
pub mod xor_of_all_pairs_bitwise_and_of_two_arrays;
pub mod string_ith_char;
pub mod string_ith_ascii_code;
pub mod trigonometry_tau_with_pi;
pub mod pi_with_arccosine;
pub mod dist_2d_to_the_power_of_2;
pub mod bucket_sort_make_argument_left_table;
pub mod bucket_sort_make_argument_right_table;
pub mod bx_tree;
pub mod bytes_to_char_vec;
pub mod cache_oblivious_distributing_sort;
pub mod cached_fibonacci_number;
pub mod carmichael_theorem;
pub mod cartesian_product;
pub mod cartesian_tree;
pub mod cascade_merge_sort;
pub mod category;
pub mod category_theory;
pub mod centroid_decomposition;
pub mod chinese_remainder_theorem;
pub mod choose;
pub mod cht;
pub mod chu_liu_edmonds_minimum_spanning_arborescence;
pub mod cipolla_algorithm;
pub mod circle_dividing;
pub mod circle_hough_transform;
pub mod closest_pair_points;
pub mod cmp;
pub mod cocktail_shaker_sort;
pub mod collection;
pub mod collection_macro;
pub mod comb_sort;
pub mod combination;
pub mod combination_choose;
pub mod combinatorics;
pub mod comparison_sort;
pub mod complete_digraph;
pub mod complete_graph;
pub mod composition_category_theory;
pub mod connected_components;
pub mod connected_components_bfs;
pub mod connected_components_dfs;
pub mod connected_components_dfs_recurse;
pub mod connected_components_dsu;
pub mod connected_components_group_by_id;
pub mod container;
pub mod convert_to_bool;
pub mod convex_hull_trick;
pub mod count_common_subsequences;
pub mod count_common_substrings;
pub mod count_distinct_substrings;
pub mod count_divisors_by_factorization;
pub mod count_divisors_naive;
pub mod count_leading_zeros;
pub mod count_leading_zeros_std;
pub mod count_subsequences;
pub mod count_subset_sum;
pub mod count_trailing_zeros_in_digits_factorial;
pub mod count_trailing_zeros_std;
pub mod counting_argsort;
pub mod counting_array_rank;
pub mod counting_sort;
pub mod cover_tree;
pub mod crt;
pub mod cumulative_array;
pub mod cut_vertex;
pub mod dancing_link;
pub mod dancing_tree;
pub mod day_stout_warren;
pub mod decision_tree;
pub mod default;
pub mod deletion;
pub mod desopo_pape;
pub mod dial_sortest_path;
pub mod dijkstra_arborescence;
pub mod dijkstra_dense;
pub mod dijkstra_queue_binary_heap_std;
pub mod dijkstra_sparse;
pub mod dijkstra_sparse_from_potential;
pub mod dijkstra_sparse_general_extended;
pub mod dijkstra_sparse_option;
pub mod dijkstra_sparse_parents;
pub mod dijkstra_sparse_path_count;
pub mod dijkstra_sparse_predecessors;
pub mod dijkstra_sparse_queue;
pub mod dijkstra_tree;
pub mod directed_acyclic_word_graph;
pub mod directed_lowlink;
pub mod discrete_logarithm;
pub mod divisor;
pub mod divisors_count_from_prime_factors;
pub mod divisors_count_table;
pub mod divisors_from_prime_factors;
pub mod divisors_sum_by_fatorization;
pub mod divisors_sum_from_prime_factors;
pub mod divisors_sum_table;
pub mod dlp;
pub mod doubly_chained_tree;
pub mod dynamic_matrix_trait;
pub mod dynamic_tensor;
pub mod dynamic_tensor_shape;
pub mod eppstein_algorithm;
pub mod ett;
pub mod euler_criterion;
pub mod euler_jacobi_pseudo_prime;
pub mod euler_phi_function;
pub mod euler_totient_function;
pub mod euler_totient_prime_factorize;
pub mod euler_tour_teqnique;
pub mod eulerian_circuit;
pub mod eulerian_path;
pub mod eulerian_trail;
pub mod exchange_sort;
pub mod exponential_tree;
pub mod ext_euclid;
pub mod factorial;
pub mod factorial_table;
pub mod failure_function_kmp_table_0_indexed;
pub mod failure_function_kmp_table_1_indexed;
pub mod fast_fourier_transform;
pub mod fast_mobius_transform;
pub mod fast_modulo_transform;
pub mod fast_zeta_transform;
pub mod fenwick_tree;
pub mod fenwick_tree_additive;
pub mod fenwick_tree_multiset;
pub mod fermat_factorization_method;
pub mod fft;
pub mod fibonacci_heap;
pub mod fibonacci_number;
pub mod field;
pub mod find_divisor_pollard_rho_brent;
pub mod find_divisor_pollard_rho_floyd;
pub mod find_divisor_pollard_rho_repeat_brent;
pub mod find_divisors_for_const_remainders;
pub mod find_divisors_for_same_remainders;
pub mod find_divisors_median_low;
pub mod find_divisors_structive;
pub mod find_divisors_trial_division;
pub mod find_first_set;
pub mod find_kth_permutation;
pub mod find_kth_set_bit_by_removing_lsb;
pub mod find_prime_factor_pollard_rho_brent;
pub mod find_root;
pub mod finger_tree;
pub mod flat_nonzero;
pub mod float_absolute_error_check;
pub mod float_relative_error_check;
pub mod flow;
pub mod floyd_warshall;
pub mod floyd_warshall_apsp;
pub mod fold;
pub mod ford_johnson_algorithm;
pub mod formal_power_series;
pub mod fourier_transform;
pub mod fractal_tree_index;
pub mod frobenius_endmorphism;
pub mod gamma_function;
pub mod garner_algorithm;
pub mod garner_composite_modular;
pub mod gcd;
pub mod gcds_for_lcm;
pub mod gcds_for_sum;
pub mod general_dijkstra_sparse;
pub mod genetic_algorithm;
pub mod geometric_series;
pub mod geometry;
pub mod ghost_leg;
pub mod gnome_sort;
pub mod gradient_boostring;
pub mod graph;
pub mod graph_disconnected;
pub mod graph_edge_trait;
pub mod graph_impl;
pub mod graph_old;
pub mod graph_pointer_directed;
pub mod graph_pointer_mixed;
pub mod graph_pointer_undirected;
pub mod graph_trait_pointer_mixed;
pub mod graphops;
pub mod greatest_prime_factor_table;
pub mod group_theory_id;
pub mod hamming_distance;
pub mod hash_tree;
pub mod heapsort;
pub mod heavly_light_decomposition;
pub mod height;
pub mod hilbert_r_tree;
pub mod histogram_sort;
pub mod hld;
pub mod homogeneous_product;
pub mod homomorphism;
pub mod hopcroft_karp;
pub mod identifier;
pub mod implicit_k_d_tree;
pub mod index;
pub mod insertion;
pub mod insertion_sort;
pub mod int_cube_root;
pub mod int_kth_root_binary_search;
pub mod int_kth_root_fast;
pub mod int_kth_root_linear;
pub mod int_kth_root_newton_method;
pub mod interpolation_sort;
pub mod inverse_factorial_table;
pub mod io;
pub mod iops;
pub mod is_absorbing;
pub mod is_adjacency_matrix;
pub mod is_arborescence;
pub mod is_eulerian_graph;
pub mod is_identity;
pub mod is_invertible;
pub mod is_multitree;
pub mod is_pairwise_coprime;
pub mod is_perfect_number;
pub mod is_polytree;
pub mod is_prime_naive;
pub mod is_prime_table;
pub mod is_prime_with_small_prime_numbers;
pub mod is_quadratic_residue;
pub mod is_quadratic_residue_z_pz_euler_criterion;
pub mod is_regular_graph;
pub mod is_setwise_coprime;
pub mod is_subsequence;
pub mod is_twin_prime;
pub mod is_undirected_dense_graph;
pub mod isomorphism;
pub mod jacobi_symbol;
pub mod jacobi_symbol_recurse;
pub mod join;
pub mod k_d_tree;
pub mod karatsuba_algorithm;
pub mod karatsuba_mul_quotient_pow_2_power_of_2_128;
pub mod kmp;
pub mod kmp_findall;
pub mod knapsack;
pub mod knuth_morris_pratt;
pub mod kosaraju_scc;
pub mod las_vegas_algorithm;
pub mod lazy_sqrt_decomposition;
pub mod lca;
pub mod lcm;
pub mod lcs;
pub mod least_prime_factor_table;
pub mod leftist_tree;
pub mod legendre_function;
pub mod legendre_symbol;
pub mod legendre_symbol_euler_criterion;
pub mod levenstein_distance;
pub mod library_sort;
pub mod lightgbm;
pub mod linear_programming;
pub mod linear_time_minimum_spanning_tree;
pub mod link_cut_tree;
pub mod log_structured_merge_tree;
pub mod longest_border_morris_pratt_table_0_indexed;
pub mod longest_border_morris_pratt_table_1_indexed;
pub mod longest_common_prefix_array;
pub mod longest_common_prefix_array_kasai;
pub mod longest_common_substring;
pub mod longest_increasing_sequence;
pub mod longest_non_decreasing_sequence;
pub mod longest_palindromic_substring;
pub mod lower_bound_on_sequence;
pub mod lowlink;
pub mod lsm_tree;
pub mod lucas_number;
pub mod lucas_sequence;
pub mod m_ary_tree;
pub mod maclaurin_series;
pub mod make_sparse_histogram;
pub mod manacher;
pub mod matrix;
pub mod matrix_2d_vec;
pub mod matrix_constant;
pub mod matrix_dynamic;
pub mod matrix_runtime_static;
pub mod matrix_static;
pub mod maximum_cardinality_matching;
pub mod merge_insertion_sort;
pub mod merge_sort;
pub mod merge_sort_inplace;
pub mod mergeable_heap;
pub mod mergesort;
pub mod merkle_tree;
pub mod metric_tree;
pub mod min_max_pq;
pub mod minimum_cost_arborescence;
pub mod minimum_cost_elastic_matching;
pub mod minimum_pair_sum_for_const_product;
pub mod minimum_spanning_tree;
pub mod mo_algorithm;
pub mod mo_algorithm_3d;
pub mod mobius_function;
pub mod mobius_transformation;
pub mod modular;
pub mod modular_inverse_of_2_of_odd;
pub mod modular_tetration;
pub mod monte_carlo_algorithm;
pub mod montgomery_modular_multiplication;
pub mod montgomery_modular_multiplication_64;
pub mod morphism;
pub mod mst_boruvka;
pub mod mst_kruskal;
pub mod mst_prim_dense;
pub mod mst_prim_sparse;
pub mod mst_reverse_delete;
pub mod multi_key_quicksort;
pub mod multiplicative_inverse;
pub mod multiset;
pub mod n_choose_table;
pub mod n_dim_dynamic_tensor;
pub mod n_group_category;
pub mod n_group_finite_group;
pub mod negative_cycle;
pub mod network_graph_node;
pub(crate) mod new_rc_refcell;
pub mod next_prime_number;
pub mod next_prime_number_table;
pub mod normalize_sort_csgraph;
pub mod ntt;
pub mod number_of_common_subsequences;
pub mod number_of_common_substrings;
pub mod number_of_distinct_subsequences;
pub mod number_of_distinct_substrings;
pub mod number_of_subsequences;
pub mod number_theoritic_transform;
pub mod numeric_array_normalize_min_as_0;
pub mod numeric_array_normalize_min_as_offset;
pub mod odd_even_sort;
pub mod ops;
pub mod order_static_tree;
pub mod ordered_set;
pub mod oscillating_merge_sort;
pub mod p_group;
pub mod pairing_heap;
pub mod pancacke_sorting;
pub mod parity_check_matrix;
pub mod partial_order;
pub mod pascal_rule;
pub mod pascal_simplex;
pub mod pascal_triangle;
pub mod path_based_scc;
pub mod patricia_tree;
pub mod perfect_numbers;
pub mod ph_tree;
pub mod pigeonhole_sort;
pub mod pivot_tree;
pub mod pocket_euler_totient;
pub mod pocket_modint;
pub mod pocket_tree_bfs;
pub mod pocket_tree_bfs_depth;
pub mod pocket_tree_bfs_parent;
pub mod pointer_grpah;
pub mod pollard_kangaroo_algorithm;
pub mod pollard_p_1;
pub mod pollard_rho;
pub mod polyphase_merge_sort;
pub mod pop;
pub mod postman_sort;
pub mod power;
pub mod power_dynamic;
pub mod power_group;
pub mod power_group_itself;
pub mod power_group_trait;
pub mod power_monoid;
pub mod power_monoid_itself;
pub mod power_monoid_trait;
pub mod power_semigroup;
pub mod power_semigroup_itself;
pub mod power_semigroup_recurse;
pub mod power_semigroup_trait;
pub mod pq_binary_heap_std_impl;
pub mod pq_tree;
pub mod pr_tree;
pub mod prefix_tree;
pub mod preorder;
pub mod previous_prime_number;
pub mod previous_prime_number_table;
pub mod primality;
pub mod prime;
pub mod prime_counting_fast;
pub mod prime_counting_fast_half;
pub mod prime_counting_fast_optimized;
pub mod prime_counting_function;
pub mod prime_counting_meissel_lehmer;
pub mod prime_factorize_factorial_legendre_function;
pub mod prime_factorize_factorial_with_lpf;
pub mod prime_factorize_fermat;
pub mod prime_factorize_pollard_rho;
pub mod prime_factorize_pollard_rho_flat;
pub mod prime_factorize_pollard_rho_flat_2;
pub mod prime_factorize_trial_division;
pub mod prime_factorize_with_lpf;
pub mod prime_number;
pub mod prime_pi_approx_ln;
pub mod prime_pi_power_of_10;
pub mod prime_pi_table;
pub mod priority_queue;
pub mod priority_queue_trait;
pub mod priority_r_tree;
pub mod proportion_extend_sort;
pub mod proth_number;
pub mod proxmap_sort;
pub mod prufer_group;
pub mod pseudorandom_number_generator;
pub mod psieve;
pub mod quasigroup;
pub mod query;
pub mod quick_sort;
pub mod r_plus_tree;
pub mod r_star_tree;
pub mod rabin_karp;
pub mod radix_heap;
pub mod radix_sort;
pub mod radix_tree;
pub mod random_forest;
pub mod range_tree;
pub mod rank_of_permutation_for_small_n;
pub mod reachability_based_scc;
pub mod rectangle_tree;
pub mod red_black_tree;
pub mod reduce;
pub mod reflexive_relation;
pub mod rerooting;
pub mod rng;
pub mod rng_linear_congruential;
pub mod rng_mersenne_twister;
pub mod rng_static_xorshift64;
pub mod rng_xorshift;
pub mod rng_xorshift1024star;
pub mod rng_xorshift128;
pub mod rng_xorshift128plus;
pub mod rng_xorshift32;
pub mod rng_xorshift64;
pub mod rng_xorshift64star;
pub mod rng_xorshift96;
pub mod rng_xorwow;
pub mod rng_xoshiro256_core;
pub mod rng_xoshiro256plus;
pub mod rng_xoshiro256starstar;
pub mod safe_int_power;
pub mod scapegoat_tree;
pub mod scc_topological_sort;
pub mod scc_transpose;
pub mod segtree;
pub mod segtree_2d;
pub mod segtree_2d_dense;
pub mod segtree_beats;
pub mod segtree_dual;
pub mod segtree_dyn;
pub mod segtree_lazy;
pub mod selection_sort;
pub mod set_theory;
pub mod shaker_sort;
pub mod shakutori_method;
pub mod shear_sort;
pub mod shellsort;
pub mod shortest_path;
pub mod shortest_path_arborescence;
pub mod shortest_path_potential;
pub mod shortest_path_predecessors;
pub mod shortest_path_tree;
pub mod shuffle_sort;
pub mod simulated_annealing;
pub mod single_source_shortest_path;
pub mod size;
pub mod skew_heap;
pub mod sliding_window_aggregation;
pub mod slope_trick;
pub mod slowsort;
pub mod smallest_enclosing_circle;
pub mod smawk_algorithm;
pub mod smoothsort;
pub mod sort;
pub mod sorting_network;
pub mod sorting_number;
pub mod spaghetti_sort;
pub mod sparse_table;
pub mod spfa;
pub mod splay_tree;
pub mod splay_tree_node;
pub mod split;
pub mod spqr_tree;
pub mod spreadsort;
pub mod sqrt_decomposition;
pub mod sqrt_tree;
pub mod square_matrix_trait;
pub mod sssp_dijkstra_sparse_with_general;
pub mod sssp_faster_algorithm;
pub mod stable_sort;
pub mod static_matrix;
pub mod static_matrix_impl_mul;
pub mod static_matrix_properties_example;
pub mod static_matrix_trait;
pub mod static_tensor_shape;
pub mod steiner_tree;
pub mod stooge_sort;
pub mod strconv;
pub mod strongly_connected_components;
pub mod subset_sum;
pub mod subset_sum_at_most_k;
pub mod subset_sum_min_count;
pub mod subset_sum_multiple_same_values;
pub mod subset_sum_problem;
pub mod suffix_array;
pub mod suffix_array_doubling_argsort;
pub mod suffix_array_doubling_argsort_const_faster;
pub mod suffix_array_doubling_counting_argsort;
pub mod suffix_array_induced_sort;
pub mod suffix_array_induced_sort_recurse;
pub mod suffix_automaton;
pub mod suffix_tree;
pub mod sum_arithmetic_progression;
pub mod sum_of_divisors_count;
pub mod sum_of_divisors_count_times_i;
pub mod sum_of_divisors_sum;
pub mod sum_of_multiples;
pub mod sum_of_multiples_count_range;
pub mod sum_of_multiples_count_times_i_range;
pub mod sum_of_multiples_sum;
pub mod sum_of_multiples_sum_range;
pub mod swag;
pub mod t_tree;
pub mod tango_tree;
pub mod tarjan_lowlink_scc;
pub mod taylor_series;
pub mod tensor;
pub mod tensor_property;
pub mod tensor_trait;
pub mod ternary_heap;
pub mod ternary_search;
pub mod ternary_search_tree;
pub(crate) mod test_fast_prime_counting;
pub(crate) mod test_int_kth_root;
pub mod top_tree;
pub mod topological_sort;
pub mod topology;
pub mod torus;
pub mod total_order;
pub mod tournament_sort;
pub mod transitive_relation;
pub mod traveling_salesperson;
pub mod traveling_salesperson_giving;
pub mod traveling_salesperson_taking;
pub mod traveling_salesperson_taking_mem_access_optim;
pub mod tree_diameter;
pub mod tree_edges_to_graph;
pub mod tree_node;
pub mod tree_path_query;
pub mod tree_path_query_binary_lifting;
pub mod tree_path_query_hld;
pub mod tree_sort;
pub mod treeops;
pub mod tribonacci_number;
pub mod two_three_four_tree;
pub mod two_three_heap;
pub mod two_three_tree;
pub mod ub_tree;
pub mod undirected_lowlink;
pub mod undirected_tuple_edges_to_adjacency_list;
pub mod undirected_tuple_edges_with_data_to_adjacency_list;
pub mod union_find;
pub mod union_find_persistent;
pub mod union_find_potentialized;
pub mod union_find_rollback;
pub mod union_find_trait;
pub mod upper_bound_on_sequence;
pub mod usize_u64_impl_graph_edge_trait;
pub mod van_emde_boas_tree;
pub mod vector;
pub mod vector_rotation_2d_by_rad_with_matrix;
pub mod vector_rotation_3d_by_rad_with_matrix;
pub mod vector_space;
pub mod vector_unique;
pub mod verbal_arithmetic;
pub mod vertex_cut;
pub mod vertex_seperator;
pub mod virtual_tree;
pub mod vp_tree;
pub mod wavelet_matrix;
pub mod weighted_union_algorithm;
pub mod x_tree;
pub mod z_algorithm;
pub mod z_algorithm_findall_substr;
pub mod zero_element;
pub mod zero_one_bfs;
// pub mod rerooting_dynamic;
