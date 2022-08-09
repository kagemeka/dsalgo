#![feature(once_cell)]
#![feature(int_log)]
#![feature(generic_const_exprs)]
#![feature(inherent_associated_types)]
#![feature(array_chunks)]
#![feature(iterator_try_collect)]
// #![allow(dead_code)]
pub mod a_star_search_algorithm;
pub mod aa_tree;
pub mod ab_tree;
pub mod abs_diff;
pub mod accumulate_iterator;
pub mod adaptive_heap_sort;
pub mod add_with_xor_and_bitwise_and;
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
pub mod argmax;
pub mod argsort;
pub mod arithmetic_series;
pub mod array_compression_unique_binary_search;
pub mod array_rank_with_argsort;
pub mod articulation_point;
pub mod articulation_points_detection_chain_decomposition;
pub mod articulation_points_detection_lowlink;
pub mod automorphism;
pub mod auxiliary_tree;
pub mod avl_tree;
pub mod avl_tree_ngtkn;
pub mod avl_tree_node_with_key_value_size_box_recurse;
pub mod b_plus_tree;
pub mod b_star_tree;
pub mod balanced_tree;
pub mod ball_tree;
pub mod barrett_reduction;
pub mod base_conversion_base_k_to_decimal;
pub mod base_conversion_decimal_to_base_k_with_divmod;
pub mod base_conversion_decimal_to_base_k_with_euclid_divrem;
pub mod batcher_odd_even_mergesort;
pub mod bead_sort;
pub mod beatty_sequence;
pub mod bellman_ford;
pub mod bellman_ford_dense;
pub mod bellman_ford_tree;
pub mod bidirected_graph;
pub mod bijection;
pub mod bin_count;
pub mod binary_function;
pub mod binary_greatest_common_divisor_u64;
pub mod binary_heap;
pub mod binary_heap_std_impl_priority_queue;
pub mod binary_min_heap_0_indexed;
pub mod binary_min_heap_impl_priority_queue;
pub mod binary_relation;
pub mod binary_search_i64;
pub mod binary_search_on_slice_bisection_of_2_ok;
pub mod binary_search_on_slice_bisection_of_ng_ok;
pub mod binary_tree;
pub mod binary_tree_node;
pub mod binomial_heap;
pub mod bisection_analysis;
pub mod bit_array;
pub mod bit_length_binary_search_u64;
pub mod bit_length_naive_u64;
pub mod bit_length_primitive;
pub mod bit_length_table;
pub mod bit_length_with_count_leading_zeros_u128;
pub mod bit_length_with_count_leading_zeros_u64;
pub mod bit_set;
pub mod bit_vector;
pub mod bitonic_sort;
pub mod bitops;
pub mod bk_tree;
pub mod block_cut_tree;
pub mod block_sort;
pub mod bool_to_int;
pub mod borsuk_ulam;
pub mod brent_cycle_detection;
pub mod bridge_finding;
pub mod bubble_sort;
pub mod bucket_sort;
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
pub mod catalan_numbers_constant;
pub mod catalan_numbers_table_modular_usize_with_dp;
pub mod category;
pub mod category_theory;
pub mod ceil_division_i64;
pub mod centroid_decomposition;
pub mod check_two_circles_intersection;
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
pub mod combination_choose;
pub mod combination_from_u64;
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
pub mod const_generics_modular_int_i64;
pub mod const_generics_shaped_matrix;
pub mod const_generics_shaped_matrix_impl_semiring_with_std_ops;
pub mod const_generics_shaped_matrix_with_flattened_data;
pub mod const_generics_sized_square_matrix;
pub mod const_modulus_trait;
pub mod const_square_matrix_property_trait;
pub mod container;
pub mod convert_to_bool;
pub mod convex_hull_trick;
pub mod coordinates_compression;
pub mod count_common_subsequences;
pub mod count_common_substrings;
pub mod count_distinct_substrings;
pub mod count_divisors_by_factorization;
pub mod count_divisors_naive;
pub mod count_leading_zeros;
pub mod count_leading_zeros_std;
pub mod count_subsequences;
pub mod count_subset_sum;
pub mod count_trailing_zeros_in_digits_double_factorial;
pub mod count_trailing_zeros_in_digits_factorial_legendre;
pub mod count_trailing_zeros_std;
pub mod counting_argsort;
pub mod counting_array_rank;
pub mod counting_sort;
pub mod cover_tree;
pub mod crt;
pub mod cumulative_array;
pub mod cut_vertex;
pub mod cycle_detection_undirected_graph_union_find;
pub mod dancing_link;
pub mod dancing_tree;
pub mod day_stout_warren;
pub mod decision_tree;
pub mod default;
pub mod default_static_modular_arithmetic;
pub mod define_const_modulus_macro;
pub mod define_const_modulus_with_const_generics_macro;
pub mod define_static_modulus_macro_with_atomic_cell;
pub mod deletion;
pub mod dial_sortest_path;
pub mod digits_sum;
pub mod dijkstra_arborescence;
pub mod dijkstra_dense_i64_with_inf;
pub mod dijkstra_dense_option_u64;
pub mod dijkstra_queue_binary_heap_std;
pub mod dijkstra_sparse;
pub mod dijkstra_sparse_from_potential;
pub mod dijkstra_sparse_general_extended;
pub mod dijkstra_sparse_option;
pub mod dijkstra_sparse_parents;
pub mod dijkstra_sparse_path_count;
pub mod dijkstra_sparse_predecessors;
pub mod dijkstra_sparse_queue;
pub mod dijkstra_sparse_tuple_edges_adjacency_list_i64_with_const_inf;
pub mod dijkstra_sparse_tuple_edges_adjacency_list_i64_with_initial_dist;
pub mod dijkstra_sparse_tuple_edges_adjacency_list_u64_with_inf;
pub mod dijkstra_tree;
pub mod directed_acyclic_word_graph;
pub mod directed_lowlink;
pub mod discrete_logarithm;
pub mod dist_2d_to_the_power_of_2;
pub mod divisor;
pub mod divisors_count_from_prime_factors;
pub mod divisors_count_table;
pub mod divisors_from_prime_factors;
pub mod divisors_sum_by_fatorization;
pub mod divisors_sum_from_prime_factors;
pub mod divisors_sum_table;
pub mod divmod;
pub mod dlp;
pub mod doubly_chained_tree;
pub mod dual_unbounded_subset_sum_min_count_item_oriented_with_inf;
pub mod dual_unbounded_subset_sum_min_count_sum_oriented_with_inf;
pub mod dynamic_matrix_property_trait;
pub mod dynamic_modular_arithmetic_trait;
pub mod dynamic_modulus;
pub mod dynamic_modulus_trait;
pub mod dynamic_shaped_matrix_with_flattened_data;
pub mod dynamic_tensor;
pub mod dynamic_tensor_shape;
pub mod enumerate_divisors;
pub mod enumerate_highly_composite_numbers_bigint_priority_search;
pub mod enumerate_highly_composite_numbers_prime_factor_dp;
pub mod enumerate_highly_composite_numbers_priority_search;
pub mod enumerate_prime_factor_candidates_for_highly_composite_numbers;
pub mod enumerate_stepping_numbers_between_with_bfs;
pub mod enumerate_stepping_numbers_less_than_with_bfs;
pub mod eppstein_algorithm;
pub mod ett;
pub mod euclidean_division_i64;
pub mod euler_criterion;
pub mod euler_jacobi_pseudo_prime;
pub mod euler_phi_function;
pub mod euler_totient_function;
pub mod euler_totient_with_prime_factorize;
pub mod euler_totient_with_trial_division_u64;
pub mod euler_tour_edges;
pub mod euler_tour_edges_recurse;
pub mod euler_tour_nodes_direct;
pub mod euler_tour_nodes_direct_recurse;
pub mod euler_tour_nodes_from_edges;
pub mod euler_tour_teqnique_as_struct;
pub mod eulerian_circuit;
pub mod eulerian_path;
pub mod eulerian_trail;
pub mod exchange_sort;
pub mod exponential_tree;
pub mod extended_euclidean_gcd_generic_int_recurse;
pub mod extended_euclidean_gcd_i64;
pub mod extended_euclidean_gcd_i64_recurse;
pub mod extended_euclidean_modular_gcd_inverse_i64_with_extgcd;
pub mod extended_euclidean_modular_gcd_inverse_u64_direct;
pub mod factorial;
pub mod factorial_table_from_u64;
pub mod failure_function_kmp_table_0_indexed;
pub mod failure_function_kmp_table_1_indexed;
pub mod fast_fourier_transform;
pub mod fast_mobius_transform;
pub mod fast_modulo_transform;
pub mod fast_zeta_transform;
pub mod fenwick_tree;
pub mod fenwick_tree_additive_from_i32;
pub mod fenwick_tree_dual_i64_add_1_indexed;
pub mod fenwick_tree_dynamic_cumulative_sum_2_i64;
pub mod fenwick_tree_dynamic_cumulative_sum_3_i64;
pub mod fenwick_tree_i32_add_0_indexed;
pub mod fenwick_tree_i32_add_1_indexed;
pub mod fenwick_tree_multiset;
pub mod fenwick_tree_range_add_range_sum_i64;
pub mod fenwick_tree_with_static_commutative_monoid;
pub mod fenwick_tree_xor;
pub mod fermat_factorization_method;
pub mod fft;
pub mod fibonacci_heap;
pub mod fibonacci_number;
pub mod fibonacci_sequence_modular;
pub mod field;
pub mod find_divisor_pollard_rho_brent;
pub mod find_divisor_pollard_rho_floyd;
pub mod find_divisor_pollard_rho_repeat_brent;
pub mod find_divisors_for_const_remainders;
pub mod find_divisors_for_same_remainders;
pub mod find_divisors_median_low;
pub mod find_divisors_structive;
pub mod find_divisors_trial_division_u64;
pub mod find_first_set;
pub mod find_kth_permutation;
pub mod find_kth_set_bit_by_removing_lsb;
pub mod find_prime_factor_pollard_rho_brent;
pub mod find_root;
pub mod finger_tree;
pub mod flat_nonzero_int;
pub mod flat_nonzero_with_to_bool;
pub mod float_absolute_error_check;
pub mod float_relative_error_check;
pub mod floor_division_i64;
pub mod flow;
pub mod floyd_warshall_apsp_option_i64;
pub mod floyd_warshall_i64_with_inf;
pub mod floyd_warshall_u64;
pub mod floyd_warshall_with_ternary_map;
pub mod fold;
pub mod ford_johnson_algorithm;
pub mod formal_power_series;
pub mod fourier_transform;
pub mod fractal_tree_index;
pub mod frobenius_endmorphism;
pub mod gamma_function;
pub mod garner_algorithm;
pub mod garner_composite_modular;
pub mod gaussian_elimination_xor;
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
pub mod graph_bfs_reachablity_from_any_of_multiple_nodes;
pub mod graph_disconnected;
pub mod graph_edge_trait;
pub mod graph_impl;
pub mod graph_old;
pub mod graph_pointer_directed;
pub mod graph_pointer_mixed;
pub mod graph_pointer_undirected;
pub mod graph_trait_pointer_mixed;
pub mod graphops;
pub mod greatest_common_divisor;
pub mod greatest_common_divisor_euclidean_recurse_i64;
pub mod greatest_common_divisor_euclidean_u64;
pub mod greatest_prime_factor_from_least_prime_factor;
pub mod greatest_prime_factor_table_with_sieve_of_eratosthenes;
pub mod group_theory_id;
pub mod hamming_distance;
pub mod hash_tree;
pub mod hcn;
pub mod heapsort;
pub mod heavly_light_decomposition;
pub mod height;
pub mod highly_composite_numbers;
pub mod hilbert_r_tree;
pub mod histogram_sort;
pub mod hld;
pub mod homogeneous_product;
pub mod homomorphism;
pub mod hopcroft_karp;
pub mod ida_star;
pub mod identifier;
pub mod impl_add_assign_from_add;
pub mod impl_static_modulus_get_for_const_modulus;
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
pub mod intersection_length_of_2_intervals;
pub mod intersection_of_2_intervals;
pub mod inverse_factorial_table_from_u64;
pub mod inversion_number_with_array_compression_and_fenwick_tree;
pub mod io;
pub mod is_absorbing;
pub mod is_adjacency_matrix;
pub mod is_arborescence;
pub mod is_eulerian_graph;
pub mod is_identity;
pub mod is_invertible;
pub mod is_multiple_of_9;
pub mod median_priority_queue_with_2_binary_heap;
pub mod min_max_priority_queue_with_binary_heap;
pub mod modular_cumprod_i64;
pub mod modular_factorial_table_i64;
pub mod modular_int_with_arithmetic;
pub mod modular_inverse_euclidean_i64_no_error;
pub mod modular_inverse_euclidean_u64;
pub mod modular_inverse_euler_theorem_u64;
pub mod modular_inverse_factorial_table_i64;
pub mod modular_inverse_fermat_little_theorem_i32;
pub mod modular_mul_u128_with_add_doubling;
pub mod modular_power_i32;
pub mod modular_power_u32;
pub mod modular_power_u64;
pub mod next_subset_bits;
pub mod number_of_distinct_subsequences_with_min_step_modular_i64;
pub mod static_modular_arithmetic_trait;
pub mod static_modulus_trait;
// pub mod is_multitree;
pub mod add_middle_nodes_and_make_double_tree_undirected_tuple_edges;
pub mod avl_array;
pub mod avl_tree_array;
pub mod avl_tree_node_with_box_recurse_merge_split_based;
pub mod avl_tree_node_with_rc_refcell_merge_split_based_recurse;
pub mod avl_tree_node_with_value_size_box_recurse;
pub mod avl_tree_ordered_multiset;
pub mod avl_tree_ordered_multiset_merge_split_based;
pub mod avl_tree_ordered_multiset_merge_split_based_rc_refcell;
pub mod bdd;
pub mod bfs_01_priority_queue;
pub mod bfs_on_sparse_graph_in_degree_oriented;
pub mod bfs_on_sparse_graph_in_degree_oriented_with_data;
pub mod binary_decision_diagram;
pub mod binary_search_f64_with_max_epoch;
pub mod binary_search_f64_with_terminate_func;
pub mod binary_search_numeric;
pub mod binary_space_partitioning;
pub mod bit_length_with_count_leading_zeros_usize;
pub mod bit_reverse_divide_and_conquer_butterfly_usize;
pub mod bit_reverse_with_std_usize;
pub mod bits_mask_less_than;
pub mod bits_mask_range;
pub mod bsp;
pub mod catalan_number_with_formula_modular_with_factorial_tables_usize;
pub mod catalan_number_with_formula_modular_with_instant_choose_fn_usize;
pub mod circular_buffer_deque;
pub mod circular_buffer_queue;
pub mod complete_permutations;
pub mod connected_components_labels_to_groups;
pub mod const_generics_n_dim_dynamic_shaped_tensor;
pub mod const_matrix_property_trait;
pub mod const_montmort_numbers_usize;
pub mod cumulative_product_vec_with_std_mul;
pub mod dearangement;
pub mod deque_with_2_stacks;
pub mod dijkstra_shortest_path_count_modular_i64_with_inf_sparse;
pub mod double_ended_queue;
pub mod double_factorial_table_from_i32;
pub mod doubly_linked_list_deque;
pub mod doubly_linked_list_node;
pub mod dynamic_array_queue;
pub mod dynamic_shaped_matrix;
pub mod dynamic_sliding_window_maximum_queue_i64;
pub mod dynamic_sliding_window_sum_deque_i64;
pub mod enumerate_combinations_bits_with_next_combination;
pub mod enumerate_combinations_dfs;
pub mod enumerate_combinations_dfs_recurse;
pub mod enumerate_combinations_inplace_iterative;
pub mod enumerate_homogeneous_products_dfs_recurse;
pub mod enumerate_homogeneous_products_inplace_iterative;
pub mod enumerate_montmort_numbers_from_i32;
pub mod enumerate_nodes_in_rectangle_static_offline_with_event_sort;
pub mod enumerate_nodes_in_rectangle_static_with_1d_bisect;
pub mod enumerate_nodes_in_rectangle_static_with_array_compression_bisect;
pub mod enumerate_nodes_in_rectangle_static_with_kd_tree;
pub mod enumerate_repeated_products_dfs_recurse;
pub mod enumerate_repeated_products_inplace_iterative;
pub mod euler_totient_function_table_usize;
pub mod euler_totient_with_trial_division_usize;
pub mod factorial_table_from_i32;
pub mod factorial_tables_frequent_ops_from_i32;
pub mod factorial_tables_frequent_ops_modular_usize;
pub mod fairfield_ad_day_formula;
pub mod fenwick_tree_usize_add_1_indexed;
pub mod find_divisors_trial_division_usize;
pub mod flatten_2d_tournament_list_to_1d;
pub mod functional_graph;
pub mod functional_graph_doubling_table;
pub mod functional_graph_kth_from;
pub mod functional_graph_kth_from_any_with_doubling;
pub mod generalized_greatest_common_divisor_trait;
pub mod greatest_common_divisor_euclid;
pub mod greatest_common_divisor_euclidean;
pub mod greatest_common_divisor_euclidean_recurse;
pub mod greatest_common_divisor_euclidean_reduce;
pub mod greatest_common_divisor_euclidean_signed;
pub mod inverse_factorial_table_from_i32;
pub mod is_pairwise_coprime_with_prime_factorize;
pub mod is_pairwise_coprime_with_sum_of_multiple_count;
pub mod is_perfect_number;
pub mod is_polytree;
pub mod is_prime_naive;
pub mod is_prime_table_from_enumerate_primes;
pub mod is_prime_with_small_prime_numbers;
pub mod is_quadratic_residue;
pub mod is_quadratic_residue_z_pz_euler_criterion;
pub mod is_regular_graph;
pub mod is_setwise_coprime;
pub mod is_subsequence;
pub mod is_twin_prime;
pub mod is_undirected_dense_graph;
pub mod isomorphism;
pub mod iterative_deepening_a_star_algorithm;
pub mod jacobi_symbol;
pub mod jacobi_symbol_recurse;
pub mod join;
pub mod k_d_tree;
pub mod karatsuba_algorithm;
pub mod karatsuba_mul_quotient_pow_2_power_of_2_128;
pub mod kmp;
pub mod kmp_findall_substr;
pub mod knapsack;
pub mod knapsack_01_dual_table_with_inf;
pub mod knapsack_01_for_large_weights_with_dual;
pub mod knapsack_01_table;
pub mod knapsack_unbounded_table_bottom_up_max_value_oriented;
pub mod knapsack_unbounded_table_item_oriented;
pub mod knuth_morris_pratt;
pub mod kosaraju_scc;
pub mod las_vegas_algorithm;
pub mod lazy_binary_heap_accepting_negative_count;
pub mod lazy_sqrt_decomposition;
pub mod lca;
pub mod lcm;
pub mod least_common_multiple;
pub mod least_common_multiple_of_prime_factorization;
pub mod least_common_multiple_with_gcd_i64;
pub mod least_common_multiple_with_gcd_reduce_u64;
pub mod least_common_multiple_with_gcd_u64;
pub mod least_prime_factor_table_from_sieve_of_eratosthenes;
pub mod least_significant_bit_from_lsb_number;
pub mod least_significant_bit_number_direct_i64;
pub mod least_significant_bit_number_from_lsb_usize;
pub mod least_significant_bit_with_std_ctz_u64;
pub mod leftist_tree;
pub mod legendre_formula;
pub mod legendre_symbol;
pub mod legendre_symbol_euler_criterion;
pub mod levenstein_distance;
pub mod levenstein_distance_low_memory;
pub mod levenstein_distance_low_memory_inplace;
pub mod library_sort;
pub mod lightgbm;
pub mod linear_programming;
pub mod linear_time_minimum_spanning_tree;
pub mod link_cut_tree;
pub mod log_2_floor_u64;
pub mod log_structured_merge_tree;
pub mod logarithm_f64_for_any_base_with_log_e;
pub mod logarithm_u64_floor_for_any_base_recursive;
pub mod longest_border_morris_pratt_table_0_indexed;
pub mod longest_border_morris_pratt_table_1_indexed;
pub mod longest_common_prefix_array;
pub mod longest_common_prefix_array_kasai;
pub mod longest_common_subsequence;
pub mod longest_common_substring;
pub mod longest_increasing_sequence;
pub mod longest_non_decreasing_sequence;
pub mod longest_palindromic_substring;
pub mod lower_bound_on_slice;
pub mod lowlink;
pub mod lsm_tree;
pub mod lucas_number;
pub mod lucas_numbers_table;
pub mod lucas_sequence;
pub mod m_ary_tree;
pub mod maclaurin_series;
pub mod make_sparse_histogram;
pub mod manacher;
pub mod matrix;
pub mod matrix_as_2d_vec;
pub mod matrix_with_static_property;
pub mod matrix_with_static_square_property_impl_semiring_with_std;
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
pub mod modular_combination_choose_with_factorial_tables_usize;
pub mod modular_cumprod_usize;
pub mod modular_division_i64;
pub mod modular_factorial_table;
pub mod modular_factorial_table_usize;
pub mod modular_frequent;
pub mod modular_int_with_static_modulus;
pub mod modular_int_with_static_modulus_i64;
pub mod modular_inverse_factorial_table;
pub mod modular_inverse_factorial_table_for_prime_usize;
pub mod modular_inverse_of_2_for_odd_modulus;
pub mod modular_inverse_power_of_2_table_for_odd_modulus_i64;
pub mod modular_inverse_table_usize;
pub mod modular_power_for_prime_usize_recurse;
pub mod modular_power_of_k_table;
pub mod modular_power_usize_recurse;
pub mod modular_tetration;
pub mod monte_carlo_algorithm;
pub mod montgomery_modular_multiplication;
pub mod montgomery_modular_multiplication_64;
pub mod montgomery_static_modular_int_with_id_u64;
pub mod montmort_number;
pub mod morphism;
pub mod most_significant_bit_number_with_binary_search;
pub mod most_significant_bit_number_with_msb;
pub mod most_significant_bit_with_bit_length_u64;
pub mod mst_boruvka;
pub mod mst_kruskal;
pub mod mst_prim_dense;
pub mod mst_prim_sparse;
pub mod mst_reverse_delete;
pub mod multi_key_quicksort;
pub mod multiplicative_inverse;
pub mod multiset;
pub mod n_choose_table;
pub mod n_group_category;
pub mod n_group_finite_group;
pub mod negative_cycle;
pub mod network_graph_node;
pub(crate) mod new_rc_refcell;
pub mod newton_raphson_division;
pub mod next_combination_bits;
pub mod next_power_of_2_table_const_usize;
pub mod next_power_of_two_with_bit_length_u64;
pub mod next_power_of_two_with_builtin_u64;
pub mod next_prime_number;
pub mod next_prime_number_table;
pub mod normalize_sort_csgraph;
pub mod ntt;
pub mod number_of_common_subsequences_low_memory_modular_i64;
pub mod number_of_common_subsequences_modular_i64;
pub mod number_of_common_substrings;
pub mod number_of_complete_permutations;
pub mod number_of_days_between_2_dates;
pub mod number_of_dearangement;
pub mod number_of_distinct_subsequences;
pub mod number_of_distinct_subsequences_modular_i64;
pub mod number_of_distinct_substrings;
pub mod number_of_nodes_reachable_into_cycle_bfs_rev_edges;
pub mod number_of_nodes_reachable_into_cycle_dfs_recurse;
pub mod number_of_subsequences;
pub mod number_of_topological_sort;
pub mod number_of_topological_sort_modular;
pub mod number_of_undirected_cycle_graph_table;
pub mod number_of_undirected_path_graph_table;
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
pub mod pascal_rule_cached_from_usize;
pub mod pascal_simplex;
pub mod pascal_triangle_from_i32;
pub mod pascal_triangle_from_u64_low_memory;
pub mod pascal_triangle_with_instance_semiring;
pub mod path_based_scc;
pub mod patricia_tree;
pub mod perfect_numbers;
pub mod permutation_argsort;
pub mod permutation_functional_graph_kth_from_any;
pub mod ph_tree;
pub mod pi_with_arccosine;
pub mod pigeonhole_sort;
pub mod pivot_tree;
pub mod pocket_modint_u32;
pub mod pocket_tree_bfs_depth;
pub mod pocket_tree_bfs_parent;
pub mod pointer_grpah;
pub mod pollard_kangaroo_algorithm;
pub mod pollard_p_1;
pub mod pollard_rho;
pub mod polyphase_merge_sort;
pub mod pop;
pub mod popcount_bit_by_bit;
pub mod popcount_cached_usize;
pub mod popcount_divide_and_conquer;
pub mod popcount_divide_and_conquer_optimized;
pub mod popcount_resetting_lsb_usize;
pub mod popcount_table;
pub mod popcount_table_const_8_bit_usize;
pub mod popcount_with_const_8_bit_table_usize;
pub mod popcount_with_k_bit_table_usize;
pub mod popcount_with_std_u64;
pub mod postman_sort;
pub mod power;
pub mod power_dynamic;
pub mod power_group;
pub mod power_group_itself;
pub mod power_group_trait;
pub mod power_monoid;
pub mod power_monoid_itself;
pub mod power_monoid_trait;
pub mod power_multiplicative_semigroup_with_std_ops;
pub mod power_multiplicative_semigroup_with_std_ops_recurse;
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
pub mod prime_factorize_factorial_histogram_with_trial_division;
pub mod prime_factorize_factorial_with_legendre_formula_u32;
pub mod prime_factorize_factorial_with_legendre_formula_usize;
pub mod prime_factorize_factorial_with_lpf;
pub mod prime_factorize_fermat;
pub mod prime_factorize_pollard_rho;
pub mod prime_factorize_pollard_rho_flat;
pub mod prime_factorize_pollard_rho_flat_2;
pub mod prime_factorize_trial_division;
pub mod prime_factorize_trial_division_usize;
pub mod prime_factorize_with_least_prime_factor_table;
pub mod prime_factorize_with_least_prime_factor_table_usize;
pub mod prime_number;
pub mod prime_pi_approx_ln;
pub mod prime_pi_power_of_10;
pub mod prime_pi_table_from_enumerate_primes;
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
pub mod queue_with_2_stacks;
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
pub mod rerooting_dp;
pub mod rerooting_dp_with_instance_commutative_group;
pub mod rerooting_dp_with_instance_commutative_group_with_std_ops;
pub mod rerooting_dp_with_instance_commutative_monoid;
pub mod rerooting_dp_with_instance_commutative_monoid_old;
pub mod rerooting_dp_with_instance_commutative_monoid_recurse;
pub mod rerooting_dp_with_instance_commutative_monoid_with_std_ops;
pub mod rerooting_dp_with_node_priority_with_instance_monoid;
pub mod reset_least_significant_bit_direct_u64;
pub mod reset_least_significant_bit_smart;
pub mod reset_least_significant_bit_smart_u64;
pub mod reset_least_significant_bit_subtract_lsb_number;
pub mod rle;
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
pub mod round_up_with_int_u64;
pub mod run_length_encoding;
pub mod safe_int_power;
pub mod sbbst;
pub mod scapegoat_tree;
pub mod scc_topological_sort;
pub mod scc_transpose;
pub mod segment_tree_2d;
pub mod segment_tree_2d_dense;
pub mod segment_tree_additive;
pub mod segment_tree_beats;
pub mod segment_tree_dual;
pub mod segment_tree_dynamic_node;
pub mod segment_tree_i64_add;
pub mod segment_tree_i64_min;
pub mod segment_tree_lazy_additive_range_update_range_sum_modint;
pub mod segment_tree_lazy_additive_with_std_ops;
pub mod segment_tree_lazy_i64_range_add_range_sum;
pub mod segment_tree_lazy_range_add_range_minimum;
pub mod segment_tree_lazy_range_update_range_minimum;
pub mod segment_tree_lazy_range_update_range_sum;
pub mod segment_tree_lazy_with_instance_ops;
pub mod segment_tree_lazy_with_instance_ops_recurse;
pub mod segment_tree_lazy_with_static_ops;
pub mod segment_tree_min;
pub mod segment_tree_point_update_get_range_sum_and_range_prefix_sum_min_i64;
pub mod segment_tree_with_instance_monoid;
pub mod segment_tree_with_static_monoid;
pub mod selection_sort;
pub mod self_balancing_binary_search_tree;
pub mod set_theory;
pub mod shaker_sort;
pub mod shakutori_method;
pub mod shear_sort;
pub mod shellsort;
pub mod shortest_path_01_bfs_sparse;
pub mod shortest_path_a_star_2d_grid_path_or_wall_udlr_option_u32;
pub mod shortest_path_a_star_sparse_tuple_edges_adjacency_list_i64_with_inf;
pub mod shortest_path_arborescence;
pub mod shortest_path_bfs_2d_grid_path_or_wall_simple_udlr_move;
pub mod shortest_path_bfs_sparse_tuple_edges_adjacency_list_usize;
pub mod shortest_path_desopo_pape_sparse;
pub mod shortest_path_potential;
pub mod shortest_path_predecessors;
pub mod shortest_path_tree;
pub mod shortest_path_viterbi;
pub mod shuffle_sort;
pub mod sieve_of_eratosthenes_enumerate_primes;
pub mod sieve_of_eratosthenes_greatest_prime_factor_table_direct;
pub mod sieve_of_eratosthenes_is_prime_table;
pub mod sieve_of_eratosthenes_least_prime_factor_table_direct;
pub mod sieve_of_eratosthenes_low_memory_prime_generator;
pub mod sieve_of_eratosthenes_range_sieve;
pub mod simulated_annealing;
pub mod single_source_shortest_path;
pub mod singly_linked_list_node_with_box;
pub mod singly_linked_list_node_with_rc_refcell;
pub mod singly_linked_list_queue;
pub mod singly_linked_list_stack;
pub mod size;
pub mod skew_heap;
pub mod sliding_window_aggregation;
pub mod sliding_window_aggregation_deque_with_instance_group;
pub mod sliding_window_aggregation_queue_with_instance_group;
pub mod sliding_window_aggregation_queue_with_instance_monoid;
pub mod sliding_window_maximum_with_deque;
pub mod sliding_window_minimum_with_deque;
pub mod slope_trick;
pub mod slowsort;
pub mod smallest_enclosing_circle;
pub mod smawk_algorithm;
pub mod smoothsort;
pub mod sort;
pub mod sorting_network;
pub mod sorting_number;
pub mod spaghetti_sort;
pub mod spanning_forest_with_uf;
pub mod sparse_table_with_instance_idempotent_binary_operation;
pub mod sparse_table_with_static_idempotent_binary_operation;
pub mod sparse_table_with_static_idempotent_semigroup;
pub mod spfa;
pub mod splay_tree_node_key_value_based_with_box_recurse;
pub mod splay_tree_node_with_trait_rc_refcell_merge_split_based_bottom_up;
pub mod split;
pub mod spqr_tree;
pub mod spreadsort;
pub mod sqrt_decomposition;
pub mod sqrt_tree;
pub mod srt_division;
pub mod sssp_dijkstra_sparse_with_general;
pub mod sssp_faster_algorithm;
pub mod stable_sort;
pub mod stack_with_vec;
pub mod static_matrix_property_i64_2_2;
pub mod static_matrix_property_trait;
pub mod static_modular_int_i64;
pub mod static_modular_int_with_id_i64;
pub mod static_square_matrix_property_trait;
pub mod static_tensor_shape;
pub mod steiner_tree;
pub mod stooge_sort;
pub mod strconv;
pub mod string_ith_ascii_code;
pub mod string_ith_char;
pub mod strongly_connected_components;
pub mod subset_sum;
pub mod subset_sum_at_most_k;
pub mod subset_sum_limited_count_multiple_same_values;
pub mod subset_sum_max_less_than_meet_in_the_middle_usize;
pub mod subset_sum_min_count;
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
pub mod sum_of_all_pairs_xor_in_array_modular;
pub mod sum_of_divisors_count;
pub mod sum_of_divisors_count_times_i;
pub mod sum_of_divisors_sum;
pub mod sum_of_gcd_for_each_element_is_1_to_k_euler_phi_from_usize;
pub mod sum_of_gcd_for_each_element_is_1_to_k_fast_mobius_transform_from_usize;
pub mod sum_of_gcd_for_each_element_is_1_to_k_fast_mobius_transform_usize;
pub mod sum_of_gcd_for_each_element_is_1_to_k_mobius_transform_from_usize;
pub mod sum_of_gcd_for_each_element_is_1_to_k_mobius_transform_usize;
pub mod sum_of_gcd_with_k_for_1_to_n_with_divisors_euler_phi;
pub mod sum_of_gcd_with_k_for_1_to_n_with_divisors_factorize_fast_mobius;
pub mod sum_of_i_times_n_choose_i;
pub mod sum_of_multiples;
pub mod sum_of_multiples_count_range;
pub mod sum_of_multiples_count_times_i_range;
pub mod sum_of_multiples_sum;
pub mod sum_of_multiples_sum_range;
pub mod sum_of_n_choose_i;
pub mod sum_of_xor_prod_of_all_subsets_in_array_modular;
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
pub mod transpose_sparse_graph_with_unweighted_edges;
pub mod transpose_sparse_graph_with_weighted_edges;
pub mod traveling_salesperson;
pub mod traveling_salesperson_giving_with_inf;
pub mod traveling_salesperson_taking_mem_access_optim_with_inf;
pub mod traveling_salesperson_taking_with_inf;
pub mod tree_bfs_parent_depth;
pub mod tree_diameter_and_path_weigted_edge_find_farthest_2_times_with_dfs;
pub mod tree_diameter_dp_for_each_subtree_with_dfs;
pub mod tree_diameter_finding_farthest_2_times_with_bfs;
pub mod tree_diameter_path_unweighted;
pub mod tree_edges_to_graph;
pub mod tree_get_path_with_lifting;
pub mod tree_node;
pub mod tree_path_aggregation;
pub mod tree_path_aggregation_with_binary_lifting;
pub mod tree_path_aggregation_with_hld;
pub mod tree_sort;
pub mod treeops;
pub mod triangle_2d_area_with_vector_cross_product;
pub mod tribonacci_number;
pub mod tribonacci_sequence_modular;
pub mod trigonometry_tau_with_pi;
pub mod two_three_four_tree;
pub mod two_three_heap;
pub mod two_three_tree;
pub mod ub_tree;
pub mod undirected_bridge_detection_chain_decomposition;
pub mod undirected_bridge_detection_lowlink;
pub mod undirected_lowlink;
pub mod undirected_tuple_edges_to_adjacency_list;
pub mod undirected_tuple_edges_with_data_to_adjacency_list;
pub mod union_find_low_memory;
pub mod union_find_low_memory_with_trait;
pub mod union_find_persistent;
pub mod union_find_potentialized_with_static_abelian_group_and_trait;
pub mod union_find_rollback;
pub mod union_find_traits;
pub mod union_find_weighted;
pub mod upper_bound_on_slice;
pub mod usize_u64_impl_graph_edge_trait;
pub mod van_emde_boas_tree;
pub mod vector;
pub mod vector_dedup;
pub mod vector_rotation_2d_by_radian_with_matrix;
pub mod vector_rotation_3d_by_radian_with_matrix;
pub mod vector_space;
pub mod vector_unique;
pub mod verbal_arithmetic;
pub mod vertex_cut;
pub mod vertex_seperator;
pub mod virtual_tree;
pub mod viterbi_algorithm;
pub mod volume_of_torus;
pub mod vp_tree;
pub mod wavelet_matrix;
pub mod wavl_tree;
pub mod weak_avl_tree;
pub mod weighted_union_algorithm;
pub mod x_tree;
pub mod xor_of_all_pairs_bitwise_and_of_two_arrays;
pub mod xor_vector_space_basis_with_cumulative_min;
pub mod xor_vectors_rank_online;
pub mod z_algorithm;
pub mod z_algorithm_findall_substr;
pub mod zeller_day_of_week_congruence_formula;
pub mod zero_element;
pub mod zero_one_bfs;
// pub mod rerooting_dynamic;
