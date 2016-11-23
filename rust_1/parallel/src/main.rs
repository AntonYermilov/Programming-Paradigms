extern crate rand;
extern crate rayon;

use rand::{Rng, SeedableRng, XorShiftRng};
use std::time::Instant;

fn quick_sort<T: Ord + Send>(v: &mut [T]) {
    if v.len() <= 8 * 1024 {
        v.sort();
        return;
    }

    let mid = partition(v);
    let (lo, hi) = v.split_at_mut(mid);
    rayon::join(|| quick_sort(lo), || quick_sort(hi));
}

fn partition<T: Ord>(v: &mut [T]) -> usize {
    let pivot = v.len() - 1;
    let mut i = 0;
    for j in 0..pivot {
        if v[j] <= v[pivot] {
            v.swap(i, j);
            i += 1;
        }
    }
    v.swap(i, pivot);
    i
}

fn is_sorted<T: Ord>(v: &[T]) -> bool {
    (1..v.len()).all(|i| v[i - 1] <= v[i])
}

fn random_vec(n: usize) -> Vec<u32> {
    let mut rng = XorShiftRng::from_seed([0, 1, 2, 3]);
    (0..n).map(|_| rng.next_u32()).collect()
}

fn timed_sort<F: FnOnce(&mut [u32])>(n: usize, f: F, name: &str) -> u64 {
    let mut v = random_vec(n);

    let start = Instant::now();
    f(&mut v[..]);
    let dur = Instant::now() - start;
    let nanos = dur.subsec_nanos() as u64 + dur.as_secs() * 1_000_000_000u64;
    println!("{} sorted {} ints: {} s", name, n, nanos as f32 / 1e9f32);

    // Check correctness
    assert!(is_sorted(&mut v[..]));

    nanos
}


fn main() {
    let n = 10_000_000;
    let p = timed_sort(n, quick_sort, "parallel");
    let s = timed_sort(n, |xs| xs.sort(), "sequential");
    println!("speedup {}", s as f32 / p as f32);
}
